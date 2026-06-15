---
name: participant-summary
description: "Generate comprehensive per-participant summaries from interview transcripts and personal notes. Supports three modes: (1) from scratch using transcript + discussion guide, (2) from personal notes augmented with transcript quotes, (3) style-matched to existing summaries in the study. Use when documenting individual research participants after interviews."
---

# Participant Summary Skill

Generate comprehensive participant summaries from interview transcripts using three different modes to accommodate various starting points and contexts.

> **⚠️ FILE NAMING — NON-NEGOTIABLE:**
> - Save the file as **`px name - AI Summary.md`** (e.g., `p2 jesus - AI Summary.md`)
> - Do NOT name it "Summary.md", "Final Summary.md", or anything else. It is ALWAYS "AI Summary.md".

## Core Rules
- Always ground outputs in actual workspace files
- Never fabricate or infer information not present in source files
- Never fabricate quotes — only use exact quotes found in cleaned VTT transcript files
- **CRITICAL: Only include quotes from the specific participant being summarized. NEVER include quotes from other participants.**
- All summaries must be saved as `px name - AI Summary.md` in the participant's folder
- Quote format: blockquote style (`>`), with attribution on a new line as a plain em-dash (not a bullet): `— First Name, Role at Company` (NEVER use last names)
- **NEVER include participant last names in any output.**

## Formatting Rules
- **Open with a prose sentence** introducing who the participant is and what their company does. Do NOT start with a bullet list or a "Background" header.
- **Do not invent section headers.** Use only headers that are warranted by the content. Never add "Background", "Key Takeaways", "Tech Stack", or "Current Process" as standalone sections just to have structure.
- **Keep background context minimal and woven in** — a sentence or two to orient the reader, not a comprehensive profile.
- Use ✅ and ⚠️ inline on bold reaction bullet headlines to signal positive vs. concerning findings — but only in sections where the participant is reacting to something (a concept, a prototype, a feature). Do not use in exploratory or background sections.
- **A Concept Reactions (or equivalent) section is only appropriate for CVT, usability, or other evaluative studies** where the participant is explicitly responding to something shown to them. Infer this from the discussion guide — if there's a concept/demo/prototype being reacted to, include it. If it's a pure discovery or generative study, omit it.
- **Ratings section**: Read the discussion guide. If there are explicit rating or ranking questions (e.g., Likert scales, stack ranks), include only those verbatim questions as section labels with the participant's answer and a supporting quote. Do NOT repeat other discussion guide questions.
- **Recordings section always last.** Always include it. Format:
  ```
  ## Recordings
  Teams: <link>
  Marvin: <link>
  ```
  **Auto-populating recording links:**
  - **Teams link**: If the user has not provided a Teams meeting recap link, use the `mcp_workiq_ask_work_iq` tool to search for the meeting. Ask WorkIQ for the Teams meeting recap link using the participant name, company, and approximate session date. Include the returned link in the summary.
  - **Marvin link**: If the user has not provided a Marvin link, use the Marvin MCP tools to find it:
    1. Call `mcp_marvin_list_projects` and search for the study/project name
    2. Call `mcp_marvin_list_project_files` with the project ID and find the file matching the participant name
    3. Construct the link as `https://app.heymarvin.com/projects/{project_id}/media/{file_id}/`
    If Marvin MCP tools are not available, leave as `Marvin:` (empty) for the user to fill in manually.

## Required Inputs
- **Always Required**: Transcript file (VTT format, preferably cleaned)
- **Optional**: Discussion guide, hypothesis list, personal notes, backchannel chat content, existing summaries from the same study

## Backchannel Chat Content
Backchannel chat is where PMs, designers, engineers, and other product team members discuss observations during the interview in real-time. It serves as:
- **Signal of importance**: Topics discussed indicate what the product team finds noteworthy
- **Interpretation layer**: Team members share their takeaways and connect observations to product strategy
- **Coverage check**: May highlight important moments not captured in personal notes

**When backchannel chat is available**, use it to:
1. Identify which moments/topics the product team found most significant
2. Understand team interpretations and strategic connections
3. Fill gaps where personal notes may have missed important insights

## Summary Modes

### Mode 1: From Scratch (Transcript + Discussion Guide/Hypothesis)
**When to use**: Starting a new study or first participant summary with no prior summaries available

