# 11 — Conceptual Architecture v0.1

> **Week 11 deliverable**

## 1. สิ่งที่รับมาจาก W10

| สิ่งที่รับ | สาระจาก W10 ของ Case 04 | ใช้ใน W11 ตรงไหน |
| :--- | :--- | :--- |
| **Scope** | **Build now:** <br>UC-01 ตรวจสอบสถานะอาหารและคิว (FR-01, NFR-01) <br> UC-02 จัดลำดับคิวและปรุงอาหาร (FR-04, NFR-03) <br> UC-04 ยกเลิกคำสั่งซื้อภายใต้ Cut-off (FR-03, BR-01)<br>**Overview:**<br> UC-03 ตรวจสอบสถิติและความหนาแน่นของคิว (FR-06)<br>**Later:**<br> ประมาณเวลารอล่วงหน้า (FR-02) <br> อัปเดตแจ้งเตือนเมนูหมด (FR-05)<br>**ไม่ทำ:**<br> ระบบชำระเงินออนไลน์ (ISSUE-01) <br> ระบบแทรกคิวอัตโนมัติ (ISSUE-02) | ขีดขอบระบบ (หัวข้อ 2) และเลือก container ที่รุ่นแรกต้องมี (หัวข้อ 3) |
| **Design drivers** | **D1**<br> Cut-off time ชัดเจน ไม่อนุญาตให้ลูกค้ายกเลิกเมื่อออเดอร์เป็น “กำลังทำ” (FR-03, BR-01)<br>**D2**<br> จัดลำดับคิวเคร่งครัดตาม FIFO — หน้าจอพนักงานแสดงออเดอร์ตามเวลาที่ได้รับจริง (FR-04, NFR-03)<br>**D3**<br> การเปลี่ยนสถานะเป็นไปตามสิทธิ์ และส่งผลต่อสถานะฝั่งลูกค้าอย่างสอดคล้องกัน (NFR-01, NFR-03, BR-01) | เหตุผลว่ากติกาอยู่ container ไหน (หัวข้อ 3–6) |
| **Design Spine** | เส้นทางคำขอหนึ่งใบ 6 ขั้น (ขั้น 1–6 Build now) | เดินทดสอบ container diagram (หัวข้อ 7) |
| **Open decisions** | OD-01 ถึง OD-04 | ติดป้าย TBD บนภาพ (หัวข้อ 8) |

## 2. Architecture View

![Conceptual Architecture](../diagrams/architecture/conceptual-architecture.png)

## 3. Components / Modules

| Component | Responsibilities | Inputs/Outputs | Related Requirements |
|---|---|---|---|
| [Component] | [กรอก] | [กรอก] | FR-xx |

## 4. Data and External Dependencies

| Dependency | Purpose | Risks / Constraints | Related Design Decision |
|---|---|---|---|
| [กรอก] | [กรอก] | [กรอก] | D-xx |

## 5. Architecture Rationale

- [เหตุผลที่เลือก architecture นี้]
- [ข้อดี/ข้อจำกัด]

## 6. Quality Attribute Evaluation Questions

- [เช่น การออกแบบนี้ช่วยให้ข้อมูลการจองไม่ซ้ำกันได้อย่างไร?]
- [เช่น ผู้ใช้บนมือถือเข้าถึงได้อย่างไร?]
