# Course Alignment — การเชื่อมโยง Student Repository กับ ENGSE206 Course Repository

Repository นี้ถูกออกแบบให้สอดคล้องโดยตรงกับโฟลเดอร์ `templates/`, `weeks/` และ `docs/artefact-roadmap.md` ของ **ENGSE206 Course Repository**

## หลักการใช้งาน

- ENGSE206 Course Repository = แหล่งบทเรียน Workshop, Case Card, rubric และคำสั่งงาน
- Repository ของกลุ่ม = พื้นที่สร้าง ช่วยกันปรับปรุง และเก็บหลักฐานของ **ชิ้นงานเฉพาะกลุ่ม**
- ไฟล์ชื่อหลักใน student repo ตั้งใจให้ตรงกับชื่อ template ใน course repo เพื่อให้ผู้สอนตรวจได้ง่าย

## Mapping ชิ้นงาน

| Week | Course Repository Activity | Student Repository Artefact | สถานะเป้าหมาย |
|---:|---|---|---|
| 1 | Problem Brief Kick-off | `docs/01-problem-brief-v0.1.md` + `project-management/team-worklog.md` | Draft |
| 2 | Stakeholder / Context / Scope | `docs/02-stakeholder-context-scope.md` + diagrams | Draft |
| 3 | Elicitation Plan & Interview Design | `docs/03-elicitation-plan.md` | Ready for execution |
| 4 | Simulation / Evidence / Negotiation | `docs/04-evidence-log.md` + `evidence/week-04/` | Evidence-based |
| 5 | Requirement Analysis & Prioritization | `docs/05-requirement-backlog.md` | Prioritized |
| 6 | User Story / Use Case / Acceptance Criteria | `docs/06-requirement-models.md` + `diagrams/` | Modelled |
| 7 | SRS Authoring Studio | `docs/07-srs-v1.md` | Baseline candidate |
| 8 | Validation / Traceability / Change | `docs/08-validation-traceability.md` | Reviewed |
| 9 | Midterm | `final/midterm-snapshot/` (หากผู้สอนกำหนด) | Frozen snapshot |
| 10 | Design Strategy | `design/10-design-strategy.md` | Draft |
| 11 | Conceptual Architecture | `design/11-conceptual-architecture.md` + architecture diagrams | Draft |
| 12 | UX/UI Prototype & Accessibility | `design/12-ux-ui-prototype.md` + prototype evidence | Draft |
| 13 | Detailed Design Studio | `design/13-detailed-design.md` + detailed diagrams | Draft |
| 14 | Design Review Simulation | `design/14-design-review.md` + evidence | Reviewed |
| 15 | Usability / Peer Test / Iteration | `evidence/week-15/` + revised docs/design | Revised |
| 16 | Showcase / Pitch / Reflection | `final/` + `feedback/15-individual-reflection.md` | Final |
| 17 | Final Exam | ตามที่อาจารย์กำหนด | Completed |

## วิธีตรวจตัวเอง

ทุกสัปดาห์เปิดไฟล์ในโฟลเดอร์ `weekly/` ที่ตรงกับสัปดาห์นั้น แล้วทำ checklist ให้ครบก่อน commit และ push
