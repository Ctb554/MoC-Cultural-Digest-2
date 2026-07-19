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

CANONICAL MARKDOWN FORMAT this script expects (see SKILL.md Stage 3):

    # Headlines, <DATE>

    ## Saudi Arabia/Regional
    - Headline one
    - Headline two

    ## Negative Articles
    - Headline one

    ## Global
    - Headline one

    # Saudi Arabia/Regional

    ## General
    - [Outlet] reported that ... . The article is relevant as a ... item,
      ... . ([Outlet](https://example.com/article))

    ## Museums
    - ...

    # Negative Articles

    ## General
    - ...

    # Global

    ## Film
    - ...

    # Risks and Opportunities

    ## Risks

    1. [paragraph]

    Source: [Outlet](url), [Outlet](url)

    Consideration: [paragraph]

    ## Opportunities

    2. [paragraph]

    Source: [Outlet](url), [Outlet](url)

    Consideration: [paragraph]

Usage:
    python3 scripts/build_docx.py reports/MoC_Digest_2026-07-19.md \\
        --output reports/MoC_Digest_2026-07-19.docx
"""

import argparse
import re
import sys
from pathlib import Path

from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

FONT_NAME = "Arial"
FONT_SIZE = 11
HYPERLINK_COLOR = RGBColor(0x05, 0x63, 0xC1)

MD_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


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


def add_mixed_text_with_link(paragraph, text_with_md_link):
    """
    Adds text to a paragraph where exactly one markdown-style [label](url)
    link may be present (the outlet-name link at the end of a bullet, per
    the digest's link-only-in-outlet-name rule). Plain text before/after the
    link is added as normal runs; the link itself becomes a real hyperlink.
    """
    match = MD_LINK_RE.search(text_with_md_link)
    if not match:
        paragraph.add_run(text_with_md_link)
        return

    before = text_with_md_link[: match.start()]
    label = match.group(1)
    url = match.group(2)
    after = text_with_md_link[match.end() :]

    if before:
        paragraph.add_run(before)
    add_hyperlink(paragraph, label, url)
    if after:
        paragraph.add_run(after)


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


def parse_markdown(md_text):
    """
    Parses the canonical markdown into a structure:
    {
        "title": "Headlines, 19 July 2026",
        "headline_bullets": {"Saudi Arabia/Regional": [...], "Negative Articles": [...], "Global": [...]},
        "sections": {
            "Saudi Arabia/Regional": {"General": [bullet_text, ...], "Museums": [...]},
            "Negative Articles": {"General": [...]},
            "Global": {"Film": [...], ...},
        },
        "risks_and_opportunities": {
            "risks": {"paragraph": "...", "source": "...", "consideration": "..."},
            "opportunities": {"paragraph": "...", "source": "...", "consideration": "..."},
        }
    }
    """
    lines = md_text.split("\n")
    result = {
        "title": "",
        "headline_bullets": {},
        "sections": {},
        "risks_and_opportunities": {},
    }

    # Split into top-level (#) blocks
    blocks = []
    current_h1 = None
    current_lines = []
    for line in lines:
        if line.startswith("# ") and not line.startswith("## "):
            if current_h1 is not None:
                blocks.append((current_h1, current_lines))
            current_h1 = line[2:].strip()
            current_lines = []
        else:
            current_lines.append(line)
    if current_h1 is not None:
        blocks.append((current_h1, current_lines))

    headline_h1_names = {"Saudi Arabia/Regional", "Negative Articles", "Global"}
    seen_headline_block = False

    for h1_name, h1_lines in blocks:
        if h1_name.startswith("Headlines,"):
            result["title"] = h1_name
            # This block contains the headline-bullet sub-sections
            current_h2 = None
            for line in h1_lines:
                if line.startswith("## "):
                    current_h2 = line[3:].strip()
                    result["headline_bullets"].setdefault(current_h2, [])
                elif line.strip().startswith("- ") and current_h2:
                    result["headline_bullets"][current_h2].append(line.strip()[2:].strip())
            seen_headline_block = True

        elif h1_name in headline_h1_names:
            # This is a full-summary section (second occurrence of these names)
            current_h2 = None
            section_dict = result["sections"].setdefault(h1_name, {})
            for line in h1_lines:
                if line.startswith("## "):
                    current_h2 = line[3:].strip()
                    section_dict.setdefault(current_h2, [])
                elif line.strip().startswith("- ") and current_h2:
                    section_dict[current_h2].append(line.strip()[2:].strip())

        elif h1_name == "Risks and Opportunities":
            current_h2 = None
            buffer = []
            ro = {}

            def flush(label):
                text = "\n".join(buffer).strip()
                if not text:
                    return
                para_match = re.match(r"^\d+\.\s*(.*)", text, re.DOTALL)
                source_match = re.search(r"Source:\s*(.+)", text)
                consideration_match = re.search(r"Consideration:\s*(.+)", text, re.DOTALL)
                ro[label] = {
                    "paragraph": para_match.group(1).split("\n\nSource:")[0].strip() if para_match else text,
                    "source": source_match.group(1).strip() if source_match else "",
                    "consideration": consideration_match.group(1).strip() if consideration_match else "",
                }

            for line in h1_lines:
                if line.startswith("## "):
                    if current_h2:
                        flush(current_h2.lower())
                    current_h2 = line[3:].strip()
                    buffer = []
                else:
                    buffer.append(line)
            if current_h2:
                flush(current_h2.lower())

            result["risks_and_opportunities"] = ro

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

    # Headline bullets (three sections, in fixed order)
    for section_name in ["Saudi Arabia/Regional", "Negative Articles", "Global"]:
        bullets = parsed["headline_bullets"].get(section_name, [])
        heading = doc.add_paragraph()
        run = heading.add_run(section_name)
        run.bold = True
        run.font.size = Pt(13)
        for bullet_text in bullets:
            p = doc.add_paragraph(style="List Bullet")
            p.add_run(bullet_text)

    doc.add_page_break()

    # Full summaries, grouped by section then commission
    for section_name in ["Saudi Arabia/Regional", "Negative Articles", "Global"]:
        section_heading = doc.add_paragraph()
        run = section_heading.add_run(section_name)
        run.bold = True
        run.font.size = Pt(15)

        commissions = parsed["sections"].get(section_name, {})
        for commission_name, bullets in commissions.items():
            if not bullets:
                continue
            commission_heading = doc.add_paragraph()
            run = commission_heading.add_run(commission_name)
            run.bold = True
            run.italic = True
            run.font.size = Pt(12)

            for bullet_text in bullets:
                p = doc.add_paragraph(style="List Bullet")
                add_mixed_text_with_link(p, bullet_text)

    doc.add_page_break()

    # Risks and Opportunities
    ro_heading = doc.add_paragraph()
    run = ro_heading.add_run("Risks and Opportunities")
    run.bold = True
    run.font.size = Pt(15)

    ro = parsed.get("risks_and_opportunities", {})
    for label in ["risks", "opportunities"]:
        entry = ro.get(label)
        if not entry:
            continue
        sub_heading = doc.add_paragraph()
        run = sub_heading.add_run(label.capitalize())
        run.bold = True
        run.font.size = Pt(13)

        p = doc.add_paragraph()
        p.add_run(entry["paragraph"])

        if entry.get("source"):
            p = doc.add_paragraph()
            run = p.add_run("Source: ")
            run.bold = True
            # Source line may contain multiple [Outlet](url) links comma-separated
            remainder = entry["source"]
            while True:
                match = MD_LINK_RE.search(remainder)
                if not match:
                    if remainder.strip():
                        p.add_run(remainder)
                    break
                if remainder[: match.start()]:
                    p.add_run(remainder[: match.start()])
                add_hyperlink(p, match.group(1), match.group(2))
                remainder = remainder[match.end() :]

        if entry.get("consideration"):
            p = doc.add_paragraph()
            run = p.add_run("Consideration: ")
            run.bold = True
            p.add_run(entry["consideration"])

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
