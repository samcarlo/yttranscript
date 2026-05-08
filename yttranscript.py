#!/usr/bin/env python3

import sys
import re
import os
from youtube_transcript_api import YouTubeTranscriptApi


def extract_video_id(url):
    patterns = [
        r"(?:v=|\/)([0-9A-Za-z_-]{11})",
        r"youtu\.be\/([0-9A-Za-z_-]{11})",
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None


def main():
    if len(sys.argv) not in (2, 3):
        print(f"Usage: {sys.argv[0]} <youtube-url> [destination-folder]")
        sys.exit(1)

    url = sys.argv[1]
    dest = sys.argv[2] if len(sys.argv) == 3 else "."
    video_id = extract_video_id(url)

    if not video_id:
        print(f"Error: could not extract video ID from URL: {url}")
        sys.exit(1)

    transcript = YouTubeTranscriptApi().fetch(video_id)
    text = " ".join(snippet.text for snippet in transcript)

    # Collapse whitespace and normalize newlines from caption line breaks
    text = re.sub(r"\s+", " ", text).strip()

    os.makedirs(dest, exist_ok=True)
    output_file = os.path.join(dest, f"{video_id}.txt")
    with open(output_file, "w") as f:
        f.write(text + "\n")

    print(f"Transcript saved to {output_file}")


if __name__ == "__main__":
    main()
