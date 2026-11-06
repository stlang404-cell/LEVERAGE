"""Local link, frozen-evidence, manifest, size and accidental-secret checks."""
from pathlib import Path
import re,json,hashlib
root=Path.cwd()
required=('README','VISION','BOARD_GAME_RESEARCH','CORPORATE_WORLD','FINANCE_AND_RESEARCH','UI_ART_DIRECTION','FEATURE_AUDIT','IMPLEMENTATION_ROADMAP','CLAUDE_MASTER_PROMPT','OPEN_QUESTIONS')
for name in required:assert (root/'docs'/f'LEVERAGE_{name}.md').is_file(),name
paths=[root/'README.md',*sorted((root/'docs').rglob('*.md')),*sorted((root/'research').rglob('*.md'))]
links=0
for path in paths:
 for dest in re.findall(r'\]\(([^)]+)\)',path.read_text()):
  if '://' in dest or dest.startswith('#'):continue
  dest=dest.split('#')[0]
  assert (path.parent/dest).is_file(),(path.relative_to(root),dest)
  links+=1
for filename,field in [('research/results/manifest.json','files_sha256'),('research/results/continuation_manifest.json','sha256')]:
 manifest=json.loads((root/filename).read_text())
 for name,digest in manifest[field].items():assert hashlib.sha256((root/name).read_bytes()).hexdigest()==digest,name
patterns=[re.compile(rb'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----'),re.compile(rb'gh[pousr]_[A-Za-z0-9]{30,}'),re.compile(rb'AKIA[0-9A-Z]{16}')]
files=[root/'README.md',*filter(lambda p:p.is_file() and '__pycache__' not in p.parts,(root/'docs').rglob('*')),*filter(lambda p:p.is_file() and '__pycache__' not in p.parts,(root/'research').rglob('*'))]
for path in files:
 assert path.stat().st_size<2*1024*1024,('oversized',path.relative_to(root))
 assert path.suffix not in ('.pyc','.env'),('accidental artifact',path.relative_to(root))
 data=path.read_bytes()
 assert not any(p.search(data) for p in patterns),('possible secret',path.relative_to(root))
print(f'PASS: {len(paths)} Markdown files, {links} local links, both manifests, {len(files)} intended files <2 MiB each, bounded secret-pattern scan. Not a comprehensive credential detector.')
