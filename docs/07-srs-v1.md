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
| BR/NFR/DR links | `NFR-01`, `DR-01`, `DR-02` |
| US/UC/AC links | `US-01`, `UC-01`, `AC-01` |
| Verification | **Demonstration**: เปลี่ยนสถานะฝั่งร้านค้า แล้วตรวจดูการอัปเดตบนหน้าจอลูกค้าและการส่งสัญญาณแจ้งเตือน |
| Status/TBD | Ready / Covered |

| Field | Value |
|---|---|
| Requirement ID | `FR-04` |
| Statement | หน้าจอฝั่งพนักงานต้องแสดงรายการคิวโดยเรียงตามลำดับเวลารับออเดอร์ (FIFO) และมีการแบ่งกลุ่มสถานะชัดเจน |
| Rationale/Goal | ลดภาระงานของพนักงานและป้องกันการทำอาหารผิดลำดับคิวช่วงเร่งด่วน (`PP-02`, `G-03`) |
| Source | `RC-04`, `E-01`, `E-03`, `E-04`, `UN-02` |
| Priority/Admission | Must / End-to-End Core |
| Trigger | พนักงานเปิดหรือรีเฟรชหน้าจอควบคุมคิวฝั่งร้านค้า |
| Preconditions/guards | มีรายการออเดอร์ส่งเข้าสู่ระบบฝั่งร้านค้า |
| Expected result | แสดงรายการคิวแบ่งตามสถานะ (`ออเดอร์ใหม่`, `กำลังทำ`, `พร้อมรับ`) โดยกลุ่มออเดอร์ใหม่เรียงจากเวลาเก่าไปใหม่ |
| BR/NFR/DR links | `NFR-03`, `DR-01`, `DR-03` |
| US/UC/AC links | `US-02`, `US-03`, `US-04`, `US-06`, `UC-02`, `AC-02` |
| Verification | **Inspection**: ป้อนออเดอร์ทดสอบต่างเวลากัน แล้วตรวจดูการจัดเรียงลำดับคิวจากบนลงล่างบนหน้าจอพนักงาน |
| Status/TBD | **Ready / Covered** |

| Field | Value |
|---|---|
| Requirement ID | `FR-03` |
| Statement | ระบบต้องมีฟังก์ชันให้ลูกค้ายกเลิกออเดอร์ได้ด้วยตนเองผ่านระบบ |
| Rationale/Goal | เพิ่มความยืดหยุ่นให้ลูกค้าและลดภาระพนักงานในการหาบิลกระดาษมายกเลิก (`UN-03`, `E-08`) |
| Source | `RC-03`, `E-08`, `UN-03` |
| Priority/Admission | Should / End-to-End Core |
| Trigger | ลูกค้าเปิดดูออเดอร์ตนเองและกดปุ่ม "ยกเลิกออเดอร์" |
| Preconditions/guards | สถานะออเดอร์ต้องเป็น `ออเดอร์ใหม่` เท่านั้น (ขึ้นอยู่กับกฎ `BR-01`) |
| Expected result | หากผ่าน Guard: เปลี่ยนสถานะออเดอร์เป็น `Cancelled` และถอดคิวออกจากหน้าจอพนักงาน |
| BR/NFR/DR links | `BR-01`, `DR-01` |
| US/UC/AC links | `US-10`, `UC-04`, `AC-05` |
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
| US/UC/AC links | `US-05`, `US-07`, `UC-03`, `AC-03` |
| Verification | **Data Inspection**: เรียกดูรายงานสถิติตามช่วงเวลา แล้วตรวจวัดความถูกต้องเทียบกับประวัติออเดอร์จริง |
| Status/TBD | Ready / Covered |


## 4. Business Rules

