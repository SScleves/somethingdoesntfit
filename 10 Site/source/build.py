import json, re, glob, os, hashlib, sys
here = os.path.dirname(os.path.abspath(__file__))
book = json.load(open(os.path.join(here, 'book.json')))
import subprocess; subprocess.run(['python3', os.path.join(here, 'link_drafts.py')], check=False)
drafts = json.load(open(os.path.join(here, 'drafts.json'))) if os.path.exists(os.path.join(here, 'drafts.json')) else {'by': {}, 'unmatched': []}
GROUP = {'blocks-brief.json': 'MindBook brief', 'blocks-essay.json': "Santi's essay", 'blocks-vault.json': 'The vault: List, concepts, ledger'}
KINDS = {'conspiracy', 'case', 'document', 'theory', 'method', 'scene seed'}
REAL = {'documented', 'contested', 'claim', 'invented'}
def slug(s): return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')
STOP = set('the a an of and in on to for by with from at as is was his her their its'.split())
def toks(s): return {w for w in re.findall(r'[a-z0-9]+', s.lower()) if w not in STOP and len(w) > 2}
order = ['blocks-vault.json', 'blocks-essay.json', 'blocks-brief.json', 'blocks-mb1.json', 'blocks-mb2.json', 'blocks-mb3.json']
blocks, dropped = [], []
# The raw block files are not in the repo. When none is present, reuse the merged blocks.json as-is.
if not any(os.path.exists(os.path.join(here, fn)) for fn in order):
    blocks = json.load(open(os.path.join(here, 'blocks.json')))
    order = []
for fn in order:
    path = os.path.join(here, fn)
    if not os.path.exists(path): print('missing', fn); continue
    try: arr = json.load(open(path))
    except Exception as e: print('bad json', fn, e); continue
    for b in arr:
        t = (b.get('title') or '').strip(); s = (b.get('summary') or '').strip()
        if not t or not s: continue
        k = (b.get('kind') or 'case').strip().lower(); k = k if k in KINDS else 'case'
        r = (b.get('real') or 'claim').strip().lower(); r = r if r in REAL else 'claim'
        src = (b.get('source') or '').strip()
        grp = GROUP.get(fn) or ('MindBook: ' + re.split(r'\s+(?:by|—|-|\(|,)\s*', src)[0].strip() if src else 'MindBook')
        s = s.replace(' — ', ', ').replace('—', ', ')
        nb = {'title': t, 'kind': k, 'real': r, 'summary': s, 'source': src, 'group': grp}
        if b.get('fit'): nb['fit'] = b['fit'].strip()
        # dedupe on title overlap
        tt = toks(t); dup = None
        for o in blocks:
            ot = toks(o['title'])
            if tt and ot and (tt == ot or len(tt & ot) / len(tt | ot) >= 0.67): dup = o; break
        if dup:
            if src and src not in dup['source']: dup['source'] += '; ' + src
            if len(s) > len(dup['summary']): dup['summary'] = s
            dropped.append((t, dup['title'])); continue
        blocks.append(nb)
# Extra research batches (blocks-web-*.json) are appended once, by title.
have = {b['title'] for b in blocks}
for fn in sorted(glob.glob(os.path.join(here, 'blocks-web-*.json'))):
    tag = os.path.basename(fn)[len('blocks-web-'):-len('.json')]
    byt = {b['title']: b for b in blocks}
    for b in json.load(open(fn)):
        b = dict(b); b['group'] = 'Web research, ' + tag
        if b['title'] in have:
            # refresh text of an entry that came from this batch earlier; keep its id so placements survive
            o = byt[b['title']]
            if o.get('group') == b['group']:
                for k in ('kind', 'real', 'summary', 'source', 'fit'): o[k] = b.get(k, o.get(k))
            continue
        have.add(b['title']); blocks.append(b)
mpath = os.path.join(here, 'merges.json')
if order and os.path.exists(mpath):
    byt = {b['title']: b for b in blocks}
    for keep, absorb in json.load(open(mpath)):
        k = byt.get(keep)
        if not k: print('merge: missing', keep); continue
        for t in absorb:
            a = byt.get(t)
            if not a or a is k: print('merge: missing', t); continue
            if len(a['summary']) > len(k['summary']): k['summary'] = a['summary']
            for src in a['source'].split('; '):
                if src and src not in k['source']: k['source'] += '; ' + src
            if not k.get('fit') and a.get('fit'): k['fit'] = a['fit']
            blocks.remove(a); dropped.append((t, keep))
seen = set()
for b in blocks:
    if b.get('id'): seen.add(b['id']); continue
    base = 'b-' + slug(b['title'])[:40]
    i = base; n = 2
    while i in seen: i = f'{base}-{n}'; n += 1
    seen.add(i); b['id'] = i
json.dump(blocks, open(os.path.join(here, 'blocks.json'), 'w'), ensure_ascii=False, indent=0)
emb = lambda o: json.dumps(o, ensure_ascii=False).replace('</', '<\\/')
html = open(os.path.join(here, 'template.html')).read()
html = html.replace('/*BOOK_DATA*/null', emb(book)).replace('/*BLOCK_DATA*/[]', emb(blocks)).replace('/*DRAFT_DATA*/null', emb(drafts))
out = os.path.join(here, 'book-atlas.html'); open(out, 'w').write(html)
print('blocks', len(blocks), 'merged dupes', len(dropped), 'bytes', len(html))
from collections import Counter
print(Counter(b['group'] for b in blocks).most_common())
if '-v' in sys.argv:
    for t, d in dropped: print('  dup:', t, '=>', d)
