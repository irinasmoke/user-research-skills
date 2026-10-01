---
name: learnings-outline
description: "Read final participant summaries and requested feedback sources, extract every learning, organize specific findings beneath broader categories, group supporting evidence by participant/company, and write a root learnings-summary.md file. Use when the user wants to: (1) synthesize final participant summaries, (2) ensure no learning is missed, (3) include requested stakeholder or field feedback while excluding out-of-scope sources, (4) separate broad categories from evidence-driven learnings, or (5) produce a complete cross-participant learnings synthesis."
---

# Learnings Outline

## Purpose
Produce a complete cross-participant learnings synthesis from final participant summaries.

## Core Task Contract
- Read all final participant summaries and any additional feedback sources explicitly included in scope.
- Extract every learning from every summary.
- Organize specific, evidence-driven learnings beneath broader categories.
- Group evidence by participant and company within each learning.
- Allow the same learning to appear under more than one theme if relevant.
- For each learning, write a short paragraph stating the synthesized finding.
- Create a new file at the workspace root named `learnings-summary.md` unless the user requests a different filename.

## Scope Rules
- Default scope is final participant summaries.
- Include stakeholder, field, GBB, internal, or other feedback only when the user explicitly requests it or clearly includes that source set in the task.
- Respect explicit exclusions such as "include GBB feedback but not Internal Feedback."
- State the included and excluded source sets at the top of the output.
- Do not silently exclude a participant because their final file uses an unexpected filename.
- If source scope remains ambiguous after discovery, ask the user before synthesizing.

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
- Discover final files case-insensitively and flexibly. Search for common variants including:
  - `*final summary*.md`
  - `*final*.md`
  - files such as `name - final.md`, `name-final summary.md`, and `Final Summary.md`
- Do not rely on one exact glob. Inventory participant/source folders and inspect plausible summary filenames before concluding that a final summary is missing.
- Use only one primary summary per participant, prioritizing in this order:
  1. A file explicitly identified by the user
  2. A participant-authored or researcher-edited final summary
  3. The latest clearly labeled final summary
  4. An AI summary only when the user explicitly includes it or no final exists and the user approves
- When multiple plausible final files exist and precedence is unclear, ask rather than guessing.
- Additional requested source sets may use their latest final summary or latest clearly versioned summary when no final exists.

## What Counts as a Learning
- A learning is a substantive observation, need, behavior, expectation, pain point, reaction, implication, or supported recommendation.
- Background context belongs in the synthesis only when it explains a need, use case, adoption constraint, or meaningful difference between participants.
- Recordings, links, empty bullets, repeated quotes, and duplicated takeaway bullets are not separate learnings.
- Consolidate duplicate statements from the same source into one atomic learning, but do not drop distinct nuances.
- Do not convert the source document's section headings directly into output learnings unless the evidence supports a specific finding.

## Output Format
Use a two-level hierarchy: broad category, then specific learning.

```markdown
## <Broad Category>

### <Specific evidence-driven learning>

<Short paragraph, usually 2-4 sentences, synthesizing exactly what the evidence shows.>

Evidence by participant:

- **<Participant Name> — <Company or organization>**
  - <Specific supporting evidence>
  - <Additional directly supporting evidence>
- **<Participant Name> — <Company or organization>**
  - <Specific supporting evidence>
```

At the top of the output, include:

```markdown
Coverage: <included sources/participants>. Excluded: <explicitly excluded source sets>.
```

If priority input contains unsupported claims, add a final section:

```markdown
### Priority notes not evidenced in the summaries

- <Unsupported priority claim>
```

## Category and Learning Rules
- Categories are broad navigational groupings, such as:
  - Understanding the Value Proposition
  - Ontology Creation and Configuration
  - What's Working Well in the UI
  - Evaluation and Adoption
- Learnings are specific claims that state the actual finding, such as:
  - "The ontology preview is the product's best explainer, but participants do not find it."
  - "Customers expect Microsoft to generate an ontology and let them refine it in place."