| BR | Rule | Authority / Source | Affected FR / UC | Status |
| :--- | :--- | :--- | :--- | :--- |
| **BR-01** | ไม่อนุญาตให้ยกเลิกคำสั่งซื้อ หากสถานะออเดอร์ถูกเปลี่ยนเป็น 'กำลังทำ' แล้ว | เจ้าของร้าน / `E-05`, `C-01 (04-evidence-log.md)` | `FR-03`, `UC-04` | Confirmed for case |
##### Detailed Rule Specification: BR-01
* **Rule ID**: `BR-01`
* **Statement**: ระบบจะไม่อนุญาตให้ลูกค้ายกเลิกคำสั่งซื้อ หากสถานะออเดอร์ถูกเปลี่ยนเป็น 'กำลังทำ' แล้ว
* **Business Authority**: เจ้าของร้านค้า (`04-evidence-log.md` ข้อตกลง `C-01`)
* **Rationale**: ป้องกันความเสียหายทางธุรกิจและรักษาต้นทุนวัตถุดิบจากการยกเลิกคำสั่งซื้อหลังลงมือปรุงอาหารแล้ว
* **Enforcement & Guard**: เมื่อพนักงานกดเปลี่ยนสถานะเป็น `กำลังทำ` ระบบจะล็อกปุ่มยกเลิกฝั่งลูกค้าทันที หากคำขอยกเลิกมาถึงในเวลาเดียวกัน ระบบจะยึด Server Timestamp เป็นหลัก หากสถานะใน DB เป็น `Cooking` ก่อน คำขอยกเลิกจะถูกปฏิเสธ
* **Affected Behaviors**: `FR-03`, `US-10`, `US-11`, `UC-04`, `AC-05`
## 5. Non-functional Requirements

| NFR | Quality Statement | Context / Stimulus | Response / Measure | Source | Verification | Status / TBD |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **NFR-03** | หน้าจอฝั่งร้านค้าต้องกดเปลี่ยนสถานะออเดอร์ได้สำเร็จด้วยการกดไม่เกิน 2 คลิก | พนักงานกดเปลี่ยนสถานะคิวหน้าเตาช่วงเวลาเร่งด่วน | จำนวนการกด/สัมผัส 2 ครั้ง | `01-problem-brief-v0.1.md` | Usability Test | **Ready / Covered** |
| **NFR-01** | ระบบต้องแสดงผลการอัปเดตสถานะไปที่หน้าจอลูกค้าภายใน 3 วินาที | พนักงานกดเปลี่ยนสถานะออเดอร์ฝั่งร้านค้า | Real-time Latency  3 วินาที | `01-problem-brief-v0.1.md` | Load Test (50 Users) | **Needs Follow-up / TBD** |
| **NFR-02** | ระบบต้องจัดเก็บเฉพาะข้อมูลจำเป็น โดยไม่เก็บข้อมูลประวัติการแพ้อาหาร | การบันทึกข้อมูลคำสั่งซื้อเข้าสู่ระบบ | ไม่พบฟิลด์เก็บข้อมูลสุขภาพ/แพ้อาหาร | `02-stakeholder-context-scope.md` | Audit Inspection | **Needs Follow-up / TBD** |

## 6. Data Requirements

ส่วนนี้เป็น conceptual data requirement ยังไม่ใช่ physical database schema

