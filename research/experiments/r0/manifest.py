"""Snapshot final R0 sources, results and current design documents, excluding self-reference."""
from pathlib import Path
import hashlib,json,platform

def main():
    base=Path('research/results/r0');target=base/'manifest.json'
    paths=[*Path('research/experiments/r0').glob('*.py'),Path('research/experiments/r0/README.md'),Path('research/experiments/test_r0.py'),*base.glob('*'),Path('research/20_R0_FORMAL_CANDIDATES.md'),Path('research/21_R0_RESULTS.md'),Path('README.md'),*Path('docs').glob('*.md')]
    files=sorted({p for p in paths if p.is_file() and p!=target},key=str)
    data=dict(baseline_commit='ac7c71964f7331f1fc56282320891497385ce6c0',rule_versions={'A':'EA-0.3.0','B':'BW-0.3.0','C':'WR-0.3.0'},protocol='r0-1',python=platform.python_version(),platform=platform.platform(),resources={'cpu_quota':'400000 / 100000 microseconds','memory_limit_bytes':34359738368},main_seeds=[0,31],main_nodes=1200,diagnostic_deep_nodes=6000,commands='research/experiments/r0/README.md',sha256={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in files})
    target.write_text(json.dumps(data,indent=2)+'\n');print('R0 manifest saved:',len(files),'files')
if __name__=='__main__':main()
