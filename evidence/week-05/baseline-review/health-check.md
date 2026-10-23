# Artefact Health Check — W01–W05

> สรุปจาก evidence/week-05/artefact-health-check.md, docs/08-validation-traceability.md และ worklog ของวันที่ 18/08/2569

| Artefact                               | Path                                                       | สถานะ | สิ่งที่พบ                                                                                   | การแก้ไขที่มีบันทึก |
| -------------------------------------- | ---------------------------------------------------------- | ---------- | ---------------------------------------------------------------------------------------------------- | -------------------------------------- |
| Problem Brief                          | docs/01-problem-brief-v0.1.md                              | ครบ     | มีเป้าหมาย ปัญหา ผู้มีส่วนได้ส่วนเสีย และ NFR เริ่มต้น | -                                      |
| Stakeholder · Context · Scope        | docs/02-stakeholder-context-scope.md                       | ครบ     | ระบุผู้เกี่ยวข้อง ขอบเขต ข้อจำกัด และแผนภาพแล้ว          | -                                      |
| Elicitation Plan · Interview Guide    | docs/03-elicitation-plan.md, docs/03-interview-guide.md    | ครบ     | มี EO และคำถาม 12 ข้อ พร้อม bias check                                             | -                                      |
| Evidence Log · Requirement Candidates | docs/04-evidence-log.md, docs/04-requirement-candidates.md | ครบ     | มี E-ID, conflict และ candidate เชื่อมโยงกัน; candidate ยังมาจาก simulation | -                                      |
| Requirement Backlog                    | docs/05-requirement-backlog.md                             | -          | -                                                                                                    | -                                      |

## สิ่งที่ส่งต่อ

- ตรวจว่าไฟล์ Backlog ที่ใช้กับ baseline-v1.0 มี Acceptance Measure ครบทุกข้อ
- ตรวจว่าเนื้อหาใน Backlog ตรงกับ CR-05-01, CR-05-02 และ DEC-05-01
- คง NFR-CFQP-01 เป็น Conditional Baseline ตาม docs/08 จนกว่าจะมีหลักฐานจากผู้ใช้จริง