| DR | Concept | Requirement / Minimum Data | Relationships | Classification | Source | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **DR-01** | **Customer Order** | ข้อมูลคำสั่งซื้อที่ลูกค้าส่งเข้าระบบ (`Order ID`, `Order Timestamp`, `Current Status`, `Queue Number`) | 1:1 กับ `Queue Token`, Many:1 กับ `Food Stall` | Internal Domain | `RC-01`, `RC-03` | **Ready / Covered** |
| **DR-02** | **Queue Token** | ตัวแทนลำดับคิวและสถานะออเดอร์ปัจจุบัน (`Queue Number`, `Sequence Position`, `Last Status Change Time`) | 1:1 กับ `Customer Order` | Internal Domain | `RC-01` | **Ready / Covered** |
| **DR-03** | **Food Stall** | ข้อมูลร้านอาหารที่ลงทะเบียนใช้งานระบบ (`Stall ID`, `Stall Name`, `Operational Status`) | 1:Many กับ `Customer Order`, 1:Many กับ `Menu Item` | Master Data | `02-stakeholder-context-scope.md` | **Ready / Covered** |
| **DR-04** | **Menu Item** | รายการอาหารที่เปิดให้บริการสั่งซื้อ (`Menu ID`, `Menu Name`, `Stock Availability`) | Many:1 กับ `Food Stall` | Master Data | `RC-05` | **Ready / Covered** |
| **DR-05** | **Queue Density Report** | สรุปข้อมูลสถิติปริมาณคิวและความหนาแน่น (`Time Interval`, `Total Order Volume`, `Average Wait Duration`) | Aggregated จาก `Customer Order` และ `Food Stall` | Derived Report | `02: Data Flow` | **Ready / Covered** |

##  รายละเอียด

### DR-01: Customer Order (ข้อมูลคำสั่งซื้อ)
* **ความหมายทางธุรกิจ**: สิ่งแทนรายการสั่งซื้ออาหารที่ลูกค้าส่งเข้าระบบ เพื่อขอรับบริการคิวและติดตามสถานะการปรุงอาหาร
* **ข้อมูลขั้นต่ำที่จำเป็น (Minimum Data)**: `Order ID` (รหัสคำสั่งซื้อ), `Order Timestamp` (เวลาที่สั่งซื้อ), `Current Status` (`New`, `Cooking`, `Ready`, `Completed`, `Cancelled`), `Queue Number` (หมายเลขคิว)
* **ความสัมพันธ์ (Relationships)**: สัมพันธ์แบบ 1:1 กับ Queue Token (`DR-02`), แบบ Many:1 กับ Food Stall (`DR-03`) และแบบ 1:Many กับ Order Item
* **ประเภทข้อมูล (Classification)**: Internal Domain Data
* **แหล่งที่มา (Source)**: `RC-01`, `RC-03`

### DR-02: Queue Token (คิวและสถานะ)
* **ความหมายทางธุรกิจ**: ตัวแทนลำดับคิวและสถานะออเดอร์ ณ เวลาปัจจุบัน สำหรับใช้จัดลำดับการปรุงอาหารฝั่งพนักงาน และแสดงผลการแจ้งเตือนฝั่งลูกค้า
* **ข้อมูลขั้นต่ำที่จำเป็น (Minimum Data)**: `Queue Number` (หมายเลขคิวประจำวัน), `Sequence Position` (ลำดับแถวคิว FIFO), `Last Status Change Time` (เวลาอัปเดตสถานะล่าสุด)
* **ความสัมพันธ์ (Relationships)**: สัมพันธ์แบบ 1:1 กับ Customer Order (`DR-01`)
* **ประเภทข้อมูล (Classification)**: Internal Domain Data
* **แหล่งที่มา (Source)**: `RC-01`

### DR-03: Food Stall (ข้อมูลร้านค้า)
* **ความหมายทางธุรกิจ**: ร้านอาหารภายในโรงอาหารที่ลงทะเบียนใช้งานระบบ เพื่อรับคำสั่งซื้อ จัดลำดับคิว และอัปเดตสถานะอาหาร
* **ข้อมูลขั้นต่ำที่จำเป็น (Minimum Data)**: `Stall ID` (รหัสประจำร้าน), `Stall Name` (ชื่อร้านค้า), `Operational Status` (สถานะการเปิด/ปิดรับคิว)
* **ความสัมพันธ์ (Relationships)**: สัมพันธ์แบบ 1:Many กับ Customer Order (`DR-01`) และแบบ 1:Many กับ Menu Item (`DR-04`)
* **ประเภทข้อมูล (Classification)**: Master Data
* **แหล่งที่มา (Source)**: `02-stakeholder-context-scope.md`

