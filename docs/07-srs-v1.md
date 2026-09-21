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

ระบบ Campus Food Queue and Preorder เป็นแอปพลิเคชันสารสนเทศอิสระ (Standalone Web/Mobile Application) ที่ทำงานรูปแบบ Client-Server (แยกส่วนฝั่งผู้ใช้และส่วนประมวลผล) เชื่อมโยง 3 ส่วนประสานงานหลัก ได้แก่ แอปพลิเคชันติดตามสถานะฝั่งลูกค้า (Student Web App), แอปพลิเคชันควบคุมคิวฝั่งร้านค้า (Kitchen Control Panel) และแดชบอร์ดบริหารจัดการฝั่งผู้ดูแลพื้นที่ (Admin Analytics Dashboard)
### 2.2 User Classes and Authority

| Actor (บทบาทผู้ใช้) | Goal (เป้าหมายหลัก) | Authorized Actions (การกระทำที่ได้รับสิทธิ์) | Restrictions (ข้อจำกัดสิทธิ์) | Source (แหล่งอ้างอิง) |
| :--- | :--- | :--- | :--- | :--- |
| นักศึกษา / ลูกค้า  | ตรวจสอบคิวและรับอาหารได้ตรงเวลา โดยไม่ต้องยืนรอหน้าร้าน | - สั่งซื้ออาหารและติดตามคิว<br>- ขอยกเลิกออเดอร์ในสถานะ `ออเดอร์ใหม่` | - ห้ามยกเลิกเมื่อออเดอร์เข้าสถานะ `กำลังทำ`<br>- มองเห็นเฉพาะคิวของตนเองและคิวรวม | `02-stakeholder-context-scope.md` (Section 2.1) |
| พนักงานร้านค้า  | ปรุงอาหารตามลำดับคิวและอัปเดตสถานะออเดอร์ได้รวดเร็ว | - เรียกดูคิวตามลำดับ FIFO<br>- กดเปลี่ยนสถานะออเดอร์ (`กำลังทำ`, `พร้อมรับ`) | - ไม่สามารถแก้ไขนโยบายร้านค้าหรือดูรายงานผู้ดูแลพื้นที่ | `02-stakeholder-context-scope.md` (Section 2.1) |
| เจ้าของร้านค้า  | ควบคุมนโยบายร้านค้าและป้องกันความเสียหายของวัตถุดิบ | - กำหนดนโยบายจุดตัดการยกเลิก (Cut-off)<br>- จัดการรายการเมนูอาหาร | - ไม่สามารถแก้ไขสถิติภาพรวมโรงอาหารของผู้ดูแลพื้นที่ | `02-stakeholder-context-scope.md` (Section 2.1) |
| ผู้ดูแลพื้นที่อาหาร  | วิเคราะห์ความหนาแน่นและบริหารจัดการพื้นที่ส่วนกลาง | - เรียกดูรายงานสถิติความหนาแน่นคิวรายช่วงเวลา | - ไม่สามารถแทรกแซงการปรุงอาหารหรือยกเลิกออเดอร์แทนร้านค้า | `02-stakeholder-context-scope.md` (Section 2.1) |

### 2.3 Capabilities

| CAP | Capability | FR / BR / NFR / DR | US / UC / AC | Coverage |
| :--- | :--- | :--- | :--- | :--- |
| **CAP-01** | การติดตามคิวและแจ้งเตือนสถานะฝั่งลูกค้า | `FR-01` | `US-01`, `UC-01`, `AC-01` | **Detailed** |
| **CAP-02** | การจัดลำดับคิว FIFO ฝั่งพนักงานหน้าเตา | `FR-04`, `NFR-03` | `US-02`..`06`, `US-08`, `UC-02`, `AC-02`, `AC-04` | **Detailed** |
| **CAP-03** | การยกเลิกออเดอร์และกฎจุดตัด Cut-off | `FR-03`, `BR-01` | `US-10`, `US-11`, `UC-04`, `AC-05` | **Detailed** |
| **CAP-04** | การรายงานสถิติความหนาแน่นคิวโรงอาหาร | `FR-06` | `US-05`, `US-07`, `UC-03`, `AC-03` | **Detailed** |
| **CAP-05** | การประเมินเวลารอคิวล่วงหน้า | `FR-02` | - | **Partial / TBD** |
| **CAP-06** | การอัปเดตแจ้งเตือนเมนูวัตถุดิบหมด | `FR-05`, `NFR-01` | - | **Partial / TBD** |


### 2.4 Constraints and Assumptions

