# Saudi Culture Search Parameters — Audited & Expanded

## Why this file exists
An audit of the three existing Booleans (MoC / Commissions / Saudi Culture) plus
the supporting Google-style searches found they reliably catch:
- the **Ministry** and named **Minister / Vice Minister**,
- the **11 commissions** (by name, EN + AR), and
- **generic phrases** ("Saudi culture", "Saudi heritage", "Saudi film"…).

But they DO NOT catch the **named cultural bodies, venues, festivals, prizes and
executives** where a large share of English-language international coverage
actually lands. A story headlined *"Ithra opens…"*, *"Diriyah Biennale names…"*,
*"Film AlUla backs…"*, *"Jerry Inzerillo says…"* or *"MDLBEAST announces…"* would
only be caught by accident via a generic phrase. This is the Saudi-side coverage
hole (distinct from the Global-breadth hole).

The three existing Booleans are RETAINED unchanged. Add the blocks below.

---

## NEW BOOLEAN — Saudi Cultural Entities & Venues
Run alongside the existing three, last-24h window.

```
("Ithra" OR "King Abdulaziz Center for World Culture" OR "King Abdulaziz Centre for World Culture"
OR "Diriyah Company" OR "Diriyah Gate Development Authority" OR "DGDA"
OR "Royal Commission for AlUla" OR "RCU" OR "Film AlUla" OR "Arts AlUla" OR "Maraya"
OR "Misk Art Institute" OR "Misk Foundation" OR "Mohammed bin Salman Foundation"
OR "Red Sea Film Foundation" OR "Red Sea International Film Festival" OR "RSIFF" OR "Red Sea Souk"
OR "Cultural Development Fund" OR "Saudi Film Commission"
OR "National Museum of Saudi Arabia" OR "King Abdulaziz Public Library" OR "King Fahad National Library"
OR "King Fahad Cultural Center" OR "Royal Diriyah Opera House"
OR "SAMoCA" OR "Saudi Arabia Museum of Contemporary Art" OR "JAX District"
OR "Red Sea Global" OR "NEOM" OR "Qiddiya" OR "New Murabba" OR "King Salman Park"
OR "Hegra" OR "AlUla" OR "At-Turaif" OR "Historic Jeddah" OR "Al-Balad"
OR "General Commission for Audiovisual Media" OR "GCAM"
OR "Diriyah Biennale Foundation"
OR "Riyadh University of Arts" OR "RUA"
OR "Royal Institute of Traditional Arts" OR "Wrth"
OR "Art Jameel" OR "Hayy Jameel"
OR "Royal Commission for Riyadh City"
OR "Quality of Life Program" AND "Saudi")
```

## NEW BOOLEAN — Saudi Cultural Festivals, Seasons, Biennales & Prizes
```
("Diriyah Contemporary Art Biennale" OR "Diriyah Biennale"
OR "Islamic Arts Biennale"
OR "Desert X AlUla"
OR "Wadi AlFann" OR "Wadi Al-Fann"
OR "Noor Riyadh" OR "Riyadh Art" OR "Art Week Riyadh" OR "Tuwaiq Sculpture"
OR "AlUla Arts Festival" OR "Winter at Tantora" OR "AlUla Skies Festival" OR "Azimuth AlUla"
OR "Diriyah Season" OR "Jeddah Season" OR "Riyadh Season"
OR "MDLBEAST" OR "MDLBEAST Soundstorm" OR "Soundstorm"
OR "Ithra Art Prize" OR "Tanween"
OR "Red Sea Fashion Week" OR "Riyadh Fashion Week" OR "Saudi 100 Brands"
OR "Riyadh International Book Fair" OR "Jeddah Book Fair"
OR "Zarqa Al Yamama"
OR "Saudi Founding Day" OR "Founding Day"
OR "Year of Handicrafts" OR "Saudi Cultural Years"
OR "Saudi Cup" ) AND ("Saudi" OR "Riyadh" OR "Jeddah" OR "AlUla" OR "Diriyah" OR "KSA")
```
> Note: the trailing `AND (Saudi OR Riyadh…)` guards against name collisions
> (e.g. "Noor", "Tanween", generic "book fair", "Founding Day").

---

## 6-MONTH COVERAGE-FREQUENCY AUDIT (Feb–Jul 2026)
A review of international coverage over the past six months shows the following
programs/initiatives recur most frequently — ranked by observed prominence in
non-Saudi international media. These drive the Boolean expansions above.

**Tier 1 — near-continuous international coverage:**
1. **Diriyah Contemporary Art Biennale** — 3rd edition, 30 Jan–2 May 2026,
   "In Interludes and Transitions," JAX District. Organiser: **Diriyah Biennale
   Foundation** (CEO **Aya Al-Bakree**; co-artistic directors **Nora Razian** and
   **Sabih Ahmed**). Covered by SCMP, ArchDaily, art trades throughout Feb–May.
2. **Venice Biennale Saudi Pavilion** — **Dana Awartani**, 9 May–22 Nov 2026;
   commissioned by the **Visual Arts Commission** (CEO **Dina Amin**), curated by
   **Antonia Carver** (Art Jameel). Rolling coverage since Nov 2025, ongoing
   through the Biennale's run.
3. **The AlUla cluster** — **Desert X AlUla 2026** ("Space Without Measure";
   Neville Wakefield, Raneem Farsi, Wejdan Reda, Zoé Whitley), **AlUla Arts
   Festival**, **Wadi AlFann** land-art commissions (James Turrell, Michael
   Heizer, Agnes Denes, Manal AlDowayan, Ahmed Mater; lead curator Iwona
   Blazwick — permanent works due end-2026), Winter at Tantora, AlUla Skies.
