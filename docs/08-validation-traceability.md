# 08 — Validation, Traceability and Change Management

> **Week 8 deliverable (Updated for Baseline v1.0)**

## Case 04
| ขั้นตอน | เนื้อหา (Case 04) | อ้างอิง | ตรวจ |
| :--- | :--- | :--- | :--- |
| Problem | ในช่วงพักระหว่างคาบ ร้านอาหารและร้านเครื่องดื่มมีลูกค้าจำนวนมาก นักศึกษาต้องยืนรอโดยไม่รู้เวลารอจริง ร้านรับคำสั่งซื้อด้วยเสียงหรือกระดาษ ทำให้สื่อสารผิดพลาด เกิดการรับสินค้าผิดคน และเกิดความแออัดหน้าเคาน์เตอร์ | `CASE_CARD.md`<br>`docs/01` (PP-01, PP-02, PP-04)<br>`docs/02` (Problem Statement) | [x] |
| Stakeholder | 1. **นักศึกษา / ลูกค้า** (ผู้รับผลกระทบหลักโดยตรง)<br>2. **พนักงานร้าน** (ผู้ต้องตะโกนเรียกคิว)<br>3. **เจ้าของร้าน** (ผู้กังวลเรื่องออเดอร์ผิดพลาด)<br>4. **ผู้ดูแลพื้นที่อาหาร** (ผู้ต้องการลดความแออัด) | `CASE_CARD.md`<br>`docs/02` (Stakeholder Inventory) | [x] |
| Evidence | สัมภาษณ์/จำลอง: "โรงอาหารเสียงดังมาก ทำให้ลูกค้ากังวลว่าจะไม่ได้ยินเสียงเรียกคิวจนโดนข้าม จึงต้องยืนเฝ้าหน้าร้านตลอดเวลา" | `docs/04` (Evidence ID: E-07) | [x] |
| Need | ต้องการรู้คิวและเวลารอที่ชัดเจน เพื่อให้ตรวจสอบคิวได้โดยไม่ต้องพึ่งพาการฟังเสียงเรียก และจะได้ไม่ต้องยืนเบียดหน้าร้าน | `docs/01` (UN-01)<br>`docs/04` (RC-01) | [x] |
| FR/NFR | **FR-CFQP-01**: <br>ระบบต้องแสดง "หมายเลขคิวปัจจุบัน" และ "สถานะอาหาร" บนหน้าจอฝั่งลูกค้า เพื่อให้ลูกค้าตรวจสอบได้โดยไม่ต้องพึ่งพาการฟังเสียงเรียก | `docs/05` (FR-CFQP-01) | [x] |
| Priority | **Must** (เป็น Core Feature ที่แก้ปัญหาหลักเรื่องลูกค้ายืนรอโดยไม่รู้คิวและลดความแออัดหน้าร้าน ตอบโจทย์เป้าหมายหลัก G-01) | `docs/05` (Priority Rationale) | [x] |

## Open Question / Assumption

| Req ID | มาจาก Evidence (E-xx) | ผูกกับ Stakeholder | Need/Candidate (RC) | ลากครบ? | หมายเหตุ |
|---|---|---|---|---|---|
| **FR-CFQP-01** | E-07 | นักศึกษา/ลูกค้า | RC-01 |  ครบ | มีที่มาชัดเจน ลากกลับไปถึงปัญหาเรื่องโรงอาหารเสียงดังได้ |
| **BR-CFQP-01** | E-05 | เจ้าของร้าน | RC-03 |  ครบ | มีที่มาชัดเจน ลากกลับไปถึงนโยบายลดการสูญเสียต้นทุนของเจ้าของร้าน |
| **NFR-CFQP-01** |  ขาด (ระบุเป็น Assumption-01) | นักศึกษา/ลูกค้า |  ขาด (OQ-01) |  ขาด | **เจอ Gap!** เป็นข้อที่บอกว่า "ระบบต้องแสดงผลภายใน 3 วินาที" ข้อนี้โผล่มาในเอกสารโดยไม่มีการสัมภาษณ์มารองรับ จึงตั้งเป็นสมมติฐานไว้ก่อน |

## 1. Validation Plan

| Validation Activity | Artefact | Participants | Criteria | Evidence |
|---|---|---|---|---|
| Requirement Baseline Review (Self-Directed Studio) | `docs/01` ถึง `docs/05` | ศักดิ์ณรงค์, จิรายุ | completeness, feasibility, testability, traceability | `evidence/week-05/artefact-health-check.md` |

## 2. Requirements Quality Checklist