| ID | Type | Statement | Source | Status / Next Action |
| :--- | :--- | :--- | :--- | :--- |
| **CT-01** | Constraint | หน้าจอฝั่งพนักงานต้องกดเปลี่ยนสถานะได้ในไม่เกิน 2 คลิก/สัมผัส | `01-problem-brief-v0.1.md (Section 9)` | Active constraint |
| **CT-02** | Constraint | ระบบต้องจัดเก็บเฉพาะข้อมูลจำเป็น ไม่เก็บประวัติการแพ้อาหาร | `02-stakeholder-context-scope.md (Section 5)` | Active constraint |
| **AS-01** | Assumption | ร้านค้ามีอุปกรณ์แท็บเล็ต/สมาร์ตโฟนเชื่อมต่ออินเทอร์เน็ตประจำหน้าเตา | `01-problem-brief-v0.1.md (Section 10)` | Verified assumption |
| **AS-02** | Assumption | นักศึกษายินดีใช้ระบบดิจิทัลดูคิวแทนการสอบถามพนักงานหน้าร้าน | `01-problem-brief-v0.1.md (Section 10)` | Verified assumption |

### 2.5 External Interfaces

| ID | System | Data / Direction | Core / Extension | TBD / Failure Concern |
| :--- | :--- | :--- | :--- | :--- |
| **EXT-01** | Web Push Notification Service | สัญญาณแจ้งเตือนเมื่ออาหารพร้อมรับ (Outbound) | Core | การหลุดเชื่อมต่อของสัญญาณอินเทอร์เน็ตมือถือ |
| **EXT-02** | Stall Display Unit | รายการคิวและปุ่มกดเปลี่ยนสถานะหน้าเตา (Bi-directional) | Core | หน้าจอค้างหรือสัมผัสไม่ติดช่วงเร่งด่วน |

## 3. Functional Requirements

จัดกลุ่มตาม capability/workflow ทุก W05 FR ต้องมี disposition

| FR | Requirement | Source | Priority/admission | BR/NFR/DR | US/UC/AC | Status |
|---|---|---|---|---|---|---|
| `FR-01` | ระบบต้องแสดงหมายเลขคิวปัจจุบันและสถานะอาหารบนหน้าจอฝั่งลูกค้า | `RC-01`, `E-07`(`04-evidence-log.md`) | Must / Core | NFR-01 | US-01, UC-01, AC-01 | Ready / Covered |
| `FR-04` | ระบบต้องแสดงรายการคิวเรียงลำดับเวลารับออเดอร์ (FIFO) แบ่งกลุ่มสถานะฝั่งพนักงาน | `RC-04`, `E-01`(`04-evidence-log.md`) | Must / Core | NFR-03 | US-02, US-03, US-04, US-06, UC-02, AC-02 | Ready / Covered |
| `FR-03` | ระบบต้องให้ลูกค้ายกเลิกคำสั่งซื้อผ่านระบบได้ด้วยตนเอง | `RC-03`, `E-08`(`04-evidence-log.md`) | Should / Core | BR-01 | US-10, UC-04, AC-05 | Ready / Covered |
| `FR-06` | ระบบต้องแสดงผลรายงานสถิติความหนาแน่นคิวรายช่วงเวลาให้ผู้ดูแลพื้นที่ | `02: Data Flow` | Could / Supporting | DR-05 | US-05, US-07, UC-03, AC-03 | Ready / Covered |
| `FR-02` | ระบบต้องแสดงจำนวนคิวรอและประเมินเวลารอก่อนยืนยันสั่งซื้อ | `RC-02`, `E-06`(`04-evidence-log.md`) | Must / Deferred | - | (Unmodeled) | Needs Follow-up / TBD |
| `FR-05` | ระบบต้องอัปเดตสถานะเมนูหมดฝั่งลูกค้าภายใน 3 วินาที | `RC-05`, `E-02`(`04-evidence-log.md`) | Should / Deferred | NFR-01 | (Unmodeled) | Needs Follow-up / TBD |

### Detailed Requirement Record

| Field | Value |
|---|---|
| Requirement ID | `FR-01` |
| Statement | ระบบต้องแสดง "หมายเลขคิวปัจจุบัน" และ "สถานะอาหาร" บนหน้าจอฝั่งลูกค้า เพื่อให้ลูกค้าตรวจสอบได้โดยไม่ต้องฟังเสียงเรียก |
| Rationale/Goal | แก้ปัญหาโรงอาหารเสียงดังและลดการยืนรอแออัดหน้าร้าน (`PP-01`, `G-01`) |
| Source | `RC-01`, `E-07`, `PP-01`, `UN-01` |
| Priority/Admission | Must / End-to-End Core |
| Trigger | ลูกค้าเปิดหน้าติดตามคิว หรือ พนักงานกดเปลี่ยนสถานะออเดอร์หน้าเตา |
| Preconditions/guards | ลูกค้าทำรายการสั่งซื้อสำเร็จและมีหมายเลขคิวบันทึกอยู่ในระบบ |
| Expected result | 1. หน้าจอฝั่งลูกค้าแสดงหมายเลขคิว และสถานะการปรุงอาหารล่าสุด (`ออเดอร์ใหม่` -> `กำลังทำ` -> `พร้อมรับ` -> `รับแล้ว`)<br>2. เมื่อสถานะเปลี่ยนเป็น `พร้อมรับ` ระบบต้องส่งสัญญาณแจ้งเตือน (Notification) ไปยังโทรศัพท์มือถือของลูกค้า
 |
