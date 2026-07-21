#!/usr/bin/env python3
"""
RSS pre-filter for the Saudi Arabia/Regional section.

This is a SUPPLEMENT to the live-search architecture, not a replacement for
it -- scoped narrowly to the ~20 outlets below, to solve one specific
problem: WebSearch depends on a search engine having already indexed an
outlet's latest article, which can lag by hours. An outlet's own RSS feed
updates the instant it publishes, with zero indexing lag. This script pulls
those feeds directly, filters to items from the last 24 hours that mention
Saudi Arabia/KSA, and hands the routine a candidate list -- every candidate
STILL has to pass the normal Stage 2 verification gates (real, in-window,
non-Saudi-owned, not previously used) before it can be written into the
digest. This script finds candidates; it never decides what's true.

FEED URL STATUS (as of 2026-07-20): the URLs below are either verified
working, or are standard, long-documented feed patterns for these outlets
that are very likely correct -- but this script was built inside a sandboxed
environment without general internet access, so the exact URLs could NOT be
live-tested against the real outlets here. The cloud routine environment has
full internet access -- the FIRST real run using this script should log
which feeds actually resolved vs. 404'd/timed out, and this config should be
corrected based on that real-world result, not assumed correct from this
build alone. A feed 404ing is not a crisis -- it just means that outlet
falls back to the existing WebSearch-based check for now.

Usage:
    python3 scripts/rss_saudi_filter.py --hours 24 --output /tmp/rss_candidates.json
"""

import argparse
import json
import re
import sys
import time
from datetime import datetime, timedelta, timezone

import feedparser

# Word-boundary regex so "KSA" doesn't match inside an unrelated word, and
# "Saudi" doesn't need a separate check for "Saudi Arabia" specifically.
SAUDI_MENTION_RE = re.compile(r"\b(saudi|ksa)\b", re.IGNORECASE)

# Feed URLs: see the FEED URL STATUS note in the module docstring above.
# Al Jazeera was REMOVED 2026-07-20 based on real operational evidence from
# a separate, already-running project's RSS infrastructure: its feed went
# stale (stopped returning fresh items) around 2026-06-17. That's not a
# guess -- it's confirmed history from a live system, and outranks this
# script's own "should be correct" confidence for any outlet.
#
# Outlets known to have NO reliable public RSS feed (Bloomberg, Reuters, FT,
# WSJ, Semafor, Axios, Politico, Al-Monitor, AGBI, Amwaj.media, MEED, Gulf
# News, Arabian Business, The National, Nikkei Asia, and most of the smaller
# sector trade press) are deliberately NOT included here -- they stay on the
# existing WebSearch-based outlet sweep in SKILL.md, which remains the
# fallback for every outlet not listed below, not just these. Bloomberg,
# Reuters, AP, Politico, Gulf News, MEED, and The National being confirmed
# stale in that same separate project's operational history corroborates
# this exclusion rather than contradicting it.
OUTLET_FEEDS = {
    "BBC News (Middle East)": "https://feeds.bbci.co.uk/news/world/middle_east/rss.xml",
    "The Guardian (Middle East)": "https://www.theguardian.com/world/middleeast/rss",
    "The New York Times (Middle East)": "https://rss.nytimes.com/services/xml/rss/nyt/MiddleEast.xml",
    "Deutsche Welle (All)": "https://rss.dw.com/rdf/rss-en-all",
    "Middle East Eye": "https://www.middleeasteye.net/rss",
    "The Diplomat": "https://thediplomat.com/feed/",
    "Foreign Policy": "https://foreignpolicy.com/feed/",
    "HeritageDaily": "https://www.heritagedaily.com/feed",
    "Arkeonews": "https://arkeonews.net/feed/",
    "The Art Newspaper": "https://www.theartnewspaper.com/rss",
    "Dezeen": "https://www.dezeen.com/feed/",
    "ArchDaily": "https://www.archdaily.com/rss/",
    "Variety": "https://variety.com/feed/",
    "The Hollywood Reporter": "https://www.hollywoodreporter.com/feed/",
    "Deadline": "https://deadline.com/feed/",
    "WWD": "https://wwd.com/feed/",
    "Billboard": "https://www.billboard.com/feed/",
    "Publishers Weekly": "https://www.publishersweekly.com/pw/corp/rss/index.html",
    "Eater": "https://www.eater.com/rss/index.xml",
}


