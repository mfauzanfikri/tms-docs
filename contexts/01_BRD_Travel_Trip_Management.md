# BRD — Travel Trip Management System

## 1. Latar Belakang
Perusahaan merupakan agensi jasa travel wisata yang menyediakan Open Trip dan Private Trip. Operasional melibatkan peserta, Tour Leader, planning wisata, destinasi, aktivitas, vendor bus, vendor penginapan, dan vendor restoran.

Saat ini proses administrasi masih banyak dilakukan secara manual. Invoice, bukti pembayaran peserta, dan dokumen pembayaran vendor masih tersebar sehingga menyulitkan monitoring, pencarian dokumen, rekonsiliasi, dan kontrol operasional.

## 2. Tujuan
- Memusatkan data trip dan peserta.
- Mengelola booking, invoice, pembayaran, dan refund secara terstruktur.
- Mengelola planning dan vendor dalam satu trip.
- Memudahkan monitoring status peserta dan trip.
- Mengurangi dokumen tercecer dan human error.
- Menyediakan informasi keuangan trip dan histori transaksi.

## 3. Scope
### In Scope
- Customer & participant management
- Open Trip & Private Trip
- Inquiry/order/booking
- Invoice peserta
- Payment peserta
- Minimum participant validation
- Refund / transfer ke travel partner
- Trip planning & itinerary
- Tour Leader
- Vendor bus, penginapan, restoran
- Invoice dan payment vendor
- Document management
- Dashboard & reporting
- Role & approval

### Out of Scope Awal
- Integrasi otomatis dengan platform iklan
- Payment gateway
- Booking tiket transportasi umum otomatis
- GPS tracking
- Full accounting system

## 4. Stakeholder
- Customer/Peserta
- Admin
- Finance
- Operational
- Tour Leader
- Owner
- Vendor
- Travel Partner

## 5. Business Rules
| ID | Rule |
|---|---|
| BR-01 | Sistem mendukung Open Trip dan Private Trip. |
| BR-02 | Open Trip memiliki minimum 20 peserta, sesuai rule saat ini. |
| BR-03 | Peserta yang belum DP tidak dihitung sebagai peserta minimum. |
| BR-04 | DP harus terverifikasi agar dihitung sebagai peserta. |
| BR-05 | Validasi minimum peserta dilakukan pada H-5 keberangkatan. |
| BR-06 | Jika jumlah peserta >= 20 pada H-5, trip dapat dilanjutkan. |
| BR-07 | Jika jumlah peserta < 20 pada H-5, trip tidak memenuhi minimum dan proses cancel dimulai. |
| BR-08 | Keputusan penanganan setelah minimum tidak tercapai berada pada Owner. |
| BR-09 | Owner memilih Full Refund atau dialihkan ke travel lain. |
| BR-10 | Full Refund mengembalikan seluruh pembayaran peserta yang telah diterima, sesuai kebijakan perusahaan. |
| BR-11 | Peserta yang belum DP tidak dihitung dalam minimum participant. |
| BR-12 | Perubahan/override rule harus memiliki kewenangan dan histori sesuai keputusan Owner. |

## 6. Functional Requirements
### FR-01 Customer
Sistem dapat membuat, mengubah, mencari, dan melihat histori customer.

### FR-02 Trip
Sistem dapat membuat trip, menentukan tipe trip, tanggal keberangkatan, minimum participant, status, dan detail operasional.

### FR-03 Booking
Sistem mencatat inquiry/order/booking dan membedakan booking dengan participant confirmed.

### FR-04 Participant
Sistem menampilkan peserta yang sudah DP terverifikasi sebagai peserta yang dihitung untuk minimum Open Trip.

### FR-05 Invoice Peserta
Sistem membuat invoice, total harga, DP, outstanding, due date, dan status pembayaran.

### FR-06 Payment Peserta
Sistem mencatat setiap pembayaran, nominal, tanggal, metode, bukti, dan status verifikasi.

### FR-07 H-5 Validation
Sistem melakukan validasi jumlah peserta pada H-5 dan menghasilkan status memenuhi/tidak memenuhi minimum.

### FR-08 Cancellation Handling
Jika minimum tidak tercapai, sistem membuat status waiting owner action dan menyediakan pilihan Full Refund atau Transfer to Travel Partner.

### FR-09 Refund
Sistem mencatat nominal refund, peserta, tanggal, metode, bukti refund, dan status.

### FR-10 Travel Partner Transfer
Sistem mencatat travel partner, peserta yang dialihkan, nilai transaksi, dan status transfer.

### FR-11 Planning
Sistem mengelola destinasi, aktivitas, durasi, itinerary, bus, penginapan, dan restoran.

### FR-12 Vendor
Sistem mengelola master vendor dan keterkaitannya dengan trip.

### FR-13 Vendor Payment
Sistem mencatat invoice/tagihan vendor, DP, pelunasan, outstanding, dan bukti pembayaran.

### FR-14 Document Management
Dokumen disimpan dan dikaitkan dengan customer, trip, invoice, payment, vendor, refund, atau transfer.

### FR-15 Dashboard
Dashboard menampilkan trip aktif, peserta, status pembayaran, outstanding, vendor cost, dan estimasi/aktual profit.

## 7. Non-Functional Requirements
- Role-based access control.
- Audit trail untuk perubahan penting.
- Pencarian data cepat.
- Dokumen tersimpan berdasarkan konteks transaksi/trip.
- Interface sederhana untuk operasional.
- Backup dan keamanan data.

## 8. Acceptance Criteria Utama
1. Customer yang baru mengisi form tetapi belum DP tidak dihitung sebagai participant minimum.
2. Payment yang belum diverifikasi tidak dihitung sebagai DP confirmed.
3. Open Trip dengan 20 DP terverifikasi atau lebih pada H-5 berstatus dapat berangkat.
4. Open Trip dengan 19 atau kurang pada H-5 masuk proses cancel.
5. Owner dapat memilih Full Refund atau Transfer to Travel Partner.
6. Setiap refund memiliki histori dan bukti.
7. Satu trip dapat menampilkan peserta, invoice, payment, planning, vendor, Tour Leader, dan dokumen dari satu tempat.

## 9. Open Questions untuk Finalisasi
- Apakah Owner boleh override minimum 20?
- Apakah sistem melakukan auto-cancel langsung atau hanya auto-flag lalu Owner melakukan konfirmasi?
- Apakah refund selalu 100% tanpa pengecualian?
- Bagaimana aturan jika peserta cancel setelah H-5?
- Bagaimana perlakuan biaya vendor yang sudah dibayar ketika trip cancel?
- Bagaimana mekanisme persetujuan peserta jika dialihkan ke travel lain?
