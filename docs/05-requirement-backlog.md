# 05 — Requirement Backlog v0.1: Campus Food Queue and Preorder

## 1. Project Metadata

| Field | Value |
|---|---|
| Course / Week | ENGSE206 / Week05 |
| Case | Campus Food Queue and Preorder (Case 04) |
| Source Week04 file | `04-evidence-log.md` |
| Backlog version | `v0.1` |
| Date | 2026-08-11 |

## 2. Prioritization Method

ใช้ MoSCoW โดยพิจารณาจาก 4 มิติดังนี้:

| Dimension | วิธีใช้ในตัวอย่างนี้ |
|---|---|
| Value | ใครได้ประโยชน์โดยตรง และประโยชน์นั้นเกี่ยวข้องกับปัญหาหลักของการจัดการคิวและเวลารอหรือไม่ (อ้างอิง 01-problem-brief) |
| Risk | หากไม่ทำฟีเจอร์นี้ จะเกิดผลกระทบด้านความผิดพลาดทางการสื่อสาร หรือข้อพิพาทเรื่องการยกเลิกอาหาร/ต้นทุนวัตถุดิบมากน้อยเพียงใด (อ้างอิง 02-stakeholder-context-scope และ 04-evidence-log) |
| Urgency | เป็นฟีเจอร์ที่ต้องมี เพื่อแก้ปัญหาลูกค้ายืนรอและลดความแออัดหน้าเคาน์เตอร์ทันที |
| Dependency | ฟีเจอร์นี้ต้องรอการยืนยัน นโยบายร้านค้า  หรือข้อมูลอื่นจาก Stakeholder ก่อนหรือไม่ (อ้างอิง 03-elicitation-plan และ 04-evidence-log) |

## 3. Requirement Backlog v0.1

| Req ID | Source RC | Evidence / Need Trace | Requirement Statement | Type | Priority | Rationale | Status | Open Question | Week06 Use |
|---|---|---|---|---|---|---|---|---|---|
| FR-CFQP-01 | RC-01 | E-07, PP-01, UN-01 | ระบบต้องแสดง "หมายเลขคิวปัจจุบัน" และ "สถานะอาหาร" บนหน้าจอฝั่งลูกค้า เพื่อให้ลูกค้าตรวจสอบได้โดยไม่ต้องพึ่งพาการฟังเสียงเรียก | Functional | Must | แก้ปัญหาหลักที่ลูกค้ายืนรอโดยไม่รู้คิวและเสียงดัง | Ready for Week06 | - | Use Case + User Story |
| FR-CFQP-02 | RC-02 | E-06, E-08, UN-01 | ระบบต้องแสดงข้อมูล จำนวนคิวที่รออยู่ และ ประมาณเวลารอ ให้ลูกค้าทราบก่อนทำการกดยืนยันสั่งอาหาร | Functional | Must | ช่วยนักศึกษาตัดสินใจและบริหารเวลาพักที่มีจำกัด | Needs Follow-up | หาวิธีคำนวณเวลาที่คลาดเคลื่อนไม่เกิน 5 นาที (ST-04) | User Story |
| FR-CFQP-03 | RC-03 | UN-03, E-08 | ระบบต้องมีฟังก์ชันให้ลูกค้ายกเลิกออเดอร์ได้ด้วยตนเองผ่านระบบ | Functional | Should | เพิ่มความยืดหยุ่นให้ลูกค้า และลดภาระพนักงานในการหาบิลกระดาษมายกเลิก | Needs Follow-up | ยืนยัน Cut-off time ที่ชัดเจนกับเจ้าของร้าน (ST-02) | Alternate Flow |
| BR-CFQP-01 | RC-03 | E-05, C-01 | ระบบจะไม่อนุญาตให้ลูกค้ายกเลิกคำสั่งซื้อ หากสถานะออเดอร์ถูกเปลี่ยนเป็น 'กำลังทำ' แล้ว | Business Rule | Must | ป้องกันการยกเลิกเมื่อลงมือทำแล้ว เพื่อรักษาต้นทุนวัตถุดิบของร้านค้า | Needs Follow-up | - | Acceptance Criteria |
| FR-CFQP-04 | RC-04 | E-01, E-03, E-04, UN-02 | หน้าจอฝั่งพนักงานต้องแสดงรายการคิวเรียงลำดับอย่างชัดเจน และมีการแบ่งกลุ่มสถานะ (เช่น ออเดอร์ใหม่, กำลังทำ, ทำเสร็จรอมารับ) | Functional | Must | ช่วยพนักงานจัดลำดับการทำงานหน้าเตา ลดความสับสนและความผิดพลาด | Ready for Week06 | - | Use Case + User Story |
| FR-CFQP-05 | RC-05 | E-02, UN-04 | ระบบต้องมีฟังก์ชันให้พนักงานกดระบุเมนูที่ "วัตถุดิบหมด" เพื่อแจ้งเตือนไปยังออเดอร์ของลูกค้าที่ค้างอยู่ทันที | Functional | Should | ลดข้อพิพาทและประหยัดเวลาพนักงานที่ต้องมาคอยตะโกนตามหาลูกค้าหน้าร้าน | Needs Follow-up | กำหนด Flow การคืนเงินหรือเปลี่ยนเมนู (Week 05) | Exception Flow |
| FR-CFQP-06 | - | 02: Data Flow | ระบบสามารถส่งออกหรือแสดงรายงานสถิติข้อร้องเรียนและความหนาแน่นของคิวในช่วงเวลาต่างๆ ให้ผู้ดูแลพื้นที่อาหาร | Functional | Could | มีประโยชน์ต่อผู้ดูแลพื้นที่ หลักของการสั่งอาหาร-รับอาหาร| Needs Follow-up | ต้องการรายงานในรูปแบบใดและถี่แค่ไหน | - |
| NFR-CFQP-01 | - | 01: Sect 9 | ระบบต้องแสดงผลการอัปเดตสถานะ  ไปที่หน้าจอของลูกค้าแบบทันที  | Non-functional | Must | เพื่อลดความสับสนของลูกค้า | Ready for Week06 | - | Quality Scenario |
| NFR-CFQP-02 | - | 02: Sect 5 | ระบบต้องจัดเก็บเฉพาะข้อมูลที่จำเป็น  โดยไม่เก็บข้อมูลละเอียดอ่อน เช่น ประวัติการแพ้อาหาร | Non-functional | Must | ป้องกันความเสี่ยงด้าน Privacy ตามกรอบจริยธรรมที่ตกลงไว้ | Ready for Week06 | - | Quality Scenario |
| NFR-CFQP-03 | - | 01: Sect 9 | หน้าจอฝั่งร้านค้าต้องออกแบบให้พนักงานกดเปลี่ยนสถานะได้รวดเร็วที่สุด โดยไม่ต้องละมือจากการทำอาหารนาน | Non-functional | Should | ตอบโจทย์ Usability ในช่วงเวลาที่ร้านวุ่นวายและคนเยอะ | Ready for Week06 | - | Quality Scenario |
| ISSUE-CFQP-01| - | 02: Sect 6 (Feedback) | การรวมระบบรับชำระเงินออนไลน์  เข้ากับระบบคิว | Issue | Won't yet | อยู่นอก Scope โครงงานและตามคำแนะนำของ Instructor ให้โฟกัสเฉพาะ Queue flow | Hold | - | - |
| ISSUE-CFQP-02| - | E-04, 03: Q-05 | ระบบคำนวณการแทรกคิวหรือลัดคิวอัตโนมัติ  สำหรับเมนูที่ทำง่ายและเสร็จไวกว่า | Issue | Won't yet | ขาดกฎเกณฑ์ที่ตายตัวของร้านค้าและอาจกระทบความรู้สึกยุติธรรม  ของลูกค้าคิวก่อนหน้า | Hold | เจ้าของร้านมีกฎการแทรกคิวที่ตายตัวและยุติธรรมหรือไม่ | - |

