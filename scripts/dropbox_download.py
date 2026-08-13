#!/usr/bin/env python3
"""One-off helper: download files from the Dropbox test folder by name so a
run can ingest prior delivered editions when the repo's own reports/ history
is missing. Uses the same refresh-token flow and namespace path-root header
as dropbox_upload.py. Not part of the committed pipeline surface."""

import base64
import json
import os
import sys
import urllib.parse
import urllib.request

DEST = os.environ["DROPBOX_DEST_FOLDER"].rstrip("/")
NS = os.environ.get("DROPBOX_NAMESPACE_ID")


def token():
    data = urllib.parse.urlencode({
        "grant_type": "refresh_token",
        "refresh_token": os.environ["DROPBOX_REFRESH_TOKEN"],
    }).encode()
    req = urllib.request.Request("https://api.dropbox.com/oauth2/token", data=data, method="POST")
    auth = f'{os.environ["DROPBOX_APP_KEY"]}:{os.environ["DROPBOX_APP_SECRET"]}'
    req.add_header("Authorization", "Basic " + base64.b64encode(auth.encode()).decode())
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read().decode())["access_token"]


def download(access, name, outdir):
    dest_path = f"{DEST}/{name}"
    req = urllib.request.Request("https://content.dropboxapi.com/2/files/download", method="POST")
    req.add_header("Authorization", "Bearer " + access)
    req.add_header("Dropbox-API-Arg", json.dumps({"path": dest_path}))
    if NS:
        req.add_header("Dropbox-API-Path-Root",
                       json.dumps({".tag": "namespace_id", "namespace_id": NS}))
    out = os.path.join(outdir, name)
    with urllib.request.urlopen(req) as r:
        with open(out, "wb") as f:
            f.write(r.read())
    print(f"downloaded {name} -> {out}")


if __name__ == "__main__":
    outdir = sys.argv[1]
    names = sys.argv[2:]
    os.makedirs(outdir, exist_ok=True)
    access = token()
    for n in names:
        download(access, n, outdir)
