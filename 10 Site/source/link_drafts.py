"""Link the v6 manuscript drafts to the Atlas chapters.

Reads ../../01 Manuscript/v6/*.md, matches each file to a chapter in book.json by title
(exact-ish, then the overrides below), and writes drafts.json:
  {"by": {"<chapter id>": {"file","words","status","blurb","guess","mentions":[...]}},
   "unmatched": [{"file","words","status"}], "names": [...]}
Run by build.py; safe to run alone. Edit OVERRIDES when a filename and a chapter title differ.
"""
import json, os, re, glob
here = os.path.dirname(os.path.abspath(__file__))
V6 = os.path.join(here, '..', '..', '01 Manuscript', 'v6')
book = json.load(open(os.path.join(here, 'book.json')))
CH = [c for p in book['parts'] for c in p['chapters']]

# filename stem (after the number) -> chapter id. True = confident, False = my guess from the status line.
OVERRIDES = {
    'Cold open': ('ch-the-reading-room-the-opening', True),
    'Utrecht. A phone call. 1993': ('ch-utrecht-1993', True),
    'Deventer. A Thursday in March': ('ch-deventer-march', True),
    'The seventh tee': ('ch-a-round-with-a-stranger', False),
    'A car park. Thursday': ('ch-a-car-park', True),
    'A street. Night': ('ch-a-street-night', True),
    'A corridor. He is sixteen': ('ch-a-corridor-sixteen', True),
    'The floor': ('ch-the-night-he-stops-being-afraid', False),
    'The long table, again': ('ch-the-long-table-again', True),
    'Leiden. A printer’s shop. 1931': ('ch-leiden-1931', True),
    "Leiden. A printer's shop. 1931": ('ch-leiden-1931', True),
    'The table': ('ch-the-dinner', False),
    'The depot. Monday': ('ch-monday', True),
    'Coda': ('ch-epilogue', True),
}
# the same title twice in v6 and in the book: map by order
DUPES = {'Leave it': ['ch-leave-it', 'ch-leave-it-2']}

NAMES = ['James', 'Ana', 'Buddy', 'Mora', 'Frank', 'Pieter', 'Kalder', 'Bram', 'Anneke', 'Noor', 'Aylin', 'Els',
         'Beard Man', 'the professor', 'Koster', 'Verhoef', 'Dave', 'Tresidder']

def norm(s):
    s = s.lower().replace('’', "'")
    s = re.sub(r'\(.*?\)', ' ', s)
    return re.sub(r'[^a-z0-9]+', ' ', s).strip()

byt = {norm(c['title']): c['id'] for c in CH}
out, unmatched, seen_dupe = {}, [], {}
files = sorted(glob.glob(os.path.join(V6, '*.md')))
for f in files:
    base = os.path.basename(f)[:-3]
    if base.lower().startswith('readme'): continue
    stem = re.sub(r'^\d+\s*[—\-]\s*', '', base)
    txt = open(f, encoding='utf-8').read()
    lines = txt.split('\n')
    status = ''
    if lines and lines[0].startswith('> Status:'):
        status = lines[0][len('> Status:'):].strip(); body = '\n'.join(lines[1:])
    else: body = txt
    body = re.sub(r'^#.*$', '', body, flags=re.M)
    words = len(re.findall(r"[\w'’-]+", body))
    state = 'santi' if 'SANTI' in status.upper() else 'draft'
    blurb = re.sub(r'^.*?\d{4}\.\s*', '', status, count=1)  # drop "v6 DRAFT — Fable, 11 Oct 2026."
    mentions = [n for n in NAMES if re.search(r'\b' + re.escape(n) + r'\b', body, flags=re.I)]
    cid, guess = None, False
    if stem in DUPES:
        i = seen_dupe.get(stem, 0); seen_dupe[stem] = i + 1
        if i < len(DUPES[stem]): cid = DUPES[stem][i]
    elif stem in OVERRIDES: cid, sure = OVERRIDES[stem]; guess = not sure
    elif norm(stem) in byt: cid = byt[norm(stem)]
    rec = {'file': base + '.md', 'words': words, 'status': state, 'blurb': blurb[:220], 'guess': guess, 'mentions': mentions}
    if cid and cid not in out: out[cid] = rec
    else: unmatched.append({'file': base + '.md', 'words': words, 'blurb': blurb[:220]})
res = {'by': out, 'unmatched': unmatched, 'names': NAMES, 'folder': '01 Manuscript/v6'}
json.dump(res, open(os.path.join(here, 'drafts.json'), 'w'), ensure_ascii=False, indent=0)
if __name__ == '__main__':
    print('matched', len(out), 'unmatched', [u['file'] for u in unmatched], 'guesses', [k for k, v in out.items() if v['guess']])
