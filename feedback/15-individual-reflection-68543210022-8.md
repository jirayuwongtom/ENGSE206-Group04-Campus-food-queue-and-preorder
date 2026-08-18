# 15 — Individual Reflection

> ให้สมาชิกแต่ละคนคัดลอก template นี้เป็นไฟล์ของตนเอง เช่น `15-individual-reflection-student-id.md`

## Student Information

| Field | Detail |
|---|---|
| Student ID | 68543210022-8 |
| Name | จิรายุ วงศ์ต่อม |
| Primary Role(s) | Scribe / Facilitator (Traceability Matrix, Decision Log, Release Baseline)  |

## 1. My Contribution

อธิบายสิ่งที่ทำจริง พร้อมอ้างอิง file/commit/evidence

- ตรวจสอบ Traceability Matrix และดูแลรับผิดชอบบันทึกข้อแก้ปัญหา (Traceability Gap) ของ NFR-CFQP-01 ลงในเอกสาร `docs/08-validation-traceability.md` 
- สรุปและลงบันทึกการตัดสินใจสำคัญของทีมลงในเอกสาร `project-management/decision-log.md` (DEC-05-01 และ DEC-05-02)
- รวบรวมเอกสารทั้งหมด สรุปผล Readiness Gate ก่อนปิดงาน และเตรียมการล็อก Git Tag `baseline-v1.0` 

## 2. What I Learned About Requirements and Design

ได้เรียนรู้เกี่ยวกับการจัดการ Requirement ลอย (Requirement ที่ไม่มี Evidence มารองรับ) ผ่านการทำ Traceability Audit ทำให้ทราบว่าหากเราเจอความต้องการระดับ "Must" ที่ขาดความเชื่อมโยงกลับไปยังต้นตอ เราไม่ควรลบทิ้งในทันที แต่ควรมีกระบวนการจัดการอย่างเป็นระบบด้วยการตั้งสมมติฐาน (Assumption) และบันทึกเป็น Open Question เพื่อไปเก็บหลักฐานสัมภาษณ์เพิ่มเติม 

## 3. A Decision I Influenced

ส่วนร่วมหลักในการตัดสินใจเกี่ยวกับการจัดการ Requirement ลอยของ NFR-CFQP-01 โดยผมเป็นคนบันทึกชี้แจงร่องรอยการตัดสินใจนี้ลงในเอกสารว่าเราจะคงสถานะ Must ไว้แบบ Conditional Baseline ควบคู่กับการประกาศ Assumption-01 เพื่อเตรียมลงพื้นที่ไปเก็บหลักฐานสนับสนุนเพิ่มเติมในสัปดาห์หน้า 

## 4. Feedback I Received and How I Responded

รับ Feedback จาก Peer Review ว่า NFR-CFQP-01 ซึ่งถูกตั้งความสำคัญไว้ระดับ Must นั้น ไม่มีสาย Traceability หรือ Evidence (E-xx) มารองรับ จึงรับผิดชอบตอบสนองโดยการบันทึกชี้แจงสมมติฐานและแผนการแก้ไขปัญหาลงในส่วน "Traceability Exceptions & Assumptions Log" ท้ายเอกสาร docs/08 เพื่ออธิบายร่องรอยการทำงานให้ชัดเจน

## 5. What I Would Improve Next Time

ทำ Traceability Matrix ควบคู่ไปกับการจัดทำ Requirement Backlog ตั้งแต่แรก แทนที่จะมาทำแยกทีหลัง เพื่อที่จะได้เห็นช่องโหว่ (Gap) หรือ Requirement ลอยได้ไวขึ้น และสามารถตั้งคำถามถาม Stakeholder ได้ทันในรอบที่กำลังเก็บข้อมูล

## 6. Evidence Links

- `docs/08-validation-traceability.md` 
- `project-management/decision-log.md` 
- Release Tag `baseline-v1.0`