from pathlib import Path
p=next((Path(__file__).resolve().parents[1]/'.claude/agents').glob('*.md'))
s=p.read_text(encoding='utf8')
assert s.startswith('---\n') and 'tools: Read, Grep, Glob' in s
assert 'model: inherit' in s and 'permissionMode: default' in s
assert all(x not in s for x in ['bypassPermissions','tools: Bash','api_key:'])
print('Definición validada. La calidad de respuestas requiere evaluación en Claude Code.')
