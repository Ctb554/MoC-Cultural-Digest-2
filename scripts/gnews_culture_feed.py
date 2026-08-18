#!/usr/bin/env python3
"""
Google News RSS builder for the Saudi Arabia/Regional CULTURE layer.

WHAT THIS IS FOR (and, just as importantly, what it is NOT for):
This is a targeted supplement aimed at ONE specific, diagnosed gap -- the
Saudi *culture* layer, especially Arabic-language cultural coverage that the
English-first live-search net under-reaches. It is NOT a replacement for the
live WebSearch/WebFetch architecture, and it is deliberately NOT pointed at
the geopolitical/General bucket. It exists because:
  - Google News RSS supports the exact Boolean-ish operators already used
    (when:, allinurl:, intitle:, quoted phrases) and, critically, an Arabic
    locale (hl=ar&gl=SA&ceid=SA:ar), which is the real identified gap.
  - It's free and needs no key.

HONEST LIMITATIONS -- read before trusting output (from real, current
third-party testing of Google News RSS, not assumptions):
  1. STALENESS. A July 2026 sample of 48 queries found median item age ~6.6
     days, with only ~7.6% of items <6h old. For a 24-hour digest this is a
     real weakness. The hours filter below is a HARD gate -- anything
     outside the window is dropped -- expect many queries to return zero
     in-window items on any given day. That's the tool being stale, not a
     bug here.
  2. REDIRECT URLS. Every <link> is an opaque news.google.com/rss/articles/
     redirect, NOT the publisher URL. This script surfaces candidates for
     the routine to resolve/verify -- it does NOT emit final citation URLs.
     The routine MUST follow each redirect to the real publisher URL and
     cite THAT, never the google.com redirect. A digest bullet citing a
     news.google.com link would fail the normal audit and must not happen.
  3. UNDOCUMENTED/UNSTABLE. No contract, no status page, format has changed
     without notice before. Best-effort scaffolding, not infrastructure. If
     it breaks, the culture layer falls back to normal WebSearch creative
     retrieval (SKILL.md) -- nothing here is load-bearing.
  4. 100-ITEM CAP + DEDUP. Each feed returns <=100 items; stories recur
     across queries. Dedup here is best-effort by title similarity only --
     the routine's normal not-previously-used gate is the real backstop.

EVERY candidate this emits is UNVERIFIED. It has passed only: (a) the query,
(b) the 24h window filter on the feed's own pubDate, (c) a not-Saudi-owned
domain check where the source domain is visible. It still must pass every
normal Stage 2 verification gate (real, in-window confirmed via the resolved
publisher page, non-Saudi-owned confirmed on the real domain, not previously
used) before anything is written into the digest.

Usage:
    python3 scripts/gnews_culture_feed.py --hours 24 --output /tmp/gnews_culture.json
"""

import argparse
import json
import re
import sys
import time
import urllib.parse
from datetime import datetime, timedelta, timezone

import feedparser

# Saudi-owned domains to drop if they appear as the GNews <source>. This is a
# convenience pre-filter only; the routine's full ownership check (including
# parent-company checks like SRMG -> hiamag.com) remains authoritative. Keep
# this in sync with audit_report.py's EXCLUDED_SAUDI_DOMAINS.
EXCLUDED_SAUDI_DOMAINS = [
    "arabnews.com", "saudigazette.com.sa", "spa.gov.sa", "aleqt.com",
    "okaz.com.sa", "sabq.org", "argaam.com", "asharq.com", "aawsat.com",
    "hiamag.com", "sayidaty.net", "majalla.com", "arrajol.com",
]

# The culture queries. Each maps to the three creative-retrieval angles in
# SKILL.md: reviews/criticism, named figures abroad, and Saudi work/brands
# at international events. Deliberately NO geopolitical/General queries --
# this feed exists to fill the culture layer only.
CULTURE_QUERIES_EN = [
    '"Saudi film" review',
    '"Saudi cinema" festival',
    '"Saudi movie" premiere OR screening',
    '"Saudi artist" exhibition',
    '"Saudi art" biennale OR gallery',
    '"Saudi designer" fashion OR collection',
    '"Saudi author" OR "Saudi writer" book OR novel',
    '"Saudi architect" OR "Saudi architecture" design',
    '"Saudi chef" OR "Saudi cuisine" restaurant OR Michelin',
    '"Saudi musician" OR "Saudi singer" album OR concert',
    '"Saudi photographer" OR "Saudi sculptor" exhibition',
    'Saudi pavilion Venice OR Cannes OR Berlinale OR biennale',
    'Saudi "fashion week" Paris OR Milan OR London OR "New York"',
    'Saudi "book fair" OR "literary festival"',
    'Saudi film "Toronto" OR "Sundance" OR "Red Sea" festival',
    '"Saudi Arabia" UNESCO heritage OR inscription',
    '"Diriyah Biennale" OR "Islamic Arts Biennale"',
    '"Red Sea International Film Festival" OR "Red Sea Film"',
    'AlUla exhibition OR concert OR festival OR residency',
    'Diriyah OR "JAX District" art OR exhibition',
    '"Ithra" OR "King Abdulaziz Center" exhibition OR programme',
    '"National Museum of Saudi Arabia" OR "Black Gold Museum"',
    'MDLBEAST OR "Riyadh Season" culture OR music',
    '"Ahmed Mater" OR "Manal Al Dowayan" OR "Dana Awartani"',
    '"Haifaa Al-Mansour" film OR director',
    'Saudi brand takeover Selfridges OR Harrods OR "department store"',
    'Saudi fashion OR beauty brand international retail',
]
CULTURE_QUERIES_AR = [
    'الفن السعودي معرض',
    'الفنان السعودي',
    'الفيلم السعودي مهرجان',
    'السينما السعودية',
    'الأزياء السعودية مصمم',
    'التراث السعودي',
    'الأدب السعودي كتاب',
    'الموسيقى السعودية حفل',
    'المطبخ السعودي مطعم',
    'العمارة السعودية تصميم',
    'بينالي الدرعية',
    'مهرجان البحر الأحمر السينمائي',
    'العلا فعاليات',
    'متحف السعودية',
    'الفنون السعودية معرض',
]

