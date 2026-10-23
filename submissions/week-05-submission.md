# Week 05 Submission — Requirement Analysis and Prioritization

## 1. Assignment Source

| Field | Value |
|---|---|
| Assignment ID | `W05-v1.0` |
| Course assignment URL | https://github.com/se-rmutl/engse206-lab/blob/main/weeks/week-05-requirement-analysis-prioritization/assignment-contract.md |
| Course version/commit read | main |
| Date checked | 2026-08-11 |
| Case ID / Case URL | Case 04 ระบบจัดการคิวร้านอาหารหรือร้านเครื่องดื่มในมหาวิทยาลัย |

## 2. Artefacts Submitted

ผลลัพธ์หลัก: **Categorized and Prioritized Backlog**

Expected paths: `docs/05-requirement-backlog.md`, `evidence/week-05/`, `submissions/week-05-submission.md`

| Artefact | Repository path / URL | Owner | Status |
|---|---|---|---|
| Requirement Backlog v0.1 | [docs/05-requirement-backlog.md](../docs/05-requirement-backlog.md) | ศักดิ์ณรงค์ นำนนท์ | Completed |
| Prioritization Rationale | [docs/05-prioritization-rationale.md](../docs/05-prioritization-rationale.md) | จิรายุ วงศ์ต่อม | Completed |
| Open Questions and Issues | [docs/05-open-questions-and-issues.md](../docs/05-open-questions-and-issues.md) | ศักดิ์ณรงค์ นำนนท์ | Completed |
| Week 05 Artefact Health Check | [evidence/week-05/artefact-health-check.md](../evidence/week-05/artefact-health-check.md) | ศักดิ์ณรงค์ นำนนท์, จิรายุ วงศ์ต่อม | Completed |

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
| นายศักดิ์ณรงค์ นำนนท์ | Requirements Lead  จัดทำตาราง Requirement Backlog (FR-01 ถึง FR-06, BR-01, NFR-01 ถึง NFR-03) และปรับถ้อยคำให้วัดผลได้ | docs/05-requirement-backlog.md, evidence/week-05/artefact-health-check.md |
| นายจิรายุ วงศ์ต่อม | Team Coordinator  วิเคราะห์และบันทึกเหตุผลการจัดลำดับความสำคัญด้วย MoSCoW 4 มิติ (Value, Risk, Urgency, Dependency) Design / Evidence Lead | docs/05-prioritization-rationale.md, project-management/decision-log.md , docs/05-open-questions-and-issues.md |

## 5. Tabletop / Review Summary

- สิ่งที่นำเสนอ: รายการ Requirement Backlog ที่แปลงมาจาก Requirement Candidates ใน Week 04 พร้อมจัดหมวดหมู่ (Functional, Business Rule, Non-functional, Issue) และจัดลำดับความสำคัญแบบ MoSCoW (Must 6 ข้อ, Should 3 ข้อ, Could 1 ข้อ, Won't yet / Hold 2 ข้อ)
- Feedback ที่ได้รับ: คำอธิบายใน FR-04, FR-05, NFR-01 และ NFR-03 มีถ้อยคำกำกวม เช่น "ชัดเจน", "ทันที", "รวดเร็วที่สุด" ทำให้เขียน Test Script ตรวจรับยาก และควรแยกประเด็นที่ยังไม่มีนโยบายร้านค้ารองรับออกจาก Requirement ที่พร้อมทำโมเดล
- สิ่งที่แก้ก่อนส่ง: ปรับถ้อยคำเป็นเกณฑ์ที่วัดผลได้ (FR-04 เรียงตามลำดับเวลารับออเดอร์ FIFO, FR-05/NFR-01 แสดงผลภายใน 3 วินาที, NFR-03 เปลี่ยนสถานะภายในไม่เกิน 2 คลิก) และแยก ISSUE-01 (Payment Gateway) กับ ISSUE-02 (การแทรกคิวอัตโนมัติ) ออกเป็นสถานะ Hold ใน docs/05-open-questions-and-issues.md

## 6. Final Submission Snapshot

| Field | Value |
|---|---|
| Commit message | `submit(w05): prioritized requirement backlog` |
| Commit hash | 95160a31 |
| Submitted at | 2026-08-11 23:30 |
| Known limitations / open questions | OQ-01 สูตรคำนวณเวลารอคลาดเคลื่อนไม่เกิน 5 นาที (FR-02), OQ-02 ยืนยันจุดตัดเวลา Cut-off time กับเจ้าของร้าน (FR-03, BR-01), OQ-03 ขั้นตอนชดเชยเมื่อวัตถุดิบหมดกะทันหัน (FR-05) |

## 7. Revision after Feedback

| Date | Feedback | Change made | New commit |
|---|---|---|---|
| 2026-08-18 | ปรับแก้ถ้อยคำที่กำกวมใน Backlog ให้วัดผลและทดสอบได้จริง | แก้ไขถ้อยคำใน FR-04, FR-05, NFR-01, NFR-03 ตามบันทึก CR-05-01 และ DEC-05-01 | 95160a31 |
