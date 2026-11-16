"""Read the conspiracy-engines library (08 Research/Engines and ADDENDUM 05) into engines.json for the Atlas's Engines tab.

Each piece Santi can answer gets a stable note id (en-...), derived from its title, so notes survive a rebuild:
transfer proposals in each map's section 5, the ranked changes, the mechanisms, the Part Two chapter rows
and the canon conflicts. Skipped quietly when the folder isn't there (branches without the library).
"""
import glob, json, os, re
import markdown

here = os.path.dirname(os.path.abspath(__file__))
root = os.path.abspath(os.path.join(here, '..', '..'))
eng = os.path.join(root, '08 Research', 'Engines')
out = os.path.join(here, 'engines.json')
add_glob = os.path.join(root, '08 Research', 'Comps', 'ADDENDUM 05*.md')


def slug(s): return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')[:48]


def prep(md):
    # python-markdown wants a blank line before a list or a table; the notes often don't leave one
    lines, prev = [], ''
    for ln in md.split('\n'):
        starts = re.match(r'\s*([-*+] |\d+\. |\|)', ln)
        pstarts = re.match(r'\s*([-*+] |\d+\. |\|)', prev)
        if starts and prev.strip() and not pstarts: lines.append('')
        lines.append(ln); prev = ln
    return '\n'.join(lines)


def html(md):
    return markdown.markdown(prep(md), extensions=['tables', 'sane_lists'])


def plain(md):
    return re.sub(r'[*_`]', '', md).strip()


def h2s(md):
    """[(title, body)] split at '## ' headings; text before the first one has title ''."""
    parts, cur, buf = [], '', []
    for ln in md.split('\n'):
        if ln.startswith('## '):
            parts.append((cur, '\n'.join(buf))); cur, buf = ln[3:].strip(), []
        else: buf.append(ln)
    parts.append((cur, '\n'.join(buf)))
    return parts


def bold_items(body, pat):
    """Split a section at paragraphs that open with a bold label matching pat; returns (intro, [(label, md)])."""
    items, intro, cur = [], [], None
    for ln in body.split('\n'):
        m = re.match(r'\*\*(' + pat + r')', ln)
        if m:
            cur = [m.group(1), [ln]]; items.append(cur)
        elif cur: cur[1].append(ln)
        else: intro.append(ln)
    return '\n'.join(intro), [(l, '\n'.join(b).strip()) for l, b in items]


def item_html(md):
    # the title is shown as the item's heading, so drop the bold label that opens the text
    return html(re.sub(r'^\*\*.+?\*\*[ .:]*', '', md.strip(), count=1))


def bold_title(md):
    m = re.match(r'\*\*(.+?)\*\*', md)
    return plain(m.group(1)).rstrip('.') if m else plain(md[:80])


def read_for():
    rd = os.path.join(eng, 'README.md'); res = {}
    if not os.path.exists(rd): return res
    for ln in open(rd, encoding='utf8'):
        cells = [c.strip() for c in ln.strip().strip('|').split('|')]
        if len(cells) == 3 and cells[0] not in ('Book', '---'): res[plain(cells[0])] = (plain(cells[1]), cells[2])
    return res


def book(folder, rf):
    name = os.path.basename(folder)
    author, title = [x.strip() for x in name.split('—', 1)]
    bid = 'en-' + slug(author.split()[0] + '-' + title)[:30]
    mp = os.path.join(folder, '00-map.md')
    md = open(mp, encoding='utf8').read()
    sections = []
    for t, body in h2s(md):
        if not t:
            # the H1 line goes; the coverage/brief block stays as the book's intro
            intro = re.sub(r'^# .*\n', '', body).strip()
            continue
        sec = {'title': t, 'html': '', 'items': []}
        if t.startswith('5'):
            pre, items = bold_items(body, r'(?:5\.)?\d+\.?\d*\s')
            sec['html'] = html(pre)
            for label, b in items:
                num = label.strip().rstrip('.').replace('.', '-')
                sec['items'].append({'id': f'{bid}-p{num}', 'title': bold_title(b), 'html': item_html(b)})
        else:
            sec['html'] = html(body)
        sections.append(sec)
    notes = []
    for f in sorted(glob.glob(os.path.join(folder, '[0-8][0-9]-*.md'))):
        if os.path.basename(f).startswith('00-'): continue
        txt = open(f, encoding='utf8').read()
        h = re.match(r'#\s*(.+)', txt)
        lab = h.group(1).split('—')[-1].strip() if h else os.path.basename(f)
        notes.append({'file': os.path.basename(f), 'title': lab, 'html': html(re.sub(r'^# .*\n', '', txt))})
    qa = os.path.join(folder, '91-qa.md')
    readfor = ''
    for k, (r, _) in rf.items():
        if slug(title)[:10] in slug(k): readfor = r; break
    return {'id': bid, 'author': author, 'title': title, 'folder': '08 Research/Engines/' + name, 'readfor': readfor,
            'intro': html(intro), 'sections': sections, 'notes': notes,
            'qa': html(re.sub(r'^# .*\n', '', open(qa, encoding='utf8').read())) if os.path.exists(qa) else ''}


