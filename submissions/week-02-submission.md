# Week 02 Submission — Stakeholder, Context and Scope
 
## 1. Assignment Source
 
| Field | Value |
|---|---|
| Assignment ID | `W02-v1.0` |
| Course assignment URL | https://github.com/se-rmutl/engse206-lab/blob/main/weeks/week-02-stakeholder-context-scope/assignment-contract.md |
| Course version/commit read | main |
| Date checked | 2026-10-23 |
| Case ID / Case URL | Case 04 ระบบจัดการคิวร้านอาหารหรือร้านเครื่องดื่มในมหาวิทยาลัย |
 
## 2. Artefacts Submitted
 
ผลลัพธ์หลัก: **Stakeholder Map + System Context + Scope**
 
Expected paths: `docs/02-stakeholder-context-scope.md`, `diagrams/context/`, `feedback/week-02-peer-feedback.md`, `submissions/week-02-submission.md`
 
| Artefact | Repository path / URL | Owner | Status |
|---|---|---|---|
| Stakeholder, Context and Scope | [`docs/02-stakeholder-context-scope.md`](../docs/02-stakeholder-context-scope.md) | ศักดิ์ณรงค์ นำนนท์ | Done |
| System Context Diagram | [`diagrams/context/SystemContextDiagram.drawio`](../diagrams/context/SystemContextDiagram.drawio) + [`.png`](../diagrams/context/SystemContextDiagram.png) | จิรายุ วงศ์ต่อม | Done |
| Stakeholder Map | [`diagrams/stakeholders/StakeholderMap.drawio`](../diagrams/stakeholders/StakeholderMap.drawio) + [`.png`](../diagrams/stakeholders/StakeholderMap.png) | จิรายุ วงศ์ต่อม | Done |
| Peer Feedback | [`feedback/week-02-peer-feedback.md`](../feedback/week-02-peer-feedback.md) | ศักดิ์ณรงค์ นำนนท์ | Done |
| Worklog | [`project-management/week-02-week-03-worklog.md`](../project-management/week-02-week-03-worklog.md) | ทุกคน | Done |
 
## 3. Evidence and Quality Check
 
- [x] มี source file ที่แก้ไขได้
- [x] diagram มี `.drawio` และ export `.png`/`.pdf` เมื่อเกี่ยวข้อง
- [x] evidence อ้างอิงกลับไปยัง artefact ได้ (Case Card + peer feedback → §1.1, §3, §7, D-01)
- [x] อัปเดต worklog และ AI use log แล้ว (สัปดาห์นี้ไม่ได้ใช้ AI)
- [x] peer/instructor feedback ถูกบันทึกแล้ว
- [x] ไม่มีข้อมูลส่วนบุคคล/secret

## 4. Team Contribution
 
| Member | Role / Work completed | Evidence (commit/file) |
|---|---|---|
| จิรายุ วงศ์ต่อม | Facilitator/Timekeeper — ปรับ Problem Frame และ Scope Statement และ Evidence checker/Presenter| `docs/02-stakeholder-context-scope.md` `docs/02-stakeholder-context-scope.md` |
| ศักดิ์ณรงค์ นำนนท์ | Note taker  รวบรวมเอกสาร ตรวจ Scope และตั้ง Open Questions Stakeholder Inventory, Profiles และวาด Stakeholder Map | `docs/02-stakeholder-context-scope.md` `diagrams/stakeholders/StakeholderMap.drawio` |
 
## 5. Tabletop / Review Summary
 
- สิ่งที่นำเสนอ: Stakeholder Map (พนักงานร้าน, เจ้าของร้าน, ผู้ดูแลพื้นที่อาหาร, นักศึกษา/ลูกค้า), System Context Diagram และ In/Out Scope
- Feedback ที่ได้รับ: Reviewer Team แนะนำให้แยก "พนักงานร้าน" กับ "เจ้าของร้าน" ให้ชัดเจน และถามว่าหากเมนูหมดจะคืนเงินอย่างไร · instructor cue: รายวิชานี้ไม่รวม Payment gateway ให้โฟกัส flow ของสถานะ "คิว" · Peer Feedback: ขอให้ระดับ Influence และ Interest ของแต่ละบทบาทเห็นความต่างชัดขึ้น
- สิ่งที่แก้ก่อนส่ง: แยกผู้ปฏิบัติงาน (พนักงานร้าน) กับผู้ควบคุมนโยบาย (เจ้าของร้าน) ใน Stakeholder Map · ปรับ System Context ให้ครอบคลุมการอัปเดต "พร้อมรับ/หมด" และการดูรายงานแยกกัน · ระบุ Out of Scope ให้ชัด (Payment Gateway, Food delivery) · แยก Influence และ Interest เป็นคอลัมน์ใน Stakeholder Inventory · เพิ่ม Open Questions เรื่องจุดตัดเวลายกเลิก (OQ-01), ผู้เปลี่ยนสถานะ (OQ-02) และเมนูหมดหลังรับออเดอร์ (OQ-03)
## 6. Final Submission Snapshot
 
| Field | Value |
|---|---|
| Commit message | `submit(w02): stakeholder context and scope` |
| Commit hash | aa08e08 |
| Submitted at | 2026-10-23 12:05 |
| Known limitations / open questions | OQ-01–OQ-04 ยังเปิด (ส่งต่อ W03) · ยังไม่ได้ยืนยันกติกาการยกเลิกและจังหวะการอัปเดตคิวกับ stakeholder จริง · คำถามถึงผู้สอน: ใน W04 stakeholder simulation ควรให้ role card ของ "เจ้าของร้าน" และ "ลูกค้า" มีสถานการณ์ความขัดแย้ง (เช่น เมนูหมดกะทันหัน หรือลูกค้ามารับช้าจนคิวชะงัก) เจาะจงเพียงใด เพื่อให้ทีมใช้คำถามสัมภาษณ์ดึง requirement เรื่องการจัดการความคาดหวัง/ความผิดหวังได้ครบ |
 
## 7. Revision after Feedback
 
| Date | Feedback | Change made | New commit |
|---|---|---|---|
|  | |  |  |
