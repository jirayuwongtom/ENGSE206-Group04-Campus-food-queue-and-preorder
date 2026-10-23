# Midterm Snapshot Manifest — Campus Food Queue and Preorder (Group 04)

> ไฟล์นี้ใช้เป็นสารบัญเอกสารช่วง Week 05–08 ของโครงงานระบบจัดการคิวร้านอาหารหรือร้านเครื่องดื่มในมหาวิทยาลัย (Case 04) ไฟล์งานยังอยู่ที่ตำแหน่งเดิมใน repository ตามลิงก์ด้านล่าง ไม่ได้คัดลอกมาซ้ำในโฟลเดอร์นี้

## เอกสารความต้องการ

| ไฟล์ | เนื้อหาและสถานะ |
|---|---|
| [`docs/05-requirement-backlog.md`](../../docs/05-requirement-backlog.md) | Backlog v0.1 เริ่มจาก FR, BR, NFR และรายการที่พักไว้ 2 เรื่อง (`ISSUE-01` การชำระเงินออนไลน์ และ `ISSUE-02` การแทรกคิวอัตโนมัติ) โดย `baseline-v1.0` เก็บฉบับ Week 05 ไว้ให้ตรวจย้อนหลังได้ |
| [`docs/06-requirement-models.md`](../../docs/06-requirement-models.md) | User Stories, Use Cases และ Acceptance Criteria สำหรับการดูคิว การจัดคิวแบบ FIFO การดูสถิติคิว และการยกเลิกออเดอร์ตาม Cut-off time |
| [`docs/07-srs-v1.md`](../../docs/07-srs-v1.md) | SRS Draft v1, เอกสาร `CASE-04-SRS-W07-v1`, เวอร์ชัน `0.1-draft`; ยังระบุสถานะ Draft / Baseline Candidate และมีประเด็นที่ต้องหาข้อมูลเพิ่ม |
| [`docs/08-validation-traceability.md`](../../docs/08-validation-traceability.md) | บันทึกผล Baseline Review, ช่องว่าง traceability, สมมติฐาน `NFR-CFQP-01` / `OQ-01` และ Change Request `CR-05-01`, `CR-05-02` ที่ระบุว่า Accepted |
| [`docs/requirements-change-log.md`](../../docs/requirements-change-log.md) | ประวัติการเปลี่ยน requirement ปัจจุบันมีรายการ `CR-05` และรายการย้อนหลัง `CR-RETRO` ที่เพิ่มในเดือนกันยายน จึงไม่ใช่สำเนาของสถานะ ณ Week 08 เพียงอย่างเดียว |

## แผนภาพที่มีอยู่

| ไฟล์ | ใช้ประกอบ |
|---|---|
| [`diagrams/use-case/06-requirement-models.drawio.png`](../../diagrams/use-case/06-requirement-models.drawio.png) | Use Case Diagram ของแบบจำลองความต้องการ Week 06 |
| [`diagrams/activity/06ActivityDiagram.drawio.png`](../../diagrams/activity/06ActivityDiagram.drawio.png) | Activity Diagram ของขั้นตอนทำงานและการจัดการคิว |
| [ไฟล์ SystemContextDiagram.drawio](../../diagrams/architecture/System%20Context%20%28C4%20level%201%29.drawio) · [ไฟล์ SystemContextDiagram.png](../../diagrams/architecture/System%20Context%20%28C4%20level%201%29.png) | แผนภาพบริบทของระบบที่ใช้อ้างอิงในเอกสาร SRS |

## ประเด็นที่ยังต้องติดตาม

- `OQ-01`: ยังต้องหา Evidence เพิ่มเพื่อรองรับเป้าหมายการอัปเดตสถานะภายใน 3 วินาที (`NFR-CFQP-01`) ตามบันทึก Baseline Review
- `ISS-01`: ยืนยันวิธีประเมินเวลารอให้คลาดเคลื่อนไม่เกิน 5 นาที (`FR-02`)
- `ISS-02`: ตรวจสอบการแจ้งเมนูหมดแบบ real-time และผลทดสอบภายใต้โหลด (`FR-05`, `NFR-01`)
- `ISS-03`: กำหนดแนวทางความเป็นส่วนตัวและระยะเวลาเก็บข้อมูล (`NFR-02`)
- `ISS-04`: ยืนยันรูปแบบรายงานสถิติคิวที่ผู้ดูแลพื้นที่ต้องการ (`FR-06`)
- รายการ `ISSUE-01` และ `ISSUE-02` ใน Backlog ยังคงพักไว้ตามเหตุผลและสถานะที่บันทึกในเอกสาร Week 05

## ใบส่งงานที่เกี่ยวข้อง

- [`submissions/week-05-submission.md`](../../submissions/week-05-submission.md)
- [`submissions/baseline-review-submission.md`](../../submissions/baseline-review-submission.md)
- [`submissions/week-06-submission.md`](../../submissions/week-06-submission.md)
- [`submissions/week-07-submission.md`](../../submissions/week-07-submission.md)
- [`submissions/week-08-submission.md`](../../submissions/week-08-submission.md)

หมายเหตุ: ใน `week-08-submission.md` ยังมีช่อง `[กรอก]` และ `[YYYY-MM-DD]` ที่ควรตรวจและเติมก่อนนำเอกสารไปส่ง
