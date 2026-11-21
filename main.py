#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
main.py for the-poem-about-two-agents-20261121-1441
Reads poem.txt beside this script, validates length (1 to 280 code points)
and non-whitespace content, and writes it to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

from pathlib import Path
import os
import sys

def main():
    script_dir = Path(__file__).resolve().parent
    poem_path = script_dir / "poem.txt"
    
    if not poem_path.is_file():
        print(f"Error: poem.txt not found at {poem_path}", file=sys.stderr)
        sys.exit(1)
        
    poem_text = poem_path.read_text(encoding="utf-8")
    
    # Gate checks
    if not poem_text or not poem_text.strip():
        print("Error: poem.txt is empty or only whitespace", file=sys.stderr)
        sys.exit(1)
        
    char_count = len(poem_text)
    if not (1 <= char_count <= 280):
        print(f"Error: poem length {char_count} out of bounds (1-280)", file=sys.stderr)
        sys.exit(1)
        
    output_dir_env = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    output_dir = Path(output_dir_env)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(poem_text, encoding="utf-8")
    print(f"Successfully wrote {char_count} chars to {entry_path}")

if __name__ == "__main__":
    main()
