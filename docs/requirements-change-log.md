# Requirements Change Log

> สรุปการเปลี่ยน Requirement ที่มีบันทึกใน `08-validation-traceability.md` และประวัติ Git ของ `05-requirement-backlog.md` รายการ `CR-RETRO-*` จดเพิ่มย้อนหลังจากการเปลี่ยนใน Git เพราะยังไม่พบ Change Request หรือมติอนุมัติประกอบ จึงยังไม่ถือว่าเหตุผลและผลกระทบได้รับการยืนยันครบแล้ว

| Date | Change ID | Requirement(s) | Type | Summary | Reason | Impacted Design | Status |
|---|---|---|---|---|---|---|---|
| 2026-08-18 | CR-05-01 | `FR-CFQP-04` → `FR-04`; `FR-CFQP-05` → `FR-05`; `NFR-CFQP-01` → `NFR-01`; `NFR-CFQP-03` → `NFR-03` | Changed | ปรับคำกำกวมให้ตรวจรับได้ เช่น เรียงคิวแบบ FIFO, แสดงสถานะภายใน 3 วินาที และเปลี่ยนสถานะได้ไม่เกิน 2 คลิก | Peer Cross-Review พบว่าคำเดิมนำไปเขียน Test Script ได้ไม่ชัด | `docs/05-requirement-backlog.md`; ไม่มี design impact แยกบันทึก | Accepted — Baseline v1.0 |
| 2026-08-18 | CR-05-02 | ทุกแถวใน Backlog (FR, BR, NFR และ Issue) | Changed | เพิ่มคอลัมน์ `Acceptance Measure` เพื่อระบุเกณฑ์ตรวจรับใน Backlog | Artefact Health Check พบว่ายังขาดเกณฑ์ตรวจรับที่ชัดเจน | `docs/05-requirement-backlog.md`; ไม่มี design impact แยกบันทึก | Accepted — Baseline v1.0 |
| 2026-09-16 | CR-RETRO-01 | `FR-CFQP-01–06` → `FR-01–06`; `BR-CFQP-01` → `BR-01`; `NFR-CFQP-01–03` → `NFR-01–03`; `ISSUE-CFQP-01–02` → `ISSUE-01–02` | Changed (IDs) | เปลี่ยนรูปแบบรหัสใน Backlog ให้สั้นลง โดยไม่พบ Change Request ที่ระบุ mapping นี้ไว้ | Commit `b304d4b` ระบุว่าเพิ่มรหัสใหม่และปรับความชัดเจนของ FR แต่ไม่พบเหตุผลหรือมติอนุมัติใน Decision Log | `docs/05-requirement-backlog.md`; `docs/08-validation-traceability.md` ยังใช้รหัสเดิม; `design/10` และ `design/11` ใช้รหัสใหม่ | ทำแล้วในไฟล์; รอตรวจเหตุผลและปรับ traceability ให้ตรงกัน |
| 2026-09-16 | CR-RETRO-02 | `FR-06`, `NFR-01` | Changed (Status) | เปลี่ยนสถานะในแถว Requirement: `FR-06` จาก Needs Follow-up เป็น Ready และ `NFR-01` จาก Ready เป็น Needs Follow-up | Commit `7bc1de8` แสดงการแก้สถานะ แต่ไม่พบเหตุผลหรือมติประกอบ | `docs/05-requirement-backlog.md`; ไม่มี design impact แยกบันทึก | เปลี่ยนในไฟล์แล้ว; เหตุผลยังไม่ถูกบันทึก |
| 2026-09-17 | CR-RETRO-03 | `FR-03`, `BR-01`, `NFR-02` | Changed (Readiness Summary) | เพิ่ม `FR-03` และ `BR-01` ในกลุ่ม Ready และ `NFR-02` ใน Needs Follow-up ในสรุปท้ายไฟล์ แต่สถานะในแถว Requirement ยังเป็น Needs Follow-up, Needs Follow-up และ Ready ตามลำดับ | Commit `320ed4f` แก้รายการสรุป แต่ไม่พบเหตุผลหรือมติประกอบ | `docs/05-requirement-backlog.md`; ต้องเทียบสรุปกับคอลัมน์ Status ก่อนใช้วางแผน | รายการสรุปเปลี่ยนแล้ว; ยังมีข้อมูลไม่ตรงกัน |

## ประเด็นที่ต้องตามต่อ

- ตรวจ mapping รหัสเดิมกับรหัสปัจจุบัน แล้วอัปเดต `docs/08-validation-traceability.md` ให้ตรงกับ Backlog
- ยืนยันเหตุผลของการปรับสถานะ `FR-06` และ `NFR-01` ในเดือนกันยายน
- แก้สรุป Ready/Needs Follow-up ให้ตรงกับสถานะราย Requirement สำหรับ `FR-03`, `BR-01` และ `NFR-02`
- ตรวจความไม่ตรงของ `FR-05`: แถว Requirement ใน Backlog ระบุ Must แต่ Priority Summary จัดไว้ใน Should; `design/10` และ `design/11` ก็ยังจัดไว้ Later / Should-Deferred
- คง `CR-RETRO-01` ถึง `CR-RETRO-03` เป็นรายการย้อนหลังจนกว่าจะพบคำขอหรือมติที่ยืนยันได้; ไม่ถือว่าเป็นการอนุมัติใหม่
