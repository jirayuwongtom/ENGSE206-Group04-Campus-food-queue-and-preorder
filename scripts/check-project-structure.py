#!/usr/bin/env python3
"""Basic local check for ENGSE206 group repository structure.
Run: python3 scripts/check-project-structure.py
"""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
required = [
    'README.md', 'TEAM.md', 'CASE_CARD.md',
    'docs/00-project-profile.md', 'docs/01-problem-brief-v0.1.md',
    'docs/05-requirement-backlog.md', 'docs/07-srs-v1.md',
    'docs/08-validation-traceability.md', 'design/10-design-strategy.md',
    'design/11-conceptual-architecture.md', 'design/12-ux-ui-prototype.md',
    'design/13-detailed-design.md', 'design/14-design-review.md',
    'project-management/team-worklog.md', 'final/README.md'
]
missing = [p for p in required if not (root / p).exists()]
if missing:
    print('Missing required files:')
    for p in missing:
        print(' -', p)
    raise SystemExit(1)
print('PASS: required ENGSE206 project files are present.')
