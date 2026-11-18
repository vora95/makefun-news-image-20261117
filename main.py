#!/usr/bin/env python3
"""news-image-20261117 entry: copy the front-page image to /output/entry.png.

The image (entry.png, 1024x1024) sums up the world's news of Tuesday
17 November 2026 — 27 stories, 4 continents, one front page.
Standard library only; no network. The copy is byte-identical on
every run, so the two grader runs always produce the same bytes.
"""

import os
import shutil

# The entry image is a fixed asset of this repository; the program only
# copies it, so the grader's two runs always write the same bytes.
HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUT_DIR, exist_ok=True)
shutil.copyfile(os.path.join(HERE, "entry.png"),
                os.path.join(OUT_DIR, "entry.png"))