- Never use one vague "theme" for every product area and stop there. A category must contain one or more specific learnings.
- Do not make categories so narrow that each category contains only one learning unless the evidence genuinely warrants a standalone area.
- A learning title should be meaningful without reading the evidence bullets.
- Avoid vague learning titles such as "Configuration feedback," "Graph UX," or "Value proposition."

## Evidence-Fit Rules
- Every evidence bullet must directly and fully support the learning under which it appears.
- Apply a strict test: if the evidence does not support the entire learning claim, move it to a different learning or create a new learning.
- Do not use adjacent positive feedback as evidence for a discoverability problem. For example:
  - "The ontology visualization is clear and effective" is not evidence that participants fail to find Preview.
  - It belongs under a separate learning about what works well once the visualization is opened.
- Do not stretch a learning to make it look more robust or cross-participant than the evidence supports.
- A learning supported by one participant is valid when it is specific and important; label only that participant's evidence.
- Distinguish:
  - **Observed evidence:** what a participant did, said, misunderstood, or requested
  - **Researcher interpretation:** a supported synthesis or implication
  - **Priority framing:** user-provided importance that still requires source evidence
- Never present priority framing or researcher speculation as participant evidence.

## Attribution Rules
- Group evidence once by participant/company within each learning.
- Do not append `- Name, Role at Company` to every bullet; repeated attribution makes the evidence appear more numerous than it is.
- Use a consistent group label: `**Name — Company or organization**`.
- Include role only when it meaningfully distinguishes participants or the user requests it.
- Preserve distinct evidence bullets under the participant label rather than combining unrelated observations.

## Workflow
1. Inventory all participant/source folders in scope.
2. Locate final summaries using flexible, case-insensitive discovery; do not depend on one filename pattern.
3. Resolve one primary file per participant/source according to the precedence rules.
4. Record explicit inclusions and exclusions.
5. If optional priority input exists, parse it into a priority checklist.
6. Extract atomic learnings from every primary source.
7. Create a source-to-learning ledger with one row for every substantive source bullet or paragraph:
   - Source participant/file
   - Atomic source learning
   - Output category
   - Output learning
   - Status: mapped, duplicate, contextual only, or explicitly excluded
8. Cluster atomic learnings into specific synthesized findings.
9. Group related findings beneath broader categories.
10. Run the evidence-fit test for every participant bullet under every learning.
11. Split any learning whose evidence supports only part of the claim.
12. Duplicate genuinely cross-cutting learnings across categories only when useful; do not duplicate merely to increase apparent support.
13. Write the category → learning → grouped evidence structure.
14. If priority input exists, verify each item is represented or explicitly marked as not evidenced.
15. Audit the output against every source file using the source-to-learning ledger.
16. Add any missing learning before finalizing.
17. Write the output to the workspace root as `learnings-summary.md`.

## Required Coverage Audit
Before claiming the synthesis is complete:
- Compare every substantive bullet and paragraph in every source against the ledger.
- Confirm every source participant appears in the output or is explicitly excluded.
- Confirm each atomic learning is:
  - Represented in the output
  - Consolidated as a documented duplicate
  - Marked contextual-only with a reason
  - Explicitly excluded by scope
- Search for distinctive source concepts and terminology as a secondary check, but do not treat keyword presence as proof of semantic coverage.
- If the audit finds missing items, add them before reporting completion.
- Do not claim "every learning is accounted for" until this audit is complete.

## Quality Checklist
- Output has broad categories and specific learnings beneath them.
- Every learning has a concise synthesis paragraph plus grouped participant evidence.
- Every evidence bullet directly supports the complete learning claim.
- Evidence is grouped by participant/company without repeated per-bullet attribution.
- Single-participant learnings remain separate when they do not support a broader claim.
- Coverage audit confirms all substantive source learnings are mapped or deliberately classified.
- All participants and requested source sets in scope are represented.
- Explicitly excluded source sets are not used.
- Cross-cutting learnings may appear in multiple categories when genuinely useful.
- Evidence bullets retain concrete detail without inflating the apparent evidence count.
- If optional priority input was provided, all priority items are accounted for (mapped or flagged not evidenced).
- Output file exists at the workspace root as `learnings-summary.md`.
