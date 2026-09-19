# 07 — Software Requirements Specification (SRS) v1

> **Week 7 deliverable**  
> เวอร์ชัน: v1.0 | สถานะ: Baseline Candidate | วันที่: [DD/MM/YYYY]

## Document Control

| Version | Date | Author | Reviewer | Summary of Change |
|---|---|---|---|---|
| 0.1 | | | | Initial draft |
| 1.0 | | | | Baseline candidate |

## 1. Introduction

### 1.1 Purpose
[กรอก]

### 1.2 Scope
#### In Scope
- เริ่มจากร้านจำลอง 1 ร้านและเมนูจำกัด
- รองรับกรณีเมนูหมดและรับสินค้าไม่ตรงเวลา  
- การจัดการคิว การแสดงเวลารอ และการอัปเดตสถานะออเดอร์

#### Out of Scope
- ไม่รวม payment gateway จริง  
- ไม่รวมระบบบัญชีร้าน และระบบจัดซื้อวัตถุดิบ  
- ไม่รวมแพลตฟอร์ม food delivery เต็มรูปแบบ  
- ไม่เก็บข้อมูลแพ้อาหารเชิงสุขภาพละเอียด  

### 1.3 Definitions, Acronyms and Abbreviations
ดู [Glossary](glossary.md)

### 1.4 References
- Case Card
- Evidence log
- Course materials

## 2. Overall Description

### 2.1 Product Perspective
[กรอก]

### 2.2 User Classes and Characteristics
- นักศึกษา / ลูกค้า : สั่งอาหารได้ง่าย รู้เวลารอที่ชัดเจน และได้รับสินค้าที่ถูกต้อง
- พนักงานร้าน : รับออเดอร์ได้ชัดเจน ลดความสับสน และสามารถจัดลำดับงานได้
- เจ้าของร้าน : มองเห็นภาพรวมภาระงานทั้งหมด และลดข้อผิดพลาดของออเดอร์
- ผู้ดูแลพื้นที่อาหาร : ลดความแออัดในพื้นที่และลดข้อร้องเรียนจากนักศึกษา/ร้านค้า

### 2.3 Operating Environment
[กรอก]

### 2.4 Constraints
- แต่ละร้านมีระยะเวลาในการเตรียมอาหารไม่เท่ากัน
- ไม่เปิดใช้งานระบบตัดเงินจริงในเฟสโครงงานรายวิชานี้

### 2.5 Assumptions and Dependencies
- นักศึกษามีสมาร์ตโฟนที่สามารถเชื่อมต่ออินเทอร์เน็ตสำหรับดูคิวได้
- พนักงานมีอุปกรณ์ (เช่น Tablet หรือมือถือ) สำหรับกดเปลี่ยนสถานะออเดอร์
- ลูกค้าและพนักงานยินดีปรับตัวใช้งานระบบคิวแบบใหม่แทนการตะโกนสั่งแบบเดิม

## 3. Functional Requirements

> สรุปจาก `05-requirement-backlog.md` และต้องคง ID เดิม

| ID | Requirement | Priority | Acceptance / Verification |
|---|---|---|---|
| FR-01 | [กรอก] | Must | [กรอก] |

## 4. Non-functional Requirements

| ID | Quality Attribute | Requirement | Measure |
|---|---|---|---|
| NFR-01 | [กรอก] | [กรอก] | [กรอก] |

## 5. External Interface Requirements

### 5.1 User Interfaces
[กรอก]

### 5.2 Software / External System Interfaces
[กรอก]

### 5.3 Data Interfaces
[กรอก]

## 6. Business Rules

| ID | Rule | Related Requirement |
|---|---|---|
| BR-01 | ระบบจะไม่อนุญาตให้ลูกค้ายกเลิกคำสั่งซื้อ หากสถานะออเดอร์ถูกเปลี่ยนเป็น 'กำลังทำ' แล้ว | FR-03 |

## 7. Requirement Models

- Use Case Diagram: [link]
- Activity Diagram(s): [link]
- Domain Model: [link]

## 8. Open Issues

| ID | Issue / Question | Owner | Due / Status |
|---|---|---|---|
| OQ-01 | [กรอก] | [ชื่อ] | Open |

## 9. Approval / Review Record

| Reviewer | Date | Result | Key Feedback |
|---|---|---|---|
| [ชื่อ/บทบาท] | | Approved / Revision | |
