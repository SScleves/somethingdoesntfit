import re, json, sys
src = sys.argv[1]; out = sys.argv[2]
L = open(src, encoding='utf-8').read().split('\n')

def slug(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')[:48]

def norm(t):
    t = re.sub(r'\(.*?\)', '', t)
    return re.sub(r'[^a-z0-9 ]', '', t.lower()).strip()

def md(s):
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'\*(.+?)\*', r'<i>\1</i>', s)
    return s

# ---- locate sections
def idx(prefix, start=0):
    for i in range(start, len(L)):
        if L[i].startswith(prefix): return i
    raise SystemExit('missing ' + prefix)
p1 = idx('## PART 1'); p2 = idx('## PART 2'); p3 = idx('## PART 3')

KINDS = [("santi's chapter", 'santi'), ('a real story', 'real'), ('the villain alone', 'villain'),
         ('the organisation', 'org'), ("james's past", 'past'), ('coded scene', 'coded')]
def kind_of(tag):
    t = tag.lower()
    for k, v in KINDS:
        if k in t: return v
    return 'james'

# ---- Part 1: chapters
parts = []; cur = None; last = None
for i in range(p1 + 1, p2):
    line = L[i]
    if line.startswith('### '):
        name = line[4:].strip()
        cur = {'id': slug(name.split('—')[0]), 'name': name, 'chapters': [], 'summary': '', 'questions': []}
        parts.append(cur); continue
    m = re.match(r'^\*\*(.+?)\.\*\*\s*(.*)$', line)
    if m and cur is not None:
        title = m.group(1).strip(); rest = m.group(2)
        tag = ''
        mt = re.match(r'^\((.+?)\)\s*(.*)$', rest)
        if mt: tag, rest = mt.group(1), mt.group(2)
        last = {'title': title, 'tag': tag, 'kind': kind_of(tag), 'text': md(rest), 'why': '', 'beats': [], 'words': 0, 'meta': ''}
        cur['chapters'].append(last); continue
    if line.startswith("*Why it's here:*") and last:
        last['why'] = md(line.split(':*', 1)[1].strip()); continue
    if re.match(r'^\*Part \w+ ends', line) and cur:
        cur['summary'] = md(line.strip('*')); continue

# ---- Part 2: beats
beat_parts = []; bcur = None; blast = None; pending_q = None
for i in range(p2 + 1, p3):
    line = L[i]
    if line.startswith('### '):
        bcur = {'name': line[4:].strip(), 'blocks': []}; beat_parts.append(bcur); continue
    mq = re.match(r'^\*What it asks: (.+)\*$', line)
    if mq: pending_q = mq.group(1).strip(); continue
    m = re.match(r'^\*\*(.+?)\*\*\s*(.*)$', line)
    if m and bcur is not None:
        blast = {'title': m.group(1).strip(), 'meta': m.group(2).strip(' ·()'), 'bullets': [], 'q': pending_q}
        pending_q = None; bcur['blocks'].append(blast); continue
    if line.startswith('- ') and blast is not None:
        blast['bullets'].append(md(line[2:].strip()))

def words(meta):
    m = re.search(r'about ([\d,]+) words', meta)
    return int(m.group(1).replace(',', '')) if m else 0

# match blocks to chapters, part by part, in order
for pi, part in enumerate(parts):
    blocks = beat_parts[pi]['blocks'] if pi < len(beat_parts) else []
    used = set()
    for b in blocks:
        names = [n.strip() for n in b['title'].split(',')]
        titles = {norm(c['title']) for c in part['chapters']}
        if len(names) > 1 and all(norm(n) in titles for n in names):  # grouped block (Santi's four)
            for n in names:
                for ch in part['chapters']:
                    if norm(ch['title']) == norm(n):
                        pref = [x for x in b['bullets'] if norm(x.split(':')[0]) in (norm(n), norm(n).replace('the ', ''))]
                        ch['beats'] = [re.sub(r'^[^:]+:\s*', '', x) for x in pref]
                        ch['meta'] = b['meta']
            continue
        target = norm(b['title'])
        if target == 'coda': target = 'epilogue'
        elif target == 'epilogue':
            for ch in part['chapters']:
                if norm(ch['title']) == 'epilogue': ch['farFuture'] = 'PLACEHOLDER: the far-future scene is still Santi\'s to decide.'
            continue
        for ci, ch in enumerate(part['chapters']):
            if ci in used: continue
            if norm(ch['title']) == target:
                ch['beats'] = b['bullets']; ch['meta'] = b['meta']; ch['words'] = words(b['meta'])
                if b['q']: ch['movement'] = b['q']
                used.add(ci); break
        else:
            print('UNMATCHED beat block:', pi, b['title'], file=sys.stderr)

seen = {}
for part in parts:
    for ch in part['chapters']:
        base = 'ch-' + slug(ch['title'])
        n = seen.get(base, 0); seen[base] = n + 1
        ch['id'] = base if n == 0 else f'{base}-{n+1}'
        if not ch['beats']: print('no beats:', ch['title'], file=sys.stderr)

decisions = []
for i in range(p3 + 1, len(L)):
    m = re.match(r'^(\d+)\. (.+)$', L[i])
    if m: decisions.append({'id': 'dc-' + m.group(1), 'n': int(m.group(1)), 'text': md(m.group(2))})

# Part 0 blocks (raw, for the Foundations view)
part0 = []
for i in range(idx('## PART 0') + 1, p1):
    if L[i].strip() and L[i].strip() != '---': part0.append(md(L[i]))

data = {'version': re.sub(r'^# ', '', L[0]).strip(), 'parts': parts, 'decisions': decisions, 'part0': part0}
json.dump(data, open(out, 'w', encoding='utf-8'), ensure_ascii=False)
n = sum(len(p['chapters']) for p in parts)
print('parts', len(parts), 'chapters', n, 'decisions', len(decisions), 'words', sum(c['words'] for p in parts for c in p['chapters']))
for p in parts: print(p['id'], [c['id'] + ':' + c['kind'] for c in p['chapters']])
