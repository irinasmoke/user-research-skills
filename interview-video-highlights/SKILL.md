---
name: interview-video-highlights
description: Turns user interview recordings (video + VTT transcript) into highlight reels, structured notes docs, and Slack TL;DRs. Use this skill when the user asks to make a clip reel, analyze an interview transcript, create interview notes, or generate a highlight reel from a recorded interview.
---

# Interview Highlights Skill

Turns recorded user interviews into shareable deliverables: video highlight reels with title cards and subtitles, structured Word notes docs, and Slack-ready TL;DR summaries.

**Trigger**: Any request involving interview clip reels, interview analysis, interview highlight videos, or structured notes from a recorded user interview.

**Input required**: A video file (.mp4) and a VTT transcript file (.vtt) from the same interview recording (typically Zoom or Teams).

---

## Prerequisites

Before first use, the researcher's machine needs:

```bash
# 1. FFmpeg with subtitle support (one-time install)
brew tap homebrew-ffmpeg/ffmpeg
brew install homebrew-ffmpeg/ffmpeg/ffmpeg

# 2. Python packages
pip3 install python-docx Pillow numpy

# 3. Verify subtitle support works
ffmpeg -filters 2>&1 | grep subtitles
# Should output: .. subtitles  V->V  Render text subtitles...
```

**Font**: Mona Sans must be installed at `/Library/Fonts/MonaSans*.ttf` for branded outputs. If not available, fall back to Helvetica Neue.

Run this verification check at the start of every session. If anything is missing, help the researcher install it before proceeding.

---

## Modules

This skill has three independent modules. The researcher can request any combination:

- **Module A**: Highlight reel (video clips + title cards + burned-in subtitles)
- **Module B**: Structured notes doc (Word, themed, full quotes with timestamps)
- **Module C**: Slack TL;DR (plain text findings + opportunities section)

If the researcher doesn't specify, ask which modules they want.

---

## Step 0: Gather context

Before doing any analysis, ask the researcher these questions (use ask_user tool):

1. **What was this interview about?** (study name, research questions, participant context)
2. **Which modules do you want?** (A: highlight reel, B: notes doc, C: Slack TL;DR, or all)
3. **Participant code**: What should we call this participant? (e.g., P1, P2, P3). Never use real names/titles/companies in any output.
4. **For Module A (highlight reel)**:
   - How long should the highlight reel be? (default: under 10 minutes)
   - Roughly how many clips/insights? (default: 10-15)
   - Do you already have key themes or quotes you want included, or should I surface them from the transcript?
5. **For Module C (Slack TL;DR)**: Any specific Slack channel context or audience to tailor for?

Support two flows for theme selection:
- **Researcher-led**: They provide the themes/quotes they want highlighted. You find the best clips and timestamps.
- **Agent-led**: You read the full transcript, propose themes with quotes, and the researcher curates.

---

## Step 1: Parse the transcript

1. Read the VTT file and parse into structured entries: (timestamp, speaker, text)
2. Merge consecutive entries from the same speaker into single utterances
3. Count total utterances, duration, and speakers
4. Report to the researcher: "Parsed 50-minute interview with 4 speakers. [Participant] has 115 utterances."

---

## Step 2: Identify themes and quotes

### If agent-led:
1. Read the full merged transcript carefully
2. Identify the strongest, most quotable moments - look for:
   - Vivid language, metaphors, strong opinions
   - Specific examples and stories (not vague generalities)
   - Pain points, workarounds, and unmet needs
   - Moments of surprise, emotion, or emphasis
   - Unprompted feature requests or product feedback
3. Group quotes into themes
4. For each quote, record the exact VTT start and end timestamps
5. Select a contextual card question for each clip (see Title Card Rules below)

### If researcher-led:
1. Take the researcher's themes/quotes and find the exact timestamps in the VTT
2. Propose additional themes if you spot strong moments they may have missed
3. Still write the contextual card questions

### Present the clip guide
Generate a markdown file at `outputs/{project-name}/clip_guide.md` with:

