# FLOW — Alur Operasional End-to-End Travel & Tour Management

## A. Akuisisi Pelanggan (Customer Acquisition)
1. *Customer* melihat iklan di media sosial atau saluran promosi.
2. *Customer* mengklik tautan iklan dan diarahkan ke WhatsApp Admin.
3. *Customer* melakukan *inquiry* terkait *Tour Plan* atau jadwal keberangkatan (*Tour Departure*).
4. Admin memberikan informasi detail, ketersediaan kuota, dan harga.
5. *Customer* memutuskan untuk melakukan pemesanan (*order*).

## B. Pemesanan & Pembayaran DP (Booking & Down Payment)
6. Admin membuat draf *Order / Booking*.
7. Admin mengirimkan formulir registrasi (*Booking Form*) kepada *Customer*.
8. *Customer* mengisi data *Traveler* (nama, kontak, identitas) pada formulir.
9. Admin menerbitkan *Invoice* pembayaran dengan rincian total biaya dan batas pembayaran DP (*Due Date*).
10. *Customer* melakukan pembayaran Down Payment (DP) dan mengunggah bukti transfer.
11. Tim Finance memverifikasi bukti pembayaran masuk (*Payment Verification*).
12. Begitu DP terverifikasi, status *Booking* berubah menjadi Confirmed dan *Traveler* tercatat resmi dalam *Manifest*.
13. *Traveler* resmi dihitung ke dalam kalkulasi kuota minimum *Tour Departure*.

## C. Persiapan Operasional (Tour Preparation)
14. Tim Operational menyiapkan *Itinerary*, destinasi, dan susunan aktivitas dari *Tour Plan*.
15. Tim Operational menugaskan **Tour Leader** yang bertanggung jawab memimpin keberangkatan.
16. Tim Operational melakukan reservasi dan menerbitkan *Purchase Order* (PO) kepada:
    - Vendor Transportasi (*Bus / Van / Shuttle*).
    - Vendor Penginapan (*Hotel / Villa / Homestay*), jika bermalam.
    - Vendor Konsumsi (*Restoran / Catering*).
17. Dokumen kontrak, voucher layanan, dan rincian transaksi vendor ditautkan langsung ke entitas *Tour Departure*.

## D. Evaluasi Kuota Minimum H-5 (D-5 Minimum Participant Milestone)
18. Sistem memicu evaluasi otomatis pada **H-5 / D-5 sebelum tanggal keberangkatan**.
19. Sistem menghitung total *Traveler* aktif yang memiliki status **DP Terverifikasi**.
20. **Decision Gateway:** Apakah jumlah peserta terverifikasi $\ge 20$?

---

### Skenario 1: Kuota Tercapai ($\ge 20$ Peserta) — Trip CONFIRMED
21. Status *Tour Departure* berubah menjadi CONFIRMED.
22. Admin mengirimkan notifikasi penagihan pelunasan (*Final Settlement*) kepada seluruh peserta.
23. Peserta melakukan pelunasan sebelum batas waktu yang ditentukan.
24. Operational merilis *Final Manifest* dan dokumen *Service Voucher* kepada Tour Leader dan Vendor.
25. **Tour Execution:** Keberangkatan dilaksanakan (IN_OPERATION), aktivitas dipantau, hingga perjalanan selesai.
26. Status *Tour Departure* ditutup menjadi COMPLETED.
27. Tim Finance memproses penutupan buku operasional (*Financial Closing*).

---

### Skenario 2: Kuota Tidak Tercapai ($< 20$ Peserta) — WAITING OWNER ACTION
21. *Tour Departure* tidak memenuhi kuota minimum dan otomatis masuk status CANCELLED / WAITING OWNER ACTION.
22. **Owner Decision Gateway:** Owner menentukan tindakan penyelesaian:

#### Opsi A: Full Refund (100% Pengembalian Dana)
23. Tim Finance merekapitulasi seluruh dana masuk per *Booking*.
24. Finance memproses transfer pengembalian dana 100% kepada setiap *Customer*.
25. Bukti transfer *refund* diunggah ke sistem.
26. Status pembayaran *Customer* diperbarui menjadi REFUNDED.
27. Status *Tour Departure* ditutup menjadi CLOSED_CANCELLED.

#### Opsi B: Transfer to Travel Partner (Pengalihan ke Mitra)
23. Owner/Operational menentukan *Travel Partner* yang memiliki jadwal keberangkatan serupa.
24. Peserta dihubungi untuk konfirmasi dan persetujuan pengalihan.
25. Data *manifest* dan alokasi dana ditransfer ke mitra *Travel Partner*.
26. Bukti disposisi/perjanjian pengalihan diunggah ke sistem.
27. Status peserta diperbarui menjadi TRANSFERRED dan *Tour Departure* ditutup.

---

## E. Penutupan Keuangan (Financial Closing)
Laporan ringkasan finansial merekonsiliasi:
- **Total Customer Revenue:** Total nilai invoice peserta.
- **Total Payment Received:** Realisasi dana masuk (DP + Pelunasan).
- **Outstanding Receivables:** Sisa piutang peserta.
- **Total Vendor Cost:** Total tagihan vendor transportasi, penginapan, restoran, dll.
- **Vendor Payables / Outstanding:** Sisa hutang ke vendor.
- **Total Refunds Issued:** Total pengembalian dana jika terjadi pembatalan.
- **Gross Profit Realized:** $\text{Gross Profit} = \text{Total Payment Received} - \text{Total Vendor Costs} - \text{Other Expenses}$.

---

## F. Aturan Kritis (Critical Rule)
> [!IMPORTANT]
> **Kalkulasi Kuota Peserta (Participant Count) = Jumlah Traveler dengan DP yang sudah TERVERIFIKASI oleh Finance.**
> 
> *Inquiry*, formulir registrasi yang belum dibayar, atau pembayaran DP yang belum diverifikasi oleh Finance **TIDAK BOLEH dihitung** ke dalam kuota minimum keberangkatan.
