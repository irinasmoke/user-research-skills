
import re


# Flexible filler word matching using regex
import string
FILLER_PATTERNS = [
    r"^mhm[.!?,]*$",
    r"^mm[.!?,]*$",
    r"^mm-hmm[.!?,]*$",
    r"^mmhmm[.!?,]*$",
    r"^ok[.!?,]*$",
    r"^okay[.!?,]*$",
    r"^yeah[.!?,]*$",
    r"^uh[.!?,]*$",
    r"^um[.!?,]*$",
    r"^cool[.!?,]*$",
    r"^got it[.!?,]*$",
    r"^hello[.!?,]*$",
    r"^thank you[.!?,]*$",
    r"^uh huh[.!?,]*$",
    r"^uh-huh[.!?,]*$",
    r"^sounds good[.!?,]*$",
    r"^great[.!?,]*$",
    r"^right[.!?,]*$",
    r"^sure[.!?,]*$",
    r"^alright[.!?,]*$",
    r"^yep[.!?,]*$",
    r"^no[.!?,]*$",
    r"^yes[.!?,]*$",
    r"^thanks[.!?,]*$",
    r"^fine[.!?,]*$",
    r"^bye[.!?,]*$",
    r"^hi[.!?,]*$",
    r"^good[.!?,]*$",
    r"^okay[.!?,]*$",
    r"^all right[.!?,]*$",
    r"^alright[.!?,]*$",
    r"^right[.!?,]*$",
    r"^sure[.!?,]*$",
    r"^yup[.!?,]*$",
    r"^hmm[.!?,]*$",
    r"^oh[.!?,]*$",
    r"^well[.!?,]*$",
    r"^nope[.!?,]*$",
    r"^thanks[.!?,]*$",
    r"^thank you[.!?,]*$",
    r"^bye[.!?,]*$",
    r"^hi[.!?,]*$",
    r"^hello[.!?,]*$",
    r"^and[.!?,]*$",
    # Patterns for repeated filler words
    r"^(ok[.!?,]*\s*){2,}$",
    r"^(yeah[.!?,]*\s*){2,}$",
    r"^(mhm[.!?,]*\s*){2,}$",
    r"^(uh[.!?,]*\s*){2,}$",
]

def is_filler(text):
    txt = text.strip().lower()
    # Remove punctuation for matching
    txt_no_punct = txt.translate(str.maketrans('', '', string.punctuation))
    
    # Check individual patterns
    for pat in FILLER_PATTERNS:
        if re.match(pat, txt_no_punct, re.IGNORECASE):
            return True
    
    # Check if text consists only of combinations of common filler words
    filler_words = ['ok', 'okay', 'yeah', 'mhm', 'uh', 'um', 'uh-huh', 'uhuh', 'cool', 'right', 'sure', 'yep', 'no', 'yes', 'good', 'great', 'fine', 'alright', 'all right']
    words = txt_no_punct.split()
    if len(words) > 0 and all(word in filler_words for word in words):
        return True
    
    # Special case for hyphenated filler words like "uh-huh"
    if txt_no_punct in ['uhhuh', 'uhuh']:
        return True
    
    return False

def clean_vtt_transcript(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    cleaned = []
    current_speaker = None
    current_text = []

    speaker_pattern = re.compile(r'<v ([^>]+)>')
    for line in lines:
        # Remove </v> from the line if present
        line = line.replace('</v>', '')
        # Skip WEBVTT, timestamps, and empty lines
        if line.strip() == '' or re.match(r'^\d{2}:\d{2}:\d{2}\.\d{3}', line) or line.startswith('WEBVTT') or re.match(r'^[a-f0-9-]+', line):
            continue

        match = speaker_pattern.search(line)
        if match:
            speaker = match.group(1)
            text = speaker_pattern.sub('', line).strip()
            if is_filler(text):
                continue
            if speaker == current_speaker:
                current_text.append(text)
            else:
                if current_speaker and current_text:
                    block = ' '.join(current_text).strip()
                    if not is_filler(block):
                        cleaned.append(f"{current_speaker}: {block}\n")
                current_speaker = speaker
                current_text = [text] if not is_filler(text) else []
        else:
            # Continuation of previous speaker's text
            if current_speaker and not is_filler(line.strip()):
                current_text.append(line.strip())

    # Add last speaker block
    if current_speaker and current_text:
        block = ' '.join(current_text).strip()
        # Remove block if every line in it is a filler
        block_lines = [line.strip() for line in block.split('\n') if line.strip()]
        if not is_filler(block) and not all(is_filler(line) for line in block_lines):
            cleaned.append(f"{current_speaker}: {block}\n")

    # Final pass: remove any remaining lines that are pure filler
    final_cleaned = []
    for line in cleaned:
        # Extract just the text part after "Speaker: "
        if ': ' in line:
            text_part = line.split(': ', 1)[1].strip()
            if not is_filler(text_part):
                final_cleaned.append(line)
        else:
            final_cleaned.append(line)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.writelines(final_cleaned)

# Usage example:
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 3:
        clean_vtt_transcript(sys.argv[1], sys.argv[2])
    else:
        print("Usage: python clean_vtt_transcript.py <input.vtt> <output.txt>")
