# Diagrams Workspace

เก็บทั้งไฟล์ต้นฉบับและไฟล์ export เพื่อให้ตรวจสอบและแก้ไขได้ในอนาคต

## โครงสร้าง

| Folder | ใช้เก็บ |
|---|---|
| `context/` | stakeholder map, system context |
| `use-case/` | use case diagram |
| `activity/` | activity/workflow diagrams |
| `domain-model/` | domain model / conceptual class model |
| `architecture/` | conceptual architecture, C4-like views |
| `sequence/` | sequence diagram |
| `erd/` | ERD / logical data model |
| `ui-flow/` | user flow / navigation flow |

## Naming Convention

- Source: `booking-cancellation-flow.drawio`
- Export: `booking-cancellation-flow.png`
- หาก diagram รองรับ version ให้ใส่ version ในไฟล์ export เช่น `system-context-v1.png`

## แนวทางคุณภาพ

- ทุก diagram ต้องมีชื่อ ชุดสัญลักษณ์ที่สม่ำเสมอ และคำอธิบายสั้น ๆ
- ห้ามมี diagram ที่ไม่อ้างอิง requirement หรือ design decision ใดเลย
- ใส่ลิงก์ไปยัง diagram จากเอกสาร `docs/` หรือ `design/`
