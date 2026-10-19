# The Atlas site

**Live page (private to Santi):** https://claude.ai/artifact/57zHit7EYNwWhgZiVBm9q7

The site is built from `02 Structure/THE BOOK v8 — every chapter explained.md`. Notes, verdicts, board cards and block placements are saved in the live page's own database, not in this folder. Ask Claude to read them back and fold them into THE BOOK.

- `Something Doesn't Fit Atlas.html` is a copy of the page. Opened from disk it is read-only, because saving only works inside claude.ai.
- `Story blocks — the library.md` holds all the story blocks, readable in Obsidian.
- `source/` holds the template, the parser for THE BOOK, the merged blocks and the build script. To rebuild after THE BOOK changes, run `parse_book.py` on THE BOOK, then `build.py`, then republish to the same link. Block IDs come from their titles, so placements survive a rebuild.
