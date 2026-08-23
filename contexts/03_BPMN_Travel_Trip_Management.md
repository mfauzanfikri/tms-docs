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

## 3. Main BPMN Flow (Diagram Alur Lintas Peran)

```mermaid
flowchart TD
    subgraph Customer["Customer"]
        C_Start([Mulai]) --> C_Ad[Melihat & Klik Iklan]
        C_Ad --> C_Inq[Inquiry via WhatsApp]
        C_Form[Isi Booking Form / Data Traveler]
        C_Pay[Bayar Down Payment DP]
        C_Settle[Bayar Pelunasan / Final Settlement]
        C_Tour([Mengikuti Tour & Selesai])
        C_Refunded([Dana Diterima Kembali 100%])
        C_Transferred([Berangkat Bersama Mitra])
    end

    subgraph Admin["Admin / Sales"]
        A_Resp[Respons Inquiry & Kirim Form]
        A_Order[Buat Booking & Terbitkan Invoice]
        A_InvoiceSettle[Kirim Tagihan Pelunasan]
    end

    subgraph Finance["Finance"]
        F_Verify{G1: DP Terverifikasi?}
        F_SettleVerify[Verifikasi Pelunasan]
        F_Refund[Transfer Full Refund 100%]
        F_Close[Proses Financial Closing]
    end

    subgraph Operational["Operational & Tour Leader"]
        O_Prep[Siapkan Tour Plan & Itinerary]
        O_TL[Assign Tour Leader]
        O_Vendor[Reservasi & Terbitkan PO Vendor]
        O_Manifest[Rilis Final Manifest & Service Voucher]
        O_Execute[Eksekusi Tour di Lapangan]
    end

    subgraph System["System (Automations)"]
        S_DPCheck[Update Status: DP Confirmed]
        S_D5Trigger[Trigger Evaluasi H-5 / D-5]
        S_D5Gate{G2: Peserta DP Valid >= 20?}
        S_Confirm[Status Departure: CONFIRMED]
        S_FlagCancel[Status Departure: WAITING OWNER ACTION]
    end

    subgraph Owner["Owner"]
        O_Decide{G3: Keputusan Disposisi Pembatalan?}
    end

    subgraph Partner["Vendor & Travel Partner"]
        V_PO[Terima PO Layanan: Bus/Hotel/Resto]
        P_Transfer[Terima Delegasi Manifest & Dana]
    end

    %% Workflow Connections
    C_Inq --> A_Resp
    A_Resp --> A_Order
    A_Order --> C_Form
    C_Form --> C_Pay
    C_Pay --> F_Verify

    F_Verify -- Tidak Valid --> A_Resp
    F_Verify -- Valid --> S_DPCheck

    O_Prep --> O_TL --> O_Vendor --> V_PO

    S_DPCheck --> S_D5Trigger
    S_D5Trigger --> S_D5Gate

    %% Jalur Sukses (Kuota Terpenuhi)
    S_D5Gate -- Ya: Kuota >= 20 --> S_Confirm
    S_Confirm --> A_InvoiceSettle
    S_Confirm --> O_Manifest
    A_InvoiceSettle --> C_Settle
    C_Settle --> F_SettleVerify
    F_SettleVerify --> O_Execute
    O_Manifest --> O_Execute
    O_Execute --> C_Tour
    C_Tour --> F_Close

    %% Jalur Gagal (Kuota Tidak Terpenuhi)
    S_D5Gate -- Tidak: Kuota < 20 --> S_FlagCancel
    S_FlagCancel --> O_Decide

    O_Decide -- Pilihan A: Full Refund --> F_Refund
    F_Refund --> C_Refunded

    O_Decide -- Pilihan B: Transfer Partner --> P_Transfer
    P_Transfer --> C_Transferred
```

---

## 4. Decision Gateways Kritis

### **Gateway 1 (G1) — Payment Verification Gateway**
- **Trigger:** Bukti transfer pembayaran DP diunggah oleh Customer/Admin.
- **Logika:** 
  - `NO` $\rightarrow$ Status tetap `Pending Verification` / Notifikasi perbaikan bukti bayar ke Customer.
  - `YES` $\rightarrow$ Status pembayaran berubah menjadi `VERIFIED`, status booking menjadi `CONFIRMED`, data *traveler* resmi dihitung ke dalam kuota keberangkatan.

### **Gateway 2 (G2) — D-5 Minimum Quota Gateway**
- **Trigger:** Pemicu otomatis dari sistem pada **H-5 / D-5 (00:00 WIB)** sebelum tanggal keberangkatan.
- **Logika:**
  - $\text{Count(DP Verified)} \ge 20 \rightarrow$ Status departure berubah ke `CONFIRMED`, memicu penagihan pelunasan (*Final Settlement*) dan penerbitan manifes operasional.
  - $\text{Count(DP Verified)} < 20 \rightarrow$ Status departure berubah ke `CANCELLED / WAITING_OWNER_ACTION`, memicu notifikasi darurat kepada Owner.

### **Gateway 3 (G3) — Owner Decision Gateway**
- **Trigger:** Keberangkatan gagal memenuhi kuota minimum 20 peserta pada evaluasi D-5.
- **Pilihan Tindakan:**
  1. **Full Refund (100%):** Membuka antrean kerja bagi Tim Finance untuk memproses transfer pengembalian seluruh dana masuk ke rekening masing-masing *Customer*.
  2. **Transfer to Travel Partner:** Mengalihkan manifes peserta dan alokasi dana ke agensi mitra setelah konfirmasi dan persetujuan peserta.

---

## 5. Catatan Arsitektur BPMN
1. **Audit Trail:** Transisi status dari `WAITING_OWNER_ACTION` menuju `REFUNDING` atau `TRANSFERRED` wajib mencatat aktor pengambil keputusan (*Owner ID*), *timestamp*, serta catatan disposisi.
2. **Pemisahan Notifikasi:** Setiap perubahan jalur keputusan otomatis memicu notifikasi berbasis template WhatsApp/Email kepada Customer dan Vendor terkait.
