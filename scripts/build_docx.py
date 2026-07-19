#!/usr/bin/env python3
"""
Build the MoC Daily Cultural Digest .docx from its canonical markdown, using
python-docx. The canonical markdown is the single source of truth; this
script is a faithful renderer, not an editor.

WHY python-docx INSTEAD OF DIRECT XML ON A PINNED TEMPLATE:
The conflict-monitoring skill this repo was adapted from edits a pre-branded,
SHA-256-pinned template directly via XML, for exact brand fidelity. This repo
does not yet have a real branded MoC Word template to pin, so it builds a
clean, professionally formatted document from scratch instead. Once a real
branded template (letterhead, logo, house styles) is supplied, swap this
script for the pinned-template direct-XML-edit approach the same way the
conflict-monitoring skill does -- see templates/README.md for how to pin one.

CANONICAL MARKDOWN FORMAT this script expects (see SKILL.md Stage 3,
confirmed against a real delivered edition on 2026-07-19):

    # Headlines, <DATE>

    ## Saudi Arabia/Regional
    - Headline one
    - Headline two

    ## Negative Articles
    - Headline one

    ## Global
    - Headline one

    # Saudi Arabia/Regional

    ## General (عام)
    - Free-form analytical bullet ending in a plain citation. ([Outlet](url))

    ## Heritage (التراث)
    - ...

    # Negative Articles
    - Bullets go directly here -- NO commission subheadings in this section.
    - ([Outlet](url))

    # Global

    ## Museums (المتاحف)
    - ...

    # Risks and Opportunities

    ## Risks

    1. **Short bold headline naming the specific risk**
    Analytical paragraph.
    Source: [Outlet](url), [Outlet](url)
    Consideration: paragraph.

    2. **A second risk, if supported**
    Paragraph.
    Source: [Outlet](url)
    Consideration: paragraph.

    ## Opportunities

    1. **Short bold headline naming the specific opportunity**
    Paragraph.
    Source: [Outlet](url), [Outlet](url), [Outlet](url)
    Consideration: paragraph.

Note: each of Risks/Opportunities restarts its own numbering at 1, and each
subsection can have one or more items -- the count isn't fixed.

Usage:
    python3 scripts/build_docx.py reports/MoC_Digest_2026-07-19.md \\
        --output reports/MoC_Digest_2026-07-19.docx
"""

import argparse
import re
import sys
from pathlib import Path

from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

FONT_NAME = "Arial"
FONT_SIZE = 11

MD_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
NUMBERED_ITEM_RE = re.compile(r"^\s*(\d+)\.\s*(.*)$")
BOLD_HEADLINE_RE = re.compile(r"^\*\*(.+?)\*\*\s*$")

REQUIRED_SECTIONS = ["Saudi Arabia/Regional", "Negative Articles", "Global"]
# Sections that use commission subheadings in the full-summary block.
# Negative Articles is deliberately excluded, per confirmed real production.
SECTIONS_WITH_SUBHEADINGS = {"Saudi Arabia/Regional", "Global"}


def add_hyperlink(paragraph, text, url):
    """
    Insert a real clickable hyperlink run into a python-docx paragraph.
    python-docx has no native hyperlink API, so this builds the relationship
    and run XML directly -- the standard recipe for this library.
    """
    part = paragraph.part
    r_id = part.relate_to(
        url,
        "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink",
        is_external=True,
    )

    hyperlink = OxmlElement("w:hyperlink")
    hyperlink.set(qn("r:id"), r_id)

    run = OxmlElement("w:r")
    rpr = OxmlElement("w:rPr")

    color = OxmlElement("w:color")
    color.set(qn("w:val"), "0563C1")
    rpr.append(color)

    underline = OxmlElement("w:u")
    underline.set(qn("w:val"), "single")
    rpr.append(underline)

    rFonts = OxmlElement("w:rFonts")
    rFonts.set(qn("w:ascii"), FONT_NAME)
    rFonts.set(qn("w:hAnsi"), FONT_NAME)
    rpr.append(rFonts)

    run.append(rpr)
    text_el = OxmlElement("w:t")
    text_el.set(qn("xml:space"), "preserve")
    text_el.text = text
    run.append(text_el)
    hyperlink.append(run)

    paragraph._p.append(hyperlink)
    return hyperlink


