# BPMN — Travel & Tour Operations Management System (To-Be)

## 1. Pool
**Travel & Tour Operations System**

## 2. Swimlane (Aktor & Tanggung Jawab)
1. **Customer:** Mengajukan inquiry, mengisi formulir registrasi, membayar DP & pelunasan.
2. **Admin:** Menangani inquiry, menerbitkan order & invoice, komunikasi peserta.
3. **Finance:** Verifikasi pembayaran (DP & Pelunasan), memproses refund, membayar vendor.
4. **Operational:** Menyiapkan itinerary, menugaskan Tour Leader, reservasi & PO vendor.
5. **Tour Leader:** Mengakses manifest, mendampingi peserta, melaporkan status & insiden lapangan.
6. **Owner:** Approval keputusan kuota D-5 (Full Refund / Transfer Partner), override kebijakan.
7. **Vendor / Travel Partner:** Menerima PO layanan, menyediakan akomodasi/transportasi, menerima pengalihan peserta.
8. **System:** Trigger otomatis evaluasi H-5 / D-5, kalkulasi kuota, pembuatan dokumen.

---

## 3. Main BPMN Flow

`	ext
CUSTOMER
(Start)
  ↓
Melihat iklan / promosi
  ↓
Klik link iklan
  ↓
Inquiry via WhatsApp
  ↓
Order / Reservasi
  ↓
Mengisi Booking Form (Data Traveler)
  ↓
Menerima Invoice
  ↓
Membayar Down Payment (DP)
  ↓
[Payment Verification Pending]

ADMIN
  ↓
Merespons WhatsApp Inquiry
  ↓
Membuat Draft Order / Booking
  ↓
Mengirimkan Booking Form
  ↓
Menerbitkan Invoice Pembayaran
  ↓
Mencatat Bukti Pembayaran DP

FINANCE
  ↓
Verifikasi Bukti Pembayaran DP
  ↓
◇ G1: Apakah DP Valid?
  ├── NO  → Pembayaran ditolak / Konfirmasi ulang ke Customer
  └── YES → Status Pembayaran: VERIFIED
              ↓
            Status Booking: CONFIRMED
              ↓
            Data Traveler masuk ke Manifest Resmi

OPERATIONAL
  ↓
Menyiapkan Tour Plan & Itinerary
  ↓
Mengatur Destinasi & Aktivitas
  ↓
Menugaskan Tour Leader (Assign Tour Leader)
  ↓
Reservasi & Kirim PO ke Vendor (Bus, Penginapan, Restoran)
  ↓
Persiapan Operasional Keberangkatan

SYSTEM (D-5 Milestone Event)
  ↓
Pemicu Otomatis H-5 (5 Hari Sebelum Departure)
  ↓
Hitung Total Peserta Terverifikasi DP
  ↓
◇ G2: Apakah Peserta Terverifikasi >= 20?
  ├── YES → Status Departure: CONFIRMED
  │          ↓
  │       Admin kirim tagihan Pelunasan (Final Settlement)
  │          ↓
  │       Finance verifikasi Pelunasan
  │          ↓
  │       Operational rilis Final Manifest & Service Vouchers
  │          ↓
  │       Status Departure: IN_OPERATION (Keberangkatan)
  │          ↓
  │       Tour Leader koordinasi lapangan
  │          ↓
  │       Status Departure: COMPLETED
  │          ↓
  │       Finance proses Financial Closing
  │
  └── NO → Status Departure: CANCELLED / WAITING OWNER ACTION
             ↓
        Notifikasi Darurat dikirim ke Owner

OWNER
  ↓
◇ G3: Keputusan Disposisi Pembatalan?
  ├── FULL REFUND
  │      ↓
  │   Finance menghitung total refund seluruh peserta
  │      ↓
  │   Finance memproses transfer pengembalian dana 100%
  │      ↓
  │   Upload bukti refund ke sistem
  │      ↓
  │   Status Pembayaran: REFUNDED
  │      ↓
  │   Status Departure: CLOSED_CANCELLED
  │
  └── TRANSFER TO TRAVEL PARTNER
         ↓
      Persetujuan & konfirmasi dari peserta
         ↓
      Transfer manifest & alokasi dana ke mitra
         ↓
      Upload bukti disposisi/perjanjian transfer
         ↓
      Status Peserta: TRANSFERRED
         ↓
      Status Departure: CLOSED_TRANSFERRED

(End)
`

---

## 4. Decision Gateways Kritis

### **Gateway 1 (G1) — Payment Verification Gateway**
- **Trigger:** Bukti pembayaran DP diunggah.
- **Logika:** 
  - NO $\rightarrow$ Status tetap Pending Verification / Notifikasi penolakan ke Customer.
  - YES $\rightarrow$ Status berubah menjadi Verified, booking menjadi Confirmed, peserta resmi dihitung dalam kuota.

### **Gateway 2 (G2) — D-5 Minimum Quota Gateway**
- **Trigger:** Penanda waktu sistem pada H-5 (00:00 atau jam yang ditentukan) sebelum tanggal keberangkatan.
- **Logika:**
  - $\text{Count(DP Verified)} \ge 20 \rightarrow$ Lanjut ke fase Confirmed, penagihan pelunasan, dan persiapan keberangkatan.
  - $\text{Count(DP Verified)} < 20 \rightarrow$ Otomatis memicu alur penanganan pembatalan (Waiting Owner Action).

### **Gateway 3 (G3) — Owner Decision Gateway**
- **Trigger:** Keberangkatan gagal memenuhi kuota minimum pada D-5.
- **Pilihan Tindakan:**
  1. **Full Refund (100%):** Membuka antrean kerja Finance untuk mengembalikan seluruh dana peserta.
  2. **Transfer to Travel Partner:** Mengalihkan manifes dan alokasi dana ke agensi mitra setelah konfirmasi peserta.

---

## 5. Catatan Arsitektur BPMN
1. **Audit Trail:** Transisi status dari WAITING_OWNER_ACTION menuju REFUNDING atau TRANSFERRED wajib mencatat aktor pengambil keputusan (*Owner ID*), tanggal/waktu keputusan, serta alasan persetujuan.
2. **Pemisahan Notifikasi:** Setiap perubahan jalur keputusan otomatis mengirimkan notifikasi berbasis *template* WhatsApp/Email kepada *Customer* dan *Vendor* terkait.
