# Decision Log

> ใช้สำหรับการตัดสินใจที่มีผลต่อ scope, requirement, architecture, UX/UI หรือ detailed design

| ID | Date | Decision | Options Considered | Rationale | Impacted Artefacts | Owner |
|---|---|---|---|---|---|---|
| D-01 | [date] | [กรอก] | A / B / C | [กรอก] | `docs/...`, `design/...` | [ชื่อ] |

## [DEC-05-01] การปรับแก้ถ้อยคำ Requirement และกำหนดเกณฑ์การวัดผล (Acceptance Measure)

* **Date:** Week 05 (Baseline Review Studio)
* **Status:** Approved
* **Deciders:** ศักดิ์ณรงค์, จิรายุ
* **Context:** ผลจากการทำ Peer Cross-Review พบว่า Requirement บางข้อใช้คำกำกวม เช่น "ทันที", "รวดเร็วที่สุด", "เรียงลำดับอย่างชัดเจน" ซึ่งไม่สามารถนำไปเขียน Test Script ได้จริง
* **Decision:**
  1. ปรับแก้เงื่อนไขเวลาของ `FR-CFQP-05` และ `NFR-CFQP-01` เป็น "ภายใน 3 วินาที"
  2. ระบุเงื่อนไขการเรียงคิวของ `FR-CFQP-04` เป็น "เรียงตามลำดับเวลารับออเดอร์ (FIFO)"
  3. กำหนดความง่ายในการใช้งานของ `NFR-CFQP-03` เป็น "กดเปลี่ยนสถานะได้สำเร็จภายในไม่เกิน 2 คลิก"
  4. เพิ่มคอลัมน์ `Acceptance Measure` ให้ครบทุกข้อใน Backlog
* **Rationale:** เพื่อให้ Requirement ทุกข้อมีความชัดเจน วัดผลได้จริง (Measurable) และรองรับการนำไปสร้าง Test Cases ในขั้นตอน Validation

---

## [DEC-05-02] การจัดการ Requirement ลอย (NFR-CFQP-01)

* **Date:** Week 05 (Baseline Review Studio)
* **Status:** Approved
* **Deciders:** ศักดิ์ณรงค์, จิรายุ
* **Context:** ตรวจพบว่า `NFR-CFQP-01` ไม่มี Evidence มารองรับสาย Traceability
* **Decision:** คงสถานะเป็น Must ไว้ชั่วคราวแบบ Conditional Baseline โดยระบุ `Assumption-01` และเปิดบันทึก `OQ-01` เพื่อลงพื้นที่เก็บ Evidence หน้าร้านเพิ่มเติมในสัปดาห์หน้า
* **Rationale:** ป้องกันการตัด Requirement สำคัญออกโดยทันที โดยเลือกใช้การระบุสมมติฐานและลงเก็บหลักฐานจริงย้อนหลังแทน