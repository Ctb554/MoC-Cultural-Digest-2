#!/usr/bin/env python3
"""
Upload a file (binary-safe) to Dropbox via the HTTP API.

The claude.ai Dropbox connector has no binary-upload tool; its create_file is
text-only and corrupts .docx files. This uploads via the Dropbox API using a
scoped app with a refresh token (no expiring access token to manage) --
same pattern as the conflict-monitoring repo this was adapted from.

Required environment variables:
  DROPBOX_APP_KEY        App key from dropbox.com/developers/apps
  DROPBOX_APP_SECRET     App secret
  DROPBOX_REFRESH_TOKEN  Offline refresh token (see SETUP.md for the
                         one-time authorize/exchange steps)
Optional:
  DROPBOX_DEST_FOLDER    Destination folder path. No default is hardcoded
                         here (unlike the repo this was adapted from, which
                         pointed at a specific client folder) -- set this to
                         wherever the Ministry's digest should land.
  DROPBOX_NAMESPACE_ID   Shared/team folder namespace ID. REQUIRED if
                         DROPBOX_DEST_FOLDER lives inside a Dropbox team/
                         shared folder rather than the account's own
                         personal root. Without this, the Dropbox API
                         resolves DROPBOX_DEST_FOLDER against the account's
                         PERSONAL root namespace by default -- the upload
                         will "succeed" but land in a private mirror path
                         only the authenticating account can see, not the
                         actual shared team folder. This was discovered the
                         hard way during testing: a file uploaded without
                         this header landed at
                         "/Cameron Bennett/C_Clients/C_MoC/..." (personal
                         namespace) instead of the real, colleague-visible
                         "/C_Clients/C_MoC/..." (team namespace). Get the
                         correct ID by calling Dropbox's
                         files/get_metadata on the destination folder and
                         reading sharing_info.parent_shared_folder_id, or
                         ask whoever manages the Dropbox team account.

Usage:
  dropbox_upload.py <local-file> [more-files...]

Exit codes: 0 uploaded, 78 not configured (caller treats as skip), 1 failure.
"""

import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request


def get_access_token(app_key: str, app_secret: str, refresh_token: str) -> str:
    data = urllib.parse.urlencode({
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
    }).encode()

    req = urllib.request.Request(
        "https://api.dropbox.com/oauth2/token",
        data=data,
        method="POST",
    )
    auth = f"{app_key}:{app_secret}"
    import base64
    req.add_header("Authorization", "Basic " + base64.b64encode(auth.encode()).decode())

    with urllib.request.urlopen(req) as resp:
        payload = json.loads(resp.read().decode())
    return payload["access_token"]


def upload_file(access_token: str, local_path: str, dest_folder: str, namespace_id: str = None) -> None:
    filename = os.path.basename(local_path)
    dest_path = f"{dest_folder.rstrip('/')}/{filename}" if dest_folder else f"/{filename}"

    with open(local_path, "rb") as f:
        content = f.read()

    dropbox_api_arg = json.dumps({
        "path": dest_path,
        "mode": "overwrite",
        "autorename": False,
        "mute": False,
    })

    req = urllib.request.Request(
        "https://content.dropboxapi.com/2/files/upload",
        data=content,
        method="POST",
    )
    req.add_header("Authorization", f"Bearer {access_token}")
    req.add_header("Dropbox-API-Arg", dropbox_api_arg)
    req.add_header("Content-Type", "application/octet-stream")

    if namespace_id:
        # Tells the API to resolve dest_path inside this shared/team
        # namespace instead of the authenticating account's personal root.
        # Without this, uploads to a path that LOOKS like the shared team
        # folder silently land in a private per-user mirror instead --
        # confirmed by testing (see module docstring).
        path_root = json.dumps({".tag": "namespace_id", "namespace_id": namespace_id})
        req.add_header("Dropbox-API-Path-Root", path_root)

    try:
        with urllib.request.urlopen(req) as resp:
            result = json.loads(resp.read().decode())
        print(f"Uploaded {local_path} -> {result.get('path_display', dest_path)}")
    except urllib.error.HTTPError as exc:
        body = exc.read().decode(errors="ignore")
        print(f"Upload failed for {local_path}: HTTP {exc.code} {body}", file=sys.stderr)
        raise


def main():
    app_key = os.environ.get("DROPBOX_APP_KEY")
    app_secret = os.environ.get("DROPBOX_APP_SECRET")
    refresh_token = os.environ.get("DROPBOX_REFRESH_TOKEN")
    dest_folder = os.environ.get("DROPBOX_DEST_FOLDER", "")
    namespace_id = os.environ.get("DROPBOX_NAMESPACE_ID", "")

    if not (app_key and app_secret and refresh_token):
        print("Dropbox credentials not configured -- skipping upload.", file=sys.stderr)
        sys.exit(78)

    if dest_folder and not namespace_id:
        print(
            "WARNING: DROPBOX_DEST_FOLDER is set but DROPBOX_NAMESPACE_ID is "
            "not. If the destination is inside a shared/team folder, the "
            "upload will silently land in your personal Dropbox root "
            "instead of the shared folder. See this script's docstring.",
            file=sys.stderr,
        )

    files = sys.argv[1:]
    if not files:
        print("Usage: dropbox_upload.py <local-file> [more-files...]", file=sys.stderr)
        sys.exit(1)

    try:
        access_token = get_access_token(app_key, app_secret, refresh_token)
        for f in files:
            upload_file(access_token, f, dest_folder, namespace_id)
    except Exception as exc:
        print(f"Dropbox upload failed: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
