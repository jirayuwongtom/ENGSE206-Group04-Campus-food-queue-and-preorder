# Week 04 Submission — AI Stakeholder Panel, Evidence and Negotiation

## 1. ข้อมูลงาน

| รายการ | ข้อมูล |
|---|---|
| Assignment ID | `W04` |
| Course URL / version ที่อ่าน | https://github.com/se-rmutl/engse206-lab/tree/main/weeks/week-04-stakeholder-simulation-negotiation |
| Case / Role Pack | Case 04 — ระบบจัดการคิวร้านอาหารหรือร้านเครื่องดื่มในมหาวิทยาลัย  |
| วันที่ตรวจเอกสาร | 2026-10-23 |
| วันที่ทำ simulation ตามบันทึก | 2026-08-02 |

## 2. ชิ้นงานและสถานะ

| ชิ้นงาน | ไฟล์ | ผู้รับผิดชอบ / ที่มา | สถานะ |
|---|---|---|---|
| AI Conversation Excerpt | [`evidence/week-04/ai-conversation-excerpt.md`](../evidence/week-04/ai-conversation-excerpt.md) | จิรายุ วงศ์ต่อม และศักดิ์ณรงค์ นำนนท์  | Completed |
| Requirement Candidates | [`docs/04-requirement-candidates.md`](../docs/04-requirement-candidates.md) | ศักดิ์ณรงค์ นำนนท์   | Completed |
| Simulation Log | [`evidence/week-04/ai-stakeholder-simulation-log.md`](../evidence/week-04/ai-stakeholder-simulation-log.md) | สรุปจาก E-01 ถึง E-08 | Completed |
| Evidence / Conflict | [`docs/04-evidence-log.md`](../docs/04-evidence-log.md) | ทีม |Completed |
| Negotiation Record เพิ่มเติม | [`evidence/week-04/04-negotiation-record.md`](../evidence/week-04/04-negotiation-record.md) | บันทึกวงซ้อมจำลอง | Completed |
| Risk / Issue Log | [`project-management/risk-and-issue-log.md`](../project-management/risk-and-issue-log.md) | ทีม | Completed |
| Decision Log | [`project-management/decision-log.md`](../project-management/decision-log.md) | ทีม | Completed |
| Worklog | [`project-management/team-worklog.md`](../project-management/team-worklog.md) | ทีม | Completed |
| AI Use Log | [`project-management/ai-use-log.md`](../project-management/ai-use-log.md) | ทีม | Completed |

## 3. จำนวนและการตรวจคุณภาพ

| รายการ | ผล |
|---|---|
| จำนวนบทบาท / sessions | 3 — พนักงานร้าน (S-01), เจ้าของร้าน (S-02), ลูกค้า (S-03); เป็นบทบาทจำลองด้วย AI |
| จำนวน E-ID | 8 — E-01 ถึง E-08 |
| Conflict ใน Evidence Log หลัก | 1 — C-01 เรื่องเงื่อนไขการยกเลิก; Option C มีสถานะ Provisional |
| Requirement candidates | 5 — RC-01 ถึง RC-05 |

- [x] แยก session ตามบทบาทใน simulation log; ผลทั้งหมดเป็นข้อมูลจำลอง ไม่ใช่การสัมภาษณ์คนจริง
- [x] Evidence Log ระบุแหล่งที่มา tag บริบท ระดับความเชื่อมั่น และผู้รับผิดชอบติดตามครบทุก E-ID
- [x] C-01 ระบุคู่ขัดแย้ง อำนาจตัดสินใจ ความต้องการ ทางเลือก และเหตุผลของสถานะชั่วคราว
- [x] RC-01 ถึง RC-05 อ้าง E-ID และระบุว่ายังไม่ใช่ข้อกำหนดที่ผู้ใช้จริงอนุมัติ
- [x] ไม่พบข้อมูลส่วนบุคคล; บันทึกการใช้ AI และการเทียบสรุปกับ Evidence Log แล้ว แต่ยังไม่มีการยืนยันจาก stakeholder จริง

## 4. บทบาทและหลักฐานการมีส่วนร่วม

