# FLOW — End-to-End Travel Trip Management

## A. Customer Acquisition
1. Customer melihat iklan sosial media.
2. Customer klik iklan.
3. Customer diarahkan ke WhatsApp Admin.
4. Customer melakukan inquiry.
5. Admin memberikan informasi.
6. Customer memutuskan order.

## B. Booking
7. Admin membuat order.
8. Admin mengirim form order.
9. Customer mengisi form.
10. Admin membuat invoice.
11. Customer melakukan pembayaran DP.
12. Finance/Admin memverifikasi pembayaran.
13. Jika DP terverifikasi, booking menjadi participant confirmed.
14. Participant masuk perhitungan minimum Open Trip.

## C. Trip Preparation
15. Trip memiliki planning.
16. Operational menyiapkan destination dan activity.
17. Operational menentukan Tour Leader.
18. Operational melakukan booking vendor bus.
19. Jika diperlukan, booking penginapan.
20. Booking restoran/vendor konsumsi.
21. Dokumen dan transaksi disimpan pada Trip.

## D. H-5 Minimum Participant
22. Sistem mencapai H-5 keberangkatan.
23. Sistem menghitung participant berdasarkan DP yang sudah terverifikasi.
24. Gateway: apakah participant >= 20?

### Jika YA
25. Trip Confirmed.
26. Persiapan dilanjutkan.
27. Peserta yang masih DP melakukan pelunasan.
28. Trip berangkat.
29. Trip dilaksanakan.
30. Trip selesai.
31. Finance melakukan closing trip.

### Jika TIDAK
25. Trip tidak memenuhi minimum.
26. Trip masuk status Cancelled / Waiting Owner Action.
27. Owner memilih:
   - Full Refund, atau
   - Transfer ke Travel Partner.

### Full Refund
28. Finance menghitung total pembayaran masing-masing peserta.
29. Refund diproses.
30. Bukti refund disimpan.
31. Status peserta menjadi Refunded.
32. Trip ditutup.

### Transfer Travel Partner
28. Owner/operational menentukan travel partner.
29. Peserta diberi informasi dan mengikuti mekanisme persetujuan yang ditetapkan perusahaan.
30. Data/transaksi dialihkan sesuai kesepakatan.
31. Bukti transfer/disposisi disimpan.
32. Status peserta menjadi Transferred.
33. Trip ditutup.

## E. Financial Closing
- Total revenue peserta.
- Total payment received.
- Outstanding peserta.
- Total vendor cost.
- Outstanding vendor.
- Refund jika ada.
- Other cost.
- Estimasi/actual profit.

## F. Critical Rule
**Participant Count untuk Open Trip = jumlah peserta dengan DP yang sudah terverifikasi.**

Peserta yang baru inquiry, baru mengisi form, atau belum membayar DP **tidak dihitung** dalam minimum 20 peserta.