### DR-04: Menu Item (รายการอาหาร)
* **ความหมายทางธุรกิจ**: รายการเมนูอาหารที่ร้านค้าเปิดให้บริการสั่งซื้อ พร้อมสถานะความพร้อมของวัตถุดิบหน้าร้าน
* **ข้อมูลขั้นต่ำที่จำเป็น (Minimum Data)**: `Menu ID` (รหัสรายการอาหาร), `Menu Name` (ชื่อเมนู), `Stock Availability` (`In-Stock`, `Out-of-Stock`)
* **ความสัมพันธ์ (Relationships)**: สัมพันธ์แบบ Many:1 กับ Food Stall (`DR-03`)
* **ประเภทข้อมูล (Classification)**: Master Data
* **แหล่งที่มา (Source)**: `RC-05`

### DR-05: Queue Density Report (รายงานสถิติความหนาแน่นคิว)
* **ความหมายทางธุรกิจ**: ข้อมูลสรุปสถิติปริมาณคิวและเวลารอเฉลี่ยรายชั่วโมง สำหรับให้ผู้ดูแลพื้นที่อาหารใช้พิจารณาบริหารจัดการพื้นที่โรงอาหารส่วนกลาง
* **ข้อมูลขั้นต่ำที่จำเป็น (Minimum Data)**: `Time Interval` (ช่วงเวลาสังเกตการณ์), `Total Order Volume` (จำนวนออเดอร์รวมช่วงเวลา), `Average Wait Duration` (ประวัติเวลารอเฉลี่ยจริง)
* **ความสัมพันธ์ (Relationships)**: ข้อมูลสรุประดับรวม (Aggregated Data) จาก Customer Order (`DR-01`) และ Food Stall (`DR-03`)
* **ประเภทข้อมูล (Classification)**: Derived Report
* **แหล่งที่มา (Source)**: `02: Data Flow`

## 7. Behavioral Model References

| Model | IDs / Version | Requirement Anchors | Coverage / Gap | SRS Use |
| :--- | :--- | :--- | :--- | :--- |
| **User Stories** | US-01..US-08, US-10, US-11  | FR-01, FR-03, FR-04, FR-06, BR-01, NFR-03 | Covered  | Section 3, Section 4, Section 5 |
| **Use Cases** | UC-01,UC-04  | FR-01, FR-03, FR-04, FR-06, BR-01, NFR-03 | Covered  | Section 3, Section 4, Section 5 |
| **Acceptance Criteria**| AC-01,AC-05  | FR-01, FR-03, FR-04, FR-06, BR-01, NFR-03 | Covered  | Section 11  |

### 7.1 Lifecycle Rules

| From State | Trigger Event | To State | Guard Condition / Rule | Source |
| :--- | :--- | :--- | :--- | :--- |
| None | ลูกค้าส่งคำสั่งซื้อสำเร็จ | New | ข้อมูลรายการอาหารครบถ้วน | FR-01 |
| New | ลูกค้าสแกน/กดปุ่มขอยกเลิก | Cancelled | สถานะปัจจุบันใน DB ยังไม่เป็น Cooking (BR-01) | FR-03, BR-01 |
| New | พนักงานกดเริ่มทำอาหารหน้าเตา | Cooking | พนักงานสแกนหรือสัมผัสเลือกออเดอร์ | FR-04, NFR-03 |
| Cooking | พนักงานปรุงอาหารเสร็จและวางจุดส่งมอบ | Ready | ออเดอร์ผ่านสถานะ Cooking เรียบร้อย | FR-01, NFR-01 |
| Ready | พนักงานยื่นอาหารให้ลูกค้า | Completed | หมายเลขคิวฝั่งลูกค้าตรงกับออเดอร์ | FR-01 |

## 8. External Interface Requirements