| BR/NFR/DR links | ``NFR-01`, `DR-01`, `DR-02`` |
| US/UC/AC links | ``US-01`, `UC-01`, `AC-01`` |
| Verification | **Demonstration**: เปลี่ยนสถานะฝั่งร้านค้า แล้วตรวจดูการอัปเดตบนหน้าจอลูกค้าและการส่งสัญญาณแจ้งเตือน |
| Status/TBD | Ready / Covered |

| Field | Value |
|---|---|
| Requirement ID | `FR-04` |
| Statement | หน้าจอฝั่งพนักงานต้องแสดงรายการคิวโดยเรียงตามลำดับเวลารับออเดอร์ (FIFO) และมีการแบ่งกลุ่มสถานะชัดเจน |
| Rationale/Goal | ลดภาระงานของพนักงานและป้องกันการทำอาหารผิดลำดับคิวช่วงเร่งด่วน (`PP-02`, `G-03`) |
| Source | ``RC-04`, `E-01`, `E-03`, `E-04`, `UN-02`` |
| Priority/Admission | Must / End-to-End Core |
| Trigger | พนักงานเปิดหรือรีเฟรชหน้าจอควบคุมคิวฝั่งร้านค้า |
| Preconditions/guards | มีรายการออเดอร์ส่งเข้าสู่ระบบฝั่งร้านค้า` |
| Expected result | แสดงรายการคิวแบ่งตามสถานะ (`ออเดอร์ใหม่`, `กำลังทำ`, `พร้อมรับ`) โดยกลุ่มออเดอร์ใหม่เรียงจากเวลาเก่าไปใหม่ |
| BR/NFR/DR links | ``NFR-03`, `DR-01`, `DR-03`` |
| US/UC/AC links | ``US-02`, `US-03`, `US-04`, `US-06`, `UC-02`, `AC-02`` |
| Verification | **Inspection**: ป้อนออเดอร์ทดสอบต่างเวลากัน แล้วตรวจดูการจัดเรียงลำดับคิวจากบนลงล่างบนหน้าจอพนักงาน |
| Status/TBD | **Ready / Covered** |

| Field | Value |
|---|---|
| Requirement ID | `FR-03` |
| Statement | ระบบต้องมีฟังก์ชันให้ลูกค้ายกเลิกออเดอร์ได้ด้วยตนเองผ่านระบบ |
| Rationale/Goal | เพิ่มความยืดหยุ่นให้ลูกค้าและลดภาระพนักงานในการหาบิลกระดาษมายกเลิก (`UN-03`, `E-08`) |
| Source | ``RC-03`, `E-08`, `UN-03`` |
| Priority/Admission | Should / End-to-End Core |
| Trigger | ลูกค้าเปิดดูออเดอร์ตนเองและกดปุ่ม "ยกเลิกออเดอร์" |
| Preconditions/guards | สถานะออเดอร์ต้องเป็น `ออเดอร์ใหม่` เท่านั้น (ขึ้นอยู่กับกฎ `BR-01`) |
| Expected result | หากผ่าน Guard: เปลี่ยนสถานะออเดอร์เป็น `Cancelled` และถอดคิวออกจากหน้าจอพนักงาน |
| BR/NFR/DR links | ``BR-01`, `DR-01`` |
| US/UC/AC links | ``US-10`, `UC-04`, `AC-05`` |
| Verification | **Test Case**: กดปุ่มยกเลิกในสถานะ `ออเดอร์ใหม่` แล้วตรวจสอบว่าเปลี่ยนสถานะเป็น `Cancelled` สำเร็จ |
| Status/TBD | Ready / Covered |

| Field | Value |
|---|---|
| Requirement ID | `FR-06` |
| Statement | ระบบสามารถแสดงรายงานสถิติความหนาแน่นของคิวในช่วงเวลาต่างๆ ให้ผู้ดูแลพื้นที่อาหาร |
| Rationale/Goal | สนับสนุนผู้ดูแลพื้นที่ในการวิเคราะห์ปริมาณคิวและวางแผนจัดการพื้นที่ส่วนกลาง (`02: Data Flow`) |
| Source | `02: Data Flow`, `02-stakeholder-context-scope.md` |
| Priority/Admission | Could / Supporting Core` |
| Trigger | ผู้ดูแลพื้นที่เปิดหน้ารายงานสถิติบนระบบแอดมินและเลือกช่วงเวลา |
| Preconditions/guards | ผู้ดูแลพื้นที่เข้าสู่ระบบด้วยสิทธิ์แอดมิน |
| Expected result | แสดงรายงานในรูปแบบ On-screen Dashboard สรุปปริมาณคิวและเวลารอเฉลี่ยรายชั่วโมง |
| BR/NFR/DR links | `DR-05` |
| US/UC/AC links | ``US-05`, `US-07`, `UC-03`, `AC-03`` |
| Verification | **Data Inspection**: เรียกดูรายงานสถิติตามช่วงเวลา แล้วตรวจวัดความถูกต้องเทียบกับประวัติออเดอร์จริง |
| Status/TBD | Ready / Covered |


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
