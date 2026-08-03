# Week 04 — Evidence-linked Requirement Candidates

> **Important:** รายการนี้เป็น Candidate/Provisional สำหรับนำไปวิเคราะห์ใน Week 05 ยังไม่ใช่ Approved requirement

## 1. Requirement candidates

| RC ID | Candidate statement | Type | Evidence / Decision | Status | Confidence | Follow-up / acceptance hint |
|---|---|---|---|---|---|---|
| RC-01 | ระบบต้องแสดง "จำนวนคิวที่รออยู่" และ "เวลารอโดยประมาณ" ให้ลูกค้าเห็นก่อนตัดสินใจสั่งอาหาร | Functional | E-06 | Candidate | High | ยืนยันวิธีคำนวณเวลา (Week 05) |
| RC-02 | ระบบอนุญาตให้ลูกค้ายกเลิกออเดอร์ได้ แต่ปุ่มจะถูกล็อกทันทีเมื่อพนักงานเปลี่ยนสถานะออเดอร์เป็น "กำลังทำ" | Business rule | E-05, E-08, N-01 | Provisional | Medium | ยืนยัน Cut-off time กับเจ้าของร้าน (ST-02) |
| RC-03 | UI หน้าจอพนักงานต้องใช้งานง่ายด้วยการกดเพียง 1-2 ครั้ง และแสดงคิวเรียงลำดับชัดเจนเพื่อลดภาระทางความคิด | Functional / UI | E-01 | Candidate | Medium | นำ Wireframe เบื้องต้นไปทดสอบ |
| RC-04 | ระบบต้องมีปุ่มระบุว่า "เมนูหมด (Out of stock)" เพื่อแจ้งเตือนกลับไปยังลูกค้ารายนั้นทันทีโดยไม่ต้องรอถึงคิว | Functional | E-02 | Candidate | Medium | หากระบวนการคืนเงินกรณีตัดบัตรแล้ว |
| RC-05 | ระบบต้องมีปุ่มหรือการแสดงผลรองรับการทำอาหารข้ามคิว (สำหรับเมนูทำง่าย) และแสดงสถานะแต่ละคิวให้โปร่งใส | Functional | E-04, E-07, N-02 | Provisional | Medium | ตรวจสอบว่าระบบจัดเรียงรายการบนจออย่างไร |
| RC-06 | ระบบควรมีสถานะแยกสำหรับออเดอร์ "พร้อมรับแต่มารับช้า (Late pickup)" เพื่อแยกออกจากคิวที่กำลังรันอยู่หน้าเคาน์เตอร์ | Functional | E-03 | Provisional | Medium | หารือเรื่องขีดจำกัดเวลา (กี่นาทีถึงจะถือว่า Late) |

## 2. Coverage and traceability matrix

| Week 03 objective (EO) | Week 04 evidence/negotiation | Requirement Candidate |
|---|---|---|
| EO-01: หาระยะเวลายกเลิกออเดอร์ | E-05, E-08, N-01 | RC-02 |
| EO-02: หากระบวนการทำงานและแบ่งหน้าที่ | E-01, E-03, E-04, N-02 | RC-03, RC-05, RC-06 |
| EO-03: หาวิธีสื่อสารเมื่อวัตถุดิบหมด | E-02 | RC-04 |
| EO-04: ข้อมูลหน้าจอลูกค้าเพื่อประกอบการตัดสินใจ | E-06, E-07 | RC-01, RC-05 |

## 3. Quality review

- [x] Traceable: RC ทุกข้ออ้าง E-ID และ/หรือ N-ID ชัดเจน
- [x] No unsupported approval: ทุกข้อใช้สถานะ Candidate หรือ Provisional
- [x] Solution-neutral: RC-02 กำหนด Flow แต่ยังไม่เจาะจงเทคโนโลยีเบื้องหลัง