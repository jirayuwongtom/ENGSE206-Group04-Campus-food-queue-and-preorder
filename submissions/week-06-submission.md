# Week 06 Submission — Requirement Models and Acceptance Criteria

## 1. Assignment Source

| Field | Value |
|---|---|
| Assignment ID | `W06-v1.0` |
| Course assignment URL | https://github.com/se-rmutl/engse206-lab/blob/main/weeks/week-06-requirement-modeling-negotiation/assignment-contract.md |
| Course version/commit read | main |
| Date checked | 2026-08-25 |
| Case ID / Case URL | Case 04  ระบบจัดการคิวร้านอาหารหรือร้านเครื่องดื่มในมหาวิทยาลัย |

## 2. Artefacts Submitted

ผลลัพธ์หลัก: **User Stories + Use Cases + Acceptance Criteria**

Expected paths: `docs/06-requirement-models.md`, `diagrams/use-case/`, `diagrams/activity/`, `submissions/week-06-submission.md`

| Artefact | Repository path / URL | Owner | Status |
|---|---|---|---|
| Requirement Models (US, UC, AC) | [docs/06-requirement-models.md](../docs/06-requirement-models.md) | ศักดิ์ณรงค์ นำนนท์, จิรายุ วงศ์ต่อม | Completed |
| Use Case Diagram | [diagrams/use-case/06-requirement-models.drawio.png](../diagrams/use-case/06-requirement-models.drawio.png) | ศักดิ์ณรงค์ นำนนท์, จิรายุ วงศ์ต่อม | Completed |
| Activity Diagram | [diagrams/activity/06ActivityDiagram.drawio.png](../diagrams/activity/06ActivityDiagram.drawio.png) | ศักดิ์ณรงค์ นำนนท์, จิรายุ วงศ์ต่อม | Completed |

## 3. Evidence and Quality Check

- [x] มี source file ที่แก้ไขได้
- [x] diagram มี `.drawio` และ export `.png`/`.pdf` เมื่อเกี่ยวข้อง
- [x] evidence อ้างอิงกลับไปยัง artefact ได้
- [x] อัปเดต worklog และ AI use log แล้ว
- [x] peer/instructor feedback ถูกบันทึกแล้ว
- [x] ไม่มีข้อมูลส่วนบุคคล/secret

## 4. Team Contribution

| Member | Role / Work completed | Evidence (commit/file) |
|---|---|---|
| นายศักดิ์ณรงค์ นำนนท์ | Requirements Lead — เขียน User Stories (US-01 ถึง US-10) และ Acceptance Criteria รูปแบบ Given-When-Then (AC-01 ถึง AC-05) | docs/06-requirement-models.md |
| นายจิรายุ วงศ์ต่อม | Team Coordinator — จัดทำ Use Case Specifications (UC-01 ถึง UC-04) พร้อมระบุ Main Success Scenario, Alternate/Exception Flows และบันทึก Negotiation/Trade-off Notes | docs/06-requirement-models.md |
| ศักดิ์ณรงค์ นำนนท์, จิรายุ วงศ์ต่อม | Design Lead — ออกแบบและวาด Use Case Diagram และ Activity Diagram แสดงลำดับการทำงานและจุดตัดเวลาการยกเลิกออเดอร์ (Cut-off time) | diagrams/use-case/06-requirement-models.drawio.png, diagrams/activity/06ActivityDiagram.drawio.png |

## 5. Tabletop / Review Summary

- สิ่งที่นำเสนอ: แบบจำลองความต้องการประกอบด้วย User Stories 10 ข้อ (US-01 ถึง US-10), Use Cases 4 รายการ (UC-01 ตรวจสอบสถานะอาหารและคิว, UC-02 จัดลำดับคิวและปรุงอาหารแบบ FIFO, UC-03 ตรวจสอบสถิติความหนาแน่นคิว, UC-04 ยกเลิกคำสั่งซื้อภายใต้กฎ Cut-off time) และเกณฑ์ตรวจรับ Given-When-Then (AC-01 ถึง AC-05)
- Feedback ที่ได้รับ: ใน UC-04 (การยกเลิกคำสั่งซื้อ) ต้องระบุ Exception Flow ให้ชัดเจนว่าหากพนักงานกดเปลี่ยนสถานะเป็น "กำลังทำ" ก่อนหรือพร้อมกับที่ลูกค้ากดยกเลิก ระบบจะจัดการอย่างไร และควรแยก Requirement ที่ยังอยู่ในสถานะ Needs Follow-up ไม่ให้นำมาเขียนโมเดลเกินหลักฐาน
- สิ่งที่แก้ก่อนส่ง: เพิ่ม Alternate/Exception Flow ใน UC-04 และ AC-05 ให้ปฏิเสธคำขอยกเลิกและล็อก/ซ่อนปุ่มทันทีเมื่อสถานะเปลี่ยนเป็น "กำลังทำ" (BR-01) พร้อมบันทึกเหตุผลที่ชะลอ FR-02, FR-05, NFR-01, NFR-02 ไว้ในหัวข้อที่ 6 (Negotiation / Trade-off Notes)

## 6. Final Submission Snapshot

| Field | Value |
|---|---|
| Commit message | `submit(w06): requirement models and acceptance criteria` |
| Commit hash | - |
| Submitted at | 2026-08-25 23:00 |
| Known limitations / open questions | FR-02 (ประมาณเวลารอ) และ FR-05 (การแจ้งเมนูหมดและแนวทางชดเชย) ยังอยู่ในสถานะ Needs Follow-up จึงยังไม่สร้าง Use Case ในรอบนี้เพื่อไม่ให้เกินหลักฐานที่มี |

## 7. Revision after Feedback

| Date | Feedback | Change made | New commit |
|---|---|---|---|
| 2026-08-25 | ระบุ Exception Flow ของการยกเลิกออเดอร์ (UC-04) และชี้แจงรายการที่ยังไม่นำมาทำโมเดล | เพิ่มรายละเอียด Alternate/Exception Flow ใน UC-04 และสรุปรายการ Needs Follow-up / Hold ในหัวข้อที่ 6 ของ docs/06-requirement-models.md | docs/06-requirement-models.md |