| Check | Result | Evidence / Note |
|---|---|---|
| Requirement มี ID และไม่ซ้ำกัน | Pass | ตรวจสอบใน `docs/05` แล้ว มี ID ชัดเจนทุกข้อ |
| ใช้ถ้อยคำชัดเจน ไม่กำกวม | **Resolved** | แก้ไขคำว่า "แบบทันที" (FR-05, NFR-01), "รวดเร็วที่สุด" (NFR-03) และ "ชัดเจน" (FR-04) เรียบร้อยแล้วใน Baseline v1.0 |
| ตรวจรับหรือวัดผลได้ | **Resolved** | เพิ่มคอลัมน์ Acceptance Measure ในตาราง `docs/05` เรียบร้อยแล้ว |
| มี source/rationale | **Resolved (Conditional)** | พบ Gap ใน NFR-CFQP-01 แต่ได้ทำการบันทึกเป็น Assumption และ Open Question (OQ-01) ไว้แล้ว |
| Scope เหมาะสม | Pass | ขอบเขตอยู่ในเรื่องการจัดการคิวและการสั่งอาหารล่วงหน้าตามที่ตกลงไว้ (ตัดระบบ Payment) |

## 3. Traceability Matrix

| Stakeholder Need / Evidence | FR / NFR | User Story / Use Case | Design Element | Verification / Review |
|---|---|---|---|---|
| UN-01, E-07 (อยากตรวจสอบคิวได้เอง) | FR-CFQP-01 | *[รอทำใน Week 06]* | - | - |
| UN-02, E-01 (ลดความผิดพลาดออเดอร์) | FR-CFQP-04 | *[รอทำใน Week 06]* | - | - |
| C-01, E-05 (รักษาต้นทุนวัตถุดิบ) | BR-CFQP-01 | *[รอทำใน Week 06]* | - | - |
| Assumption-01, OQ-01 | NFR-CFQP-01 | *[รอทำใน Week 06]* | - | - |

## 4. Change Request Log

| CR-ID | Date | Requested Change | Reason / Evidence | Impacted Artefacts | Decision | Owner |
|---|---|---|---|---|---|---|
| CR-05-01 | 2026-08-18 | แก้ไขคำกำกวมใน Requirement ให้เป็นตัวเลขที่วัดผลได้ (เช่น "ภายใน 3 วินาที", "ไม่เกิน 2 คลิก", "เรียงแบบ FIFO") | จากผลการ Audit (Peer Review) พบว่าประโยคเดิมกำกวมและนำไปเขียน Test Script ไม่ได้ | `docs/05` (FR-04, FR-05, NFR-01, NFR-03) | **Accepted** | ศักดิ์ณรงค์ |
| CR-05-02 | 2026-08-18 | เพิ่มคอลัมน์ Acceptance Measure ในเอกสาร Backlog ทุกข้อ | ตรวจพบจาก Artefact Health Check ว่ายังขาดเกณฑ์การตรวจรับที่ชัดเจน | `docs/05` | **Accepted** | ศักดิ์ณรงค์, จิรายุ |

## 5. Baseline Decision

- **Baseline name:** `baseline-v1.0` (ตรงกับ Git Tag)
- **Date:** 2026-08-18
- **Approved/Reviewed by:** ศักดิ์ณรงค์, จิรายุ (ผ่านการทำ Requirement Review Studio)
- **Remaining open issues:** NFR-CFQP-01 ยังขาด Evidence ข้อมูลจากการสัมภาษณ์มารองรับ ตัดสินใจว่าจะเก็บเป็น Assumption ไว้ก่อน และจะไปลงพื้นที่สังเกตการณ์/สัมภาษณ์ผู้ใช้เพิ่มเติมในสัปดาห์หน้า (OQ-01)

## 6. Follow-up Backlog

- [x] อัปเดต Requirement Backlog (`docs/05`) เพิ่มคอลัมน์ Acceptance Measure และแก้ไขคำกำกวมให้วัดผลได้ (ดำเนินการเสร็จใน Baseline v1.0)

---

## 7. Traceability Exceptions & Assumptions Log

เนื่องจากพบว่ามี Requirement บางข้อที่ยังขาดความเชื่อมโยง (Traceability Gap) จากการทำ Baseline Review จึงขออธิบายสมมติฐานและแผนการแก้ไขดังนี้:

* **NFR-CFQP-01 :**
  * **Current Status:** Conditional Baseline (Pending Evidence)
  * **Gap Identified:** ถูกจัดเกรดเป็น Must แต่ยังขาดหลักฐานการสัมภาษณ์/สังเกตการณ์ (Evidence) มารองรับโดยตรง
  * **Assumption-01:** กำหนดขึ้นบนสมมติฐานพฤติกรรมลูกค้าว่า "หากระบบไม่อัปเดตสถานะให้เห็นภายใน 3 วินาที ลูกค้าจะเกิดความลังเลและเดินมาสอบถามพนักงานหน้าร้าน ซึ่งจะส่งผลกระทบให้เกิดความแออัดและการทำงานของพนักงานสะดุด"
  * **Resolution / Open Question:** บันทึกเป็น Open Question (OQ-01) เพื่อวางแผนไปเก็บ Evidence เพิ่มเติมจากการสังเกตการณ์หน้าร้านในรอบถัดไป