| Interface | Requirement/data | Direction | Owner | Failure/privacy concern | Status |
|---|---|---|---|---|---|
| **EXT-01** (Web Push Notification)| สัญญาณแจ้งเตือนอัปเดตสถานะคิวเป็น `พร้อมรับ` | Outbound | Dev Team | การหลุดเชื่อมต่อของสัญญาณเครือข่ายมือถือ | Core Scope |
|**EXT-02** (Stall Display Panel) | รายการคิวเรียงลำดับ FIFO และปุ่มกดเปลี่ยนสถานะ | Bi-directional | Dev Team | อุปกรณ์ฝั่งร้านค้าค้างหรือสัมผัสไม่ติดช่วงเร่งด่วน | Core Scope |

## 9. Traceability and Coverage

| Source Evidence | W05 Requirement | W06 Behavioral Model | SRS Section | Verification ID | Coverage Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `RC-01`, `E-07`, `PP-01` | `FR-01` (Must) | `US-01`, `UC-01`, `AC-01` | Section 3.2 | `VF-01` | **Covered** |
| `RC-04`, `E-01`, `E-03` | `FR-04` (Must) | `US-02`..`06`, `UC-02`, `AC-02` | Section 3.2 | `VF-02` | **Covered** |
| `RC-03`, `E-08` | `FR-03` (Should) | `US-10`, `UC-04`, `AC-05` | Section 3.2 | `VF-03` | **Covered** |
| `E-05`, `C-01` | `BR-01` (Must) | `US-11`, `UC-04`, `AC-05` | Section 4 | `VF-03` | **Covered** |
| `02: Data Flow` | `FR-06` (Could) | `US-05`, `US-07`, `UC-03`, `AC-03` | Section 3.2 | `VF-05` | **Covered** |
| `01: Sect 9` | `NFR-03` (Should) | `US-08`, `UC-02`, `AC-04` | Section 5 | `VF-04` | **Covered** |
| `RC-02`, `E-06` | `FR-02` (Must) | -| Section 10 | `ISS-01` | **Partial / TBD** |
| `RC-05`, `E-02` | `FR-05` (Should) | -| Section 10 | `ISS-02` | **Partial / TBD** |
## 10. Open Issues

| OI | Question/TBD | Affected IDs | Owner | Next action | Expected evidence | Needed by |
|---|---|---|---|---|---|---|
| **ISS-01** | การยืนยันสูตรประเมินเวลารอคิวที่คลาดเคลื่อนไม่เกิน 5 นาที | `FR-02` | Tech Lead | เก็บสถิติเวลาทำอาหารจริงหน้าเตาเพื่อสร้างสูตรคำนวณ | ผลการทดสอบสูตรคำนวณ | - |
| **ISS-02** | การทดสอบความเร็วการแจ้งเตือนเมนูหมดแบบ Real-time (ภายใน 3) | `FR-05`, `NFR-01` | Backend Dev | ทดสอบการส่งข้อมูลผ่าน WebSocket/SSE กำลังโหลด | รายงานผล Load Test 50 Users | - |
| **ISS-03** | การสรุป Privacy Policy และเกณฑ์ Data Retention | `NFR-02` | Compliance | ร่างข้อตกลงความเป็นส่วนตัวเรื่องการไม่เก็บประวัติแพ้อาหาร | เอกสาร Privacy Policy | - |
| **ISS-04** | รูปแบบรายงานสถิติเพิ่มเติมที่ผู้ดูแลพื้นที่ต้องการ | `FR-06` | BA | สอบถามผู้ดูแลพื้นที่เรื่องการ Export ไฟล์เพิ่มเติม | สรุปผลสัมภาษณ์ผู้ดูแลพื้นที่ | - |
## 11. Verification Plan