def add_mixed_text_with_links(paragraph, text_with_md_links, bold=False):
    """
    Adds text to a paragraph that may contain one or more markdown-style
    [label](url) links (bullet citations, or comma-separated Source lines).
    Plain text is added as normal runs; each link becomes a real hyperlink.
    """
    remainder = text_with_md_links
    any_match = False
    while True:
        match = MD_LINK_RE.search(remainder)
        if not match:
            if remainder:
                run = paragraph.add_run(remainder)
                run.bold = bold
            break
        any_match = True
        if remainder[: match.start()]:
            run = paragraph.add_run(remainder[: match.start()])
            run.bold = bold
        add_hyperlink(paragraph, match.group(1), match.group(2))
        remainder = remainder[match.end() :]
    return any_match


def set_base_style(doc):
    style = doc.styles["Normal"]
    style.font.name = FONT_NAME
    style.font.size = Pt(FONT_SIZE)
    rpr = style.element.get_or_add_rPr()
    rFonts = rpr.find(qn("w:rFonts"))
    if rFonts is None:
        rFonts = OxmlElement("w:rFonts")
        rpr.append(rFonts)
    rFonts.set(qn("w:ascii"), FONT_NAME)
    rFonts.set(qn("w:hAnsi"), FONT_NAME)


def split_h1_blocks(md_text):
    """Splits markdown into (h1_name, h1_body_lines) blocks, in order."""
    blocks = []
    current_name = None
    current_lines = []
    for line in md_text.split("\n"):
        if line.startswith("# ") and not line.startswith("## "):
            if current_name is not None:
                blocks.append((current_name, current_lines))
            current_name = line[2:].strip()
            current_lines = []
        else:
            current_lines.append(line)
    if current_name is not None:
        blocks.append((current_name, current_lines))
    return blocks


def parse_headline_block(h1_lines):
    """Parses the 'Headlines, <date>' block into {section: [headline, ...]}."""
    result = {}
    current_h2 = None
    for line in h1_lines:
        if line.startswith("## "):
            current_h2 = line[3:].strip()
            result.setdefault(current_h2, [])
        elif line.strip().startswith("- ") and current_h2:
            result[current_h2].append(line.strip()[2:].strip())
    return result


def parse_full_summary_block(h1_name, h1_lines):
    """
    Parses a full-summary section into {commission_label: [bullet, ...]}.
    Sections in SECTIONS_WITH_SUBHEADINGS use ## commission subheadings;
    Negative Articles (and any other section not in that set) has bullets
    directly under the H1, with no subheading -- stored under a single
    implicit "" key.
    """
    result = {}
    if h1_name in SECTIONS_WITH_SUBHEADINGS:
        current_h2 = None
        for line in h1_lines:
            if line.startswith("## "):
                current_h2 = line[3:].strip()
                result.setdefault(current_h2, [])
            elif line.strip().startswith("- ") and current_h2:
                result[current_h2].append(line.strip()[2:].strip())
    else:
        result[""] = []
        for line in h1_lines:
            if line.strip().startswith("- "):
                result[""].append(line.strip()[2:].strip())
    return result


def parse_risks_opportunities_block(h1_lines):
    """
    Parses the Risks and Opportunities block into:
    {
        "risks": [ {"headline": str, "paragraph": str, "source": str, "consideration": str}, ... ],
        "opportunities": [ ... ],
    }
    Each ## subsection contains one or more numbered items. An item starts
    at a line matching NUMBERED_ITEM_RE and runs until the next numbered
    item or the end of the subsection.
    """
    result = {"risks": [], "opportunities": []}
    current_h2 = None
    item_lines = []

    def flush_item():
        if not item_lines:
            return
        text = "\n".join(item_lines).strip()
        if not text:
            return

        lines = text.split("\n")
        # First line: strip the leading "N. " if present, then strip **bold**
        first_line = lines[0]
        num_match = NUMBERED_ITEM_RE.match(first_line)
        headline_raw = num_match.group(2).strip() if num_match else first_line.strip()
        bold_match = BOLD_HEADLINE_RE.match(headline_raw)
        headline = bold_match.group(1).strip() if bold_match else headline_raw

        body = "\n".join(lines[1:]).strip()
        source_match = re.search(r"Source:\s*(.+?)(?:\nConsideration:|$)", body, re.DOTALL)
        consideration_match = re.search(r"Consideration:\s*(.+)", body, re.DOTALL)

        if source_match:
            paragraph = body[: source_match.start()].strip()
        else:
            paragraph = body.strip()

        item = {
            "headline": headline,
            "paragraph": paragraph,
            "source": source_match.group(1).strip() if source_match else "",
            "consideration": consideration_match.group(1).strip() if consideration_match else "",
        }
        key = current_h2.lower() if current_h2 else "risks"
        result.setdefault(key, []).append(item)

    for line in h1_lines:
        if line.startswith("## "):
            flush_item()
            item_lines = []
            current_h2 = line[3:].strip()
        elif NUMBERED_ITEM_RE.match(line.strip()) and item_lines:
            # A new numbered item starts -- flush the previous one first
            flush_item()
            item_lines = [line.strip()]
        elif line.strip():
            item_lines.append(line.strip())
    flush_item()

    return result


