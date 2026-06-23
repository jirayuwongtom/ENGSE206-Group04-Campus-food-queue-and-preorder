# กติกาการทำงานร่วมกัน (Contributing Guide)

## 1. ก่อนเริ่มแก้ไข

- เปิด weekly checklist ของสัปดาห์นั้น
- อ่าน artefact ที่มีอยู่แล้วก่อนแก้ไข
- ระบุใน `project-management/team-worklog.md` ว่ารับผิดชอบส่วนใด
- ดึงงานล่าสุดด้วย `git pull origin main`

## 2. การตั้งชื่อไฟล์และโฟลเดอร์

- ใช้ภาษาอังกฤษตัวพิมพ์เล็กและขีดกลาง เช่น `stakeholder-map.drawio`
- หลีกเลี่ยงชื่อคลุมเครือ เช่น `new-final-final2.md`
- ไฟล์ diagram ต้องเก็บทั้ง **source file** และ **exported image/PDF** เมื่อใช้ในรายงาน

## 3. Commit message

ใช้รูปแบบ `type: message` เช่น

| type | ใช้เมื่อ | ตัวอย่าง |
|---|---|---|
| `docs` | เพิ่ม/แก้เอกสาร | `docs: add FR-06 notification preference` |
| `diagram` | เพิ่ม/แก้ diagram | `diagram: add booking activity flow` |
| `design` | เพิ่ม/แก้แบบออกแบบ | `design: revise layered architecture rationale` |
| `evidence` | เพิ่มหลักฐาน workshop/test | `evidence: add week 15 usability notes` |
| `chore` | จัดโครงสร้าง/แก้ไฟล์ทั่วไป | `chore: organize evidence folders` |

หลีกเลี่ยงคำว่า `update`, `fix`, `งานใหม่` โดยไม่อธิบายสิ่งที่เปลี่ยน

## 4. การตรวจทานก่อน merge/submit

- ตรวจเนื้อหาให้สอดคล้องกับ case card และ requirement ที่ตกลงกัน
- ตรวจว่า requirement เป็นข้อความตรวจสอบได้ และมี ID เมื่ออยู่ใน backlog/SRS
- ตรวจว่า design ทุกส่วนอ้างอิง requirement ที่เกี่ยวข้องได้
- ตรวจภาษา ชื่อ diagram และลิงก์ภายใน
- ขอให้เพื่อนอย่างน้อย 1 คน review artefact สำคัญ เช่น SRS, Architecture, Design Review

## 5. AI และจริยธรรมวิชาการ

ใช้ AI ช่วย brainstorming, ตรวจภาษา หรือสร้างโครงร่างได้ แต่

1. ต้องตรวจข้อเท็จจริงและตัดสินใจด้วยทีมเอง
2. ห้ามใส่ข้อมูลส่วนบุคคลหรือข้อมูลลับลงในบริการ AI
3. บันทึกการใช้ที่มีผลต่อชิ้นงานใน `project-management/ai-use-log.md`
4. ห้ามนำเนื้อหากลุ่มอื่นมาส่งเป็นของกลุ่มตนเอง