def addendum(path):
    md = open(path, encoding='utf8').read()
    parts = h2s(md)
    head = parts[0][1]
    d = {'file': '08 Research/Comps/' + os.path.basename(path), 'title': '', 'intro': '', 'sections': []}
    m = re.search(r'^# (.+)$', head, re.M); d['title'] = m.group(1) if m else 'Addendum 05'
    d['intro'] = html(re.sub(r'^# .*\n', '', head).replace('\n---', ''))
    for t, body in parts[1:]:
        body = re.sub(r'\n---\s*$', '', body.strip())
        sid = 'en-add-' + t[0]
        sec = {'id': sid, 'title': t, 'html': '', 'items': [], 'rows': [], 'kind': 'plain'}
        if t.startswith('a.'):
            pre, items = bold_items(body, r'[A-Z]\.\s|[A-Z][a-z].{0,40}?\.\*\*')
            sec['html'] = html(pre); sec['kind'] = 'items'
            for label, b in items:
                sec['items'].append({'id': 'en-mech-' + slug(bold_title(b))[:24], 'title': bold_title(b), 'html': item_html(b)})
        elif t.startswith('b.'):
            pre = []; rows = []; head_cells = None
            for ln in body.split('\n'):
                if ln.startswith('|'):
                    cells = [c.strip() for c in ln.strip().strip('|').split('|')]
                    if head_cells is None: head_cells = cells
                    elif not re.match(r'^-+$', cells[0]): rows.append(cells)
                elif not rows: pre.append(ln)
            sec['html'] = html('\n'.join(pre)); sec['kind'] = 'rows'; sec['cols'] = head_cells
            for r in rows:
                sec['rows'].append({'id': 'en-row-' + slug(plain(r[0])), 'chapter': plain(r[0]),
                                    'cells': [markdown.markdown(c).removeprefix('<p>').removesuffix('</p>') for c in r]})
        elif t.startswith('c.'):
            pre, items = bold_items(body, r'\d+\.\s|What moved')
            sec['html'] = html(pre); sec['kind'] = 'items'
            for label, b in items:
                iid = 'en-top-' + label.strip().rstrip('.') if label[0].isdigit() else ''
                sec['items'].append({'id': iid, 'title': bold_title(b), 'html': item_html(b)})
        elif t.startswith('d.'):
            sec['kind'] = 'items'
            m = re.split(r'\n\*\*Canon conflicts[^\n]*\n', body, maxsplit=1)
            sec['html'] = html(m[0])
            if len(m) > 1:
                sec['subhead'] = 'Canon conflicts: these are yours to decide'
                for b in re.split(r'\n(?=- \*\*)', '\n' + m[1].strip()):
                    b = b.strip()
                    if not b.startswith('- **'): continue
                    b = b[2:]
                    sec['items'].append({'id': 'en-cc-' + slug(bold_title(b))[:30], 'title': bold_title(b), 'html': item_html(b), 'decision': True})
        else:
            sec['html'] = html(body)
        d['sections'].append(sec)
    return d


