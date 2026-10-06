---
name: research-readout-deck-outline
description: "Transform a research report into a source-faithful Slide Deck Outline.md for a PowerPoint readout using research-readout-deck-builder. Use when creating or revising a research readout outline. Preserves report wording, findings, quotes, diagrams, and recommendations; uses only the user's authorized sources."
---

# Deck Outline Skill

Transform a research report into a structured slide deck outline (`Slide Deck Outline.md`) optimized for conversion into a polished PowerPoint readout. This is a change of presentation format, not a new research synthesis. The outline is a checkpoint — the user reviews and edits it before the deck is generated.

## Rules

- Ground every title, bullet, finding, quote, recommendation, and study detail in the authorized sources. Do not invent statistics, outcomes, priorities, requirements, or claims about what the user requested.
- Preserve the report's finding titles, terminology, meaning, organization, and uncertainty. Do not silently reframe, rename, merge, or omit distinct findings.
- Never fabricate quotes. When a report is the sole source, copy its quotes and attributions exactly. Do not imply they were checked against transcripts you did not read.
- Use `quote-tools` for quote selection and verification within the authorized source scope. Do not clean or rewrite already approved report quotes unless asked.
- Keep slide bodies skimmable: **at most five bullets**, with fewer when sufficient. Do not add filler to meet a minimum. The Key Learnings overview and participant table have their own formats.
- Prefer participant quotes that are vivid, specific, or surprising — not generic statements.
- By default, cover the report's findings rather than choosing an arbitrary subset. Select or merge themes only when the user requests a shorter or audience-focused deck; ask before making a substantial content cut if the scope is unclear.
- Layout defaults are not user requirements. Do not invent slide-count limits, recommendation caps, or category quotas, or describe a skill default or assistant choice as something the user asked for.
- Match the source report's voice. Consult `ReferenceReports/` only when authorized and useful for style, never as evidence for this study.
- Preserve user edits to an existing outline. Do not change the report, generate a PowerPoint, or create or modify a hosted slide page unless requested.

## Inputs

### Source selection

1. If the user names a report or file, read that file first and treat it as the canonical content source. If they say it contains everything or is the sole source, do not open participant summaries, transcripts, Word equivalents, metadata, or Microsoft 365 materials to supplement it.
2. If no source is named, identify the current report in `Summary/`. Do not assume it is named `Quick Pulse Summary*.md`. If multiple reports could be canonical and the choice is unclear, ask which to use.
3. Read the complete canonical report before outlining it, including detailed findings, recommendations, diagrams, tables, and limitations. Preserve its current wording, including user edits.
4. Use additional evidence only when the user authorizes it or the task explicitly calls for a fresh synthesis. Missing information is not permission to broaden the source scope.

### Additional inputs when authorized

These are optional supplements, not mandatory prerequisites:

- **Customer Table** — `Summary/Customer Table.md`
- **Individual participant summaries** — `P*/P* - Agent Summary.md`
- **Study metadata** — CSV file in the study root
- **Cleaned transcripts** — for new quote extraction or transcript-level verification

Existing screenshots, photos, and logos may be checked as presentation assets without treating them as additional research evidence. Do not inspect unrelated files while locating them.

## Workflow

### Step 1: Orient
Read the canonical report and any explicitly authorized supplements. Identify:
- Study name, date range, participant count, author, and study type, only where stated
- Report sections, distinct findings, recommendations, limitations, and supporting evidence
- Diagrams and other visuals that belong with particular findings

Build a source-to-slide mapping in working context before writing. Use detailed finding headings as learning titles. If there is no finding heading, use an existing finding sentence verbatim rather than inventing a headline. Use that same title on the overview and corresponding slide. If the report's overview and detailed findings differ materially, ask rather than silently reconciling them into a new finding.

Omit unavailable metadata or clearly flag it as missing in notes. Ask only if it blocks the requested deliverable; do not guess dates, methods, participant roles, or authors from unrelated files.

### Step 2: Select Quotes
For each finding, use `quote-tools` within the authorized source scope to:
- Select the strongest supporting quotes already in the report when building from a report
- Extract and verify new quotes from participant materials only when those sources are authorized
- Preserve report quote text and attribution; for new quotes, use `Name, Role at Company` only when those details are supported and permitted
- Note an existing participant image path when available; do not require a photo or broaden the evidence search to fill a layout

Prefer quotes from different participants when available. Use one or no quotes if that is all the report provides. Do not fabricate, repeat, or borrow unrelated quotes to fill a two- or three-quote layout.

### Step 3: Build the Outline
Write the outline using the format below. Preserve section order, distinct findings, recommendation categories, and caveats from the report. Condense supporting prose without changing its meaning; do not replace source headings with punchier interpretations.

Include a brief source note in the outline identifying the canonical report with a relative link. Use slide notes to identify the source heading for findings and recommendations where traceability is not otherwise clear. Include existing visuals as described below.

Save to `Summary/Slide Deck Outline.md` unless the user specifies another location. If revising an existing outline, integrate user edits and preserve valid assets and callout notes.

### Step 4: Validate before claiming completion

