# The Atlas site

**Live page (private to Santi):** https://claude.ai/artifact/57zHit7EYNwWhgZiVBm9q7

The site is built from `02 Structure/THE BOOK v8 — every chapter explained.md`. Notes, verdicts, board cards and block placements are saved in the live page's own database, not in this folder. Ask Claude to read them back and fold them into THE BOOK.

- `Something Doesn't Fit Atlas.html` is a copy of the page. Opened from disk it is read-only, because saving only works inside claude.ai.
- `Story blocks — the library.md` holds all the story blocks, readable in Obsidian.
- `source/` holds the template, the parser for THE BOOK, the merged blocks (`blocks.json`), the extracted `book.json` and the build script. To rebuild after THE BOOK changes, run `parse_book.py` on THE BOOK, then `build.py` (it reuses `blocks.json` when the raw block files are absent), then republish to the same link. Block IDs come from their titles, so placements survive a rebuild.

**What the page saves (collections in its database):** `notes` (chapter/stage/node/decision notes and verdicts), `placements` (one document per concept per place: `<block>__<target>`, where the target is a chapter `ch-…`, a part `part-…`, a journey stage `hj-…` or a map node `mm-…`, with a `how` text), `blocks` (concepts Santi wrote himself), `journey` (per-stage overrides: chapter list and text), `mapnodes` and `mapbranches` (edits, additions and hidden nodes on the mind map), `board` (pinboard cards).
