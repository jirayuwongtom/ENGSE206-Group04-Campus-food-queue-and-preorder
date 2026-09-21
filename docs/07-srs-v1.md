# Campus Food Queue and Preorder — Software Requirements Specification Draft v1

## 0. Document Control

| Field | Value |
|---|---|
| Case ID | `CASE-04` |
| Document ID | `CASE-04-SRS-W07-v1` |
| Version | `0.1-draft` |
| Status | Draft / Baseline Candidate |
| Team/Owner | `Group04` |
| W05 source snapshot | `05-requirement-backlog.md` |
| W06 source snapshot | `06-requirement-models.md` |

## 1. Introduction

### 1.1 Purpose

เอกสารฉบับนี้สรุปข้อกำหนดระบบ **Campus Food Queue and Preorder** (ระบบคิวและสั่งอาหารล่วงหน้า) โดยเชื่อมโยงปัญหาจริงจากผู้ใช้เข้ากับแบบจำลองพฤติกรรมของระบบ ได้แก่ User Story (ประโยคอธิบายความต้องการของผู้ใช้ในมุมมองของคุณค่า), Use Case (แบบจำลองการโต้ตอบระหว่างผู้ใช้กับระบบ) และ Acceptance Criteria (เกณฑ์การยอมรับเพื่อตรวจรับงาน) เพื่อให้ทีมพัฒนา นักทดสอบ และผู้เกี่ยวข้องเข้าใจตรงกัน โดยไม่ผูกติดกับเทคโนโลยีเฉพาะในชั้นการออกแบบ

### 1.2 Problem and Goals

| Goal | Desired outcome | Source | Status |
|---|---|---|---|
| `G-01` | แสดงหมายเลขคิวและสถานะอาหารชัดเจน เพื่อลดการยืนรอแออัดหน้าร้าน | ``01-problem-brief-v0.1.md` (Section 6), `PP-01`` | Fact (ข้อเท็จจริงจากพื้นที่) |
| `G-01` | ช่วยให้พนักงานร้านค้าจัดการคำสั่งซื้อได้ดีขึ้น และลดความผิดพลาดในการสื่อสาร | ``01-problem-brief-v0.1.md` (Section 6), `PP-02`` | Fact (ข้อเท็จจริงจากพื้นที่) |
| `G-01` | แสดงรายการคิวเรียงตามลำดับที่เข้าใจง่าย เพื่อให้พนักงานจัดลำดับงานทำอาหารได้ถูกต้องง | ``01-problem-brief-v0.1.md` (Section 6), `PP-03`` | Fact (ข้อเท็จจริงจากพื้นที่) |

### 1.3 Product Scope 

| In Scope | Out of Scope / Extension | Reason/source |
|---|---|---|
| การตรวจสอบคิวปัจจุบันและสถานะอาหารฝั่งลูกค้า (`FR-01`) | **ISSUE-01**: ระบบชำระเงินออนไลน์ (Payment Gateway) | ตัดออกนอกขอบเขตตามคำแนะนำ เพื่อเน้นกระบวนการจัดการคิว (`02-stakeholder-context-scope.md` Section 6) |
| หน้าจอควบคุมคิวเรียงลำดับ FIFO ฝั่งพนักงาน (`FR-04`) | **ISSUE-02**: ระบบแทรกคิวอัตโนมัติตามประเภทเมนู | Hold ไว้ เนื่องจากขาดกฎเกณฑ์ความยุติธรรมที่แน่ชัดจากร้านค้า (`05-open-questions-and-issues.md`) |
| การยกเลิกคำสั่งซื้อของลูกค้าภายใต้กฎ Cut-off (`FR-03`, `BR-01`) | ระบบจัดส่งอาหาร (Food Delivery Platform) | ไม่รวมบริการจัดส่งนอกพื้นที่โรงอาหาร (`01-problem-brief-v0.1.md` Section 7) |
| รายงานสถิติความหนาแน่นของคิวสำหรับผู้ดูแลพื้นที่ (`FR-06`) | การเก็บข้อมูลสุขภาพละเอียด เช่น ประวัติแพ้อาหาร | ยกเว้นตามหลักการลดการจัดเก็บข้อมูลที่ไม่จำเป็น (Data Minimization) (`02-stakeholder-context-scope.md` Section 5) |