| VF ID | Method | Target IDs | Procedure / Evidence | Owner | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **VF-01** | Demonstration | `FR-01` | **Procedure**: พนักงานกดเปลี่ยนสถานะเป็น `Ready` บนหน้าจอฝั่งร้านค้า <br>**Pass Criteria**: หน้าจอลูกค้าอัปเดตสถานะตรงกันและส่งสัญญาณแจ้งเตือน | QA Tester | Planned |
| **VF-02** | Inspection | `FR-04` | **Procedure**: ป้อนออเดอร์ทดสอบต่างเวลากันเข้าสู่ระบบ <br>**Pass Criteria**: หน้าจอพนักงานแสดงรายการคิวเรียงลำดับเวลาจากเก่าไปใหม่ถูกต้อง | QA Tester | Planned |
| **VF-03** | Boundary Test | `FR-03`, `BR-01` | **Procedure**: ทดสอบกดยกเลิกในสถานะ `New` และสถานะ `Cooking` <br>**Pass Criteria**: ยกเลิกสำเร็จในสถานะ `New` และถูกปฏิเสธ/ล็อกปุ่มในสถานะ `Cooking` | QA Tester | Planned |
| **VF-04** | Usability Test | `NFR-03` | **Procedure**: ทดสอบการกดเปลี่ยนสถานะออเดอร์หน้าเตาของพนักงาน <br>**Pass Criteria**: ดำเนินการเปลี่ยนสถานะได้สำเร็จโดยใช้การสัมผัส/คลิกหน้าจอ มากว่าหรือเท่ากับ 2 ครั้ง | UX Designer | Planned |
| **VF-05** | Data Inspection | `FR-06` | **Procedure**: เรียกดูรายงานสถิติตามช่วงเวลาบนหน้าจอแอดมิน <br>**Pass Criteria**: ระบบแสดงกราฟ/ตารางสรุปปริมาณคิวตรงตามประวัติคำสั่งซื้อสะสม | BA | Planned |

## 12. Review Gate

- [x] W05 FR/BR/NFR/DR ทุกข้อมี disposition
- [x] W06 US/UC/AC ย้อนกลับ W05 ได้
- [x] Partial/Extension/TBD มองเห็น
- [x] Open Issue ทุกข้อมี owner/action/evidence
- [x] Status ยังเป็น Baseline Candidate

## Appendix A — Requirement Disposition

| Backlog ID | Included/Deferred/Extension/Issue | SRS section | Reason |
|---|---|---|---|
| `FR-01` | End-to-End Core | Section 3.2 | ฟังก์ชันหลักในการแก้ปัญหาการยืนรอคิวหน้าร้าน (In-Scope Phase 1) |
| `FR-04` | End-to-End Core | Section 3.2 | ฟังก์ชันหลักในการดำเนินงานหน้าเตาของพนักงานร้านค้า (In-Scope Phase 1) |
| `FR-03` | End-to-End Core | Section 3.2 | ให้ความยืดหยุ่นแก่ลูกค้า โดยต้องอยู่ภายใต้เงื่อนไขกฎ `BR-01` |
| `BR-01` | End-to-End Core | Section 4 | กฎจุดตัด Cut-off เพื่อป้องกันความเสียหายของวัตถุดิบร้านค้า |
| `FR-06` | Supporting Core | Section 3.2 | ฟังก์ชันสนับสนุนผู้บริหารพื้นที่ส่วนกลางในการวิเคราะห์ความแออัด |
| `NFR-03` | Supporting Core | Section 5 | ข้อกำหนดด้านความสะดวกในการใช้งานของพนักงานช่วงเวลาเร่งด่วน |
| `FR-02` | Deferred / TBD | Section 10 | ชะลอการทำ Model ใน v1.0 จนกว่าจะยืนยันสูตรคำนวณเวลา |
| `FR-05` | Deferred / TBD | Section 10 | ชะลอการทำ Model ใน v1.0 จนกว่าจะทดสอบระบบ |
| `NFR-01` | Deferred / TBD | Section 5 &amp; 10 | ชะลอการกำหนดเกณฑ์วัดผล จนกว่าจะทดสอบ Latency ทางเทคนิค |
| `NFR-02` | Deferred / TBD | Section 5 &amp; 10 | ชะลอการสรุปเกณฑ์ จนกว่าจะอนุมัติ Privacy Policy |
| `ISSUE-01` | Out of Scope | Section 1.3 | ตัดออกตามคำแนะนำ Instructor เพื่อโฟกัสเฉพาะ Queue Flow |
| `ISSUE-02` |Out of Scope / Hold | Section 1.3 &amp; 10 | พักไว้เนื่องจากขาดกฎเกณฑ์ความยุติธรรมที่แน่ชัดจากร้านค้า |

