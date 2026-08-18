# 08 — Validation, Traceability and Change Management

> **Week 8 deliverable**

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
| **NFR-CFQP-01** |  ขาด (อ้างแค่ 01: Sect 9) | นักศึกษา/ลูกค้า |  ขาด (ไม่มี RC-xx) |  ขาด | เจอ Gap! เป็นข้อที่บอกว่า "ระบบต้องแสดงผลแบบทันที" ข้อนี้โผล่มาในเอกสารโดยไม่มีการสัมภาษณ์ (E-xx) มารองรับ และไม่มีใน Requirement Candidate (RC) |



## 1. Validation Plan

| Validation Activity | Artefact | Participants | Criteria | Evidence |
|---|---|---|---|---|
| Requirement Baseline Review (Self-Directed Studio) | `docs/01` ถึง `docs/05` | สมาชิกทีม 04 ทุกคน | completeness, feasibility, testability, traceability | `evidence/week-05/artefact-health-check.md` |

## 2. Requirements Quality Checklist

| Check | Result | Evidence / Note |
|---|---|---|
| Requirement มี ID และไม่ซ้ำกัน | Pass | ตรวจสอบใน `docs/05` แล้ว มี ID ชัดเจนทุกข้อ |
| ใช้ถ้อยคำชัดเจน ไม่กำกวม | **Revise** | NFR-CFQP-01 และ 03 ยังใช้คำว่า "แบบทันที", "รวดเร็วที่สุด" ซึ่งวัดผลไม่ได้ |
| ตรวจรับหรือวัดผลได้ | **Revise** | NFR บางข้อต้องเปลี่ยนเป็นตัวเลข เช่น "ภายใน 2 วินาที" |
| มี source/rationale | **Revise** | พบ Gap: NFR-CFQP-01 ไม่มี Evidence (E-xx) มารองรับ |
| Scope เหมาะสม | Pass | ขอบเขตอยู่ในเรื่องการจัดการคิวและการสั่งอาหารล่วงหน้าตามที่ตกลงไว้ |

## 3. Traceability Matrix

| Stakeholder Need | FR / NFR | User Story / Use Case | Design Element | Verification / Review |
|---|---|---|---|---|
| UN-01 (อยากตรวจสอบคิวได้เอง) | FR-CFQP-01 | *[รอทำใน Week 6]* | - | - |
| UN-02 (ลดความผิดพลาดออเดอร์) | BR-CFQP-01 | *[รอทำใน Week 6]* | - | - |
| *[Missing Need]* | NFR-CFQP-01 | *[รอทำใน Week 6]* | - | - |

## 4. Change Request Log

| CR-ID | Date | Requested Change | Reason / Evidence | Impacted Artefacts | Decision | Owner |
|---|---|---|---|---|---|---|
| CR-05-01 | [18/08/2569] | แก้ไขคำว่า "แสดงผลแบบทันที" ให้เป็นตัวเลขที่วัดได้ เช่น "อัปเดตสถานะคิวภายใน 2 วินาที" | จากผลการ Audit พบว่าประโยคเดิมกำกวมและวัดผล Test ไม่ได้ | `docs/05` (NFR-CFQP-01) | **Accepted** | [สมาชิกทีม 04 ทุกคน] |
| CR-05-02 | [18/08/2569] | เพิ่มคอลัมน์ Acceptance Measure ในเอกสาร Backlog | ตรวจพบจาก Artefact Health Check ว่ายังขาดเกณฑ์การตรวจรับ | `docs/05` | **Accepted** | [สมาชิกทีม 04 ทุกคน] |

## 5. Baseline Decision

- **Baseline name:** `requirements-baseline-v1.0` (ตรงกับ Git Tag ที่จะสร้าง)
- **Date:** [18/08/2569]
- **Approved/Reviewed by:** สมาชิกกลุ่ม 04 ทุกคน (ผ่านการทำ Requirement Review Studio)
- **Remaining open issues:** NFR-CFQP-01 ยังขาด Evidence ข้อมูลจากการสัมภาษณ์มารองรับ ตัดสินใจว่าจะเก็บไว้ก่อนและจะไปหาสัมภาษณ์ผู้ใช้เพิ่มเติมในสัปดาห์หน้า

## 6. Follow-up Backlog

- [ ] [งานที่ต้องปรับก่อนเริ่ม design]

