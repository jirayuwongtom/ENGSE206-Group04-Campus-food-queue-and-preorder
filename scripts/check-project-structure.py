#!/usr/bin/env python3
"""ENGSE206 team repo self-check (template v2).

  python3 scripts/check-project-structure.py            # every week + integrity scan
  python3 scripts/check-project-structure.py --week 4   # one week (1-8, 10, 11 or 5b)

Checks the paths named in each week's assignment contract, then scans for things the
instructor will flag: merge-conflict markers, AI citation traces "[cite: N]" without an
AI-use-log entry, template placeholders left in, and student ids in file names.
"""
from pathlib import Path
import argparse, hashlib, json, re, sys

root = Path(__file__).resolve().parents[1]
_tb = Path(__file__).with_name("template-blobs.json")
TEMPLATE = json.loads(_tb.read_text(encoding="utf-8")) if _tb.exists() else {}


def blob(p):
    d = p.read_bytes()
    return hashlib.sha1(b"blob %d\0" % len(d) + d).hexdigest()


def untouched(p):
    """True when the file is still an unedited copy of a template version."""
    return blob(p) in TEMPLATE.get(p.relative_to(root).as_posix(), [])
WEEKS = {
    "1": ["docs/01-problem-brief-v0.1.md", "evidence/week-01/", "submissions/week-01-submission.md"],
    "2": ["docs/02-stakeholder-context-scope.md", "diagrams/context/", "feedback/week-02-peer-feedback.md", "submissions/week-02-submission.md"],
    "3": ["docs/03-elicitation-plan.md", "docs/03-interview-guide.md", "evidence/week-03/", "feedback/week-03-peer-feedback.md", "submissions/week-03-submission.md"],
    "4": ["evidence/week-04/ai-conversation-excerpt.md", "docs/04-evidence-log.md", "docs/04-requirement-candidates.md", "project-management/ai-use-log.md", "submissions/week-04-submission.md"],
    "5": ["docs/05-requirement-backlog.md", "evidence/week-05/", "submissions/week-05-submission.md"],
    "5b": ["submissions/baseline-review-submission.md", "evidence/week-05/baseline-review/", "docs/08-validation-traceability.md"],
    "6": ["docs/06-requirement-models.md", "diagrams/use-case/", "diagrams/activity/", "submissions/week-06-submission.md"],
    "7": ["docs/07-srs-v1.md", "submissions/week-07-submission.md"],
    "8": ["docs/08-validation-traceability.md", "docs/requirements-change-log.md", "final/midterm-snapshot/", "submissions/week-08-submission.md"],
    "10": ["design/10-design-strategy.md", "design/00-design-spine.md", "submissions/week-10-submission.md"],
    "11": ["design/11-conceptual-architecture-v0.1.docx", "diagrams/architecture/", "design/00-design-spine.md", "evidence/week-11/", "submissions/week-11-submission.md"],
}
FILLER = {".gitkeep", "README.md"}
SKIP = {".git", "node_modules"}


def real_files(folder):
    return [p for p in folder.rglob("*") if p.is_file() and p.name not in FILLER and not untouched(p)]


def check_week(wk):
    bad = []
    for rel in WEEKS[wk]:
        p = root / rel
        if rel.endswith("/"):
            if not p.is_dir() or not real_files(p):
                bad.append(f"{rel} — ยังไม่มีไฟล์งานในโฟลเดอร์")
        elif not p.exists():
            bad.append(f"{rel} — ไม่พบไฟล์")
        elif untouched(p):
            bad.append(f"{rel} — ยังเป็น template ยังไม่ได้กรอก")
        elif p.suffix == ".md" and re.search(r"\[(กรอก|ชื่อ|ID|ROLE|ชื่อระบบ)\]", p.read_text(encoding="utf-8", errors="ignore")):
            bad.append(f"{rel} — ยังมี placeholder เช่น [กรอก]")
    return bad


def scan():
    notes = []
    guide = {"TEMPLATE_CHANGELOG.md", "submissions/submission-register.md", "STUDENT_SUBMISSION_GUIDE.md"}
    for p in root.rglob("*"):
        if not p.is_file() or set(p.relative_to(root).parts) & SKIP:
            continue
        rel = p.relative_to(root).as_posix()
        if re.search(r"[0-9]{11}-[0-9]", p.name):
            notes.append(f"{rel} — ชื่อไฟล์มีรหัสนักศึกษา (repo สาธารณะ)")
        if p.suffix not in {".md", ".txt", ".csv", ".drawio"} or rel in guide or rel.startswith("scripts/"):
            continue
        s = p.read_text(encoding="utf-8", errors="ignore")
        if re.search(r"^(<<<<<<< |>>>>>>> )", s, re.M):
            notes.append(f"{rel} — มี merge conflict ค้าง")
        if re.search(r"\[cite: ?[0-9]+\]", s):
            notes.append(f"{rel} — มีร่องรอย [cite: N] จาก AI · ต้องมีรายการใน project-management/ai-use-log.md")
        if "Example commit message" in s or "แก้เป็นงานของฉัน" in s:
            notes.append(f"{rel} — ยังมีข้อความจากตัวอย่าง/template")
    return notes


ap = argparse.ArgumentParser()
ap.add_argument("--week", choices=list(WEEKS))
a = ap.parse_args()
weeks = [a.week] if a.week else list(WEEKS)
fail = False
for wk in weeks:
    bad = check_week(wk)
    print(("PASS " if not bad else "TODO ") + f"Week {wk}")
    for b in bad:
        print("   -", b)
    fail |= bool(bad)
notes = scan()
if notes:
    print("\nต้องแก้ก่อนส่ง:")
    for n in notes:
        print("   -", n)
sys.exit(1 if fail or notes else 0)