### 1.4 Definitions

| Term | Meaning | Source/Decision |
|---|---|---|
|SRS|เอกสารข้อกำหนดความต้องการซอฟต์แวร์ (Software Requirements Specification)|IEEE 830 / Course Standard|
| FIFO (First-In, First-Out) | หลักการจัดลำดับงานแบบมาคิวแรกได้ทำก่อน ตามลำดับเวลาที่ได้รับจริง | `05-requirement-backlog.md` |
|Cut-off Time / Rule|จุดตัดเวลาหรือสถานะเงื่อนไขที่ระบบจะไม่ยินยอมให้แก้ไขหรือยกเลิกข้อมูล (ใช้ในการล็อกปุ่มยกเลิกคำสั่งซื้อ)|`04-evidence-log.md` (`C-01`)|
|TBD|ประเด็นที่รอการติดตามข้อมูลเพิ่มเติม (To Be Determined)|-|


## 2. Overall Description

### 2.1 Product Context

`[system boundary, system of record และ external systems โดยไม่เลือก technology]`

### 2.2 User Classes and Authority

| Actor | Goal | Authorized actions | Restrictions | Source |
|---|---|---|---|---|
| นักศึกษา / ลูกค้า| สั่งอาหาร ติดตามคิว รู้สถานะอาหาร | เปิดดูคิว, สั่งซื้อ, กดยกเลิกออเดอร์ (ก่อนเริ่มทำ) | ห้ามยกเลิกเมื่อสถานะเปลี่ยนเป็นกำลังทำ | `[source]` |
| พนักงานร้าน| จัดลำดับคิวและปรุงอาหารตามสั่ง | ดูตารางคิว FIFO(เข้าก่อน ออกก่อน), กดเปลี่ยนสถานะออเดอร์หน้าเตา | กดเปลี่ยนสถานะได้เฉพาะออเดอร์ในร้านตนเอง | `[source]` |
| เจ้าของร้าน| ควบคุมนโยบายและป้องกันวัตถุดิบเสียหาย | กำหนดนโยบาย Cut-off time(กำหนดเวลาในแต่ละวัน), กำกับดูแลภาพรวมร้าน | ปรับแก้เฉพาะข้อมูลร้านและกฎการยกเลิก | `[source]` |
| ผู้ดูแลพื้นที่อาหาร| บริหารจัดการลดความแออัด | เรียกดูรายงานสถิติปริมาณคิวและความหนาแน่นรายชั่วโมง | เข้าถึงเฉพาะข้อมูลสถิติสรุปรวม ไม่เห็นข้อมูลส่วนตัวลูกค้า | `[source]` |

### 2.3 Capabilities

| CAP | Capability | FR/BR/NFR/DR | US/UC/AC | Coverage |
|---|---|---|---|---|
| CAP-01 |การติดตามสถานะคิวและคำสั่งซื้อแบบเรียลไทม์ | FR-01 | US-01, UC-01, AC-01 | Detailed / Partial |
| CAP-02 |การจัดการคิวงานครัวแบบ FIFO (เข้าก่อน ออกก่อน) | FR-04, NFR-03 | US-02–US-04, US-06, US-08, UC-02, AC-02, AC-04 | Detailed / Partial |
| CAP-03 |การยกเลิกคำสั่งซื้อและการบังคับใช้เวลาตัดรอบ | FR-03, BR-01 | US-10, US-11, UC-04, AC-05 | Detailed / Partial |
| CAP-04 |การวิเคราะห์ความหนาแน่นของและข้อมูลเชิงพื้นที่ | `[IDs]` | `[IDs]` | Detailed / Partial |
| CAP-05 |การประมาณเวลารอและแจ้งสถานะสินค้าในเมนู | `[IDs]` | `[IDs]` | Detailed / Partial |


