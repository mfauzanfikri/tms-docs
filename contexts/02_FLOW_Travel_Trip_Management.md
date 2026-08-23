# FLOW — Alur Operasional End-to-End Travel & Tour Management

## A. Penjadwalan & Rilis Keberangkatan (Scheduling & Departure Release)
1. Tim Operational membuat atau memilih **Master Tour Package (Blueprint)** yang telah memiliki *itinerary*, destinasi, fasilitas (*BOM*), dan *baseline price*.
2. Sistem men-generate jadwal keberangkatan (*Tour Departure*) baik secara **otomatis melalui Flexible Recurrence Engine** (mingguan, bulanan, interval khusus) atau **manual on-demand** oleh Admin.
3. Jadwal yang baru dibuat berstatus **TENTATIVE / DRAFT**.
4. **Pre-Publish Adjustment:** Admin dapat melakukan penyesuaian manual (menggeser tanggal keberangkatan jika ada libur nasional/bentrok kalender, mengubah kuota, dsb.) pada batch tentatif tersebut.
5. Setelah terverifikasi, Admin merilis jadwal menjadi **PUBLISHED_FIXED**.
6. **Price Immutability:** Begitu berstatus *Published*, harga dasar dan jadwal terkunci mutlak (*immutable*) dan siap dipasarkan.

---

## B. Akuisisi Pelanggan & Pemesanan (Customer Acquisition & Booking)
7. *Customer* melihat promosi di saluran pemasaran (media sosial, web, iklan) dan menghubungi Admin via WhatsApp.
8. Admin memberikan informasi detail *itinerary*, kuota yang tersedia, dan harga resmi yang terkunci pada jadwal terpilih.
9. *Customer* memutuskan untuk melakukan pemesanan (*order*).
10. Admin membuat draf *Order / Booking* dan mengirimkan formulir registrasi (*Booking Form*).
11. **Aplikasi Promo & Diskon (Overlay Layer):**
    - Jika terdapat promo moneter (% atau nominal flat / kupon), diskon diterapkan sebagai pengurang total pada *Invoice*.
    - Jika terdapat promo fasilitas tambahan (*complimentary perks*, misal: *Free Makan +1x*), sistem menambahkan penandaan khusus pada profil *Traveler* tanpa memotong harga invoice.
12. *Customer* melengkapi data identitas seluruh peserta (*Traveler*).
13. Admin menerbitkan *Invoice* DP dengan batas waktu pembayaran (*Due Date*).

---

## C. Pembayaran DP & Konfirmasi Booking
14. *Customer* membayar Down Payment (DP) dan mengunggah bukti transfer.
15. Tim Finance memverifikasi bukti pembayaran (*Payment Verification*).
16. Begitu DP terverifikasi:
    - Status *Booking* berubah menjadi **CONFIRMED**.
    - Harga transaksi dikunci (*Price Snapshot*), kebal terhadap perubahan di masa depan.
    - Data *Traveler* (beserta *perks* jika ada) resmi masuk ke dalam **Manifest Keberangkatan**.
    - Jumlah peserta aktif dihitung resmi ke dalam kuota minimum *Tour Departure*.

---

## D. Pembatalan Mandiri oleh Peserta (Individual Cancellation)
17. Jika peserta mengajukan pembatalan sepihak sebelum pelaksanaan trip:
    - **Default Policy (Strict No-Refund):** Sistem memproses pembatalan dengan status pembayaran hangus (Rp 0 refund).
    - **Configured Terms:** Jika paket menerapkan S&K pengembalian bertingkat, sistem menghitung hak refund berdasarkan formula `(Total Bayar * % Refund) - Biaya Operasional`.
    - **Admin Override:** Admin dapat memasukkan nominal refund khusus atas pertimbangan khusus (*discretionary*) dengan mencantumkan alasan tertulis pada *audit log*.
18. Kursi/kuota yang dibatalkan dikembalikan ke kuota kosong keberangkatan, dan manifest diperbarui.

---

