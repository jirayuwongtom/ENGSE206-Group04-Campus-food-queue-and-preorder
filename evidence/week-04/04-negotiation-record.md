# Week 04 — Conflict and Negotiation Record

> **Status rule:** ผลการเจรจาใน controlled simulation เป็น Candidate/Provisional/Unresolved เท่านั้น ไม่ใช่นโยบายจริงหรือ Approved requirement

## 1. Negotiation register

### N-01 — Cancellation Right vs Material Cost

| Field | Record |
|---|---|
| Evidence | E-05, E-08 |
| Position A — Student | อยากยกเลิกออเดอร์ได้ หากประเมินแล้วรอนานเกินไป |
| Interest A | มีเวลาจำกัด ต้องรีบไปเรียน ไม่อยากเสียเวลาพักฟรีๆ |
| Position B — Owner | ห้ามยกเลิกเด็ดขาดถ้าเริ่มทำอาหารไปแล้ว |
| Interest B | ไม่อยากเสียต้นทุนวัตถุดิบและสูญเสียรายได้ |
| Authority/constraint | นโยบายการคืนเงินและยกเลิก เป็นอำนาจเด็ดขาดของเจ้าของร้าน |

| Option | Description | Usability (Student) | Operational effort (Owner) | Fairness |
|---|---|---:|---:|---:|
| A | ให้ลูกค้ากดยกเลิกได้ตลอดเวลา | High | Low (แบกรับความเสี่ยงสูง) | Low |
| B | ห้ามลูกค้ายกเลิกเด็ดขาดตั้งแต่กดยืนยัน | Low | High | Low |
| C | ให้ยกเลิกได้แค่ตอนที่สถานะคือ "รอดำเนินการ" และบล็อกปุ่มเมื่อสถานะเปลี่ยนเป็น "กำลังทำ" | High | High (ปลอดภัย) | High |

**Decision/status:** เลือก Option C เป็น **Provisional**  
**Rationale:** ตอบโจทย์ทั้งสองฝ่าย ลูกค้ายกเลิกได้เมื่อรอไม่ไหวและร้านยังไม่ทำ (E-08) และเมื่อร้านเริ่มทำแล้วก็บล็อกเพื่อปกป้องต้นทุน (E-05)  
**Derived candidates:** RC-02

---

### N-02 — Speed (Queue skipping) vs Strict Fairness (FIFO)

| Field | Record |
|---|---|
| Evidence | E-04, E-07 |
| Position A — Staff | ต้องการทำเมนูง่ายแทรกคิวไปก่อนเพื่อให้แถวสั้นลง |
| Interest A | ระบายคิวให้เร็วที่สุด ลดความแออัดหน้าเตา |
| Position B — Student | ต้องการให้ร้านทำอาหารเรียงตามคิวเป๊ะๆ ห้ามข้าม |
| Interest B | ความรู้สึกยุติธรรม ไม่โดนแซงคิว |
| Authority/constraint | ธรรมชาติของการทำอาหารบางเมนูใช้เวลาไม่เท่ากัน ไม่สามารถบังคับ FIFO ได้ 100% |

| Option | Description | Speed (Staff) | Fairness (Student) | Feasibility |
|---|---|---:|---:|---:|
| A | บังคับระบบรันคิว FIFO เป๊ะๆ ห้ามกดข้าม | Low | High | Low (ผิดหลักหน้าเตา) |
| B | ให้พนักงานกดข้ามคิวทำรายการที่เสร็จก่อนได้อิสระ แต่ซ่อนการมองเห็นจากลูกค้า | High | Low | Medium |
| C | พนักงานทำเมนูง่ายก่อนได้ แต่ระบบแสดงสถานะชัดเจนว่าแต่ละคิวอยู่ในขั้นตอนใดแล้วให้ลูกค้าเห็น | High | Medium-High | High |

**Decision/status:** เลือก Option C เป็น **Provisional**  
**Rationale:** สภาพหน้าเตาจริงไม่สามารถทำ FIFO เป๊ะได้ (E-04) แต่การทำให้ระบบแสดงสถานะโปร่งใส จะช่วยลดความกังวลของลูกค้าเรื่องการโดนแซงคิวได้ (E-07)  
**Derived candidates:** RC-01, RC-05