### 2.4 Constraints and Assumptions

| ID | Type | Statement | Source | Status/next action |
|---|---|---|---|---|
| CT-01 | Constraint | พนักงานร้านต้องกดเปลี่ยนสถานะออเดอร์ได้สำเร็จด้วยการคลิก/สัมผัสไม่เกิน 2 ครั้ง | `[source]` | `[status]` |
| CT-02 | Constraint | ระบบไม่จัดเก็บข้อมูลส่วนบุคคลเชิงลึก เช่น ประวัติการแพ้อาหาร หรือข้อมูลการเงิน | `[source]` | `[status]` |
| AS-01 | Assumption | ร้านค้ามีอุปกรณ์แท็บเล็ตหรือสมาร์ตโฟนเชื่อมต่ออินเทอร์เน็ตประจำหน้าเตา | `[source]` | `[status]` |
| AS-02 |  Assumption | ลูกค้าใช้ระบบผ่านสมาร์ตโฟนเชื่อมต่อเครือข่ายอินเทอร์เน็ตของมหาวิทยาลัย | `[source]` | `[status]` |

### 2.5 External Interfaces

| ID | System | Data/direction | Core/Extension | TBD/failure concern |
|---|---|---|---|---|
| `[EXT-xx]` | `[name]` | `[exchange]` | `[scope]` | `[unknown]` |

## 3. Functional Requirements

จัดกลุ่มตาม capability/workflow ทุก W05 FR ต้องมี disposition

| FR | Requirement | Source | Priority/admission | BR/NFR/DR | US/UC/AC | Status |
|---|---|---|---|---|---|---|
| `FR-01` | ระบบต้องแสดงหมายเลขคิวปัจจุบันและสถานะอาหารบนหน้าจอฝั่งลูกค้า | E-07, PP-01, UN-01 | Must / Core | NFR-01 | US-01, UC-01, AC-01 | Ready / Covered |
| `FR-04` | ระบบต้องแสดงรายการคิวเรียงลำดับเวลารับออเดอร์ (FIFO) แบ่งกลุ่มสถานะฝั่งพนักงาน | E-01, E-03, E-04, UN-02 | Must / Core | NFR-03 | US-02, US-03, US-04, US-06, UC-02, AC-02 | Ready / Covered |
| `FR-03` | ระบบต้องให้ลูกค้ายกเลิกคำสั่งซื้อผ่านระบบได้ด้วยตนเอง | UN-03, E-08 | Should / Core | BR-01 | US-10, UC-04, AC-05 | Ready / Covered |
| `FR-06` | ระบบต้องแสดงผลรายงานสถิติความหนาแน่นคิวรายช่วงเวลาให้ผู้ดูแลพื้นที่ | 02: Data Flow | Could / Supporting | - | US-05, US-07, UC-03, AC-03 | Ready / Covered |
| `FR-02` | ระบบต้องแสดงจำนวนคิวรอและประเมินเวลารอก่อนยืนยันสั่งซื้อ | E-06, E-08, UN-01 | Must / Deferred | ST-04 | (Unmodeled) | Needs Follow-up / TBD |
| `FR-05` | ระบบต้องอัปเดตสถานะเมนูหมดฝั่งลูกค้าภายใน 3 วินาที | E-02, UN-04 | Should / Deferred | NFR-01 | (Unmodeled) | Needs Follow-up / TBD |

### Detailed Requirement Record

| Field | Value |
|---|---|
| Requirement ID | `[FR-xx]` |
| Statement | `ระบบต้อง…` |
| Rationale/Goal | `[G-xx/why]` |
| Source | `[F/E/TD]` |
| Priority/Admission | `[Must/Should/Could] / [Core/Supporting/Extension]` |
| Trigger | `[observable event]` |
| Preconditions/guards | `[state/rule]` |
| Expected result | `[state/data/event]` |
| BR/NFR/DR links | `[IDs]` |
| US/UC/AC links | `[IDs]` |
| Verification | `[method + scenario]` |
| Status/TBD | `[status + gap/evidence need]` |

