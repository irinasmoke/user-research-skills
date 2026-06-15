---
name: quote-tools
description: "Clean, format, and verify quotes from transcripts or documents. Removes verbal fillers, trims rambling quotes, adds bracket notation for edits, and formats with proper attribution. In UX research contexts, enforces 'participant' terminology, research-specific attribution format, and cross-verification against source transcripts. Use when: (1) cleaning quotes for reports or publications, (2) extracting quotes from transcripts, (3) formatting quote attributions, (4) verifying quotes exist in source material."
---

# Quote Tools Skill

Clean, format, and verify quotes for readability while maintaining speaker authenticity, meaning, and intent.

## When to Use This Skill

Use this skill when you need to:
- Clean quotes from interview transcripts for publication or reports
- Remove verbal fillers while preserving speaker voice
- Format quotes with proper attribution
- Verify quotes exist in source material
- Prepare quotes for academic writing, journalism, or documentation

## Core Principles

### DO:
- Remove verbal filler words and repetitions ("uh", "um", "like", "you know", "right", repeated words)
- Cut down long, rambling quotes to their essence
- Rearrange words or phrases for better flow when needed
- Use square brackets `[...]` to indicate:
  - Omitted content that doesn't add value
  - Rewording or clarification inserted by the editor
  - Added context for clarity
- Make very minor grammar fixes for readability
- Preserve the speaker's original phrasing and vocabulary
- Keep attribution intact (speaker name, title, company)

### DON'T:
- Change the speaker's language or vocabulary significantly
- Alter the meaning or intent of the quote
- Add your own interpretations without square brackets
- Over-edit to the point where it no longer sounds like the speaker
- Remove important context or nuance
- Fabricate or invent quotes that don't exist in source material

## Editing Techniques

### 1. Removing Fillers
**Before:** "There is a there there is a there is a just like one more thing..."  
**After:** "There is just one more thing..."

### 2. Cutting Redundancy
**Before:** "I I talked about. Then a lot of customization is required, a lot of agent we have to define..."  
**After:** "A lot of customization is required, a lot of agents we have to define..."

### 3. Using Brackets for Clarity
- `[...]` - Content omitted
- `[context added]` - Editor's clarification or added context
- `[rewording of original phrase]` - Simplified version of what speaker said

**Example:**
> "A lot of customization is required [for our rapid knowledge retrieval application]. A lot of agents we have to define behind the scenes to create a complete story."

### 4. Streamlining Run-ons
Break up or condense run-on sentences while preserving meaning.

## Quote Formatting Standards

### Standard Attribution Format (Blockquote)
```markdown
> "Quote text here."
> 
> — First Name, Role at Company
```

**Important**: Attribution goes on a new line as a plain em-dash (`—`), not an inline dash. Use first name only — never last names. This format matches the `participant-summary` skill.

### With Timestamp (for reference tracking)
```markdown
> "Quote text here."
> 
> — First Name, Role at Company (00:15:32)
```

### Multiple Paragraphs
```markdown
> "First paragraph of quote.
>
> Second paragraph of quote."
> 
> — First Name, Role at Company
```

### In Bullet Lists
```markdown
- Main insight or finding
  > "Supporting quote from transcript."
  > 
  > — First Name, Role at Company
```

## Capabilities

### 1. Clean Individual Quotes
**Input:** Raw transcript excerpt or quote  
**Output:** Cleaned, formatted quote with attribution

### 2. Batch Clean Quotes in Documents
**Input:** Markdown file with quotes marked by `>` or specific patterns  
**Output:** Same document with all quotes cleaned and formatted

### 3. Verify Quote Accuracy
**Input:** Quote + source transcript file  
**Output:** Verification status + exact location in source if found

### 4. Extract and Format Quotes
**Input:** Search terms + transcript file  
**Output:** Formatted quotes with context and attribution

## Quote Cleaning Process

1. **Read the quote in full** - Understand the complete meaning and context
2. **Grep the source transcript** — Before adding any `[bracket]`, search the cleaned transcript for the exact word or phrase. If the word IS present verbatim, write it without brackets. Only bracket words that were genuinely not spoken. If a sentence trails off or is cut off mid-thought, end with `[...]` — never complete the sentence with inferred words.
3. **Identify the core message** - What is the speaker really trying to say?
4. **Remove obvious fillers** - Eliminate repetitions and verbal tics
5. **Assess length** - Is the quote too long? Can it be condensed?
6. **Edit strategically** - Use brackets appropriately to maintain clarity
7. **Verify authenticity** - Does it still sound like the speaker? Is the meaning preserved?
8. **Add attribution** - Include speaker's FIRST NAME ONLY, title, and company/organization. NEVER include last names.

## Privacy Rules

**NEVER include participant last names in any output.** Use first name only in all attributions, quotes, and references. Example: "Luke, Software Engineer at Dick's Sporting Goods" — NOT "Luke Tarr, Software Engineer at Dick's Sporting Goods."

## In UX Research Contexts

When working on UX research reports, participant summaries, or study outputs, apply these additional rules on top of the standard cleaning guidelines:

- **Terminology**: Always use "participant" (not "user" or "customer") in attribution and surrounding context
- **Source verification**: Cross-reference every quote against the cleaned VTT transcript file. If a quote can't be verified in the source transcript, skip it — do not substitute or paraphrase
- **Technical terms**: Preserve technical terminology exactly as spoken (e.g., "RAG", "AI infra", product names like "Microsoft Foundry")
- **Bracket context**: When adding clarifying context in brackets, reference Microsoft Foundry by name if relevant (e.g., `[in Microsoft Foundry]`)
- **Attribution must include role and company**: Every quote must have full attribution — name, role, and company

## Quality Checklist

Before finalizing each cleaned quote, verify:
- [ ] Core meaning is preserved
- [ ] Speaker's voice and style are intact
- [ ] All edits are clearly marked with brackets where appropriate
- [ ] Grammar is improved without changing the speaker's language
- [ ] Quote is more readable than the original
- [ ] Attribution is complete and accurate
- [ ] No misrepresentation of the speaker's intent
- [ ] Quote can be traced back to source transcript

## Example Transformations

### Example 1: Complex Technical Quote

**BEFORE:**
> "There is a there there is a there is a just like one more thing for both application right like our rapid knowledge retrieval. I believe that that that that this drag for the AI infra right I I talked about. Then a lot of customization is required, a lot of agent we have to define behind the scene to create a complete story." - Vipin, Data Science Lead at Cognizant

**AFTER:**
> "A lot of customization is required [for our rapid knowledge retrieval application and the AI infra application described earlier]. A lot of agents, we have to define behind the scenes to create a complete story." - Vipin, Data Science Lead at Cognizant

### Example 2: Long Narrative Quote

**BEFORE:**
> "There are certain SharePoint documents which is accessible to a certain audience, certain group of audience. And when we search it, when when somebody entered us some prompt or some questions, we want that it should not. If the document is not accessible to you, then it should not refer for providing any context or answer, right?" - Vipin, Data Science Lead at Cognizant

**AFTER:**
> "There are certain SharePoint documents which are accessible to a certain audience and when somebody entered some prompt we want that [...] If the document is not accessible to you, then it should not refer for providing any context or answer, right?" - Vipin, Data Science Lead at Cognizant

## Integration with Other Skills

This skill works well with:
- **transcript-processor**: Clean transcripts first, then extract and format quotes
- **docx**: Generate formatted documents with properly cleaned quotes
- Research and analysis skills that need verified, readable quotes
