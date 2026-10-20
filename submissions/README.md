# Weekly Submission Workspace

อาจารย์เริ่มตรวจจาก [submission-register.md](submission-register.md) — หน้าเดียวที่มีลิงก์ไปทุกงาน

## ส่งทุกสัปดาห์ 6 ขั้น

1. อ่าน `assignment-contract.md` ของสัปดาห์ใน [Course Repo](https://github.com/se-rmutl/engse206-lab/tree/main/weeks) — ดู path ที่ต้องส่งและข้อความ commit
2. ทำงานใน path ตาม contract แล้วรัน `python3 scripts/check-project-structure.py --week N`
3. commit + push ชิ้นงาน แล้วคัดลอก commit hash
4. กรอก `week-NN-submission.md` (ใส่ hash จากขั้น 3)
5. commit ด้วยข้อความตาม contract เช่น `submit(w04): evidence and requirement candidates` แล้ว push
6. อัปเดต `submission-register.md` — ลิงก์ permalink (กด `y` บนหน้าไฟล์ใน GitHub) + commit ฉบับส่ง + วันที่ + สถานะ

## หลักการตรวจ

- ผู้สอนตรวจตาม commit ในใบส่งงานและ register — ถ้าว่าง ตรวจตามสภาพ repo ณ วันครบกำหนด
- แก้หลังส่ง = commit ใหม่ ไม่ rewrite history · บันทึกทั้ง commit เดิมและ commit ฉบับแก้ใน register
- W05b ส่ง `baseline-review-submission.md` + tag `baseline-v1.0`
- สอบกลางภาค (งานกลุ่ม) ส่งใน branch กลางภาคตามประกาศ · สอบปลายภาคส่วน ก ส่งใน branch `final-exam`
