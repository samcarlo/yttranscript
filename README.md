# yttranscript

Fetch a clean, timestamp-free transcript from any YouTube video.

## Requirements

- Python 3
- [`python-youtube-transcript-api`](https://aur.archlinux.org/packages/python-youtube-transcript-api) (AUR) or `pip install youtube-transcript-api`

## Usage

```bash
python3 yttranscript.py <youtube-url>
```

The transcript is saved as `<video_id>.txt` in the current directory.

## Example

```bash
python3 yttranscript.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
# Output: dQw4w9WgXcQ.txt
```

Both `youtube.com/watch?v=` and `youtu.be/` URL formats are supported.