def review(path):
    """A REVIEW NN file: an intro, then '## N. section' blocks of findings that open with a bold 'N.M Title.' label."""
    md = open(path, encoding='utf8').read()
    kind, n = re.search(r'(REVIEW|STRUCTURE) (\d+)', os.path.basename(path)).groups()
    n = ('st' if kind == 'STRUCTURE' else 'rv') + n.lstrip('0')
    parts = h2s(md)
    m = re.search(r'^# (.+)$', parts[0][1], re.M)
    d = {'id': 'en-' + n, 'file': '08 Research/Comps/' + os.path.basename(path), 'title': m.group(1) if m else os.path.basename(path),
         'intro': html(re.sub(r'^# .*\n', '', parts[0][1])), 'sections': []}
    for t, body in parts[1:]:
        pre, items = bold_items(body, r'\d+\.\d+\s')
        sec = {'title': t, 'html': html(pre), 'items': []}
        for label, b in items:
            sev = re.search(r'\*(?:Severity|Verdict):\s*([^*]+?)\.?\*', b) or re.match(r'\*\*.+?\*\*\s*\*(Keep|Sharpen|Change|Merge|Cut)\.?\*', b)
            sec['items'].append({'id': f"en-{n}-{label.strip().replace('.', '-')}", 'title': bold_title(b), 'html': item_html(b),
                                 'sev': sev.group(1).strip().lower() if sev else ''})
        d['sections'].append(sec)
    return d


def toolbox(path):
    """A TOOLBOX NN file: '## N. Name' blocks, each with bold-labelled paragraphs and a 'Chapters:' line of titles split by ';'."""
    md = open(path, encoding='utf8').read()
    parts = h2s(md)
    tools = []
    for t, body in parts[1:]:
        m = re.match(r'(\d+)\.\s*(.+)', t)
        if not m: continue
        chm = re.search(r'^Chapters:\s*(.+)$', body, re.M)
        body = re.sub(r'^Chapters:.*$', '', body, flags=re.M)
        lab = lambda name: (re.search(r'\*\*' + name + r'\.\*\*\s*(.+)', body) or [None, ''])[1].strip()
        rest = re.sub(r'\*\*(The move|Test question)\.\*\*.*\n?', '', body)
        tools.append({'id': 'en-tb-' + m.group(1), 'n': int(m.group(1)), 'title': m.group(2).strip(), 'one': plain(lab('The move')),
                      'q': plain(lab('Test question')), 'html': html(rest), 'chapters': [c.strip() for c in chm.group(1).split(';')] if chm else []})
    return {'file': '08 Research/Comps/' + os.path.basename(path), 'intro': html(re.sub(r'^#+ .*\n', '', parts[0][1], flags=re.M)), 'tools': tools}


def main():
    if not os.path.isdir(eng):
        if os.path.exists(out): os.remove(out)
        print('engines: no library on this branch'); return
    rf = read_for()
    books = [book(f, rf) for f in sorted(glob.glob(os.path.join(eng, '*—*'))) if os.path.exists(os.path.join(f, '00-map.md'))]
    adds = sorted(glob.glob(add_glob))
    comps = os.path.join(root, '08 Research', 'Comps')
    revs = [review(p) for p in sorted(glob.glob(os.path.join(comps, 'STRUCTURE *.md'))) + sorted(glob.glob(os.path.join(comps, 'REVIEW *.md')))]
    tbs = sorted(glob.glob(os.path.join(comps, 'TOOLBOX *.md')))
    data = {'addendum': addendum(adds[0]) if adds else None, 'books': books, 'reviews': revs, 'toolbox': toolbox(tbs[-1]) if tbs else None}
    ids = [i['id'] for b in books for s in b['sections'] for i in s['items']]
    ids += [i['id'] for r in revs for s in r['sections'] for i in s['items']]
    if data['toolbox']: ids += [t['id'] for t in data['toolbox']['tools']]
    if data['addendum']:
        for s in data['addendum']['sections']:
            ids += [i['id'] for i in s['items'] if i['id']] + [r['id'] for r in s['rows']]
    dup = {i for i in ids if ids.count(i) > 1}
    if dup: print('engines: duplicate note ids', sorted(dup))
    json.dump(data, open(out, 'w'), ensure_ascii=False)
    print('engines:', len(books), 'books,', len(ids), 'note slots,', os.path.getsize(out), 'bytes')


if __name__ == '__main__':
    main()
