# The Atlas site

**Live page (private to Santi):** https://claude.ai/artifact/57zHit7EYNwWhgZiVBm9q7

The site is built from `02 Structure/THE BOOK v8 — every chapter explained.md`. Notes, verdicts, board cards and block placements are saved in the live page's own database, not in this folder. Ask Claude to read them back and fold them into THE BOOK.

- `Something Doesn't Fit Atlas.html` is a copy of the page. Opened from disk it is read-only, because saving only works inside claude.ai.
- `Story blocks — the library.md` holds all the story blocks, readable in Obsidian.
- `source/` holds the template, the parser for THE BOOK, the merged blocks (`blocks.json`), the extracted `book.json` and the build script. To rebuild after THE BOOK changes, run `parse_book.py` on THE BOOK, then `build.py` (it reuses `blocks.json` when the raw block files are absent), then republish to the same link. Block IDs come from their titles, so placements survive a rebuild.

**Drafts.** `source/link_drafts.py` (run by `build.py`) reads `01 Manuscript/v6/*.md`, matches each file to a chapter by title (overrides inside the script for files whose names differ; three are marked as guesses), and gives the page drafted word counts, status lines and which characters are named in each draft. Rebuild after drafting to refresh the Desk tab.

**Engines tab (15 Nov 2026).** `source/engines.py` (run by `build.py`) reads `08 Research/Engines/` and `08 Research/Comps/ADDENDUM 05 — …md` into `source/engines.json`, and the page shows them as the Engines tab: the three changes to make first, the Part Two table one chapter at a time, the canon conflicts, the four mechanisms, and every book's map, section notes and Q&A. Each proposal, table row and canon conflict has a note box; the notes are saved in the `notes` collection under ids that start with `en-` (`en-top-N`, `en-row-<chapter>`, `en-cc-<conflict>`, `en-mech-<name>`, `en-<book>-pN`). The ids come from titles, so keep titles stable. The library lives only on branch `comps-conspiracy-engines`, so rebuild the site from that branch; a build from a branch without `08 Research/Engines/` has no Engines tab.

**What the page saves (collections in its database):** `notes` (chapter/stage/node/decision notes and verdicts), `placements` (one document per concept per place: `<block>__<target>`, where the target is a chapter `ch-…`, a part `part-…`, a journey stage `hj-…` or a map node `mm-…`, with a `how` text), `blocks` (concepts Santi wrote himself), `journey` (per-stage overrides: chapter list and text), `mapnodes` and `mapbranches` (edits, additions and hidden nodes on the mind map), `board` (pinboard cards).
