"""Public documentation checks; Python standard library only."""
from pathlib import Path
import argparse,hashlib,json,re,posixpath
from urllib.parse import urlsplit,unquote
ROOT=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('--refresh',action='store_true');args=p.parse_args()
r=json.loads((ROOT/'registry.json').read_text())
files={x.relative_to(ROOT).as_posix():hashlib.sha256(x.read_bytes()).hexdigest() for x in ROOT.rglob('*') if x.is_file() and x.name not in ('registry.json','publication.md','Imperial_School_Arcade.pdf') and '__pycache__' not in x.parts and not {'.git','.github'}.intersection(x.relative_to(ROOT).parts)}
if args.refresh:
 r['files']=files
 for page in r['pages']:page['translation_source_sha256']=files[page['paths']['ru']]
 (ROOT/'registry.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
else:
 if r['files']!=files:raise SystemExit('File registry/digest mismatch. Review changes before --refresh.')
 for page in r['pages']:
  if page['translation_source_sha256']!=files[page['paths']['ru']]:raise SystemExit('Translation review required: '+page['id'])
groups=r.get('reading_groups')
if groups:
 ids=[page['id'] for page in r['pages']]
 members=[ident for group in groups for ident in group['pages']]
 if len(members)!=len(set(members)) or set(members)!=set(ids):raise SystemExit('Each chapter must belong to exactly one reading group.')
 by_id={page['id']:page for page in r['pages']}
 for lang,filename,start,end in [('ru','README.md','## Оглавление','## Репозитории'),('en','README.en.md','## Contents','## Application')]:
  content=(ROOT/filename).read_text().split(start,1)[1].split(end,1)[0]
  found=re.findall(r'\]\((docs/[^)\s]+)\)',content)
  expected=[by_id[ident]['paths'][lang] for ident in members]
  if found!=expected:raise SystemExit('README reading order differs from registry: '+filename)
for name in files:
 if not name.endswith('.md'):continue
 text=(ROOT/name).read_text()
 for target in re.findall(r'!?\[[^]\n]*\]\(([^)\s]+)\)',text):
  u=urlsplit(target)
  if u.scheme or not u.path:continue
  resolved=posixpath.normpath(posixpath.join(posixpath.dirname(name),unquote(u.path)))
  if resolved not in files:raise SystemExit('Broken local link: '+name+' -> '+target)
 if re.search(r'/var/|/opt/|BEGIN .*PRIVATE KEY|api[_-]?key\s*:',text,re.I):raise SystemExit('Private administration content: '+name)
print('OK:',len(r['pages']),'bilingual documents;',len(files),'registered files')