def fetch_and_filter_feed(outlet_name, feed_url, cutoff_time):
    """
    Fetches one feed and returns a list of candidate dicts for items that
    (a) mention Saudi/KSA by word boundary in title or summary, and
    (b) have a publish date within the cutoff window.
    Returns an empty list (not an error) on fetch failure or empty feed --
    a feed 404ing should not crash the whole run, just skip that outlet.
    """
    candidates = []
    try:
        parsed = feedparser.parse(feed_url)
        if parsed.bozo and not parsed.entries:
            # bozo=True with no entries usually means the fetch/parse
            # genuinely failed (404, malformed XML, timeout-like response)
            print(f"  [SKIP] {outlet_name}: feed did not parse cleanly, no entries", file=sys.stderr)
            return []

        for entry in parsed.entries:
            title = entry.get("title", "")
            summary = entry.get("summary", entry.get("description", ""))
            combined_text = f"{title} {summary}"

            if not SAUDI_MENTION_RE.search(combined_text):
                continue

            pub_struct = entry.get("published_parsed") or entry.get("updated_parsed")
            if pub_struct:
                pub_dt = datetime.fromtimestamp(time.mktime(pub_struct), tz=timezone.utc)
                if pub_dt < cutoff_time:
                    continue
            else:
                pub_dt = None  # No date available; include but flag for manual date check

            candidates.append({
                "outlet": outlet_name,
                "title": title,
                "link": entry.get("link", ""),
                "published": pub_dt.isoformat() if pub_dt else None,
                "date_confidence": "confirmed" if pub_dt else "UNKNOWN -- verify manually",
            })

    except Exception as exc:
        print(f"  [SKIP] {outlet_name}: {exc}", file=sys.stderr)
        return []

    return candidates


def main():
    parser = argparse.ArgumentParser(description="RSS pre-filter for Saudi Arabia/Regional coverage")
    parser.add_argument("--hours", type=int, default=24, help="Coverage window in hours")
    parser.add_argument("--output", required=True, help="Output JSON path for candidates")
    args = parser.parse_args()

    cutoff_time = datetime.now(timezone.utc) - timedelta(hours=args.hours)

    all_candidates = []
    outlets_checked = []
    outlets_failed = []

    for outlet_name, feed_url in OUTLET_FEEDS.items():
        result = fetch_and_filter_feed(outlet_name, feed_url, cutoff_time)
        outlets_checked.append(outlet_name)
        if result:
            all_candidates.extend(result)
        # Note: an outlet returning zero candidates is NOT the same as a
        # failed fetch -- fetch_and_filter_feed already logs actual failures
        # to stderr distinctly, so a silent zero here is a legitimate "this
        # outlet had nothing Saudi-related in the window" result.

    output = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "coverage_window_hours": args.hours,
        "outlets_attempted": len(OUTLET_FEEDS),
        "candidates_found": len(all_candidates),
        "candidates": all_candidates,
        "note": (
            "Every candidate here is UNVERIFIED -- it passed only the "
            "Saudi/KSA word-boundary filter and the date cutoff. It still "
            "must go through the normal Stage 2 verification gates (real "
            "source, in-window confirmed via WebFetch, non-Saudi-owned, "
            "not previously used) before it can be written into the "
            "digest. This script finds candidates; it does not verify them."
        ),
    }

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"Checked {len(outlets_checked)} outlets, found {len(all_candidates)} candidates")
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
