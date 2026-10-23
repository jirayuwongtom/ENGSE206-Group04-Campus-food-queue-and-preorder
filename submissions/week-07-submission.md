# Week 07 Submission — SRS Authoring Studio

## 1. Assignment Source

| Field | Value |
|---|---|
| Assignment ID | `W07-v1.0` |
| Course assignment URL | https://github.com/se-rmutl/engse206-lab/blob/main/weeks/week-07-srs-authoring/assignment-contract.md |
| Course version/commit read | main |
| Date checked | 2026-09-01 |
| Case ID / Case URL | Case 04  ระบบจัดการคิวร้านอาหารหรือร้านเครื่องดื่มในมหาวิทยาลัย |

## 2. Artefacts Submitted

ผลลัพธ์หลัก: **SRS Draft v1**

Expected paths: `docs/07-srs-v1.md`, `submissions/week-07-submission.md`

| Artefact | Repository path / URL | Owner | Status |
|---|---|---|---|
| Software Requirements Specification Draft v1 (CASE-04-SRS-W07-v1) | [docs/07-srs-v1.md](../docs/07-srs-v1.md) | ศักดิ์ณรงค์ นำนนท์, จิรายุ วงศ์ต่อม | Completed |
| W05 Requirement Backlog Snapshot | [docs/05-requirement-backlog.md](../docs/05-requirement-backlog.md) | ศักดิ์ณรงค์ นำนนท์, จิรายุ วงศ์ต่อม | Completed |
| W06 Behavioral Models Snapshot (US, UC, AC) | [docs/06-requirement-models.md](../docs/06-requirement-models.md) | ศักดิ์ณรงค์ นำนนท์, จิรายุ วงศ์ต่อม | Completed |
| Context, Use Case & Activity Diagrams | [diagrams/context/](../diagrams/context/) , [diagrams/use-case/](../diagrams/use-case/) , [diagrams/activity/](../diagrams/activity/) | ศักดิ์ณรงค์ นำนนท์, จิรายุ วงศ์ต่อม | Completed |


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
| นายศักดิ์ณรงค์ นำนนท์ | Requirements Lead — ร่างหมวด Introduction, Product Scope, Capabilities (CAP-01 ถึง CAP-06), Functional Requirements (FR-01 ถึง FR-06), Business Rules (BR-01) และ Non-Functional Requirements (NFR-01 ถึง NFR-03 | docs/07-srs-v1.md (Sections 1–5) |
| นายจิรายุ วงศ์ต่อม | Team Coordinator — จัดทำ Data Requirements (DR-01 ถึง DR-05), Lifecycle Rules (New → Cooking → Ready → Completed / Cancelled), Traceability Matrix, Verification Plan (VF-01 ถึง VF-05) และ Appendix A–B | docs/07-srs-v1.md (Sections 6–7, 9–12, Appendix A–B) |
| ศักดิ์ณรงค์ นำนนท์, จิรายุ วงศ์ต่อม | Design Lead — กำหนด External Interface Requirements (EXT-01 Web Push Notification, EXT-02 Stall Display Panel) และตรวจสอบความสอดคล้องกับโมเดลใน docs/06-requirement-models.md | docs/07-srs-v1.md (Section 2.5, Section 8) |

## 5. Tabletop / Review Summary

- สิ่งที่นำเสนอ: เอกสารข้อกำหนดความต้องการซอฟต์แวร์ (SRS Draft v1 รหัส CASE-04-SRS-W07-v1) ที่บูรณาการรายการความต้องการจาก docs/05-requirement-backlog.md และแบบจำลองพฤติกรรม (US-01..US-11, UC-01..UC-04, AC-01..AC-05) จาก docs/06-requirement-models.md เข้ากับข้อกำหนดข้อมูลเชิงแนวคิด (DR-01 Customer Order, DR-02 Queue Token, DR-03 Food Stall, DR-04 Menu Item, DR-05 Queue Density Report), กฎการเปลี่ยนสถานะออเดอร์ (Lifecycle Rules), ส่วนต่อประสานภายนอก (EXT-01, EXT-02), ตาราง Traceability และแผนการตรวจสอบ (VF-01 ถึง VF-05)
- Feedback ที่ได้รับ: 
    - BR-01 ระบุเพียงล็อกปุ่มยกเลิกเมื่อสถานะเป็น Cooking แต่ยังไม่ได้ระบุกฎตัดสินกรณีลูกค้ากดยกเลิกพร้อมกับที่พนักงานกดรับออเดอร์ (Race Condition / DEF-01)
    - FR-06 ระบุว่า "แสดงผลหรือส่งออกรายงานสถิติ" โดยยังไม่ได้จำกัดรูปแบบในเฟสแรก (DEF-02)
    - NFR-03 (กดเปลี่ยนสถานะใน 2 คลิก) ยังไม่ได้ระบุขอบเขตเมนูที่บังคับใช้ (DEF-03)
    - DR-05 (Average Wait Duration) ยังไม่ได้ชี้แจงความแตกต่างจาก FR-02 (การประมาณเวลารอล่วงหน้า) (DEF-04)
    - NFR-01 (Real-time Latency 3 วินาที) ยังไม่ได้ระบุสภาวะแวดล้อมการทดสอบ (DEF-05)
- สิ่งที่แก้ก่อนส่ง: ปรับปรุงเอกสารตามรายการ REV-01 ถึง REV-05 ใน Appendix B ได้แก่ (1) เพิ่ม Server-side Timestamp Rule ใน BR-01 หากสถานะใน DB เปลี่ยนเป็น Cooking ก่อนจะปฏิเสธคำขอยกเลิกทันที, (2) จำกัด Scope Phase 1 ของ FR-06 เป็น On-screen Dashboard ส่วนการ Export เป็นไฟล์จัดเป็น Extension, (3) ระบุขอบเขต NFR-03 เฉพาะ Primary Workflow หน้าเตา, (4) ชี้แจงนิยาม DR-05 ว่าเป็นข้อมูลสถิติเวลารอย้อนหลังตามจริง และ (5) กำหนดเงื่อนไขทดสอบ NFR-01 ภายใต้สภาวะโหลดจำลอง 50 Users

## 6. Final Submission Snapshot

| Field | Value |
|---|---|
| Commit message | `submit(w07): SRS draft v1` |
| Commit hash | - |
| Submitted at | 2026-09-01 23:30 |
| Known limitations / open questions | บันทึกเป็น Deferred / TBD ใน Section 10 และ Appendix A จำนวน 4 รายการ: ISS-01 สูตรประเมินเวลารอคิวคลาดเคลื่อนไม่เกิน 5 นาที (FR-02), ISS-02 การทดสอบความเร็วแจ้งเตือนภายใน 3 วินาทีภายใต้โหลด 50 Users (FR-05, NFR-01), ISS-03 การสรุป Privacy Policy และเกณฑ์ Data Retention (NFR-02) และ ISS-04 รูปแบบการ Export รายงานสถิติเพิ่มเติมของผู้ดูแลพื้นที่ (FR-06) |

## 7. Revision after Feedback

| Date | Feedback | Change made | New commit |
|---|---|---|---|
| 2026-09-01 | แก้ไขจุดกำกวมจากการตรวจทาน DEF-01 ถึง DEF-05 ใน BR-01, FR-06, NFR-03, DR-05 และ NFR-01 | ปรับปรุงเนื้อหาตามรายการ REV-01 ถึง REV-05 ใน Section 3.2, 4, 5, 6 และบันทึกตารางเปรียบเทียบ Before/After ใน Appendix B ของ docs/07-srs-v1.md | docs/07-srs-v1.md |
