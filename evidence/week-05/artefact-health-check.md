# 1. ผลการตรวจคลังชิ้นงาน (Artefact Health Check)

**สำหรับการนำไปใส่ในไฟล์:** `evidence/week-05/README.md`

| เอกสาร | ต้องมีอะไรอยู่ข้างใน | สถานะ | หมายเหตุ (สิ่งที่พบ) |
|---|---|---|---|
| **docs/01 Problem Brief** | goal เชิงผลลัพธ์, pain points, stakeholder เริ่มต้น, NFR เริ่มต้น | [x] ครบ <br> [ ] ต้องแก้ | มีเป้าหมาย, ปัญหา, ผู้มีส่วนได้ส่วนเสีย และ NFR เริ่มต้นครบถ้วน |
| **docs/02 Stakeholder/Scope** | stakeholder map, context diagram, in/out scope, constraints | [x] ครบ <br> [ ] ต้องแก้ | ระบุ In/Out Scope ชัดเจน มีข้อจำกัด และอ้างอิงไฟล์รูปภาพ Diagram ครบถ้วน |
| **docs/03 Elicitation/Interview** | objectives, คำถาม 10-12 ข้อ, bias check | [x] ครบ <br> [ ] ต้องแก้ | มี Objectives (ใน `03-elicitation-plan.md`) และมีคำถามสัมภาษณ์ 12 ข้อ พร้อม Bias Check (ใน `03-interview-guide.md`) ครบถ้วน |
| **docs/04 Evidence Log** | หลักฐานติด tag, conflict + ผลเจรจา, requirement candidates | [x] ครบ <br> [ ] ต้องแก้ | มีตารางหลักฐานติด Tag, การเจรจาข้อขัดแย้ง และ Requirement Candidates ครบถ้วน |
| **docs/05 Backlog** | FR/NFR+source+priority+acceptance measure | [ ] ครบ <br> [x] **ต้องแก้** | มี FR/NFR, Source, Priority ครบ (อยู่ใน `05-requirement-backlog.md` และอธิบายเหตุผลใน `05-prioritization-rationale.md`) แต่มีส่วนที่ต้องแก้ไขดังนี้:<br>1. **ยังไม่มีคอลัมน์ Acceptance measure** อย่างชัดเจนใน Backlog<br>2. **คำอธิบาย NFR ยังกำกวม (วัดผลไม่ได้)** เช่น "แบบทันที" และ "รวดเร็วที่สุด" |

---
### สรุปสิ่งที่ทีมต้องนำไปแก้รวมกันในช่วงที่ 5:
1. เพิ่มคอลัมน์ หรือระบุ **Acceptance measure (เกณฑ์การตรวจรับ)** สำหรับ Requirement แต่ละข้อลงใน `docs/05-requirement-backlog.md`
2. ปรับแก้คำอธิบาย **NFR ให้สามารถวัดผลเป็นตัวเลขได้ชัดเจน** ใน `docs/05-requirement-backlog.md`