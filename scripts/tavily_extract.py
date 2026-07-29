#!/usr/bin/env python3
"""Tavily reader helper: extract (advanced depth) and search.
Usage:
  tavily_extract.py extract <url> [<url> ...]
  tavily_extract.py search "<query>"
Reads TAVILY_API_KEY from env. Prints JSON summary to stdout.
"""
import json, os, sys, urllib.request, urllib.error

KEY = os.environ.get("TAVILY_API_KEY", "")

def _post(endpoint, payload):
    req = urllib.request.Request(
        f"https://api.tavily.com/{endpoint}",
        data=json.dumps(payload).encode(),
        method="POST",
    )
    req.add_header("Content-Type", "application/json")
    req.add_header("Authorization", f"Bearer {KEY}")
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        return {"error": f"HTTP {e.code}", "body": e.read().decode(errors="ignore")}
    except Exception as e:
        return {"error": str(e)}

def do_extract(urls):
    res = _post("extract", {"urls": urls, "extract_depth": "advanced"})
    out = []
    for r in res.get("results", []):
        content = r.get("raw_content") or r.get("content") or ""
        out.append({"url": r.get("url"), "chars": len(content),
                    "content": content[:3000]})
    for f in res.get("failed_results", []):
        out.append({"url": f.get("url"), "failed": True, "error": f.get("error")})
    if "error" in res:
        out.append(res)
    print(json.dumps(out, ensure_ascii=False, indent=2))

def do_search(q):
    res = _post("search", {"query": q, "search_depth": "advanced",
                            "max_results": 8, "days": 3})
    if "error" in res:
        print(json.dumps(res, indent=2)); return
    for r in res.get("results", []):
        print(json.dumps({"title": r.get("title"), "url": r.get("url"),
                          "published": r.get("published_date"),
                          "content": (r.get("content") or "")[:400]}, ensure_ascii=False))

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("usage: extract <url>... | search <query>", file=sys.stderr); sys.exit(2)
    mode = sys.argv[1]
    if mode == "extract":
        do_extract(sys.argv[2:])
    elif mode == "search":
        do_search(sys.argv[2])
    else:
        print("unknown mode", file=sys.stderr); sys.exit(2)
