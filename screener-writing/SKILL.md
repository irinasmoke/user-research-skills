---
name: screener-writing
description: "Write participant screening questionnaires (screeners) for UX research studies. Use when: (1) creating a new screener, (2) editing screener questions, (3) adding/removing screener questions, (4) adapting a screener for a different audience, or any task involving screener question authoring. NOT for uploading screeners to UserInterviews.com — use the userinterviews-project skill for that."
---

# Screener Writing

Write participant screening questionnaires for UX research recruitment. Screeners filter candidates to find qualified participants for studies.

## Question Bank — Source of Truth

⚠️ **CRITICAL: Always start from the question bank.**

Before writing ANY screener question, read the standard question bank at:
`references/screener examples/screener-questions.md`

This file is the **source of truth** — NEVER edit it.

**Process:**
1. Read `references/screener examples/screener-questions.md` first
2. Reuse questions from the bank as-is whenever they fit the study's needs
3. Adapt qualify/reject logic per study if needed, but keep the question text and answer options from the bank
4. Only create a NEW question when no question in the bank covers what you need
5. When you do create a new question, call it out explicitly so the user can decide whether to add it to the bank

## Default Background Info Question

**Always include this question unless the user explicitly says to omit it.** Place on Page 1, typically after the role question.

```markdown
### Question N

**Pick one**

How many years of professional software development experience do you have? (not including school)

* Less than 1 year **(reject)**
* 1–3 years **(accept)**
* 4–7 years **(accept)**
* 8–15 years **(accept)**
* 15+ years **(accept)**
```

Adjust accept/reject thresholds per study (e.g., a senior-only study may reject "1–3 years").

## Screener Principles

- Start broad, get specific — screen out, don't screen in
- Include demographics, behavioral criteria, psychographics
- Clear pass/fail logic with quota specifications
- Avoid telegraphing desired answers
- Estimate realistic pass rates
- Screening questions that telegraph desired answers are a common pitfall — avoid them

## Output Format

Screeners MUST use this exact markdown format. The `userinterviews-project` automation skill parses this structure directly.

```markdown
# Study Title — Participant Screener

**Target: n=X participants**

| Quota | Target |
|-------|--------|
| ... | ... |

---

## Section Name — Page 1

> **Skip logic:** If Q1 is any reject answer → End screener

### Question 1

**Pick one**

Question text here

* Option A **(accept)**
* Option B **(reject)**

---

## Section Name — Page 2

### Question N

**Pick any**

Question text here

* Option A **(may select)**
* Option B **(must select — reason)**
* None of the above **(reject)**

### Question N+1

**Short answer**

Question text here

---

## Section Name — Page 3

### Question N+2

**Long answer**

Question text here
```

### Page & Skip Logic Format

- **Page labels** are on the `## Section` header: `## Section Name — Page N`
- **Skip logic** is a blockquote right after the header: `> **Skip logic:** If QN is [condition] → End screener`
- Pages without skip logic simply omit the blockquote
- The `---` separator between sections marks the page boundary

### Question Type Mapping

| Markdown marker | User Interviews question type |
|----------------|------------------------------|
| `**Pick one**` | Single select / Radio buttons |
| `**Pick any**` | Multi-select / Checkboxes |
| `**Short answer**` | Short text input |
| `**Long answer**` | Long text / Paragraph |

### Answer Qualification Mapping

| Markdown marker | User Interviews behavior |
|----------------|--------------------------|
| `**(accept)**` | Qualify / Accept |
| `**(accept — ...)**` | Qualify / Accept (note is for recruiter, not entered in UI) |
| `**(reject)**` | Disqualify / Reject |
| `**(may select)**` | No automatic qualification (neutral) |
| `**(must select ...)**` | Qualify — this option is required (note for recruiter) |

## Screener Structure Guidelines

### Page Organization
- **Page 1**: Role, company, background info (broad screening — reject unqualified early)
- **Middle pages**: Domain-specific experience, tools, behaviors (deeper qualification)
- **Last page**: Availability, open-ended context questions (no rejection — just info gathering)

### Question Ordering Within a Page
1. Role / job title (Pick One)
2. Years of experience (Pick One) — the default background info question
3. Company type / size (Pick One)
4. Company name (Short Answer)
5. Domain-specific questions

### Skip Logic Conventions
- Place skip logic on pages where reject answers should end the screener early
- Format: `> **Skip logic:** If QN is any reject answer → End screener`
- Can also target specific pages: `> **Skip logic:** If QN is "Option text" → Page N`
- Pages with no reject-worthy answers don't need skip logic

## Common Pitfalls

- **Leading questions**: Don't telegraph which answer qualifies ("Are you experienced with...")
- **Double-barreled questions**: Ask one thing at a time
- **Too many options**: Keep Pick One to ~6-8 options max
- **Missing "Other" or "None"**: Always include an escape hatch for Pick Any questions
- **Forgetting reject logic**: Every Pick One question on screening pages should have at least one reject option
- **Overly strict screening**: Will reduce your candidate pool — balance specificity with recruitment feasibility
