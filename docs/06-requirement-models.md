# 06 — Requirement Models: User Stories, Use Cases and Acceptance Criteria

> **Week 6 deliverable**

## 1. User Stories

| ID | User Story | Priority | Linked FR | Acceptance Criteria |
|---|---|---|---|---|
| US-01 | ในฐานะ ลูกค้า ฉันต้องการ รู้หมายเลขคิวปัจจุบันและสถานะอาหาร เพื่อ ตรวจสอบได้โดยไม่ต้องพึ่งพาการฟังเสียงเรียก | Must | FR-CFQP-01 |  |
| US-02 | ในฐานะ พนักงานร้าน ฉันต้องการ ห็นรายการออเดอร์ที่จัดเรียงลำดับก่อนหลังชัดเจน เพื่อ สามารถลงมือทำอาหารตามลำดับคิวที่แท้จริงได้ถูกต้อง | Must | FR-CFQP-04 |  |
| US-03 | ในฐานะ พนักงานร้าน ฉันต้องการ เห็นคิวเรียงลำดับชัดเจน เพื่อ จัดลำดับการทำอาหารที่มีเวลาเตรียมไม่เท่ากันได้ถูกต้อง | Must | 	FR-CFQP-04 |  |
| US-04 | ในฐานะ ลูกค้า ฉันต้องการ ยกเลิกออเดอร์อาหาร เพื่อ ไปร้านที่คิวน้อยกว่า | 	Should | 	FR-CFQP-03 |  |
| US-05 | ในฐานะ เจ้าของร้าน ฉันต้องการ **ให้ระบบระงับสิทธิ์การกดยกเลิกคำสั่งซื้อของฝั่งลูกค้าอัตโนมัติเมื่อสถานะเป็น "กำลังทำ"**เพื่อ ป้องกันความเสียหายและการสูญเสียต้นทุนวัตถุดิบและเวลา | Must | BR-CFQP-01 |  |
| US-06 | ในฐานะ พนักงานร้าน ฉันต้องการ จัดคิวเรียงตามลำดับเวลารับออเดอร์ เพื่อ ลดความสับสนและความผิดพลาด | Must | FR-CFQP-04 |  |
| US-07 | ในฐานะ พนักงานร้านฉันต้องการ ให้ระบบส่งสถิติแจ้งความหนาแน่นของคิวในช่วงเวลาต่างๆ ให้กับผู้ดูแลพื้นที่อาหารเพื่อ ช่วยให้สามารถจัดระเบียบพื้นที่ส่วนกลางและระงับความแออัดของลูกค้าหน้าร้านค้าของตนได้ | Could | 	FR-CFQP-06 |  |
| US-08 | ในฐานะ ผู้ดูแลพื้นที่อาหาร ฉันต้องการ การจัดเรียงคิว เพื่อ ไม่ให้คนแออัดหน้าร้าน | Could | 	FR-CFQP-04 |  |
| US-09 | ในฐานะ ผู้ดูแลพื้นที่อาหาร ฉันต้องการ ทราบความหนาแน่นของคิวในช่วงเวลาต่างๆ เพื่อ นำไปวิเคราะห์และออกมาตรการบริหารจัดการพื้นที่ล่วงหน้าเพื่อลดข้อร้องเรียน | Could | 	FR-CFQP-06 |  |
| US-10 | ในฐานะ เจ้าของร้าน ฉันต้องการ ปรับเปลี่ยนหรือปิดสถานะรายการอาหารที่ "วัตถุดิบหมด" ในระบบได้ทันที เพื่อ ป้องกันไม่ให้ลูกค้ารายอื่นกดยืนยันออเดอร์ที่ไม่มีของ | Should | 	FR-CFQP-05 |  |

## 2. Acceptance Criteria

### AC-01 — [ชื่อ]

- Given [initial context]
- When [action]
- Then [expected result]

## 3. Use Case List

| ID | Use Case | Primary Actor | Goal | Related FR | Diagram |
|---|---|---|---|---|---|
| UC-01 | [กรอก] | [Role] | [Goal] | FR-01 | `../diagrams/use-case/...` |

## 4. Use Case Specification

### UC-01 — [ชื่อ Use Case]

| Field | Detail |
|---|---|
| Primary Actor | [กรอก] |
| Trigger | [กรอก] |
| Preconditions | [กรอก] |
| Main Success Scenario | 1. ... 2. ... |
| Alternate / Exception Flows | [กรอก] |
| Postconditions | [กรอก] |
| Related Requirements | FR-xx, NFR-xx |

## 5. Requirement Models / Diagrams

- Use Case Diagram: [link](../diagrams/use-case/README.md)
- Activity Diagram: [link](../diagrams/activity/README.md)
- Domain Model: [link](../diagrams/domain-model/README.md)

## 6. Negotiation / Trade-off Notes

บันทึกสิ่งที่ไม่ได้เลือกหรือเลื่อนออกจาก scope พร้อมเหตุผล

[กรอก]
