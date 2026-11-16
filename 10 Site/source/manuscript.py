"""Read the reading copy of the manuscript (the newest 01 Manuscript/vN folder) into manuscript.json for the Atlas's Read tab.

Each chapter keeps its paragraphs as separate blocks, so a note can be pinned to one paragraph.
The first line of a draft ("> Status: ...") says who wrote it and what changed; it is shown above the text.
"""
import glob, json, os, re
import markdown

here = os.path.dirname(os.path.abspath(__file__))
root = os.path.abspath(os.path.join(here, '..', '..'))
out = os.path.join(here, 'manuscript.json')
book = json.load(open(os.path.join(here, 'book.json')))
CH = [c for p in book['parts'] for c in p['chapters']]


def norm(s):
    s = re.sub(r'\(.*?\)', ' ', s.lower().replace('’', "'"))
    return re.sub(r'[^a-z0-9]+', ' ', s).strip()


def main():
    folders = sorted(glob.glob(os.path.join(root, '01 Manuscript', 'v[0-9]*')), key=lambda f: int(re.search(r'v(\d+)$', f).group(1)))
    if not folders:
        print('manuscript: no folder'); return
    folder = folders[-1]
    byt = {}
    for c in CH: byt.setdefault(norm(c['title']), []).append(c['id'])
    kind_of = {c['id']: c['kind'] for c in CH}
    part_of = {c['id']: pi for pi, p in enumerate(book['parts']) for c in p['chapters']}
    seen, chapters = {}, []
    for f in sorted(glob.glob(os.path.join(folder, '[0-9]*.md'))):
        base = os.path.basename(f)[:-3]
        title = re.sub(r'^\d+\s*[—-]\s*', '', base)
        txt = open(f, encoding='utf8').read().replace('\r', '')
        status = ''
        m = re.match(r'>\s*Status:\s*(.*)\n', txt)
        if m: status = m.group(1).strip(); txt = txt[m.end():]
        txt = re.sub(r'^\s*# .*\n', '', txt, count=1)
        # same title twice in the book ("Leave it"): the first file is the first chapter
        ids = byt.get(norm(title), [])
        k = seen.get(norm(title), 0); seen[norm(title)] = k + 1
        cid = ids[min(k, len(ids) - 1)] if ids else ''
        state = 'santi' if kind_of.get(cid) == 'santi' else next((w.lower() for w in ('REWRITTEN', 'EDITED', 'KEPT', 'NEW') if re.search(r'\b' + w + r'\b', status)), 'draft')
        what = re.sub(r'^.*?\[[A-Za-z\- ]+\]\.\s*', '', status, count=1)
        what = re.sub(r'^(KEPT|EDITED|REWRITTEN|NEW)[.:]?\s*', '', what)
        blocks = [markdown.markdown(b.strip()) for b in re.split(r'\n\s*\n', txt) if b.strip()]
        words = len(re.findall(r"[\w'’-]+", re.sub(r'<[^>]+>', ' ', ' '.join(blocks))))
        chapters.append({'n': len(chapters) + 1, 'file': os.path.basename(f), 'title': title, 'id': cid, 'part': part_of.get(cid, 0),
                         'state': state, 'what': what, 'words': words, 'blocks': blocks})
    data = {'folder': '01 Manuscript/' + os.path.basename(folder), 'chapters': chapters}
    json.dump(data, open(out, 'w'), ensure_ascii=False)
    print('manuscript:', data['folder'], len(chapters), 'chapters,', sum(c['words'] for c in chapters), 'words,',
          'unmatched', [c['title'] for c in chapters if not c['id']])


if __name__ == '__main__':
    main()
