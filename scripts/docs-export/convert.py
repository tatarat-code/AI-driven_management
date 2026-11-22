#!/usr/bin/env python3
"""Claude Docs の docx/markdown 書き出しを、サイトのコンテンツ(md)に変換する。
usage: convert.py <src.docx|src.md> <collection: overview|guidebook> <id: ch01|vol01|intro|appendix>
"""
import sys, re, os, subprocess, shutil, tempfile, pathlib
REPO = pathlib.Path(__file__).resolve().parents[2]
src, coll, cid = sys.argv[1], sys.argv[2], sys.argv[3]
mdfile = REPO/'src/content'/coll/f'{cid}.md'
old = mdfile.read_text(encoding='utf-8')
fm = re.match(r'^---\n(.*?)\n---\n', old, re.S).group(1)
tmp = pathlib.Path(tempfile.mkdtemp())
if src.endswith('.docx'):
    subprocess.run(['pandoc', src, '-t', 'gfm', '--wrap=none', f'--extract-media={tmp}', '-o', str(tmp/'out.md')], check=True)
    body = (tmp/'out.md').read_text(encoding='utf-8')
else:
    body = pathlib.Path(src).read_text(encoding='utf-8')

# 画像: public/images/<coll>/<id>-figN.<ext> へ移し、Markdown 画像記法に置き換える
imgdir = REPO/'public/images'/coll
imgdir.mkdir(parents=True, exist_ok=True)
if src.endswith('.docx'):
    for old_img in imgdir.glob(f'{cid}-fig*'):
        old_img.unlink()
n = 0
def repl(m):
    global n
    path, alt = m.group(1), m.group(2)
    p = pathlib.Path(path)
    if not p.is_absolute():
        p = tmp/path
    n += 1
    dest = imgdir/f'{cid}-fig{n}{p.suffix}'
    shutil.copy(p, dest)
    return f'![{alt}](/images/{coll}/{dest.name})'
body = re.sub(r'<img src="([^"]+)"[^>]*?alt="([^"]*)"[^>]*/>', repl, body)
body = re.sub(r'!\[([^\]]*)\]\(([^)\s]+)\)(\{[^}]*\})?', lambda m: m.group(0) if m.group(2).startswith('/images/') else repl(type('M',(object,),{'group':lambda s,i:{1:m.group(2),2:m.group(1)}[i]})()), body)

# 埋め込み図が書き出せなかった場合のプレースホルダー
# PDF から取り出した図（public/images/<coll>/<id>-figN.png）があれば差し込む
k = 0
def ph(m):
    global k
    k += 1
    cap = m.group(1).strip()
    img = imgdir/f'{cid}-fig{k}.png'
    if src.endswith('.md') and img.exists():
        return f'![{cap}](/images/{coll}/{img.name})\n\n*{cap}*'
    return f'*（図「{cap}」は準備中です）*'
body = re.sub(r'&#91;embedded content: ([^\]\\]*)\\?\]', ph, body)
body = re.sub(r'\[embedded content: ([^\]]*)\]', ph, body)
# 作成日・作成者の行（日付チップ・メンション）を外す
body = re.sub(r'^[A-Z][a-z]{2} \d{1,2}, \d{4}(?: · @[^\n]*)?\n', '', body, flags=re.M)

# 先頭の H1 を外す（ページ見出しはレイアウト側で出す）
lines = body.split('\n')
h1 = None
for i, l in enumerate(lines):
    if l.startswith('# '):
        h1 = l[2:].strip(); del lines[i]; break
body = '\n'.join(lines).strip() + '\n'

# リスト項目の間の空行を詰める（ゆるいリスト → きついリスト）
for _ in range(3):
    body = re.sub(r'(\n(?:- |\d+\.\s+)[^\n]*)\n\n(?=(?:- |\d+\.\s+))', r'\1\n', body)
body = re.sub(r'^(\d+\.)\s{2,}', r'\1 ', body, flags=re.M)

# 「この章の問い」「この巻の問い」を summary に
summary = None
m = re.search(r'\*\*この(?:章|巻)の問い\*\*[:：]\s*(.+)', body)
if m: summary = m.group(1).strip().replace('"', '\\"')
elif coll == 'guidebook':
    para = next((l for l in body.split('\n') if l and not l.startswith(('#','>','-','|','*','!','1.'))), '')
    first = para.split('。')[0] + '。' if para else ''
    if first.strip('。'): summary = first.replace('"', '\\"')

fm_lines = [l for l in fm.split('\n') if not l.startswith(('status:','summary:','heading:'))]
if h1:
    fm_lines.append('heading: "' + h1.replace('"','\\"') + '"')
if summary:
    fm_lines.append(f'summary: "{summary}"')
fm_lines.append('updated: 2026-11-22')
fm_lines = [l for l in fm_lines if not (l.startswith('updated:') and l != 'updated: 2026-11-22')] 
fm_lines = list(dict.fromkeys(fm_lines))
fm_lines.append('status: published')
mdfile.write_text('---\n' + '\n'.join(fm_lines) + '\n---\n\n' + body, encoding='utf-8')
print(f'{mdfile.relative_to(REPO)}: H1="{h1}" figs={n} bytes={len(body.encode())}')
