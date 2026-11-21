#!/usr/bin/env python3
"""Entry point for news-image-20261120.

Copies the front-page image this repository holds (entry.png, drawn by
draw.py in this same repository) to the harness output directory as
entry.png. Pure standard library, so it runs in the grading sandbox with
no network and nothing installed. The copy is byte-identical every run.
"""
import os
import shutil
import sys


def output_dir():
    """Harness output dir: MAKEFUN_OUTPUT_DIR, else /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def source_image():
    """entry.png sitting next to this file in the repository."""
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, "entry.png")


def main():
    src = source_image()
    if not os.path.isfile(src):
        print("missing entry image: " + src, file=sys.stderr)
        return 1
    out = output_dir()
    os.makedirs(out, exist_ok=True)
    dst = os.path.join(out, "entry.png")
    shutil.copyfile(src, dst)
    print("wrote " + dst + " (" + str(os.path.getsize(dst)) + " bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
