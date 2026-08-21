# BPMN — Travel Trip Management System (To-Be)

## 1. Pool
**Travel Trip Management**

## 2. Swimlane
1. Customer
2. Admin
3. Finance
4. Operational
5. Owner
6. Vendor / Travel Partner

## 3. Main BPMN Flow

```text
CUSTOMER
(Start)
  ↓
Melihat iklan
  ↓
Klik iklan
  ↓
Inquiry via WhatsApp
  ↓
Order
  ↓
Isi Form Order
  ↓
Terima Invoice
  ↓
Bayar DP
  ↓
[Payment Verification]

ADMIN
  ↓
Menjawab Inquiry
  ↓
Membuat Order
  ↓
Mengirim Form
  ↓
Membuat Invoice
  ↓
Mencatat Payment
  ↓
Memasukkan participant setelah DP terverifikasi

FINANCE
  ↓
Verifikasi Payment
  ↓
Payment Verified
  ↓
Participant dihitung

OPERATIONAL
  ↓
Planning Trip
  ↓
Atur Destination & Activity
  ↓
Assign Tour Leader
  ↓
Booking Vendor
  ↓
Persiapan

SYSTEM
  ↓
H-5 Event
  ↓
Count DP Verified Participants
  ↓
◇ Apakah participant >= 20?
  ├── YES → Trip CONFIRMED
  │          ↓
  │       Persiapan keberangkatan
  │          ↓
  │       Pelunasan
  │          ↓
  │       Departure
  │          ↓
  │       On Trip
  │          ↓
  │       Completed
  │
  └── NO → Trip CANCELLED
             ↓
        WAITING OWNER ACTION

OWNER
  ↓
◇ Pilihan?
  ├── FULL REFUND
  │      ↓
  │   Finance proses refund
  │      ↓
  │   Bukti refund disimpan
  │      ↓
  │   REFUNDED
  │
  └── TRANSFER TO TRAVEL PARTNER
         ↓
      Persetujuan/konfirmasi peserta
         ↓
      Transfer data/transaksi
         ↓
      TRANSFERRED

(End)
```

## 4. Gateway Penting
**G1 — Payment Verified?**
- No → tetap Waiting Verification.
- Yes → participant dihitung.

**G2 — Minimum Participant Reached?**
- Yes → trip dapat dilanjutkan.
- No → cancellation handling.

**G3 — Owner Decision**
- Full Refund.
- Transfer to Travel Partner.

## 5. Catatan BPMN
Untuk implementasi final, status `CANCELLED` sebaiknya dipisahkan dari `WAITING OWNER ACTION` jika Owner masih harus memilih tindakan. Dengan begitu sistem memiliki audit trail yang jelas.