## E. Persiapan Operasional & Vendor PO (Tour Preparation)
19. Tim Operational menugaskan **Tour Leader** yang bertanggung jawab memimpin rombongan.
20. Tim Operational menerbitkan *Purchase Order* (PO) dan *Service Voucher* kepada vendor:
    - Vendor Transportasi (*Bus / Van / Shuttle*).
    - Vendor Penginapan (*Hotel / Villa / Homestay*).
    - Vendor Konsumsi (*Restoran / Catering*), termasuk porsi tambahan jika ada peserta dengan *promo perks*.
    - Vendor Tiket & Aktivitas Wisata.
21. Biaya ekstra untuk fasilitas *promo perks* dialokasikan secara internal ke pos **Marketing Expense**.

---

## F. Evaluasi Kuota Minimum H-5 (D-5 Milestone)
22. Sistem memicu evaluasi otomatis pada **H-5 / D-5 sebelum tanggal keberangkatan**.
23. Sistem menghitung total *Traveler* aktif yang memiliki status **DP Terverifikasi**.
24. **Decision Gateway:** Apakah jumlah peserta terverifikasi $\ge 20$?

---

### Skenario 1: Kuota Tercapai ($\ge 20$ Peserta) — Trip CONFIRMED
25. Status *Tour Departure* berubah menjadi **CONFIRMED**.
26. Admin mengirimkan notifikasi penagihan pelunasan (*Final Settlement*) kepada seluruh peserta.
27. Peserta melunasi sisa tagihan, dan Finance memverifikasi pelunasan tersebut.
28. Operational merilis *Final Manifest* dan dokumen *Service Voucher* ke Tour Leader dan Vendor.
29. **Tour Execution:** Keberangkatan dilaksanakan (**IN_OPERATION**), Tour Leader memvalidasi kehadiran dan hak fasilitas peserta, serta melaporkan jalannya tour.
30. Status *Tour Departure* ditutup menjadi **COMPLETED**, dilanjutkan dengan *Financial Closing*.

---

### Skenario 2: Kuota Tidak Tercapai ($< 20$ Peserta) — WAITING OWNER ACTION
25. Status *Tour Departure* ditandai **WAITING OWNER ACTION**.
26. **Owner Decision Gateway:** Owner menentukan tindakan penyelesaian:
    - **Opsi A: 100% Full Refund:** Finance memproses pengembalian dana 100% kepada peserta.
    - **Opsi B: Transfer to Travel Partner:** Peserta dialihkan ke mitra travel dengan jadwal setara atas persetujuan bersama.

---

## G. Penanganan Disrupsi & Force Majeure (Crisis & Disruption Handling)
27. Jika terjadi bencana alam, cuaca ekstrem, atau keadaan kahar (*Force Majeure*), Admin mengaktifkan status **DISRUPTED_EXTREME** pada *Tour Departure*.
28. Admin membuka **Disruption Resolution Desk** dan menghubungi peserta untuk memilih 1 dari 4 opsi resolusi:
    - **1. Cancel with Terms / Full Refund:** Pembatalan trip dengan pengembalian dana darurat.
    - **2. Reschedule:** Menggeser tanggal peserta ke keberangkatan lain pada paket yang sama (dana berpindah 1:1).
    - **3. Switch Plan / Destination:** Mengalihkan peserta ke rute/destinasi alternatif.
    - **4. Switch Package (Pindah Paket Lain):**
      - *Mode Standar:* Rekonsiliasi selisih harga (tagih kekurangan atau kembalikan kelebihan).
      - *Mode Free Waiver (Goodwill):* Tanpa biaya tambahan bagi peserta, selisih harga disubsidi internal oleh agensi.

---

## H. Penutupan Keuangan (Financial Closing)
29. Tim Finance merekonsiliasi seluruh pos keuangan trip:
    - **Gross Customer Revenue:** Total nilai invoice dasar.
    - **Total Discounts & Promo:** Total potongan harga yang diberikan.
    - **Net Customer Revenue:** Realisasi penerimaan bersih.
    - **Total Vendor Fulfillment Cost:** Total tagihan riil vendor.
    - **Marketing & Perk Expenses:** Biaya fasilitas promo cuma-cuma.
    - **Goodwill / Disruption Loss:** Biaya kompensasi *Free Waiver* jika ada.
    - **Realized Net Profit:** $\text{Net Profit} = \text{Net Revenue} - \text{Vendor Costs} - \text{Marketing Perks} - \text{Goodwill Loss}$.
