# ENGSE206 Group Semester Project Repository
## การกำหนดความต้องการและการออกแบบทางซอฟต์แวร์
### Software Requirements Specification and Design

> Repository นี้คือ **พื้นที่ทำงานของกลุ่มนักศึกษา 1 กลุ่มตลอดภาคเรียน** สำหรับรายวิชา ENGSE206
>
> ใช้กรณีศึกษา (Case Project) เดิมตั้งแต่ Week 1 ถึง Week 16 เพื่อสะสมชิ้นงานจาก
> **เข้าใจปัญหา → เก็บความต้องการ → วิเคราะห์และระบุรายละเอียด → เขียน SRS → ออกแบบ → ตรวจสอบ → ปรับปรุง → นำเสนอ**

---

## จุดประสงค์ของ Repository นี้

Repository นี้ช่วยให้กลุ่มทำงานอย่างเป็นระบบ เก็บประวัติการปรับปรุงด้วย Git และเชื่อมโยงชิ้นงานทุกชิ้นตาม flow ของรายวิชา ENGSE206 Course Repository

- ไม่ใช่พื้นที่สำหรับเขียนโปรแกรมให้เสร็จทั้งระบบ
- เป็นพื้นที่เก็บ **เอกสารวิศวกรรมซอฟต์แวร์ แบบจำลอง หลักฐานการเก็บความต้องการ และแบบออกแบบ**
- ทุกคนต้องมีส่วนร่วมผ่าน commit, worklog, peer feedback และชิ้นงานของตน
- หาก requirement หรือ design เปลี่ยน ต้องบันทึกเหตุผลและผลกระทบไว้ในเอกสารที่กำหนด

---

## เริ่มต้นภายใน 20 นาที

1. กด **Use this template** บน GitHub หรือคัดลอกโฟลเดอร์นี้สร้าง repository ใหม่
2. ตั้งชื่อ repository เป็น `ENGSE206-GroupXX-ProjectName`  
   ตัวอย่าง `ENGSE206-Group03-CampusSpaceBooking`
3. เพิ่มอาจารย์ผู้สอน/ผู้ช่วยสอนและสมาชิกกลุ่มเป็น collaborator ตามนโยบายรายวิชา
4. กรอก [TEAM.md](TEAM.md), [CASE_CARD.md](CASE_CARD.md) และ [docs/00-project-profile.md](docs/00-project-profile.md)
5. อ่าน [COURSE_ALIGNMENT.md](COURSE_ALIGNMENT.md) และ [GITHUB_SETUP.md](GITHUB_SETUP.md)
6. เริ่ม Week 1 ที่ [weekly/week-01-problem-brief.md](weekly/week-01-problem-brief.md)

---

## แผนที่ Repository

```text
ENGSE206-GroupXX-ProjectName/
├── README.md                         # หน้าแรกของโครงงาน
├── TEAM.md                           # สมาชิก บทบาท และช่องทางติดต่อ
├── CASE_CARD.md                      # โจทย์ที่อาจารย์มอบหมาย ใช้ตลอดเทอม
├── COURSE_ALIGNMENT.md               # แผนที่เชื่อมกับ ENGSE206 Course Repository
├── GITHUB_SETUP.md                   # วิธีเริ่ม Git/GitHub บน macOS และ Windows
├── CONTRIBUTING.md                   # กติกาการทำงานร่วมกันและ commit
├── docs/                             # Requirements / SRS / Traceability
├── diagrams/                         # Source diagram + exported image/PDF
├── design/                           # Architecture / UX/UI / Detailed Design
├── project-management/               # Worklog, meetings, decisions, risks
├── evidence/                         # หลักฐาน Workshop, interview, review, test
├── weekly/                           # Checklist รายสัปดาห์และทางลัดไปชิ้นงาน
├── feedback/                         # Reflection และ peer feedback
├── final/                            # ไฟล์ส่งปลายภาค / presentation / exports
└── assets/                           # รูปภาพ ไอคอน wireframe exports ที่อ้างอิงในเอกสาร
```

