# Design Spine — เส้นทางงานหลักหนึ่งชิ้นของ Campus food queue and preorder

> ตารางนี้โตขึ้นทุกสัปดาห์: W10 เติมคอลัมน์ "W10 ระดับ"; W11 เติม "กล่อง"; W12 เติม "หน้าจอ"; W13 เติม "action/data/rule"
> แถว = ขั้นที่ผู้ใช้/ระบบทำจริงตามลำดับ 5–8 แถว จาก Core use case ใน `docs/06-requirement-models.md`
> ระดับ: **Build now** = Dev เริ่มเขียนได้หลัง W13 | **Overview** = อยู่ในภาพรวม/ข้อมูล/กติกา ยังไม่มีหน้าจอ-contract ละเอียด | **Later** = increment ถัดไป

| # | ขั้นในเส้นทาง | Actor | UC | AC หลัก | W10 ระดับ | W11 กล่องที่รับผิดชอบ | W12 หน้าจอ | W13 action / data / rule |
|---|---|---|---|---|---|---|---|---|
| 1 | ลูกค้าส่งคำสั่งซื้อและได้รับหมายเลขคิว | นักศึกษา/ลูกค้า | UC-01 | AC-01 | Build now | Mobile Application → API Application → Database → ตอบหมายเลขคิวกลับ | | |
| 2 | พนักงานเห็นคิวเรียง | พนักงานร้าน | UC-02 | AC-02 | Build now | Mobile Application → API Application (อ่านคิวของร้านเรียงตามเวลารับออเดอร์ แบ่งกลุ่มสถานะ) → Database | | |
| 3 | พนักงานเปลี่ยนเป็น "กำลังทำ" | พนักงานร้าน | UC-02 | AC-02, AC-04, AC-05 | Build now | Mobile Application → API Application → Database → API ซ่อนปุ่มยกเลิกฝั่งลูกค้า | | |
| 4 | พนักงานทำเสร็จและเปลี่ยนเป็น "พร้อมรับ" | พนักงานร้าน | UC-02 | AC-02, AC-04 | Build now | Mobile Application → API Application → Database → API ส่งสถานะ "พร้อมรับ" ไปหาลูกค้า | | |
| 5 | ระบบแจ้งเตือนลูกค้าเมื่อพร้อมรับ | ระบบ (ถึงนักศึกษา/ลูกค้า) | UC-01, UC-02 | AC-01 | Build now | API Application → EXT-01 → แจ้งเตือนไปยังโทรศัพท์ลูกค้า | | |
| 6 | ลูกค้าแสดงหมายเลขคิว รับอาหาร และพนักงานกดบันทึกสถานะเสร็จสิ้น | นักศึกษา/ลูกค้า, พนักงานร้าน | UC-01, UC-02 | AC-01 | Build now | Mobile Application (พนักงาน) → API Application → Database → อัปเดตหน้าจอลูกค้า | | |

## บันทึกการเปลี่ยนแปลง

| สัปดาห์ | เปลี่ยนอะไร | เพราะ |
|---|---|---|
| W10 | สร้างครั้งแรก เติมคอลัมน์ W10 (6 ขั้น ทั้งหมด Build now) | เรียงตามเส้นทางจริงของออเดอร์หนึ่งใบจาก UC-01 และ UC-02; UC-03 (Overview) และ UC-04 (ยกเลิก) ไม่อยู่ในเส้นทางหลักนี้ |
| W11 | เติมคอลัมน์ "กล่องที่รับผิดชอบ" จากหัวข้อ 7 ของ `design/11-conceptual-architecture.md` ทั้ง 6 ขั้นผ่านกล่อง Mobile Application, API Application, Database และ EXT-01 | เดิน Spine บน container diagram; กติกา D1–D3 และการตรวจ role อยู่ที่ API Application ทุก action |