บันทึก session ระบุว่าจิรายุและศักดิ์ณรงค์ร่วมเป็นผู้สัมภาษณ์ใน simulation ทั้งสาม session ส่วนการแก้ไฟล์รายคนและเวลาที่ใช้ยังยืนยันไม่ได้ เพราะไม่มีรายการ Week 04 ใน Team Worklog หรือ commit แยกผู้ทำ

| สมาชิก | งานที่มีหลักฐานรองรับ | หลักฐาน |
|---|---|---|
| จิรายุ วงศ์ต่อม | ร่วมดำเนิน simulation ในบทบาทผู้สัมภาษณ์; เป็น Team Coordinator ตาม TEAM.md | [`simulation log`](../evidence/week-04/ai-stakeholder-simulation-log.md); ยังไม่มี worklog หรือ commit ที่ระบุงานรายบุคคล |
| ศักดิ์ณรงค์ นำนนท์ | ร่วมดำเนิน simulation ในบทบาทผู้สัมภาษณ์; เป็น Requirements Lead ตาม TEAM.md | [`simulation log`](../evidence/week-04/ai-stakeholder-simulation-log.md); ยังไม่มี worklog หรือ commit ที่ระบุงานรายบุคคล |

## 5. สรุปผลวงซ้อมและสิ่งที่ต้องตามต่อ

- **หลักฐานสำคัญ:** E-01 ถึง E-04 สะท้อนปัญหางานหลายหน้าที่ การจัดคิว และออเดอร์ค้าง; E-06 และ E-07 สะท้อนสิ่งที่ลูกค้าจำลองอยากเห็นก่อนสั่งและระหว่างรอ
- **ข้อขัดแย้ง:** C-01 ระหว่างความต้องการยกเลิกของลูกค้าจำลอง (E-08) กับการป้องกันต้นทุนของร้าน (E-05)
- **ทางเลือกที่บันทึก:** เสนอให้ยกเลิกได้ก่อนร้านเริ่มทำ และปิดปุ่มเมื่อสถานะเป็น “กำลังทำ” (Option C); ยังต้องให้เจ้าของร้านจริงยืนยัน
- **Candidates:** สร้าง RC-01 ถึง RC-05 จาก E-01 ถึง E-08 โดยยังคงสถานะ Candidate/Provisional
- **ประเด็นค้าง:** `docs/04-requirement-candidates.md` ระบุว่า RC-05 คือการแจ้งเมนูหมด แต่ Week 05 Backlog อ้าง RC-05/E-02 ให้ FR-05 ซึ่งพูดถึงการแสดงสถานะออเดอร์ภายใน 3 วินาที ต้องปรับข้อความหรือ traceability ให้ตรงกันก่อนยืนยัน
- **ความสอดคล้องของบันทึก:** ในไฟล์เจรจาเพิ่มเติม N-01 อ้าง candidate คนละหมายเลขกับ C-01 ใน Evidence Log หลัก และ N-02 ยังไม่มีรายการคู่กันใน Evidence Log หลัก ควรจัดหมายเลขให้ตรงกันก่อนใช้เป็นหลักฐานชุดเดียว
- **ช่องว่างตาม contract:** contract กล่าวถึงบทบาท Technical/Privacy/Safety แต่บันทึกที่มีแสดงเพียงพนักงาน เจ้าของร้าน และลูกค้า; ควรเก็บ session หรือระบุขอบเขตที่ทำได้ตามจริง
- **การยืนยันภายนอก:** ยังต้องตรวจขั้นตอนจัดคิว เวลารอ จุดตัดการยกเลิก และการจัดการเมนูหมดกับพนักงาน เจ้าของร้าน และลูกค้าจริง

## 6. สรุปการส่ง

| รายการ | ข้อมูล |
|---|---|
| Commit message สำหรับส่ง | `submit(w04): stakeholder evidence negotiation and candidates` |
| Commit hash / เวลา | 57ce51f |
| ข้อจำกัด / คำถามที่ยังเปิดอยู่ | Evidence ทั้งหมดมาจาก AI simulation; excerpt ไม่มี prompt/transcript ต้นฉบับ; ยังไม่มี worklog และ decision/risk รายการ Week 04; ต้องตรวจช่องว่างของบทบาทและแก้ RC-05/FR-05 กับ mapping ใน negotiation record |