GNEWS_BASE = "https://news.google.com/rss/search"


def build_feed_url(query, hours, lang, country):
    scoped_query = f"when:{hours}h {query}"
    params = {
        "q": scoped_query,
        "hl": f"{lang}-{country}" if lang == "en" else lang,
        "gl": country,
        "ceid": f"{country}:{lang}",
    }
    return f"{GNEWS_BASE}?{urllib.parse.urlencode(params)}"


def source_domain(entry):
    src = entry.get("source", {})
    href = src.get("href", "") if isinstance(src, dict) else ""
    if href:
        return urllib.parse.urlparse(href).netloc.lower().replace("www.", "")
    return ""


def fetch_and_filter(query, hours, lang, country, cutoff_time):
    url = build_feed_url(query, hours, lang, country)
    candidates = []
    try:
        parsed = feedparser.parse(url)
        if parsed.bozo and not parsed.entries:
            print(f"  [SKIP] query {query!r} ({lang}): feed did not parse", file=sys.stderr)
            return []
        for entry in parsed.entries:
            title = entry.get("title", "")
            domain = source_domain(entry)
            if domain and any(bad in domain for bad in EXCLUDED_SAUDI_DOMAINS):
                continue
            pub_struct = entry.get("published_parsed") or entry.get("updated_parsed")
            if pub_struct:
                pub_dt = datetime.fromtimestamp(time.mktime(pub_struct), tz=timezone.utc)
                if pub_dt < cutoff_time:
                    continue
                pub_iso = pub_dt.isoformat()
            else:
                pub_iso = None
            candidates.append({
                "query": query,
                "lang": lang,
                "title": title,
                "gnews_redirect_link": entry.get("link", ""),
                "source_domain_hint": domain or "UNKNOWN",
                "published": pub_iso,
                "date_confidence": "confirmed" if pub_iso else "UNKNOWN -- verify manually",
                "note": (
                    "UNVERIFIED candidate. gnews_redirect_link is a "
                    "news.google.com redirect, NOT a citable URL -- the "
                    "routine must resolve it to the real publisher URL, "
                    "verify in-window + non-Saudi-owned on the real domain, "
                    "and cite that. Never cite the redirect link."
                ),
            })
    except Exception as exc:
        print(f"  [SKIP] query {query!r} ({lang}): {exc}", file=sys.stderr)
        return []
    return candidates


def dedupe_by_title(candidates):
    seen = {}
    out = []
    for c in candidates:
        norm = re.sub(r"[^a-z0-9\u0600-\u06FF]+", " ", c["title"].lower()).strip()
        norm = " ".join(norm.split()[:10])
        if norm and norm not in seen:
            seen[norm] = True
            out.append(c)
    return out


def main():
    parser = argparse.ArgumentParser(description="Google News RSS culture-layer feed for Saudi Arabia/Regional")
    parser.add_argument("--hours", type=int, default=24)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    cutoff_time = datetime.now(timezone.utc) - timedelta(hours=args.hours)
    all_candidates = []
    for q in CULTURE_QUERIES_EN:
        all_candidates.extend(fetch_and_filter(q, args.hours, "en", "US", cutoff_time))
    for q in CULTURE_QUERIES_AR:
        all_candidates.extend(fetch_and_filter(q, args.hours, "ar", "SA", cutoff_time))

    deduped = dedupe_by_title(all_candidates)
    output = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "coverage_window_hours": args.hours,
        "queries_run": len(CULTURE_QUERIES_EN) + len(CULTURE_QUERIES_AR),
        "candidates_found": len(deduped),
        "candidates": deduped,
        "note": (
            "Google News RSS culture-layer candidates. Every one is "
            "UNVERIFIED and every gnews_redirect_link must be resolved to a "
            "real publisher URL before use. This feed targets the Saudi "
            "CULTURE layer only, never the geopolitical General bucket. "
            "Zero in-window candidates is a normal, expected outcome on "
            "many days given documented staleness -- fall back to "
            "WebSearch creative retrieval, do not treat an empty feed as "
            "'no culture today'."
        ),
    }
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"Ran {output['queries_run']} queries, found {len(deduped)} in-window candidates")
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
