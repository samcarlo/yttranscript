# yttranscript

Fetch a clean, timestamp-free transcript from any YouTube video.

## Requirements

- Python 3
- [`python-youtube-transcript-api`](https://aur.archlinux.org/packages/python-youtube-transcript-api) (AUR) or `pip install youtube-transcript-api`

## Install (optional)

To run `yttranscript` from anywhere, symlink the script into a directory on your `PATH`:

```bash
chmod +x yttranscript.py
ln -s "$PWD/yttranscript.py" ~/.local/bin/yttranscript
```

Make sure `~/.local/bin` is on your `PATH`. After this, the examples below can be run as `yttranscript ...` instead of `python3 yttranscript.py ...`.

## Usage

```bash
python3 yttranscript.py <youtube-url> [destination-folder]
```

The transcript is saved as `<video_id>.txt` in the destination folder, or the current directory if no folder is given. The destination folder is created if it does not already exist.

## Examples

```bash
python3 yttranscript.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
# Output: ./dQw4w9WgXcQ.txt

python3 yttranscript.py "https://youtu.be/dQw4w9WgXcQ" transcripts/
# Output: transcripts/dQw4w9WgXcQ.txt
```

Both `youtube.com/watch?v=` and `youtu.be/` URL formats are supported.