> **หลักการสำคัญ:** เอกสารหลักอยู่ที่ `docs/` และ `design/` เพียงชุดเดียวตลอดเทอม  
> `weekly/` เป็น checklist และลิงก์ ไม่สร้างเอกสารซ้ำรายสัปดาห์

---

## Roadmap ตลอดภาคเรียน

| ช่วง | งานหลัก | ไฟล์/โฟลเดอร์ที่ต้องเติม |
|---|---|---|
| Week 1–2 | เข้าใจปัญหา กำหนด stakeholder และ scope | `docs/01-*`, `docs/02-*`, `project-management/team-worklog.md` |
| Week 3–4 | วางแผนเก็บข้อมูล ทำ interview/simulation และเก็บหลักฐาน | `docs/03-*`, `docs/04-*`, `evidence/week-03/`, `evidence/week-04/` |
| Week 5–8 | วิเคราะห์ จัดลำดับ ทำ model เขียน SRS ตรวจสอบ/traceability | `docs/05-*` ถึง `docs/08-*`, `diagrams/` |
| Week 10–15 | ออกแบบ strategy, architecture, UX/UI, detailed design และ review | `design/10-*` ถึง `design/14-*`, `evidence/week-15/` |
| Week 16 | สรุป ปรับปรุง นำเสนอและ reflection | `final/`, `feedback/15-individual-reflection.md` |

ดูรายละเอียดรายสัปดาห์ที่ [weekly/README.md](weekly/README.md)

---

## กติกาไฟล์และหลักฐาน

- ใช้ไฟล์เอกสารหลักเป็น Markdown (`.md`) เพื่อให้เห็น revision history ชัดเจน
- เก็บไฟล์ diagram ต้นฉบับ เช่น `.drawio`, `.fig`, `.mmd` ในโฟลเดอร์ย่อยของ `diagrams/`
- ส่งออก diagram เป็น `.png` หรือ `.pdf` สำหรับแสดงในเอกสารและนำเสนอ
- หลีกเลี่ยงการใส่ข้อมูลส่วนบุคคลจริง รหัสผ่าน ภาพบุคคล หรือข้อมูลอ่อนไหวลงใน repository
- ตั้งชื่อไฟล์เป็นภาษาอังกฤษแบบ `lowercase-kebab-case`; ใช้เลขนำหน้าเมื่อเป็น artefact ตามลำดับรายวิชา
- เขียน commit ให้สื่อความหมาย เช่น `docs: add FR-03 booking cancellation rule`

ดูรายละเอียดที่ [CONTRIBUTING.md](CONTRIBUTING.md) และ [docs/README.md](docs/README.md)

---

## Definition of Done สำหรับงานประจำสัปดาห์

ก่อนส่งงานแต่ละสัปดาห์ กลุ่มควรตรวจว่า

- [ ] เอกสารตาม weekly checklist ถูกเติมครบและลบข้อความ placeholder ที่ไม่ใช้แล้ว
- [ ] มีหลักฐาน/ภาพ/บันทึกประกอบเมื่อกิจกรรมกำหนดให้มี
- [ ] สมาชิกแต่ละคนบันทึกบทบาทใน worklog
- [ ] มีการตรวจทานในกลุ่มอย่างน้อย 1 รอบ
- [ ] commit และ push ขึ้น remote repository แล้ว
- [ ] ตั้ง tag หรือทำ release ตามที่อาจารย์กำหนดเมื่อเป็น milestone สำคัญ

---

## ลิงก์สำคัญใน Repository นี้

- [ข้อมูลโครงงานและสมาชิก](docs/00-project-profile.md)
- [Problem Brief v0.1](docs/01-problem-brief-v0.1.md)
- [Requirements Backlog](docs/05-requirement-backlog.md)
- [SRS v1](docs/07-srs-v1.md)
- [Traceability และ Change Management](docs/08-validation-traceability.md)
- [Design Strategy](design/10-design-strategy.md)
- [Conceptual Architecture](design/11-conceptual-architecture.md)
- [UX/UI Prototype](design/12-ux-ui-prototype.md)
- [Detailed Design](design/13-detailed-design.md)
- [Final Submission Guide](final/README.md)
