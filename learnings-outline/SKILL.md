---
name: learnings-outline
description: "Read final participant summaries, extract every learning, organize by theme, tag each learning with participant and company, and write a root learnings-summary file. Use when the user wants to: (1) synthesize all final participant summaries, (2) ensure no learning is missed, (3) group learnings by theme with overlap allowed, (4) add a short paragraph per theme plus tagged evidence, or any task involving complete themed learnings synthesis."
---

# Learnings Outline

## Purpose
Produce a complete cross-participant learnings synthesis from final participant summaries.

## Core Task Contract
- Read all final participant summaries in scope (for this study, P1-P9).
- Extract every learning from every summary.
- Organize learnings by theme.
- Tag each learning with participant name and company.
- Allow the same learning to appear under more than one theme if relevant.
- For each theme, write a short paragraph summarizing the theme-level learning.
- Create a new file at the workspace root named `learnings-summary` unless the user requests a different filename.

## Optional Priority Input (File or Chat)
An optional user-provided list of important points can be provided as either:
- A file in the workspace (markdown/text/doc with bullets), or
- Chat bullets pasted directly by the user.

When present, treat this input as:
- Signal of importance: prioritize these topics in theme framing and ordering.
- Interpretation layer: capture the user's framing where it is supported by participant summaries.
- Coverage check: verify each priority item is addressed in the final output.

Rules for optional priority input:
- Do not treat priority bullets as evidence by themselves; always ground claims in participant final summaries.
- If a priority bullet is unsupported by source summaries, call it out as not evidenced. Do NOT fabricate evidence or let it suppress other learnings.
- Preserve user wording for priority labels when possible, while keeping the final write-up concise.
- Do not let priority input suppress other high-signal learnings found in participant summaries.

## Input Discovery Rules
- Default source files are the final participant summaries only.
- Include files named like `*Final Summary.md` across participant folders.
- Use only one file per participant, prioritizing final summaries over agent summaries if both exist.

## Output Format
Use this structure for each theme:

## <Theme Name>
<Short paragraph (2-4 sentences) summarizing the theme across participants.>

Tagged learnings:
- <Detailed learning> - <Participant Name>, <Role> at <Company>
- <Detailed learning> - <Participant Name>, <Role> at <Company>

## Style Rules
- Keep theme paragraph concise but substantive (2-4 sentences).
- Put evidence detail in tagged bullets, not by repeating the same sentence.
- Keep each tagged bullet evidence-based and specific.
- Learnings may appear under multiple themes when relevant.
- Use consistent participant tagging format: Name, Role at Company

## Workflow
1. Locate and read all final participant summaries in scope.
2. If optional priority input exists (file or chat bullets), parse it into a priority checklist.
3. Extract atomic learnings from each participant document.
4. Create a participant-to-learning ledger to ensure full coverage.
5. Cluster learnings into themes.
6. Duplicate cross-cutting learnings across relevant themes.
7. Write a short paragraph for each theme.
8. Add all tagged learnings under each theme using Name, Role at Company tags.
9. If priority checklist exists, verify each item is represented or explicitly marked as not evidenced.
10. Validate no participant is missing and no required learning was dropped.
11. Write output to root file `learnings-summary`.

## Quality Checklist
- Every theme has a short paragraph plus tagged bullets.
- Every tagged learning includes participant name and company.
- Coverage check confirms all participants in scope are represented.
- Learnings can appear in multiple themes where relevant.
- Tagged bullets retain concrete detail.
- If optional priority input was provided, all priority items are accounted for (mapped or flagged not evidenced).
- Output file exists at workspace root as `learnings-summary`.
