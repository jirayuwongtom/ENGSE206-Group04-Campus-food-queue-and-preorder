# Week 08 Submission — SRS Validation, Traceability and Change

## 1. Assignment Source

| Field | Value |
|---|---|
| Assignment ID | `W08-v1.0` |
| Course assignment URL | https://github.com/se-rmutl/engse206-lab/blob/main/weeks/week-08-srs-validation-traceability/assignment-contract.md |
| Course version/commit read | main |
| Date checked | 2026-09-08 |
| Case ID / Case URL | Case 04 ระบบจัดการคิวร้านอาหารหรือร้านเครื่องดื่มในมหาวิทยาลัย |

## 2. Artefacts Submitted

ผลลัพธ์หลัก: **Reviewed SRS + Traceability + Baseline**

Expected paths: `docs/08-validation-traceability.md`, `docs/requirements-change-log.md`, `final/midterm-snapshot/`, `submissions/week-08-submission.md`

| Artefact | Repository path / URL | Owner | Status |
|---|---|---|---|
| Validation, Traceability and Change Management | [docs/08-validation-traceability.md](../docs/08-validation-traceability.md) | จิรายุ วงศ์ต่อม, ศักดิ์ณรงค์ นำนนท์ | Completed |
| Requirements Change Log | [docs/requirements-change-log.md](../docs/requirements-change-log.md) | จิรายุ วงศ์ต่อม, ศักดิ์ณรงค์ นำนนท์ | Completed |
| Reviewed SRS Draft v1 (Baseline Candidate) | [docs/07-srs-v1.md](../docs/07-srs-v1.md) | จิรายุ วงศ์ต่อม, ศักดิ์ณรงค์ นำนนท์ | Completed |
| Midterm Requirement Baseline Snapshot | [final/midterm-snapshot/](../final/midterm-snapshot/) | จิรายุ วงศ์ต่อม, ศักดิ์ณรงค์ นำนนท์ | Completed |

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
| นายศักดิ์ณรงค์ นำนนท์ | Requirements Lead — ตรวจสอบคุณภาพข้อกำหนดตาม Requirements Quality Checklist, ทบทวนและแก้ไขจุดกำกวมใน SRS (DEF-01 ถึง DEF-05 / REV-01 ถึง REV-05) และสรุปสถานะ Requirement Disposition | docs/08-validation-traceability.md, docs/07-srs-v1.md  |
| นายจิรายุ วงศ์ต่อม | Team Coordinator — จัดทำและเชื่อมโยง Traceability Matrix (Evidence → Requirement → US/UC/AC → Verification VF-01 ถึง VF-05), บันทึกประวัติการเปลี่ยนแปลง (CR-05-01, CR-05-02, CR-RETRO-01 ถึง CR-RETRO-03) | docs/08-validation-traceability.md, docs/requirements-change-log.md, docs/07-srs-v1.md  |


## 5. Tabletop / Review Summary

- สิ่งที่นำเสนอ: ผลการตรวจสอบความถูกต้องของเอกสาร SRS Draft v1 (CASE-04-SRS-W07-v1), ตาราง Traceability Matrix เชื่อมโยงตั้งแต่หลักฐาน (E-01 ถึง E-08, RC-01 ถึง RC-05) ไปยังข้อกำหนด (FR-01 ถึง FR-06, BR-01, NFR-01 ถึง NFR-03), แบบจำลองพฤติกรรม (US-01 ถึง US-11, UC-01 ถึง UC-04, AC-01 ถึง AC-05) และแผนการตรวจสอบ (VF-01 ถึง VF-05) รวมถึงบันทึกการเปลี่ยนแปลงใน docs/requirements-change-log.md
- Feedback ที่ได้รับ:
    - กฎ BR-01 ต้องระบุวิธีตัดสินกรณีลูกค้ากดยกเลิกพร้อมกับที่พนักงานกดเริ่มทำอาหาร (Race Condition / DEF-01)
    - ขอบเขต FR-06 ในเฟสแรกต้องระบุให้ชัดว่าเป็น On-screen Dashboard หรือรวมการ Export ไฟล์ (DEF-02)
    - เงื่อนไข NFR-03 (กดเปลี่ยนสถานะไม่เกิน 2 คลิก) ต้องระบุขอบเขตหน้าจอที่บังคับใช้ให้ชัดเจน (DEF-03)
    - ข้อมูล DR-05 (Average Wait Duration) ต้องแยกความหมายออกจาก FR-02 (การประเมินเวลารอล่วงหน้า) (DEF-04)
    - เกณฑ์ทดสอบ NFR-01 (Real-time Latency 3 วินาที) ต้องระบุสภาวะโหลดที่ใช้ทดสอบ และควรซิงค์รหัส Requirement ระหว่าง docs/05-requirement-backlog.md กับ docs/08-validation-traceability.md ให้ตรงกัน (DEF-05, CR-RETRO-01 ถึง CR-RETRO-03)
- สิ่งที่แก้ก่อนส่ง:  ปรับปรุงเอกสาร SRS ตามรายการ REV-01 ถึง REV-05 (เพิ่มกฎ Server-side Timestamp ใน BR-01, จำกัด Scope Phase 1 ของ FR-06 เป็น On-screen Dashboard, ระบุขอบเขต NFR-03 เฉพาะ Primary Workflow หน้าเตา, ชี้แจงนิยาม DR-05 และกำหนดเงื่อนไข Load Test 50 Users สำหรับ NFR-01) พร้อมบันทึกการเปลี่ยนแปลงรหัสและสถานะย้อนหลัง (CR-RETRO-01 ถึง CR-RETRO-03) ลงใน docs/requirements-change-log.md

## 6. Final Submission Snapshot

| Field | Value |
|---|---|
| Commit message | `submit(w08): SRS validation and traceability` |
| Commit hash | [กรอกหลัง push] |
| Submitted at | 2026-09-17 23:30 |
| Known limitations / open questions | ประเด็นที่ต้องติดตามต่อก่อนเข้าสู่เฟสการออกแบบ <br>1. ISS-01 ยืนยันสูตรคำนวณเวลารอคิวที่คลาดเคลื่อนไม่เกิน 5 นาที (FR-02) <br>2. ISS-02 ทดสอบความเร็วการแจ้งเตือนภายใน 3 วินาทีภายใต้โหลด 50 Users (FR-05, NFR-01) <br>3. ISS-03 สรุป Privacy Policy และเกณฑ์ Data Retention เรื่องการไม่เก็บข้อมูลแพ้อาหาร (NFR-02), <br>4. ISS-04 ยืนยันรูปแบบรายงานสถิติเพิ่มเติมของผู้ดูแลพื้นที่ (FR-06) และ <br>5. ปรับซิงค์รหัสและสถานะตามรายการ CR-RETRO-01 ถึง CR-RETRO-03 ใน docs/requirements-change-log.md |

## 7. Revision after Feedback

| Date | Feedback | Change made | New commit |
|---|---|---|---|
| | | | |