def parse_markdown(md_text):
    """
    Parses the full canonical markdown into:
    {
        "title": "Headlines, 19 July 2026",
        "headline_bullets": {section: [headline, ...]},
        "sections": {section: {commission_label: [bullet, ...]}},
        "risks_and_opportunities": {"risks": [...], "opportunities": [...]},
    }
    """
    blocks = split_h1_blocks(md_text)
    result = {
        "title": "",
        "headline_bullets": {},
        "sections": {},
        "risks_and_opportunities": {},
    }
    seen_headline_block = False

    for h1_name, h1_lines in blocks:
        if h1_name.startswith("Headlines,"):
            result["title"] = h1_name
            result["headline_bullets"] = parse_headline_block(h1_lines)
            seen_headline_block = True
        elif h1_name in REQUIRED_SECTIONS:
            result["sections"][h1_name] = parse_full_summary_block(h1_name, h1_lines)
        elif h1_name == "Risks and Opportunities":
            result["risks_and_opportunities"] = parse_risks_opportunities_block(h1_lines)

    if not seen_headline_block:
        print("WARNING: no 'Headlines, <date>' block found in markdown", file=sys.stderr)

    return result


def build_docx(parsed, output_path):
    doc = Document()
    set_base_style(doc)

    # Title
    title_p = doc.add_paragraph()
    title_run = title_p.add_run(parsed["title"] or "MoC Daily Cultural Digest")
    title_run.bold = True
    title_run.font.size = Pt(16)
    title_p.alignment = WD_ALIGN_PARAGRAPH.LEFT

    # Headline bullets FIRST (confirmed real ordering), three sections
    for section_name in REQUIRED_SECTIONS:
        bullets = parsed["headline_bullets"].get(section_name, [])
        heading = doc.add_paragraph()
        run = heading.add_run(section_name)
        run.bold = True
        run.font.size = Pt(13)
        for bullet_text in bullets:
            p = doc.add_paragraph(style="List Bullet")
            p.add_run(bullet_text)

    doc.add_page_break()

    # Full summaries, grouped by section then (where applicable) commission
    for section_name in REQUIRED_SECTIONS:
        section_heading = doc.add_paragraph()
        run = section_heading.add_run(section_name)
        run.bold = True
        run.font.size = Pt(15)

        commissions = parsed["sections"].get(section_name, {})
        for commission_name, bullets in commissions.items():
            if not bullets:
                continue
            if commission_name:  # empty string = no subheading (Negative Articles)
                commission_heading = doc.add_paragraph()
                run = commission_heading.add_run(commission_name)
                run.bold = True
                run.italic = True
                run.font.size = Pt(12)

            for bullet_text in bullets:
                p = doc.add_paragraph(style="List Bullet")
                add_mixed_text_with_links(p, bullet_text)

    doc.add_page_break()

    # Risks and Opportunities: multiple numbered items per subsection
    ro_heading = doc.add_paragraph()
    run = ro_heading.add_run("Risks and Opportunities")
    run.bold = True
    run.font.size = Pt(15)

    ro = parsed.get("risks_and_opportunities", {})
    for label in ["risks", "opportunities"]:
        items = ro.get(label, [])
        if not items:
            continue

        sub_heading = doc.add_paragraph()
        run = sub_heading.add_run(label.capitalize())
        run.bold = True
        run.font.size = Pt(13)

        for idx, item in enumerate(items, start=1):
            headline_p = doc.add_paragraph()
            run = headline_p.add_run(f"{idx}. {item['headline']}")
            run.bold = True

            if item.get("paragraph"):
                p = doc.add_paragraph()
                p.add_run(item["paragraph"])

            if item.get("source"):
                p = doc.add_paragraph()
                run = p.add_run("Source: ")
                run.bold = True
                add_mixed_text_with_links(p, item["source"])

            if item.get("consideration"):
                p = doc.add_paragraph()
                run = p.add_run("Consideration: ")
                run.bold = True
                p.add_run(item["consideration"])

    doc.save(output_path)
    print(f"Wrote {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Build the MoC Daily Cultural Digest .docx")
    parser.add_argument("markdown_path", help="Path to the canonical markdown digest")
    parser.add_argument("--output", required=True, help="Output .docx path")
    args = parser.parse_args()

    md_text = Path(args.markdown_path).read_text(encoding="utf-8")
    parsed = parse_markdown(md_text)
    build_docx(parsed, args.output)


if __name__ == "__main__":
    main()