**Process**:
1. If a cleaned VTT transcript is not available, use `transcript-processor` skill to clean the VTT file first
2. If backchannel chat is available, review it first to identify priority topics
3. If discussion guide/hypothesis list is provided, use it to identify key research questions and themes
4. Analyze the transcript to extract key insights, pain points, workflow descriptions, feature requests, and contextual background
5. For each insight, include a supporting quote from the cleaned VTT transcript using `quote-tools` skill
6. Structure as concise bullet points
7. Save as `PX Name - Summary.md` in the participant's folder

### Mode 2: From Personal Notes
**When to use**: When personal notes have been taken during or after the interview

**Process**:
1. **If a cleaned VTT transcript is not available, run `transcript-processor` skill first.** Do not proceed with quote extraction until a cleaned `.txt` transcript exists.
2. Start with personal notes as the baseline, formatted as concise bullet points
3. **Preserve the author's exact phrasing** — do not rewrite, editorialize, or improve the wording of bullet points from personal notes. If the note says "competitor is not just what we provide but whether they can build on their own easily," use that exact phrase, not a paraphrase like "the DIY alternative is a real competitive force."
4. If backchannel chat is available, review for topics the product team found significant
5. For each bullet point in the personal notes, find the supporting quote by **grepping the cleaned transcript for key phrases** to get the raw text, then pass it through `quote-tools` to clean and format. **Never write a quote from memory. Before adding any `[bracket]`, grep the transcript to confirm the word does NOT appear verbatim — if it does, write it without brackets.**
6. If no relevant quote exists, skip the quote for that bullet point
7. Add additional insights from the transcript or backchannel not captured in personal notes
8. Save as `PX Name - Summary.md` in the participant's folder

**Output Structure**: Follow the structure and themes from the personal notes, augmenting with quotes and additional insights.

### Mode 3: Style-Matched Summary with Topic Analysis
**When to use**: When adding a new participant to an existing study with prior summaries

**Process**:

**Phase 1: Topic Analysis**
1. Analyze all existing summaries to identify recurring themes, structure patterns, level of detail, tone, and types of insights captured
2. Create a topic inventory
3. If backchannel chat is available, review for what the product team found most important

**Phase 2: New Transcript Analysis**
1. Analyze the new transcript for coverage of topics from Phase 1 and new topics not in existing summaries
2. Extract supporting quotes
3. Prioritize insights aligned with backchannel discussions

**Phase 3: Summary Generation**
1. Structure to match style/tone/organization of existing summaries
2. Include a dedicated **New Topics & Observations** section for insights that don't fit existing themes
3. Save as `PX Name - Summary.md` in the participant's folder

## Quote Processing
- Always use cleaned VTT transcript files for pulling quotes
- If cleaned VTT transcript is not available, run `transcript-processor` skill first
- **PARTICIPANT QUOTES ONLY**: Never copy quotes from other participants' summaries or transcripts
- When noting similar patterns across participants, describe the pattern in your own words without quoting the other participant
- Never use Copilot or Marvin summaries for quotes

### Quote Formatting Rules
- **Never fabricate** — every word in a quote must appear verbatim in the transcript. Do not paraphrase or invent phrases dressed up as quotes.
- **`[brackets]` for added words** — any word inserted for clarity that was not spoken goes in brackets (e.g., `[evaluation system]`, `[my testing framework]`)
- **`[...]` for omissions** — use only when words are actually cut from the transcript. Never use `...` alone for an omission.
- **Strip fillers, not content** — remove "yeah", "I mean", trailing "um"s and meaningless repetition, but keep fillers that convey hesitation or voice (e.g., "like", "gut feeling")
- **Tell the whole story** — it is more important to include full context than to have a short quote. Do not truncate at the first natural pause if the key insight comes after. When a follow-up question unlocks a richer answer, include that answer in the same quote block with `[...]` bridging the gap.
- **A quote can span a follow-up exchange** — if the interviewer asked a clarifying question and the participant's follow-up answer is where the insight lives, include both turns with `[...]` between them
- **Fix punctuation for readability** — use colons, clean up run-ons, use "A+" instead of "A plus" — but never change the words
- Attribution on a new line as plain em-dash: `— First Name, Role at Company`

## Mode Selection Guide
- **Use Mode 1**: First participant in a study, or when starting fresh
- **Use Mode 2**: Personal notes are available and should drive the structure
- **Use Mode 3**: Study has existing participant summaries, want consistency and comparative insights

## Integration with Other Skills
- **transcript-processor**: Clean VTT files before analysis
- **quote-tools**: Format and verify all quotes
