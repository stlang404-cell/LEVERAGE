"""Read-only final R0 integrity, scope, counts and documentation checks."""
from pathlib import Path
from collections import Counter
import hashlib,json,subprocess,sys
from .rules import Config,State,key,terminal,legal
from .report import load

def main():
    subprocess.run([sys.executable,'research/experiments/check_docs.py'],check=True)
    base=Path('research/results/r0');manifest=json.loads((base/'manifest.json').read_text())
    for name,digest in manifest['sha256'].items():assert hashlib.sha256(Path(name).read_bytes()).hexdigest()==digest,name
    for name in ('LEVERAGE_README.md','LEVERAGE_R0_FINAL_RESEARCH_REPORT.md','LEVERAGE_CLAUDE_MASTER_PROMPT.md'):
        assert 'RESEARCH STOP' in (Path('docs')/name).read_text(),name
    assert len(load('*_main*.json'))==672
    summary=json.loads((base/'summary.json').read_text());audit=json.loads((base/'audit.json').read_text())
    assert summary['recorded_executions']==audit['recorded_executions']==920
    assert summary['distinct_trial_identities']==audit['distinct_trial_identities']==904
    assert audit['independent_transitions_checked']==42765 and audit['exact_representative_replays']==3
    case=json.loads((base/'repetition_case.json').read_text());c=Config(**case['config']);s=State(tuple(case['board']),case['turn'],tuple(case['reserves']),case['ply']);h=Counter({(tuple(x['board']),x['turn'],tuple(x['reserves'])):x['count'] for x in case['history']})
    assert h[key(s)]==2 and terminal(s,c,h)[0] is None and 120-s.ply==case['remaining_plies']
    assert [list(m) for m in legal(s,c)]==case['legal_actions']
    print('PASS: final R0 manifest, stop directives, 672 main / 920 recorded executions, independent audit and nonterminal repetition case.')
if __name__=='__main__':main()
