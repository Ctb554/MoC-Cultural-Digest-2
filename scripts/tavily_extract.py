#!/usr/bin/env python3
"""Minimal Tavily reader used only for the final selected articles that
WebFetch cannot read (bot-walled premium wires). Uses extract_depth=advanced
per the SKILL's 2026-07-20 diagnostic. Usage:
    python3 scripts/tavily_extract.py <url> [<url> ...]
Prints JSON with per-url content (truncated) to stdout."""
import json, os, sys, urllib.request

KEY = os.environ["TAVILY_API_KEY"]


def extract(urls):
    body = json.dumps({"urls": urls, "extract_depth": "advanced"}).encode()
    req = urllib.request.Request(
        "https://api.tavily.com/extract", data=body, method="POST")
    req.add_header("Content-Type", "application/json")
    req.add_header("Authorization", "Bearer " + KEY)
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode())


if __name__ == "__main__":
    res = extract(sys.argv[1:])
    for item in res.get("results", []):
        print("=" * 60)
        print("URL:", item.get("url"))
        content = item.get("raw_content") or item.get("content") or ""
        print("LEN:", len(content))
        print(content[:4000])
    failed = res.get("failed_results", [])
    if failed:
        print("FAILED:", json.dumps(failed))
