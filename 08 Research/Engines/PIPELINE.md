# PIPELINE — how the conspiracy-engine notes are built

This folder copies TheMindBook's way of working (`TheMindBook/PIPELINE.md`) for one job: reading novels for **how conspiracy material pushes a story forward**, so that an agent helping Santi with *Something Doesn't Fit* can find, cite and reuse the technique. A fresh session can continue the project from this file and the repo alone.

Santi's full brief for the job is the last section of this file. The short version: in SDF's Part Two James mostly *receives* documents. For every book we want to know (1) at each stage, why can the protagonist not stop here; (2) how a large piece of lore gets in without the story going still; (3) what James would *do* differently, in a named v8.2 chapter, if we borrowed it, with a cost.

## Layout

```
08 Research/Engines/
  README.md                  what is here and how to use it (start here)
  PIPELINE.md                this file
  <Author> — <Title>/
    00-map.md                the comp: Santi's seven sections (coverage, engine table,
                             lore, mechanism, transfer to SDF, do not take, quote bank)
    NN-<section>.md          one note per reading section (the evidence layer)
    91-qa.md                 questions an SDF agent will ask, answered with pointers
08 Research/Comps/ADDENDUM 05 — Conspiracy engines (what moves a conspiracy plot).md
                             the cross-book synthesis (after Tier 1, again after Tier 2)
```

The book texts are **never** in this repo. The repo is public. Converted text lives only in a scratch folder outside it.

## Stages, per book