| # | Theme | Card question | Quote snippet | Start | End | Duration |
|---|-------|--------------|---------------|-------|-----|----------|

Include the proposed playback order. Save this file and tell the researcher to review it.

**STOP HERE. Wait for the researcher to review, reorder, cut clips, and edit card questions before proceeding to any video work.**

---

## Step 3: Validate video file

1. Run ffprobe on the video to get: resolution, fps, codec, audio codec, duration
2. Confirm the video duration roughly matches the transcript duration
3. Report specs to the researcher

---

## Step 4: Cut clips (Module A)

### Timestamp rules
- **Never cut mid-sentence.** When a clip endpoint falls mid-sentence, extend to the next natural sentence boundary.
- **Pad endings**: Add 1-2 seconds of silence after the last word so it doesn't feel abrupt.
- **Pad beginnings**: If the quote starts mid-utterance, back up to the start of the sentence.
- Use `ffmpeg -ss [start] -to [end] -i [source] -c copy` for fast initial cuts (no re-encoding).
- Store clips in `outputs/{project-name}/clips/`

### After initial cuts
Check clip durations against the target total. If over budget, flag the longest clips and ask the researcher which to trim.

---

## Step 5: Generate title cards (Module A)

Every clip gets a 3-second title card as a transition.

### Title card rules
- **Card question must be contextual** - it should accurately reflect what the participant is actually answering in that specific clip, not just the discussion guide question. If the conversation drifted from the original question, or the best quote is responding to a follow-up, the card text should set up the viewer for what they're about to hear.
- Keep questions natural and conversational, not academic.
- Card questions come from the approved clip guide MD (the researcher may have edited them).

