#!/usr/bin/env python3
"""claude.ai の成果物リンクを、サイト内リンクに置き換える（対応がないものはリンクを外す）。"""
import re, sys, pathlib
VOL = {'GEdR58deFr48CxfHm4HbE3':1,'6V9DJBWWLhWJmEM3HUzy7T':2,'CKfgtFWR7FTdzX3qn52Yxp':3,'JjQBWKTrbVRjDSpxv3yqZL':4,
'TAXae8p9fU7UGFdQVeVP2T':5,'1S7pseR1doVtRzC9K95aEL':6,'UyAxFL7ipRoSuGNJpFfY23':7,'MyHgK8D54WwVmDVYVNZKyh':8,
'4Q3hk2XNQN1FthN6fKWic4':9,'CQxbmrwh5NwYAxcauL5rhn':10,'9C118h4BjY24mcW975GNHG':11,'RD3zZEj6qjnoUHESSXoGdL':12,
'LZB8QWR15wdK14TbecS6fS':13,'XZQCP2rhGpoz1VAcpcoxp9':14,'M13Ken7mCQVVbDXsSr3BAP':15,
'9AK8rfTevX9ziqc158vbxT':'/overview/'}
def fix(text):
    def r(m):
        label, aid = m.group(1), m.group(2)
        v = VOL.get(aid)
        if v is None: return label
        href = v if isinstance(v,str) else f'/guidebook/vol{v:02d}/'
        return f'[{label}]({href})'
    return re.sub(r'\[([^\]]+)\]\(https://claude\.ai/artifact/([A-Za-z0-9]+)[^)]*\)', r, text)
for f in sys.argv[1:]:
    p = pathlib.Path(f); s = p.read_text(encoding='utf-8'); t = fix(s)
    if s != t: p.write_text(t, encoding='utf-8'); print('fixed', f)
