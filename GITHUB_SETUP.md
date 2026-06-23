# เริ่มต้น Git / GitHub สำหรับ Repository กลุ่ม

## 1. สร้าง repository ของกลุ่ม

1. ใช้ repository นี้เป็น template หรือดาวน์โหลด/คัดลอกแล้วสร้าง repository ใหม่
2. ชื่อ repository: `ENGSE206-GroupXX-ProjectName`
3. ตั้งค่า visibility ตามที่อาจารย์กำหนด (Private หรือ Public)
4. เพิ่มอาจารย์/ผู้ช่วยสอนและสมาชิกทุกคนเป็น collaborator
5. คัดลอก URL repository ลงใน `TEAM.md`

## 2. Clone ลงเครื่อง

### macOS (iMac M1 / MacBook)

เปิด **Terminal** แล้วใช้คำสั่ง

```bash
git clone <REPOSITORY_URL>
cd ENGSE206-GroupXX-ProjectName
```

### Windows notebook

ใช้ **Git Bash** หรือ PowerShell ที่ติดตั้ง Git แล้ว

```bash
git clone <REPOSITORY_URL>
cd ENGSE206-GroupXX-ProjectName
```

> แก้ไขไฟล์ Markdown ได้ด้วย VS Code, Typora, Obsidian, GitHub Web Editor หรือโปรแกรม text editor ที่เหมาะสม

## 3. รูปแบบทำงานประจำสัปดาห์

```bash
git pull origin main
# แก้ไขไฟล์ตาม weekly checklist
git status
git add .
git commit -m "docs: complete week 01 problem brief"
git push origin main
```

## 4. ทางเลือก: ใช้ branch สำหรับงานขนาดใหญ่

```bash
git checkout -b docs/week-07-srs
# ทำงาน
git add .
git commit -m "docs: draft SRS v1"
git push -u origin docs/week-07-srs
```

จากนั้นเปิด Pull Request ให้เพื่อนหรืออาจารย์ review ตามที่ผู้สอนกำหนด

## 5. แนวทางแก้ปัญหาพื้นฐาน

- ก่อนแก้ไฟล์เสมอ ให้ `git pull origin main`
- หากแก้ไฟล์เดียวกันพร้อมกัน ให้ตกลงกันก่อนหรือแบ่ง section ที่ชัดเจน
- หากเกิด merge conflict อย่าลบงานเพื่อน ให้แจ้งสมาชิกที่เกี่ยวข้องและแก้อย่างเป็นระบบ
- อย่า commit รหัสผ่าน token หรือข้อมูลส่วนบุคคล
- หากยังไม่ถนัดคำสั่ง Git สามารถแก้ไฟล์บน GitHub Web Editor ได้ แต่ต้องเขียน commit message ที่สื่อความหมาย
