import json,sys,base64,os,re
def find(o):
    if isinstance(o,dict):
        if 'bytes_b64' in o: return o
        for v in o.values():
            r=find(v)
            if r: return r
    if isinstance(o,list):
        for v in o:
            r=find(v)
            if r: return r
    if isinstance(o,str) and o.lstrip().startswith('{'):
        try: return find(json.loads(o))
        except Exception: pass
src,out=sys.argv[1],sys.argv[2]
t=open(src).read()
d=find(json.loads(t))
open(out,'wb').write(base64.b64decode(d['bytes_b64']))
print(out,d['name'],d.get('notes'))
