# Course Alignment — Team Repo กับ ENGSE206 Course Repository

> กฎหลัก: **อ่านโจทย์จาก [Course Repo](https://github.com/se-rmutl/engse206-lab) → ทำและส่งใน Team Repo นี้**

ทุกสัปดาห์ใช้ path ตาม `assignment-contract.md` ของสัปดาห์นั้น — ตารางนี้สรุปให้

| Week | งาน | ไฟล์ใน Team Repo | ข้อความ commit ตอนส่ง |
|---:|---|---|---|
| 1 | Problem Brief | `docs/01-problem-brief-v0.1.md` · `evidence/week-01/` · `submissions/week-01-submission.md` | `submit(w01): problem brief v0.1` |
| 2 | Stakeholder · Context · Scope | `docs/02-stakeholder-context-scope.md` · `diagrams/context/` · `feedback/week-02-peer-feedback.md` · `submissions/week-02-submission.md` | `submit(w02): stakeholder context and scope` |
| 3 | Elicitation · Interview · Rehearsal | `docs/03-elicitation-plan.md` · `docs/03-interview-guide.md` · `evidence/week-03/` · `feedback/week-03-peer-feedback.md` · `submissions/week-03-submission.md` | `submit(w03): elicitation plan interview guide and rehearsal` |
| 4 | Evidence · Requirement Candidates | `evidence/week-04/ai-conversation-excerpt.md` · `docs/04-evidence-log.md` · `docs/04-requirement-candidates.md` · `project-management/ai-use-log.md` · `submissions/week-04-submission.md` | `submit(w04): evidence and requirement candidates` |
| 5 | Backlog · Prioritization | `docs/05-requirement-backlog.md` · `evidence/week-05/` · `submissions/week-05-submission.md` | `submit(w05): prioritized requirement backlog` |
| 5b | Baseline Review | `docs/05-requirement-backlog.md` · `docs/08-…` ส่วน A · `evidence/week-05/baseline-review/` · `submissions/baseline-review-submission.md` + tag `baseline-v1.0` | `submit(w05): lock requirement baseline v1.0` |
| 6 | Models · Acceptance Criteria | `docs/06-requirement-models.md` · `diagrams/use-case/` · `diagrams/activity/` · `submissions/week-06-submission.md` | `submit(w06): requirement models and acceptance criteria` |
| 7 | SRS v1 | `docs/07-srs-v1.md` · `submissions/week-07-submission.md` | `submit(w07): SRS draft v1` |
| 8 | Validation · Traceability | `docs/08-…` ส่วน B · `docs/requirements-change-log.md` · `final/midterm-snapshot/` · `submissions/week-08-submission.md` | `submit(w08): SRS validation and traceability` |
| 9 | สอบกลางภาค (งานกลุ่ม) | `midterm/` บน branch ตามประกาศ + Pull Request | ตามประกาศ |
| 10 | Design Strategy | `design/10-design-strategy.md` · `design/00-design-spine.md` · `evidence/week-10/` · `submissions/week-10-submission.md` | `submit(w10): design strategy and rationale` |
| 11 | Conceptual Architecture | `design/11-conceptual-architecture-v0.1.docx` · `diagrams/architecture/` · `design/00-design-spine.md` · `evidence/week-11/` · `submissions/week-11-submission.md` | `submit(w11): conceptual architecture` |
| 15 | สอบปลายภาค ส่วน ก | `final-exam/` บน branch `final-exam` + Pull Request | `submit(final): change-to-design take-home` |

W12–W16 ของรายวิชาเต็มยังมีไฟล์อยู่ใน repo (`design/12–14`, `evidence/week-12…16`) แต่เทอมนี้ยังไม่ใช้

## วิธีตรวจตัวเอง

```bash
python3 scripts/check-project-structure.py --week 4    # ตรวจงานสัปดาห์ที่ 4
python3 scripts/check-project-structure.py             # ตรวจทุกสัปดาห์ + ร่องรอยที่ต้องแก้
```
