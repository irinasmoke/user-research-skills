---
name: study-report-writer
description: "Synthesize UX research study data from transcripts, personal notes, participant summaries, and CSVs into a polished study-wide report. Default output is markdown saved to Summary/. Request docx output to produce a Word document using the docx skill. Use after individual participant summaries are complete to create the study-wide synthesis, customer table, and optionally a deck outline."
---

# Study Report Writer Skill

Synthesize user experience research data into polished, report-ready outputs grounded entirely in workspace files.

## First Steps (MANDATORY — do this before ANY work)
1. **Read the study plan** (`study_plan.md` or similar) to learn the study name, goals, research questions, customer profile, and hypotheses. Use the study name for all output file names.
2. **Read at least one reference report** from the `Reference Reports (docx)/`, `ReferenceReports/`, or `Past Summaries/` folder to internalize the expected tone, structure, heading style, and level of detail. Model your output after these reports.
3. **Check for existing intro/background content** — if an outline or study plan already contains a written introduction or background section, USE IT as the basis for the Background section.

## Outline Discovery (MANDATORY before writing study-wide summary)
Before writing any study-wide report content, explicitly search for an outline file.

Search scope (in order):
1. `Summary/`
2. Study-planning folders (for example, folders containing `study_plan.md`)
3. Workspace root

Match patterns:
- `*Outline*.md`
- `*outline*.md`
- `Slide Deck Outline.md`
- `learnings-summary*`

If any outline-like file is found:
- Treat it as report structure input and read it before drafting.
- Prefer the most recent, most study-specific outline when multiple candidates exist.
- If there is ambiguity between multiple valid outlines, ask the user which one to use.

**CRITICAL: Do NOT skip these steps. Never just convert markdown to docx — always properly assemble the document following the reference report format.**

## Rules
- Always ground outputs in actual workspace files (CSV, personal notes, VTT transcripts, Copilot/Marvin summaries).
- Never fabricate or infer information not present in source files.
- Never fabricate quotes. Only use exact quotes found in cleaned VTT transcript files. If a supporting quote doesn't exist, skip it — do not substitute.
- Use the term "participant" for all users/customers.
- Participant folders may contain duplicate data. Cross-reference all sources to ensure every bullet point is directly supported.
- Only use quotes from the cleaned VTT transcript. Do not use Copilot or Marvin summaries as quote sources.
- All iterations and edits to participant summaries must occur in the `PX Name - Agent Summary` file in the participant's folder.
- Name all output files using the actual study name from the study plan, not placeholder names.
- **Match the reference report's formatting conventions exactly** — if reference reports use tables (e.g., participant table in the Appendix), use proper docx tables, not bullet lists.

## Output Format
- **Default**: Markdown file saved to `Summary/` folder, named after the study
- **Docx output**: If the user requests a Word document, use the `docx` skill to produce a `.docx` file in `Summary/`

## Workflow Steps

### 1. Customer Table Generation
- Extract participant details from the CSV file:
  - Name, Role, Company, Clouds used, AI coding experience
- Save the summary table in the `Summary` folder as `Customer Table`

### 2. Individual Participant Summary
- Start with personal notes as the baseline, formatted as concise bullet points. Retain the author's original voice.
- For each bullet, include a supporting quote ONLY from the cleaned VTT transcript.
- Quote format: "Quote text." — First Name, Role at Company (NEVER use last names)
- If no relevant quote is found in the cleaned VTT transcript, skip the quote for that bullet point.
- Add additional insights from Copilot and Marvin summaries only if not already in personal notes, with supporting quotes from cleaned VTT transcript.
- Save as `PX Name - Agent Summary` in the participant's folder.

> **Note**: Use the `participant-summary` skill for this step if individual summaries don't exist yet.

### 3. Study-Wide Summary

**Before writing anything**, read the study plan to extract:
- The study's goals and research questions
- The customer profile/criteria
- Any hypotheses being tested

#### CRITICAL: The outline IS the report skeleton
If an outline file exists (from the mandatory discovery step), it defines the structure of the report. **Always use the outline as the skeleton.** Do not flatten, rearrange, merge, or omit sections:
- Reproduce every heading level (H1, H2, H3) from the outline as corresponding heading levels in the output
- Preserve nesting from the outline
- Do NOT invent your own section structure
- Populate each section with synthesized content and quotes from the Agent Summary and other source files

If NO outline file exists, ask the user for themes or fall back to the default structure below.

**Default report structure** (only when no outline exists):

#### Background
Write 2–4 sentences summarizing:
- What prompted the study (problem space, prior work or learnings if mentioned in study plan)
- What was tested or explored
- The participant profile (number of participants, roles, companies, relevant criteria)

#### Key Learnings
- Ask the user for themes, or propose them based on patterns across participant agent summaries.
- Use **descriptive headings** that capture the actual finding — not generic labels like "Theme 1."
- Under each heading, write 2–4 sentences synthesizing the finding, followed by supporting bullet points and quotes.
- Quote format: "Quote text." — First Name, Role at Company (NEVER use last names)

#### Other Observations
- List bullet points from individual summaries that do not fit under any specified theme.
- Note that the user may want to recategorize these or add a new theme.

### 4. Deck Outline Generation (ONLY when explicitly requested)
- Do NOT create a deck outline unless the user specifically asks for one.
- If requested: create a `Slide Deck Outline.md` in the `Summary/` folder using the `deck-outline` skill.

## Quote Processing
- Use the cleaned VTT transcript files for pulling quotes.
- If a cleaned VTT transcript file is not available, use `transcript-processor` skill to clean it first.
- Use `quote-tools` skill to ensure quotes are contextually accurate and represent the participant's intent.
- Format: "Quote text." — First Name, Role at Company (NEVER use last names)
- When referencing participants inline (not in quotes), use: P# (First Name, Role at Company) — e.g., "P2 (Luke, Software Engineer at Dick's Sporting Goods)". Never include last names.

## Integration with Other Skills
- **transcript-processor**: Clean VTT transcripts before synthesis
- **quote-tools**: Format and verify all quotes
- **participant-summary**: Generate individual participant summaries first
- **docx**: Use for `.docx` output when requested
- **deck-outline**: Use to create the `Slide Deck Outline.md` when a readout deck is needed
