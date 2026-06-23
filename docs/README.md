# เอกสาร Requirements และ SRS

โฟลเดอร์นี้เก็บเอกสารหลักที่พัฒนาต่อเนื่องตั้งแต่ Week 1–8 และถูกนำไปอ้างอิงตลอดส่วนการออกแบบ

## ลำดับเอกสาร

1. `00-project-profile.md` — ข้อมูลโครงงานและขอบเขตระดับสูง
2. `01-problem-brief-v0.1.md` — ความเข้าใจปัญหาเริ่มต้น
3. `02-stakeholder-context-scope.md` — ผู้เกี่ยวข้อง ขอบเขต และบริบทระบบ
4. `03-elicitation-plan.md` — แผนเก็บความต้องการและคำถามสัมภาษณ์
5. `04-evidence-log.md` — หลักฐานที่เก็บได้และสิ่งที่ตีความ
6. `05-requirement-backlog.md` — requirement ที่มี ID และการจัดลำดับ
7. `06-requirement-models.md` — user stories/use cases/acceptance criteria
8. `07-srs-v1.md` — เอกสาร SRS ฉบับรวม
9. `08-validation-traceability.md` — validation, traceability, change management

## กติกา

- เริ่มต้นจากข้อมูลจริง/หลักฐานใน `evidence/` ไม่ใช่คาดเดาโดยไม่มีเหตุผล
- เมื่อ requirement เปลี่ยน ให้ปรับ backlog, SRS และ traceability ตามความจำเป็น
- ใช้ ID คงที่ เช่น `FR-01`, `NFR-01`, `UC-01`, `ADR-01` เพื่อให้อ้างอิงง่าย
- อ้างอิงรูป/diagram ด้วย relative path และเก็บ source diagram ไว้ใน `diagrams/`
