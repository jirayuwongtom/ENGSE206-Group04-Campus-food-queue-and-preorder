# คู่มือนักศึกษา: อ่านจาก Course Repo และส่งใน Team Repo

## 1. Repository ที่ต้องเปิดสองแท็บ

- Course/Lab Repo (โจทย์ · contract · rubric · ตัวอย่าง CRBS): https://github.com/se-rmutl/engse206-lab
- Team Repo: repository ของกลุ่มที่สร้างจาก https://github.com/se-rmutl/engse206-project-template

## 2. ก่อนเริ่ม

1. กด **Use this template** สร้าง Team Repo ชื่อ `ENGSE206-GroupXX-ProjectName`
2. เพิ่มสมาชิกทุกคนและอาจารย์เป็น collaborator
3. กรอก `TEAM.md` (ชื่อ + GitHub username — **ไม่ใส่รหัสนักศึกษา**), `CASE_CARD.md`, `COURSE_REPOSITORY.md`
4. ทุกคน commit ด้วยบัญชีของตัวเอง — commit คือหลักฐานการมีส่วนร่วม

## 3. ทุกสัปดาห์

1. อ่าน `assignment-contract.md` ของสัปดาห์ — path และข้อความ commit สรุปไว้ใน [COURSE_ALIGNMENT.md](COURSE_ALIGNMENT.md)
2. ทำงานใน path ตาม contract · diagram เก็บ `.drawio` + `.png`
3. ใช้ AI ช่วยได้ แต่บันทึกทุกครั้งใน `project-management/ai-use-log.md`
4. ใช้ตัวอย่าง CRBS เป็นแบบ — **ห้ามคัดลอกข้อความ**
5. ตรวจตัวเอง `python3 scripts/check-project-structure.py --week N`
6. ส่งตาม [submissions/README.md](submissions/README.md): ใบส่งงาน → commit `submit(wNN)` → อัปเดต [submission register](submissions/submission-register.md)

## 4. Definition of Done

- [ ] ไฟล์อยู่ใน path ตาม contract และไม่มี placeholder ค้าง
- [ ] ทุก requirement อ้าง evidence (E-ID) ได้ · ไม่มีตัวเลขหรือนโยบายที่แต่งขึ้น (ใช้ TBD + Open Issue)
- [ ] diagram มี `.drawio` ที่เปิดได้จริงและ `.png`
- [ ] ไม่มี merge conflict ค้าง
- [ ] worklog และ peer score — แต่ละคนกรอกส่วนของตัวเอง
- [ ] peer feedback ระบุกลุ่มผู้ตรวจจริง (Case No.)
- [ ] ใบส่งงานมี commit hash · register อัปเดตแล้ว

## 5. แก้หลังส่ง

ไม่แก้ commit เดิม — สร้าง commit ใหม่ เช่น `fix(w04): revise conflict record after instructor feedback` แล้วใส่ทั้ง commit เดิมและ commit ฉบับแก้ใน register (สถานะ `แก้หลังกำหนด`)