4. **Film-sector incentives + Cannes presence** — the 60% rebate story, Film
   AlUla, RSIFF/Red Sea Film Foundation, Indonesia/Saudi co-operation.

**Tier 2 — strong seasonal/recurring coverage:**
5. **Riyadh Fashion Week** (3rd edition Oct 2026) + **Saudi 100 Brands** —
   Fashion Commission (CEO **Burak Cakmak**); WWD/FashionNetwork cover heavily.
6. **Tuwaiq Sculpture** (Riyadh Art / Royal Commission for Riyadh City) —
   2026 edition "Traces of What Will Be," Feb, 25 works, 18 countries.
7. **Islamic Arts Biennale** (Jeddah, alternate years with Diriyah) — next
   edition coverage will build through late 2026.
8. **Saudi Cultural Years program** — 2025 "Year of Handicrafts" retrospectives
   still generating coverage; sequence: Calligraphy → Saudi Coffee (2022) →
   Arabic Poetry (2023) → Camel (2024) → Handicrafts (2025) → AI (2026).
9. **Zarqa Al Yamama** / **Royal Diriyah Opera House** — first Saudi opera;
   recurs in Met Opera partnership and opera-sector stories.
10. **Saudi Founding Day** (February) — scaled-up national cultural programming.

**Tier 3 — emerging/institutional (watch, will grow):**
11. **Riyadh University of Arts (RUA)** — first cohort Sept 2026; partners USC,
    Guildhall, AMDA, ESSEC.
12. **Royal Institute of Traditional Arts (Wrth)** — CEO **Suzan Alyahya**;
    Quality of Life Program initiative under MoC.
13. **Art Jameel / Hayy Jameel (Jeddah)** — private foundation, key connective
    tissue to the international art world (director Antonia Carver).
14. **Cultural Development Fund (CDF)** and **Quality of Life Program** —
    financing/policy vehicles behind most of the above.
15. **Literature, Publishing & Translation Commission international book-fair
    programme** — e.g. Guest of Honor at Damascus International Book Fair 2026;
    Triennale Milano design-museum partnership; Salone del Mobile collaboration
    (Architecture and Design Commission).

### Names to add to the executives Boolean (from the frequency audit)
```
OR "Aya Al-Bakree"        # CEO, Diriyah Biennale Foundation
OR "Dina Amin"            # CEO, Visual Arts Commission
OR "Burak Cakmak"         # CEO, Fashion Commission
OR "Suzan Alyahya"        # CEO, Royal Institute of Traditional Arts
OR "Dana Awartani"        # Venice Biennale 2026 Saudi Pavilion artist
OR "Manal AlDowayan"      # Wadi AlFann / former Venice pavilion artist
OR "Ahmed Mater"          # Wadi AlFann artist
OR "Antonia Carver"       # Art Jameel / Saudi Pavilion curator
```
> Artist names (Awartani, AlDowayan, Mater) are include-worthy because coverage
> of their international shows is de facto Saudi-culture coverage even when the
> article never says "Saudi Ministry of Culture."

## NEW BOOLEAN — Named cultural executives / spokespeople
Catches quote-led and profile coverage that never uses a generic culture phrase.
```
("Jerry Inzerillo"                       # CEO, Diriyah Company
OR "Faisal Baltyuor"                      # CEO, Red Sea Film Foundation
OR "Jomana Al-Rashid"                     # CEO SRMG / Chair RSIFF
OR "Nora Aldabal"                         # Arts AlUla
OR "Phillip Jones"                        # Chief Tourism Officer, RCU
OR "Farah Abushullaih"                    # head of museums, Ithra
OR "Abdullah Al-Ayaf" OR "Abdullah Al Ayaf" # Saudi Film Commission
OR "Hamed Fayez"                          # Vice Minister of Culture
OR "Prince Badr bin Abdullah bin Farhan") # Minister of Culture
```
> Turki Al-Sheikh / General Entertainment Authority (GEA) and Riyadh Season sit
> under **entertainment**, not MoC. Include GEA/Riyadh Season hits only where the
> story is genuinely cultural (art, music, heritage), and be careful NOT to imply
> MoC ownership of GEA activity.

---

## Supporting Google-style searches — ADDITIONS
Append to the existing supporting list (still last-24h):
- Ithra Dhahran
- Diriyah Biennale
- Islamic Arts Biennale Jeddah
- Film AlUla
- Red Sea International Film Festival
- Misk Art Institute
- Noor Riyadh
- MDLBEAST
- AlUla arts
- Saudi contemporary art
- Saudi pavilion Venice Biennale
- Saudi book fair
- Saudi opera
- Saudi National Museum
- Royal Diriyah Opera House
- Saudi UNESCO World Heritage
- Desert X AlUla
- Wadi AlFann
- Dana Awartani Venice
- Saudi 100 Brands
- Tuwaiq Sculpture
- Riyadh University of Arts
- Saudi Founding Day culture
- Saudi cultural year

---

## Classification note tie-in (dual-nature stories)
Some of the entities above generate stories that are *cultural in subject but
negative in framing for Saudi Arabia* (e.g. labour/heritage-impact criticism of a
giga-project, "artwashing"/"sportswashing" framings of a festival or acquisition).
Route those to **Negative Articles** using the entity-relative sentiment + salience
rule (see classification_rule.md), NOT to Saudi Arabia/Regional > General.

## Do-not-overclaim reminder
Presence of a body in these Booleans does not mean MoC owns it. Ithra is Aramco;
Misk is the MBS Foundation; RCU, Diriyah Company, Red Sea Global, NEOM, Qiddiya are
PIF giga-projects; RSIFF is the Red Sea Film Foundation. Attribute accurately and
do not imply Ministry involvement unless the story states it.