Check the saved outline against the authorized source:
- Slide numbers are sequential. Learning numbers are continuous, and each overview item has exactly one matching numbered learning slide with identical wording.
- Every finding title is a source heading or verbatim finding sentence unless the user explicitly authorized rewriting it.
- Every bullet and recommendation is supported; no distinct required finding is omitted or silently merged, and no removed recommendation is reintroduced from another source.
- Every quote and attribution matches its authorized source. If quote cleaning was requested, verify the edits using `quote-tools` and identify them.
- Diagrams match the source exactly, including labels, decision criteria, branches, and return loops.
- Referenced image files exist, paths resolve relative to the outline, and screenshots depict the claimed UI. Prototype illustrations and sample counts are not presented as research measurements.
- Each slide body has at most five bullets. Missing metadata, missing assets, and rendering limitations are explicitly identified, not concealed by placeholders presented as completed work.

Fix failed checks before reporting completion. Mechanical checks of titles, quotes, and paths do not replace checking the meaning of bullets against the report.

After saving and validating, link to the outline and briefly state what was verified and any remaining limitations. Say that the outline is ready for review; offer `research-readout-deck-builder` as a separate next step, without generating the deck automatically. Distinguish included Mermaid source from a rendered diagram image.

---

## Deck Patterns

**Standard study deck** (usability test, generative interviews, prototype testing — the default):
- `title` → **"Study Background" `study-background`** → **"Key Learnings" `key-findings`** → sections → numbered learning slides → recommendations → `closing` → Appendix with `participant-table`
- The Study Background slide gives the audience enough context to interpret the learnings before they see them. It MUST include:
  - A short introduction to the product, concept, workflow, or research question
  - Study goals
  - Customer profile and/or methods; include both when the available space and source material allow
  - Participant photos, names, roles, companies, and/or company logos when those assets are available and useful
- Do not create a separate "Who We Talked To" slide by default. Incorporate participant and customer context into Study Background. Use a separate participant slide only when the customer profiles need substantially more space.
- The Key Learnings slide groups learnings under descriptive theme headings and numbers every learning continuously across sections.
- Every learning slide MUST use the same number and wording as its corresponding item on the Key Learnings slide.
- Each major findings heading (H2) in the report becomes a `section-header` slide. Each distinct sub-finding (H3) becomes a `finding` slide. Recommendations, background, and appendix sections use their appropriate slide types.
- **`finding` is the primary slide type for learnings.** Put finding text and supporting evidence on one slide where possible. Prefer 2-3 quotes with circle photos when supported; one or no quotes and missing photos are acceptable. A source diagram may be the main visual instead of quotes or a screenshot.
- Use `content` only for non-finding slides: recommendations and minor issues lists.
- Prefer quotes from different participants; do not add quotes solely to meet a layout quota.

**Multi-round recurring study tracker** (special case — multiple named rounds with different participants each time):
- Per round: `section-header` → `participant-table` → `task-scenario` → `success-rate-table` → `two-column-comparison` → finding slides
- `task-scenario` and `success-rate-table` are **only for this pattern** — do not use in standard decks

**Participant table placement:**
- Multi-round tracker: inside each round section
- Standard study: Appendix only
- Preserve source table columns, omissions, and anonymization. Do not restore participant names or other identifying details that the user removed.

**Recommendations:**
- Retain the report's recommendation wording, categories, and priorities where stated. Split across as many slides as needed for readability; there is no fixed recommendation-slide cap.
- Keep findings distinct from recommendations. A finding does not automatically authorize adding a TODO that the report's recommendations omit.
- Preserve links to a detailed backlog when present; do not import extra backlog items unless requested.

---

## Outline Format

