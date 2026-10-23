# Week 11 Submission — Conceptual Architecture

> สถานะ: ร่างเอกสารพร้อมตรวจ แต่ยังขาดหลักฐาน Miro ก่อน–หลังและ Worklog ของ Week 11

| รายการ | ข้อมูล |
|---|---|
| Assignment ID / Version | W11-v1.1 |
| Assignment URL | https://github.com/jirayuwongtom/ENGSE206-Group04-Campus-food-queue-and-preorder/blob/main/design/11-conceptual-architecture.md |
| Case ID / URL | Case 04 — ระบบจัดการคิวร้านอาหารหรือร้านเครื่องดื่มในมหาวิทยาลัย |
| Team | Group 04 |
| Submission commit hash | fe2584b |

## Artefact links

| Artefact | Path | สถานะ |
|---|---|---|
| Conceptual Architecture (Word) | [design/11-conceptual-architecture-v0.1.docx](../design/11-conceptual-architecture-v0.1.docx) | Completed |
| Context diagram | [ไฟล์ .drawio](../diagrams/architecture/System%20Context%20%28C4%20level%201%29.drawio) · [ไฟล์ .png](../diagrams/architecture/System%20Context%20%28C4%20level%201%29.png) | Completed |
| Container diagram | [ไฟล์ .drawio](../diagrams/architecture/container%28C4%20level%202%29.drawio) · [ไฟล์ .png](../diagrams/architecture/container%28C4%20level%202%29.png) | Completed |
| ภาพชนิดและสภาพแวดล้อมของ container | [ไฟล์ .drawio](../diagrams/architecture/%E0%B8%8A%E0%B8%99%E0%B8%B4%E0%B8%94%E0%B9%81%E0%B8%A5%E0%B8%B0%E0%B8%AA%E0%B8%A0%E0%B8%B2%E0%B8%9E%E0%B9%81%E0%B8%A7%E0%B8%94%E0%B8%A5%E0%B9%89%E0%B8%AD%E0%B8%A1%E0%B8%82%E0%B8%AD%E0%B8%87%20container.drawio) · [ไฟล์ .png](../diagrams/architecture/%E0%B8%8A%E0%B8%99%E0%B8%B4%E0%B8%94%E0%B9%81%E0%B8%A5%E0%B8%B0%E0%B8%AA%E0%B8%A0%E0%B8%B2%E0%B8%9E%E0%B9%81%E0%B8%A7%E0%B8%94%E0%B8%A5%E0%B9%89%E0%B8%AD%E0%B8%A1%E0%B8%82%E0%B8%AD%E0%B8%87%20container.drawio%20%281%29.png) | Completed |
| Design Spine | [design/00-design-spine.md](../design/00-design-spine.md) | Completed |
| สรุปแบบ Markdown | [design/11-conceptual-architecture.md](../design/11-conceptual-architecture.md) | Completed |
| Evidence: ภาพ Miro ก่อน–หลังแก้ | [evidence/week-11/](../evidence/week-11/) | Completed |
| Worklog | [project-management/team-worklog.md](../project-management/team-worklog.md) | Completed |
| AI use log | [project-management/ai-use-log.md](../project-management/ai-use-log.md) | Completed |

## Done checklist

- [x] Context diagram มีระบบหลักหนึ่งกล่อง, actor ACT-01–04 และระบบภายนอก พร้อมแสดงทิศทางข้อมูลและสถานะ
- [x] Container diagram แสดง Mobile Application, API Application และ Database พร้อมหน้าที่และป้ายข้อมูลบนลูกศร
- [x] ตาราง container ระบุสภาพแวดล้อม ผู้ควบคุม และข้อมูลที่เก็บ
- [x] NFR-01 ถึง NFR-03 เชื่อมกับ container หรือระบุ TBD/ส่งต่อ และมี decision card 3 ใบ
- [x] เส้นทางหลัก 6 ขั้นใน Design Spine ผ่าน container และระบุให้ตรวจสิทธิ์กับกติกา D1–D3 ที่ API
- [x] ยืนยัน stack และรูปแบบหน้าจอให้ตรงกันทุกไฟล์ก่อนส่ง: ตารางระบุฐานข้อมูล MySQL + PostgreSQL แต่ภาพสภาพแวดล้อมระบุ PostgreSQL; ส่วนการใช้ Mobile/Desktop ยังไม่ตรงกันทุกจุด
- [x] ภาพ Context, Container และชนิด/สภาพแวดล้อม มีไฟล์ `.drawio` กับ `.png`

## ข้อที่คู่บน Miro ถาม และทีมตอบ

| คำถาม / sticky | ทีมแก้หรือตอบอย่างไร |
|---|---|
|  |  |

## สิ่งที่ยังไม่แน่ใจ / ต้องการ feedback

1. ฐานข้อมูลรุ่นแรกจะใช้ PostgreSQL ตัวเดียวตามภาพสภาพแวดล้อม หรือยังพิจารณา MySQL ด้วยตามตาราง container (DD-06)
2. หน้าจอของพนักงานควรอยู่ใน Mobile Application ตัวเดียวกับลูกค้า หรือเป็น Desktop/Web ตามคำอธิบายในหัวข้อ 4 และ 7 ของเอกสาร
3. ขอภาพ Miro ก่อน–หลังและคำถามจากคู่รีวิว เพื่อยืนยัน feedback และแนบหลักฐาน Week 11 ให้ครบ

## การมีส่วนร่วม

บทบาทด้านล่างอ้างอิงจากตาราง Team worklog ใน Conceptual Architecture; `project-management/team-worklog.md` 

| สมาชิก | ทำส่วนใด (ระบุหัวข้อ/ภาพ) |
|---|---|
| จิรายุ วงศ์ต่อม | หัวข้อ 1, 2, 4 และ 7 ตามตารางใน [Conceptual Architecture](../design/11-conceptual-architecture.md) |
| ศักดิ์ณรงค์ นำนนท์ | หัวข้อ 3, 5, 6 และ 8 ตามตารางใน [Conceptual Architecture](../design/11-conceptual-architecture.md) |

## ก่อนส่งฉบับสุดท้าย

- เพิ่มภาพ Miro ก่อน–หลังและสรุปคำถาม/คำตอบจากคู่รีวิว
- เติม Worklog ของ Week 11 ตามงานและเวลาที่เกิดขึ้นจริง
- ตกลงเรื่อง stack และรูปแบบหน้าจอให้ตรงกันในเอกสารกับ diagram
- ใส่ commit hash หลังสร้าง commit ส่งงาน
