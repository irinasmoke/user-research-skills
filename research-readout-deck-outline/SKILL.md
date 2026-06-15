---
name: research-readout-deck-outline
description: "Transform a study summary and participant summaries into a structured Slide Deck Outline.md optimized for conversion to a PowerPoint readout using research-readout-deck-builder. Use when preparing to build a research readout deck from study findings. Reads from Summary/ and participant folders in the workspace."
---

# Deck Outline Skill

Transform study summaries into a structured slide deck outline (`Slide Deck Outline.md`) optimized for conversion into a polished PowerPoint readout. The outline is a checkpoint — the user reviews and edits it before the deck is generated.

## Rules

- Ground every slide bullet, finding, and quote in source files. Do not fabricate content.
- Never fabricate quotes. Only use exact quotes found in cleaned VTT transcripts.
- Use `quote-tools` skill to select, clean, and format every participant quote.
- Be ruthlessly selective: **3–5 bullets per content slide maximum**.
- Prefer participant quotes that are vivid, specific, or surprising — not generic statements.
- Do not include every theme from the summary. Pick the 4–6 most important themes for the audience.
- Match the tone, style, and language found in reference reports in `ReferenceReports/` folder.

## Inputs

Gather all of the following from the workspace:

1. **Customer Table** — `Summary/Customer Table.md`
2. **Study-wide summary** — `Summary/Quick Pulse Summary*.md` (most recent)
3. **Individual participant summaries** — `P*/P* - Agent Summary.md` (all participants)
4. **Study metadata** — CSV file in the study root

## Workflow

### Step 1: Orient
Read all inputs. Identify:
- Study name, date range, number of participants
- Researcher/author (from CSV or file metadata)
- Study type (usability test, generative interviews, etc.)
- Top 4–6 themes from the Quick Pulse Summary

### Step 2: Select Quotes
For each theme, use `quote-tools` to:
- Find the strongest 1–2 quotes across all participant summaries
- Clean and format with attribution: `Name, Role at Company`
- Note the participant image filename (look for `.jpg`, `.png`, `.jpeg` in participant folder)

### Step 3: Build the Outline
Write the outline using the format below. Save to `Summary/Slide Deck Outline.md` (overwrite if exists).

After saving, tell the user:
> "Deck outline saved to `Summary/Slide Deck Outline.md`. Review and edit it, then run the `research-readout-deck-builder` skill to generate the PowerPoint."

---

## Deck Patterns

**Standard study deck** (usability test, generative interviews, prototype testing — the default):
- `title` → "Who We Talked To" `content` → **"Key Findings" `key-findings` slide** → sections → recommendations → `closing` → Appendix with `participant-table`
- Each major heading (H2) in the summary becomes a `section-header` slide. Each sub-finding (H3) becomes a `finding` slide.
- **`finding` is the primary slide type for learnings.** Each finding slide has the finding text at the top AND 2-3 supporting quotes with circle photos — all on ONE slide.
- Use `content` only for non-finding slides: "Who We Talked To," recommendations, minor issues lists.
- **Use quotes from different participants** — never put 3 quotes from the same person on one slide.

**Multi-round recurring study tracker** (special case — multiple named rounds with different participants each time):
- Per round: `section-header` → `participant-table` → `task-scenario` → `success-rate-table` → `two-column-comparison` → finding slides
- `task-scenario` and `success-rate-table` are **only for this pattern** — do not use in standard decks

**Participant table placement:**
- Multi-round tracker: inside each round section
- Standard study: Appendix only

---

## Outline Format