### Card styling
- Resolution: match source video (typically 1920x1080)
- Background: #232925 (GitHub Gray 5)
- Text: #F2F5F3 (GitHub Gray 1), Mona Sans SemiBold, 48pt
- Purple left accent bar: #8534F3, 6px wide
- Header line: "{STUDY NAME} | {PARTICIPANT CODE}" in purple (#8534F3), Mona Sans SemiBold, 28pt
- No PII anywhere on cards
- Duration: 3 seconds, with silent audio track matching clip format

### Card generation
```python
# Use PIL to generate card images, then FFmpeg to convert to 3-second video
# Match source video specs: resolution, fps, pixel format, audio codec/rate
ffmpeg -y -loop 1 -i card.png \
  -f lavfi -i anullsrc=r={audio_rate}:cl=mono \
  -c:v libx264 -preset fast -crf 23 -pix_fmt yuv420p -r {fps} \
  -c:a aac -b:a 32k -ar {audio_rate} -ac 1 \
  -t 3 card.mp4
```

---

## Step 6: Generate subtitles (Module A)

1. Extract relevant VTT entries for each clip's time range
2. Convert to SRT format with timestamps relative to clip start (not source video)
3. Replace participant real names with participant codes (e.g., "Josh" -> "P2")
4. Store SRT files in `outputs/{project-name}/subs/`

---

## Step 7: Encode clips with subtitles (Module A)

Do scaling and subtitle burn-in in a single FFmpeg pass:

```bash
ffmpeg -y -i clip.mp4 \
  -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:black,subtitles=clip.srt:force_style='FontName=Mona Sans,FontSize=24,PrimaryColour=&H00FFFFFF,OutlineColour=&H40000000,BackColour=&H80000000,BorderStyle=4,Outline=1,Shadow=0,MarginV=30'" \
  -c:v libx264 -preset fast -crf 23 \
  -c:a aac -b:a 32k -ar {audio_rate} -ac 1 \
  -r {fps} -pix_fmt yuv420p \
  output.mp4
```

All clips must have matching codec parameters for concatenation.

### Optional: Participant cropping
NOT recommended for most cases - Zoom gallery layouts shift with participant count, making reliable cropping very difficult. Only attempt if:
- The recording uses speaker view (single participant fills frame)
- The researcher specifically requests it and understands it may require per-clip adjustments

If cropping is requested, extract one frame per clip, visually verify the participant's position, and get researcher approval before batch processing.

---

## Step 8: Assemble highlight reel (Module A)

1. Build a concat file alternating: card1, clip1, card2, clip2, ...
2. Use FFmpeg concat demuxer: `ffmpeg -f concat -safe 0 -i concat.txt -c copy output.mp4`
3. Verify final duration and file size
4. Report to researcher: duration, file size, output path
5. Note: GitHub issue comments support up to 10MB video. For longer reels, suggest Loom or OneDrive for sharing.

Output: `outputs/{project-name}/highlight_reel_{participant}_{version}.mp4`

---

## Step 9: Structured notes doc (Module B)

Generate a Word document using python-docx with these specs:

### Content structure
1. Title: "{Study Name} Interview Notes"
2. Subtitle: "{Participant code} - {role description, no real name}" 
3. Participant Background section
4. Themed sections (one per major theme), each containing:
   - 1-2 paragraph narrative explanation of the finding
   - Full verbatim quotes with timestamps in callout boxes
   - Bullet points for sub-findings
5. End with a section on opportunities/implications if relevant

### Styling (GitHub brand)
- **H1**: Mona Sans Bold, 18pt, #232925. No bottom border.
- **H2**: Mona Sans SemiBold, 14pt, #8534F3 (Copilot Purple)
- **Body**: Mona Sans Regular, 11pt, #232925, 12pt after, 1.15 line spacing
- **Quotes**: Purple left border bar (3pt, #8534F3), light gray background (#F2F5F3), italic text, timestamp in gray
- **Callout boxes**: Colored left border bars. Green (#0FBF3E) for positive findings, purple (#8534F3) for Copilot/AI insights, orange (#F08A3A) for concerns/trends, blue (#3094FF) for security
- **Bullets**: Use bullet points, not numbered lists (except for sequential steps)
- **No PII**: Use participant codes throughout. Role descriptions are OK (e.g., "VP of Platform Engineering at a 130-person data infrastructure company")

### Quotes
- Always include full verbatim quotes with timestamps
- Don't clean up speech patterns too aggressively - keep the voice authentic

Output: `outputs/{project-name}/{participant}_interview_notes.docx`

---

## Step 10: Slack TL;DR (Module C)

Generate a plain text file for pasting into Slack.

### Format rules
- Plain text only - no `*bold*`, `_italic_`, backticks, or special bullets
- Use plain dashes (`-`) for bullet points
- Lead with the most surprising or actionable finding
- Each bullet: one key insight with a short verbatim quote
- End with a "Biggest opportunities" section (3-5 bullets) with concrete, actionable suggestions
- Target: 10-15 finding bullets + 3-5 opportunity bullets unless researcher says otherwise

### Template
```
TL;DR: {Study Name} - {Participant code} ({role, company size})

- {Finding with quote}
- {Finding with quote}
...

Biggest opportunities for {company/team}:
- {Opportunity 1}
- {Opportunity 2}
- {Opportunity 3}
```

Output: `outputs/{project-name}/slack_tldr.txt`

---

## File organization

All outputs go in `~/Desktop/COPILOT/outputs/{project-name}/`:
```
outputs/{project-name}/
  highlight_reel_{participant}.mp4    # Final highlight reel
  {participant}_interview_notes.docx  # Structured notes
  slack_tldr.txt                      # Slack update
  clip_guide.md                       # Clip order reference
  clips/                              # Individual clips (original cuts)
  clips_final/                        # Clips with subtitles burned in
  cards/                              # Title card PNGs and MP4s
  subs/                               # SRT subtitle files per clip
```

---

## Error handling

- If FFmpeg is not installed or missing subtitle support, walk the researcher through installation before proceeding
- If the VTT timestamps don't align with the video duration, flag it and ask the researcher to verify the files match
- If a clip cuts off mid-sentence after initial extraction, extend automatically to the next sentence boundary
- If total clip duration exceeds the target, present the clips sorted by duration and ask what to trim
