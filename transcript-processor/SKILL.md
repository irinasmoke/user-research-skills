---
name: transcript-processor
description: "Clean VTT/WebVTT transcript files by removing filler words (um, uh, yeah, mhm) and consolidating fragmented speaker blocks into readable text. Use when you need to process interview, meeting, or video transcripts before analysis, summarization, quote extraction, or report writing."
---

# Transcript Processor Skill

Clean and format VTT/WebVTT transcript files by removing filler words, combining speaker blocks, and producing readable text output.

## When to Use This Skill

Use this skill when you need to:
- Clean VTT or WebVTT transcript files from interviews, meetings, podcasts, or videos
- Remove filler words (um, uh, yeah, mhm, etc.) from transcripts
- Combine fragmented speaker turns into coherent blocks
- Convert timestamped transcripts into clean, readable text
- Prepare transcripts for analysis, summarization, or quote extraction

## Capabilities

### 1. Clean VTT Transcripts
Remove filler words and consolidate speaker blocks from VTT/WebVTT files.

**Process:**
1. Search the current working directory (and subdirectories) for `.vtt` files using glob or bash. Do this immediately — before any other action.
   - If a VTT file is found, use it.
   - If no VTT file is found, search `~/Downloads/` for matching `.vtt` files. If a match is found, copy it into the current working directory and use it.
   - If still no VTT file is found, stop and ask the user to provide the file path.
2. Run `clean_vtt_transcript.py` script (provided with this skill)
3. After the script runs, do a post-processing pass to normalize speaker names (see below)
4. Output clean text file with format: `Speaker Name: [consolidated text]`

**Speaker name normalization (post-processing, applied after script):**
- The customer/participant being interviewed should appear as **first name only** (e.g., "Alan Parry:" → "Alan:")
- The interviewer/facilitator should use their first name only as well (e.g., "Irina Smoke:" → "Irina:")
- Use `sed` or string replacement to apply these substitutions across all lines of the output file after the script completes
- If speaker names are unclear from the VTT, infer from context or ask the user

**What gets removed:**
- WEBVTT headers and metadata
- Timestamps
- Filler words: um, uh, yeah, mhm, okay, mm-hmm, cool, right, sure, etc.
- Lines that are only social pleasantries: hi, hello, bye, thanks, etc.
- Speaker blocks that contain only filler words

**What gets preserved:**
- Speaker names (first name only — see normalization above)
- Meaningful content
- Speaker turn order
- Natural flow of conversation

### 2. Batch Process Multiple Transcripts
Process multiple VTT files in a directory structure.

**Process:**
1. Search for all .vtt files in workspace
2. For each file, generate cleaned output in same directory
3. Name output: `[original_name] - Cleaned.txt`

### 3. Custom Filler Word Configuration
Modify the filler word list for specific use cases (e.g., technical conversations where "right" is meaningful).

## Script Reference

The skill includes `clean_vtt_transcript.py`. Run it via:

```bash
python ~/.copilot/skills/transcript-processor/clean_vtt_transcript.py
```

Or import it:
```python
from pathlib import Path
import sys
sys.path.insert(0, str(Path.home() / ".copilot/skills/transcript-processor"))
from clean_vtt_transcript import clean_vtt_transcript

clean_vtt_transcript(
    input_path="interview.vtt",
    output_path="interview_cleaned.txt"
)
```

## Output Format

Cleaned transcripts use this format:
```
Speaker Name: First block of consolidated text from this speaker.
Other Speaker: Their response in one consolidated block.
Speaker Name: Their next turn, combining multiple fragments.
```

## Best Practices

- **Run early in workflow**: Clean transcripts before analysis, summarization, or quote extraction
- **Review output**: Scan cleaned transcripts to ensure important content wasn't removed
- **Preserve originals**: Always keep original VTT files; cleaned versions are derivatives
- **Adjust for domain**: Technical or specialized conversations may need custom filler word lists
- **File naming**: Use consistent naming like `[Name] - Cleaned.txt` for easy identification

## Limitations

- Requires VTT/WebVTT format
- Speaker names must be tagged in VTT format: `<v Speaker Name>`
- Very short responses (1-2 words) may be removed if they match filler patterns
- Does not handle quote extraction, speaker analytics, sentiment analysis, or thematic coding

## Integration with Other Skills

This skill works well with:
- **quote-tools**: Extract and format quotes from cleaned transcripts
- **participant-summary**: Feed cleaned transcripts into participant summary generation
- **study-report-writer**: Cleaned transcripts are required before synthesis