```
# Deck: [Study Name] — [Month Year]

## Slide 1: Title
- type: title
- title: [Study Name]
- subtitle: [Month Year] | [N] Participants
- author: [Researcher Name]

## Slide 2: Who We Talked To
- type: content
- title: Who We Talked To
- body:
  - [N] participants across [brief context]
  - [Study type]: [duration] sessions
  - [Key demographic detail]
  - [Key behavioral detail]

## Slide 3: Key Findings
- type: key-findings
- title: Key Findings
- sections:
  - **[Section 1: Descriptive theme label]**
  - [Short bullet — first key sub-finding]
  - [Short bullet — second sub-finding]
  - **[Section 2: Theme label]**
  - [Sub-finding bullet]
  - [Sub-finding bullet]

## Slide 4: [Section 1 Header]
- type: section-header
- title: [Section 1 — matches H2 from source]

## Slide 5: [Finding from Section 1]
- type: finding
- title: [Short punchy headline — the finding itself]
- body:
  - **[Bold lead sentence with key stat or insight.]** [Follow-up context.]
  - [Supporting detail 2]
  - [Supporting detail 3]
- photo-1: [P1 Name/image.png]
- quote-1: [Verbatim quote from participant]
- attribution-1: Name, Role at Company
- photo-2: [P2 Name/image.png]
- quote-2: [Verbatim quote from a DIFFERENT participant]
- attribution-2: Name, Role at Company
- notes:
  - [Extra quotes, caveats, or context for speaker notes]

...repeat section-header → finding pattern for each H2/H3...

## Slide N-1: Recommendations & Next Steps
- type: content
- title: [Action-oriented title]
- body:
  - [Recommendation 1]
  - [Recommendation 2]

## Slide N: Closing
- type: closing
- title: Thank You
- body:
  - [Researcher Name or contact info]

## Slide N+1: Appendix — Participants
- type: section-header
- title: Appendix

## Slide N+2: Participant Table
- type: participant-table
- title: Participants
- headers: # | Name | Role | Company | [Relevant columns]
- rows:
  - P1 | [Name] | [Role] | [Company] | [Details]
```

---

## Slide Types Reference

| Type | When to Use |
|------|-------------|
| `title` | Opening slide |
| `section-header` | Full blue background section divider |
| `key-findings` | Two-column numbered overview of all sections (always slide 3) |
| `finding` | **Primary type** — finding text + 2-3 quotes with circle photos |
| `content` | Bullet-point list only (recommendations, who-we-talked-to) |
| `two-column` | Simple side-by-side lists |
| `two-column-comparison` | "What went well / Challenges" with colored headings |
| `quote` | Single prominent quote with circle photo |
| `stacked-quotes` | 2–3 quotes stacked vertically with circle photos |
| `multi-quote-text` | Pure-text quote blocks, no photos |
| `content-photo` | Bullets + rectangular photo on right |
| `task-scenario` | Multi-round studies only |
| `success-rate-table` | Color-coded task completion (multi-round only) |
| `participant-table` | Rich participant profiles |
| `dual-screenshot` | Two screenshots side-by-side |
| `screenshot` | Finding + single screenshot |
| `screenshot-sequence` | Multi-step task walkthrough |
| `closing` | Final slide |

> **Style note:** All content slides use a plain large black bold title on white background. Titles are LEFT-ALIGNED on all slides except title and closing.

---

## Key Findings Slide Format
*(Always slide 3 — two-column numbered overview)*

```
- type: key-findings
- sections:
  - **Product-Market Fit: Who is Foundry perceived as being for?**
  - Less technical users (PMs) may be a better fit
  - Developers see it as prototyping only
  - **Knowledge Flow**
  - 100% added all 3 sources once in the right place
  - ServiceNow seen as a "tool," not knowledge
```

- Each `**Bold heading**` starts a new numbered section
- Section heading = the THEME as a descriptive label or question (rephrase to be meaningful on its own)
- Bullets = key sub-findings distilled to **short phrases** (~3–8 words)
- Every section MUST have 2–5 bullets

---

## Content Guidelines

### Headline Writing
- **Do**: "ServiceNow Is Seen as a Tool, Not a Knowledge Source"
- **Don't**: "Finding 1: ServiceNow Belongs in Tools" — never prefix with "Finding N:"
- Lead with the finding itself, stated as a fact or observation

### Bullet Points
- Start with a number or strong verb when possible: "3/5 participants...", "All teams reported..."
- One idea per bullet; maximum 5 bullets per slide

### Quote Selection
- Pick vivid, specific, or emotionally resonant quotes
- Avoid quotes that just restate a bullet point
- Prefer quotes with a concrete scenario over abstract opinions
- Length: aim for 1–3 sentences after cleaning

## Integration with Other Skills
- **quote-tools**: Select, clean, and format all participant quotes
- **study-report-writer**: Produces the study summary this skill reads from
- **research-readout-deck-builder**: Consumes the `Slide Deck Outline.md` this skill produces