## Appendix B — Review and Revision

| Item | Before | After | Reason/source | Reviewer |
|---|---|---|---|---|
| **REV-01** (Section 4: `BR-01`) | ระบุเพียงล็อกปุ่มยกเลิกเมื่อสถานะเป็น `Cooking` โดยไม่ได้ระบุเงื่อนไขกรณีส่งคำขอพร้อมกัน | **เพิ่ม Server-side Timestamp Rule**: หากสถานะใน DB เปลี่ยนเป็น `Cooking` ก่อน ระบบจะปฏิเสธคำขอยกเลิกทันที | แก้ไข Race Condition และข้อพิพาทเรื่อง Latency (`DEF-01`) | Peer Reviewer / Team Approval |
| **REV-02** (Section 3.2: `FR-06`) | ระบุว่า "แสดงผลหรือส่งออกรายงานสถิติ" โดยไม่ได้จำกัดรูปแบบการส่งออก | **จำกัด Scope Phase 1**: แสดงผลรายงานในรูปแบบ **On-screen Dashboard** ส่วนการ Export เป็นไฟล์จัดเป็น Extension | ขจัดความก้ำกวมของขอบเขตระบบ Phase 1 (`DEF-02`) | Peer Reviewer / Team Approval |
| **REV-03** (Section 5: `NFR-03`) | ระบุเปลี่ยนสถานะออเดอร์ใน 2 คลิก โดยไม่ได้ระบุขอบเขตเมนูที่บังคับใช้ | **แยก Usability Scope**: เงื่อนไข 2 คลิก บังคับใช้เฉพาะ **Primary Workflow** (การเปลี่ยนสถานะคิวหน้าเตา) | ป้องกันความสับสนในการออกแบบ UI (`DEF-03`) | Peer Reviewer / Team Approval |
| **REV-04** (Section 6: `DR-05`) | กำหนดฟิลด์ `Average Wait Duration` โดยไม่ได้ชี้แจงความต่างจาก `FR-02` | **ชี้แจงประเภทข้อมูล**: เป็นข้อมูลสถิติประวัติเวลารอย้อนหลังตามจริง ไม่ใช่การประมาณการเวลารอล่วงหน้าของ `FR-02` | ป้องกันความเข้าใจผิดเรื่อง Cross-cutting Scope (`DEF-04`) | Peer Reviewer / Team Approval |
| **REV-05** (Section 5: `NFR-01`) | ลงสถานะ TBD สำหรับ Real-time Latency (3s) โดยไม่ได้ระบุสภาวะแวดล้อมการทดสอบ | **กำหนด Load Condition**: ระบุเงื่อนไขใน TBD ว่าต้องทดสอบความเร็วส่งข้อมูลภายใต้สภาวะโหลดจำลอง 50 Users | กำหนดเกณฑ์ทดสอบสำหรับ Week 08 (`DEF-05`) | Peer Reviewer / Team Approval |

## Appendix C — AI Use Disclosure

| Activity | AI assistance | Human verification/change | Evidence |
|---|---|---|---|
| `[task]` | `[what AI did]` | `[accepted/rejected/changed]` | `[path/link]` |