## 4. Business Rules

| BR | Rule | Authority/source | Affected FR/UC | Status |
|---|---|---|---|---|
| `[BR-xx]` | `[rule]` | `[TD/source]` | `[IDs]` | Confirmed for case / TBD |

## 5. Non-functional Requirements

| NFR | Quality statement | Context/stimulus | Response/measure | Source | Verification | Status/TBD |
|---|---|---|---|---|---|---|
| `[NFR-xx]` | `ระบบต้อง…` | `[context]` | `[measure or TBD]` | `[source]` | `[method]` | `[status]` |

## 6. Data Requirements

ส่วนนี้เป็น conceptual data requirement ยังไม่ใช่ physical database schema

| DR | Concept | Requirement/minimum data | Relationships | Classification | Source | Status |
|---|---|---|---|---|---|---|
| `[DR-xx]` | `[concept]` | `[meaning + minimum data]` | `[concept links]` | `[class]` | `[IDs]` | Ready / TBD |

## 7. Behavioral Model References

| Model | IDs/version | Requirement anchors | Coverage/gap | SRS use |
|---|---|---|---|---|
| User Stories | `[US-*]` | `[W05 IDs]` | `[coverage]` | `[section]` |
| Use Cases | `[UC-*]` | `[W05 IDs]` | `[level/gap]` | `[section]` |
| Acceptance Criteria | `[AC-*]` | `[W05 IDs]` | `[coverage]` | `[verification]` |

### 7.1 Lifecycle Rules

| From | Trigger | To | Guard/result | Source |
|---|---|---|---|---|
| `[state]` | `[event]` | `[state]` | `[guard]` | `[ID]` |

## 8. External Interface Requirements

| Interface | Requirement/data | Direction | Owner | Failure/privacy concern | Status |
|---|---|---|---|---|---|
| `[EXT-xx]` | `[what]` | `[in/out]` | `[owner]` | `[concern]` | Core / Extension / TBD |

## 9. Traceability and Coverage

| Source | W05 requirement | W06 model | SRS section | Verification | Coverage |
|---|---|---|---|---|---|
| `[F/E/TD]` | `[FR/BR/NFR/DR]` | `[US/UC/AC]` | `[หัวข้อ ]` | `[VF/method]` | Covered / Partial |

## 10. Open Issues

| OI | Question/TBD | Affected IDs | Owner | Next action | Expected evidence | Needed by |
|---|---|---|---|---|---|---|
| `[OI-xx]` | `[unknown]` | `[IDs]` | `[role]` | `[action]` | `[evidence]` | `[milestone]` |

## 11. Verification Plan

| VF | Method | Target IDs | Procedure/evidence | Owner | Status |
|---|---|---|---|---|---|
| `[VF-xx]` | Review / Demo / Test / Analysis / Inspection | `[IDs]` | `[how/evidence]` | `[owner]` | Planned |

## 12. Review Gate

- [ ] W05 FR/BR/NFR/DR ทุกข้อมี disposition
- [ ] W06 US/UC/AC ย้อนกลับ W05 ได้
- [ ] Partial/Extension/TBD มองเห็น
- [ ] Open Issue ทุกข้อมี owner/action/evidence
- [ ] Status ยังเป็น Baseline Candidate

## Appendix A — Requirement Disposition

| Backlog ID | Included/Deferred/Extension/Issue | SRS section | Reason |
|---|---|---|---|
| `[ID]` | `[disposition]` | `[หัวข้อ ]` | `[reason]` |

## Appendix B — Review and Revision

| Item | Before | After | Reason/source | Reviewer |
|---|---|---|---|---|
| `[ID/section]` | `[old]` | `[new]` | `[why]` | `[name]` |

## Appendix C — AI Use Disclosure

| Activity | AI assistance | Human verification/change | Evidence |
|---|---|---|---|
| `[task]` | `[what AI did]` | `[accepted/rejected/changed]` | `[path/link]` |
