# 15 — Individual Reflection

> ให้สมาชิกแต่ละคนคัดลอก template นี้เป็นไฟล์ของตนเอง เช่น `15-individual-reflection-student-id.md`

## Student Information

| Field | Detail |
|---|---|
| Student ID | 68543210069-9 |
| Name | ศักดิ์ณรงค์ นำนนท์ |
| Primary Role(s) | Checker / Auditor (Health Check, แก้ไข Requirement Backlog, Cross-Review) |

## 1. My Contribution

อธิบายสิ่งที่ทำจริง พร้อมอ้างอิง file/commit/evidence

- ดำเนินการ Artefact Health Check สำหรับเอกสาร `docs/01` ถึง `docs/05` 
- แก้ไขปรับปรุงถ้อยคำในไฟล์ `docs/05-requirement-backlog.md` โดยปรับตัดคำที่กำกวมออกและเพิ่มคอลัมน์ Acceptance Measure เพื่อให้สามารถวัดผลได้ 
- ทำหน้าที่ Peer Cross-Review ให้กลุ่ม โดยตรวจสอบความถูกต้องตาม Checklist 5 ประการ 

## 2. What I Learned About Requirements and Design

ได้เรียนรู้ว่า Requirement ที่ดีต้องมีคุณสมบัติที่ทดสอบและวัดผลได้ (Measurability) และต้องไม่กำกวม เช่น ในตอนแรกเราเขียนใช้คำว่า "ทันที" หรือ "รวดเร็วที่สุด" ซึ่งคำเหล่านี้ไม่สามารถนำไปเขียนเป็น Test Script ที่ชัดเจนได้ จึงต้องเรียนรู้การแปลงคุณลักษณะเหล่านี้ให้เป็นตัวเลขเชิงพฤติกรรม เช่น "ภายใน 3 วินาที" หรือ "ภายในไม่เกิน 2 คลิก" 

## 3. A Decision I Influenced

ผมมีส่วนร่วมในการตัดสินใจ คือการเสนอให้ปรับแก้ถ้อยคำใน Requirement ฝั่ง NFR และ FR ทุกข้อที่มีความกำกวมให้กลายเป็นตัวเลขที่ชัดเจนทั้งหมด รวมทั้งร่วมตัดสินใจใน  เพื่อคงสถานะ NFR-CFQP-01 ไว้ชั่วคราว แม้ว่าจะไม่มี Evidence มารองรับ (Requirement ลอย) โดยเลือกที่จะเปิดเป็น Assumption และลงพื้นที่เพื่อเก็บหลักฐานจริงแทนที่จะตัดทิ้ง 

## 4. Feedback I Received and How I Responded

ได้รับ Feedback จาก Peer Review ว่ามี Requirement บางข้อ (เช่น FR-CFQP-04, FR-CFQP-05, NFR-CFQP-01, NFR-CFQP-03) ยังมีการใช้คำกำกวม และในเอกสาร Backlog ขาดเกณฑ์การตรวจรับที่ชัดเจน ผมได้ตอบสนองโดยการดำเนินการปรับแก้คำเหล่านั้นในไฟล์ Backlog (docs/05) ให้เป็นตัวเลขที่วัดผลได้ และเพิ่มคอลัมน์ Acceptance Measure เข้าไปครบทุกข้อ 

## 5. What I Would Improve Next Time

ในครั้งต่อไป กำหนดมาตรวัด (Acceptance Measure) และตกลงตัวเลขเชิงพฤติกรรมกับ Stakeholder ให้ชัดเจนตั้งแต่ตอนทำ Elicitation (การสัมภาษณ์/เก็บความต้องการ) เพื่อที่จะได้ไม่ต้องมาตีความหรือตามแก้คำกำกวมในช่วงการทำ Baseline Review 

## 6. Evidence Links

- `docs/05-requirement-backlog.md` 
- `evidence/week-05/artefact-health-check.md` 