## 4. Priority Summary

| Priority | Count | Requirement IDs | เหตุผลรวม |
|---|---:|---|---|
| Must | 6 | FR-CFQP-01, FR-CFQP-02, BR-CFQP-01, FR-CFQP-04, NFR-CFQP-01, NFR-CFQP-02 | เป็น Core Features และมาตรฐานความปลอดภัยพื้นฐานที่ช่วยแก้ปัญหาความไม่รู้เวลาของลูกค้า ตอบโจทย์เป้าหมายระบบ (G-01 ถึง G-03) |
| Should | 3 | FR-CFQP-03, FR-CFQP-05, NFR-CFQP-03 | เป็นฟีเจอร์และคุณภาพระบบที่ช่วยอำนวยความสะดวก แต่บางประเด็นยังต้องรอนโยบายเพิ่มเติม |
| Could | 1 | FR-CFQP-06 | เป็นฟีเจอร์ที่เป็นประโยชน์กับผู้ดูแลพื้นที่อาหาร (Stakeholder รอง) แต่ไม่ได้มีความจำเป็นเร่งด่วนสำหรับการรันระบบคิวในเฟสแรก |
| Won't yet | 2 | ISSUE-CFQP-01, ISSUE-CFQP-02 | เป็นสิ่งที่ถูกตัด Out of Scope ชัดเจนโดย Instructor (เรื่อง Payment) และเรื่องที่ยังไม่มีกฎระเบียบร้านค้ารองรับ (เรื่องการแทรกคิว) จึงต้อง Hold ไว้ก่อน |

## 5. Ready / Follow-up / Hold

| Status | Requirement IDs | สิ่งที่ต้องทำต่อ |
|---|---|---|
| Ready for Week06 | FR-CFQP-01, FR-CFQP-04, NFR-CFQP-01, NFR-CFQP-02, NFR-CFQP-03 | นำไปเขียน Use Case, User Story, Acceptance Criteria และ Quality Scenario |
| Needs Follow-up | FR-CFQP-02, FR-CFQP-03, FR-CFQP-05, FR-CFQP-06, BR-CFQP-01 | คุยกับ Stakeholders เพิ่มเรื่องความคลาดเคลื่อนเวลา, Cut-off time, การคืนเงิน, และรูปแบบรายงานสำหรับผู้ดูแลพื้นที่ |
| Hold | ISSUE-CFQP-01, ISSUE-CFQP-02 | แขวนไว้เนื่องจากหลุด Scope (Payment) และขาด Policy ที่ชัดเจนจากเจ้าของร้าน (การแทรกคิว) |

## 6. Review Checklist

- [x] ทุก requirement มี Source RC หรือ Evidence source
- [x] ทุก requirement อ้าง Evidence / Need Trace
- [x] Type แยกเป็น Functional / NFR / Business Rule / Constraint / Issue
- [x] Priority มี rationale จาก value/risk/urgency/dependency
- [x] Unknown หรือ policy issue ไม่ถูกยกระดับเป็น requirement โดยไม่มีหลักฐาน
- [x] มี Week06 Use สำหรับรายการที่พร้อมทำ model