```
# Deck: [Study Name] — [Month Year]

## Slide 1: Title
- type: title
- title: [Study Name]
- subtitle: [Month Year] | [N] Participants
- author: [Researcher Name]

## Slide 2: Study Background
- type: study-background
- title: Study Background
- intro: [2–4 sentence introduction to the product, concept, workflow, or research question]
- goals:
  - [Goal 1]
  - [Goal 2]
  - [Goal 3]
- methods:
  - [Study method and session format]
  - [What participants reviewed or did]
  - [What the study covered]
- customer-profile:
  - [Participant count and key roles]
  - [Relevant company, industry, platform, or behavioral mix]
- participants:
  - [Name] | [Role] | [Company] | [Photo or logo path, when available]

## Slide 3: Key Learnings
- type: key-findings
- title: Key Learnings
- sections:
  - **[Section 1: Descriptive theme label]**
  - 1. [First learning headline]
  - 2. [Second learning headline]
  - **[Section 2: Theme label]**
  - 3. [Third learning headline]
  - 4. [Fourth learning headline]

## Slide 4: [Section 1 Header]
- type: section-header
- title: [Section 1 — matches H2 from source]

## Slide 5: 1. [Learning from Section 1]
- type: finding
- learning-number: 1
- title: 1. [Same learning headline used on the Key Learnings slide]
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
| `study-background` | Study introduction, goals, customer profile, and/or methods |
| `section-header` | Full blue background section divider |
| `key-findings` | Numbered overview of learnings grouped into themed columns (always slide 3; title it "Key Learnings") |
| `finding` | **Primary type** — source finding with available quotes and/or its source diagram |
| `content` | Bullet-point list only (recommendations and minor issues) |
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

## Study Background Slide Format
*(Always slide 2)*

- Use the title **Study Background** unless the source or reference deck strongly supports a more specific title such as **Study Goals & Methods**.
- Start with a short introduction that explains what was studied and why.
- Include a **Goals** section.
- Include a **Customer Profile** and/or **Methods** section. Prefer both when the content fits without shrinking the slide excessively.
- Methods may cover session format, duration, sample, prototype or concept shown, tasks, and feedback activities.
- Customer Profile may cover participant count, roles, industries, company sizes, platform context, relevant experience, or behaviors.
- Use participant photos when available. If a participant photo is unavailable, use the participant's company logo when available. A profile may include both a participant photo and company logo when that improves identification or matches the reference-deck style.
- Never fabricate a participant photo or company logo. Only reference assets that exist in the workspace or were supplied by the user.
- Keep the content skimmable. Summarize rather than copying the full study plan.
- Include only supported study details. The template's example fields and counts are not evidence or required content.

```
- type: study-background
- title: Study Background
- intro: [What the product or concept is and what the study explored]
- goals:
  - [Goal 1]
  - [Goal 2]
  - [Goal 3]
- methods:
  - [Method and session format]
  - [What participants reviewed or did]
- customer-profile:
  - [Who participated]
  - [Relevant platform, company, or experience mix]
```

---

## Key Learnings Slide Format
*(Always slide 3 — numbered overview grouped into themed columns)*

```
- type: key-findings
- title: Key Learnings
- sections:
  - **Product-Market Fit: Who is Foundry perceived as being for?**
  - 1. Less technical participants may be a better fit
  - 2. Developers see it as prototyping only
  - **Knowledge Flow**
  - 3. All participants added all 3 sources once in the right place
  - 4. ServiceNow was seen as a tool, not knowledge
```

- Each `**Bold heading**` starts a new themed section or column
- Section headings use the report's section wording. Do not rephrase them into new themes unless the user requests it.
- Number learnings continuously from left to right and top to bottom across all sections; never restart numbering within a section
- Bullets use source finding titles or verbatim finding sentences; keep the wording identical to the corresponding learning slide title
- Keep the report's grouping, even when a section has only one learning. Do not add, merge, or drop findings to reach a section quota.
- If the overview is too dense, flag the layout issue and ask before cutting content or moving the overview across slides. Do not solve it by silently omitting findings.
- Every numbered item MUST have exactly one corresponding numbered learning slide
- Do not include an unnumbered learning slide or a numbered overview item without a matching slide

---

## Content Guidelines

### Headline Writing
- **Do on Key Learnings and learning slides**: "4. ServiceNow Is Seen as a Tool, Not a Knowledge Source"
- **Don't**: "Finding 4: ServiceNow Belongs in Tools"
- Prefix the learning headline with only the number and a period; do not add the word "Finding" or "Learning"
- Use the exact same numbered headline on the Key Learnings slide and the corresponding learning slide
- Preserve the report's exact finding wording, including capitalization, terminology, and uncertainty; do not strengthen a tentative finding into a fact

### Bullet Points
- Use source-backed counts or actions when useful. Never manufacture a frequency such as "3/5 participants" or "all teams" from a qualitative statement.
- One idea per bullet; maximum 5 bullets per slide

### Quote Selection
- Pick vivid, specific, or emotionally resonant quotes
- Avoid quotes that just restate a bullet point
- Prefer quotes with a concrete scenario over abstract opinions
- Length: prefer short quotes already available in the source. Do not trim approved report quotes solely to meet a length target; if editing is requested, use `quote-tools`.

### Diagrams, Screenshots, and Callouts
- A diagram attached to a finding in the report belongs on that finding slide, not merely in speaker notes or a separate unrelated slide.
- Copy the complete Mermaid block verbatim and add a `diagram` instruction to render it as the main visual. Preserve all labels, explanations, branches, and loop-back arrows. Do not substitute a screenshot for the workflow.
- An outline may include Mermaid source without a rendered image. State that distinction; do not claim rendering is complete until an image exists and has been checked.
- Reuse valid, named screenshots and relative asset links from the existing outline. Keep callout instructions in notes and identify what they should highlight.
- If screenshots are requested, capture the relevant UI rather than inventing it. Follow the user's browser preferences and do not modify a hosted prototype or assign fabricated metrics to make the capture work.
- If the available UI does not show the proposed comparison, query text, or diagnostic state, flag the limitation. Do not label another screen as proof of that behavior.
- Label prototype screenshots as illustrations where needed. Visible demo counts are not measured study outcomes.

## Integration with Other Skills
- **quote-tools**: Select, clean, and format all participant quotes
- **study-report-writer**: Produces the study summary this skill reads from
- **research-readout-deck-builder**: Consumes the `Slide Deck Outline.md` this skill produces