1. **Get the text.** Books arrive in `/opt/media/books/<Author>/<Title>/` (qBittorrent, category `books`). Convert with `ebook-convert book.epub book.txt` into a scratch folder outside the repo.
2. **Split into reading sections** at the author's chapter breaks, about 30,000 words each, so one reader can hold a whole section (`split.py <book.txt> <out> '<chapter-heading regex>' 30000`). A short work (a Borges story) is one section. Sections, not chapters, are the unit: the engine table wants 8 to 15 rows per book, and one section gives one to three rows.
3. **Section notes**, one reader per section, all in parallel. Each reads the ENTIRE section and writes `NN-<section>.md` from the template below. No knowledge from outside the text; if unavoidable, mark it *[from memory, not from the text]*.
4. **Quote check** (mechanical). Every quote in a section note is searched for in the source text; any that is not found verbatim is fixed or removed.
5. **Book map and Q&A**, one writer per book, after all its section notes. The writer reads the SDF Step 0 files (below), every section note of the book, and writes `00-map.md` (Santi's seven sections, at most about 2,500 words, sections 2 and 5 get the space) and `91-qa.md` (30–50 questions an SDF agent would ask, each answer pointing at a section note and, where relevant, a v8.2 chapter by title).
6. **Commit**, one commit per book, on branch `comps-conspiracy-engines`. Push. Never merge.
7. **Synthesis** after Tier 1, again after Tier 2: `08 Research/Comps/ADDENDUM 05 — …md`, per Santi's Step 3.

## Section-note template

```markdown
# <Author>, <Title> — <section label (chapters x–y)>

> Coverage: chapters x–y (about N words), read in full, <date>. Edition: <as in the file>.

## Movements
| Step | What the protagonist wants right now | What he finds | What it costs him | Why he cannot stop here | What it forces next |
(one to three rows; the "why he cannot stop here" column is the point)

## Why it grips
What makes this section work on the page, in craft terms a writer can copy: what the
reader is waiting for, what is withheld, the reversal, the pressure on the hero, the
scene that does the most work and how it is built. Concrete, with chapter cites.
Not adjectives, not praise.

## How the conspiracy moves the story here
Exactly how the conspiracy (or secret, or hidden order) changes what the hero does
next in this section: what it blocks, what it demands, what it costs, who it puts in
the room. If in this section it is only texture, say so.

## How the lore gets in
For each large piece of conspiracy, history or rule-of-the-world delivered in this section:
form (object, document, conversation, lecture, scene), roughly how long, how long until
something happens again, and whether the story stalls there and why.

## Mechanism notes
What in this section bears on the four candidate fixes (A gate, B canary, C front,
D lock and key) or shows a fifth. Cite chapter numbers.

## Quotes
At most four, each under 25 words, with chapter. Only lines that show a technique.

## Flags
Anything SDF's rules forbid (real people named as complicit, invented edits on real books).
```

Length 800–1,400 words. No plot recap beyond what the table needs. No theme essays, no praise. Santi's standing ask (11 Nov 2026): "really capture what made those books great and how the conspiracies actually helped progress the story." The map's section 1 therefore ends with two plain sentences on what makes the book work, and section 4 explains the mechanism the way a writer would explain it to another writer.

## Step 0 files every map writer reads first (branch v8-draft)

1. `02 Structure/THE BOOK v8 — every chapter explained.md` (the plan; Part 0 holds the rules)
2. `01 Manuscript/v8/_BRIEF — canon and voice for the v8 pass.md`
3. `01 Manuscript/v8/` (every chapter that exists). Part Two has no v8 chapters yet; its v7 drafts are in `01 Manuscript/v7/` (The corporate day, The drill, The money, Leiden nine years ago, The promise, The other ten, Frank loose, The reading room continued).
4. `09 The List/The List — entries.md`
5. `08 Research/MINDBOOK — Conspiracy brief for SDF.md`
6. `08 Research/Comps/PKD — VALIS.md` (the format and tone to match)
7. `08 Research/Comps/00 — SYNTHESIS (...).md` (its lesson: earlier comps recommended things already on the page)

## What Step 0 found (11 Nov 2026)

- The diagnosis holds against the drafts: in The drill and The money James notices a format and reads invoices because the job hands them to him (Saskia's folder, a role added "with a sigh"). The only cost is fear.
- Not all of Part Two is passive. **On land** uses mechanism B once in the v8.2 plan and v8 brief (the invented book; Kalder says he has read it), cashed only in The dinner ("the book you said you'd read"). Correction (Foucault map): no draft has it yet; the only draft, `01 Manuscript/v6/18 — On land.md`, is the older Deventer-slip version where Kalder breaks the friendship off. **The other ten** is active (public records, the widow in Zwolle) but ends with James choosing not to act.
- So the precise gap: no gate (nothing James must prove before he may act) and no cost of being wrong. Every transfer proposal must say whether it is already on the page, and where.

## Rules that matter

- Never commit book text, extracts longer than the quote rule, or converted files.
- Never edit anything under `01 Manuscript/` or `02 Structure/`.
- A book that is missing or unreadable gets no folder; list it in the addendum under "Not read".
- SDF rules (from the plan's Part 0) bind every proposal: reveals as objects in James's hands; he cannot hack, break in or pressure anyone; doors open only when a person chooses; the organisation discredits rather than prevents; killing is rare and a failure; real anomalies may be real, edits, people and companies are invented; never an invented edit on a real book; funny to the end; a dog under every table.
- Everything in a map or the addendum is a PROPOSAL. Santi's decisions are marked PLACEHOLDER.

## Reading list and what each book is for

Tier 1: Pérez-Reverte *The Club Dumas* (comparing copies as a whole plot); King *11/22/63* (mechanism A, the gate; the past pushing back); Borges "Tlön, Uqbar, Orbis Tertius" (one copy with extra pages; dread from a variant); Eco *Foucault's Pendulum* (mechanism B; the Diabolicals as clowns); Orwell *1984* (rewriting records; the forbidden book as the state's trap); Grady *Six Days of the Condor* (a reader of reports, one discrepancy, its price); Gibson *Pattern Recognition* (a nose, not a method; a forum as a place; clues as objects).
Tier 2: Pynchon *Lot 49*; DeLillo *Libra*; Eco *The Name of the Rose*; Powers *Declare*; Zafón *The Shadow of the Wind*; Singer *The Parallax View*; Eco *Numero Zero*; Abrams & Dorst *S.*; Shea & Wilson *Illuminatus!* (mechanism C).
Tier 3 (shorter files fine): Eco *The Prague Cemetery*; Condon *The Manchurian Candidate*; Tartt *The Secret History*; Kostova *The Historian*; Crouch *Recursion*; Ellroy *American Tabloid*; Dick *The Man in the High Castle*.
