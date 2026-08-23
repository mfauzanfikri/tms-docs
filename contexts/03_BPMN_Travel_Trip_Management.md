# BPMN — Travel & Tour Operations Management System (To-Be)

## 1. Pool
**Travel & Tour Operations System**

## 2. Swimlane (Aktor & Tanggung Jawab)
1. **Customer:** Mengajukan inquiry, mengisi form, memanfaatkan kupon/promo, membayar DP & pelunasan, mengajukan reschedule/batal jika ada kendala.
2. **Admin / Sales:** Menangani inquiry, menerapkan promo, membuat order & invoice, menyesuaikan draf jadwal pre-publish, menangani meja resolusi disrupsi & pembatalan.
3. **Finance:** Verifikasi pembayaran (DP & Pelunasan), memproses refund, membayar tagihan vendor, mencatat beban promo & goodwill, melakukan *financial closing*.
4. **Operational:** Mengelola master paket (BOM), mengatur mesin rekurensi jadwal, menugaskan Tour Leader, menerbitkan PO & voucher layanan ke vendor.
5. **Tour Leader:** Mengakses live manifest di lapangan, memvalidasi kehadiran & *special perks* peserta, melaporkan status & insiden.
6. **Owner / Executive:** Persetujuan pembatalan kuota D-5 (*Full Refund* vs *Partner Transfer*), persetujuan *override* dan subsidi *Free Waiver*.
7. **Vendor & Travel Partner:** Menerima PO layanan, menyediakan akomodasi/transportasi/konsumsi, menerima peserta transfer.
8. **System (Automations):** Mesin rekurensi jadwal, penguncian harga *published*, kalkulasi kuota D-5 otomatis, kalkulasi promo & invoice, snapshot harga booking.

---

## 3. Main BPMN Flow (Diagram Alur Lintas Peran)

```mermaid
flowchart TD
    %% Swimlane Definitions
    subgraph Operational["Operational & Tour Planning"]
        O_Package[Buat Master Package Blueprint & BOM]
        O_RecurEngine[Set Aturan Recurrence: Mingguan/Bulanan/Custom]
        O_AssignTL[Assign Tour Leader]
        O_VendorPO[Reservasi & Terbitkan PO Vendor + Extra Perks]
        O_Manifest[Rilis Final Manifest ke TL & Vendor]
        O_FieldExec[Tour Leader Pimpin Trip & Validasi Perks]
    end

    subgraph System["System (Automations & Engines)"]
        S_GenSchedule[Generate Draf Departure: TENTATIVE]
        S_LockPrice[Status PUBLISHED_FIXED: Lock Base Price]
        S_ApplyPromo[Hitung Diskon / Tandai Perks di Manifest]
        S_PriceSnapshot[Lock Price Snapshot on Booking Confirmed]
        S_D5Trigger[Trigger Evaluasi H-5 / D-5]
        S_D5Gate{G1: Peserta DP Valid >= 20?}
        S_ConfirmDep[Set Departure: CONFIRMED]
        S_FlagD5Cancel[Set Departure: WAITING OWNER ACTION]
    end

    subgraph Admin["Admin / Sales Desk"]
        A_AdjustDate[Pre-Publish Adjustment: Sesuaikan Tanggal/Kuota]
        A_Publish[Publish Jadwal ke Publik]
        A_Order[Buat Booking Order & Pasang Promo]
        A_InvoiceSettle[Kirim Tagihan Pelunasan]
        A_DisruptionDesk{G2: Meja Resolusi Disrupsi / Force Majeure}
        A_IndivCancel[Proses Pembatalan Individu: No-Refund / S&K]
    end

    subgraph Customer["Customer / Traveler"]
        C_Inq[Inquiry Jadwal & Paket]
        C_Form[Isi Form & Masukkan Kode Promo]
        C_PayDP[Bayar Down Payment DP]
        C_Settle[Bayar Pelunasan]
        C_Trip([Ikuti Tour & Nikmati Fasilitas/Perks])
        C_RefundDone([Terima Dana Pengembalian])
        C_Rebooked([Jadwal / Paket Baru Terkonfirmasi])
    end

    subgraph Finance["Finance & Ledgers"]
        F_VerifyDP{G3: DP Valid?}
        F_VerifySettle[Verifikasi Pelunasan]
        F_ProcessRefund[Eksekusi Transfer Refund]
        F_ReconTransfer[Rekonsiliasi Pindah Paket: Selisih vs Free Waiver]
        F_Close[Financial Closing: Revenue, Vendor, Promo, Goodwill]
    end

    subgraph Owner["Owner / Executive"]
        O_D5Decision{G4: Keputusan Kuota Gagal D-5?}
    end

    subgraph Partner["Vendor & Travel Partner"]
        V_POAccept[Terima PO Layanan & Ekstra Porsi Promo]
        P_TransferAccept[Terima Rombongan Pengalihan]
    end

    %% Flow: 1. Penjadwalan & Rilis
    O_Package --> O_RecurEngine --> S_GenSchedule
    S_GenSchedule --> A_AdjustDate
    A_AdjustDate --> A_Publish --> S_LockPrice

    %% Flow: 2. Booking & DP
    S_LockPrice --> C_Inq
    C_Inq --> A_Order
    A_Order --> S_ApplyPromo --> C_Form
    C_Form --> C_PayDP --> F_VerifyDP

    F_VerifyDP -- Tidak Valid --> A_Order
    F_VerifyDP -- Valid --> S_PriceSnapshot
    S_PriceSnapshot --> S_D5Trigger

    %% Flow: 3. Persiapan Operasional
    S_PriceSnapshot --> O_AssignTL --> O_VendorPO --> V_POAccept

    %% Flow: 4. Milestone D-5
    S_D5Trigger --> S_D5Gate
    S_D5Gate -- Ya: Kuota >= 20 --> S_ConfirmDep
    S_ConfirmDep --> A_InvoiceSettle
    S_ConfirmDep --> O_Manifest
    A_InvoiceSettle --> C_Settle --> F_VerifySettle
    F_VerifySettle --> O_FieldExec
    O_Manifest --> O_FieldExec --> C_Trip --> F_Close

    %% Flow: 5. Kegagalan Kuota D-5
    S_D5Gate -- Tidak: Kuota < 20 --> S_FlagD5Cancel
    S_FlagD5Cancel --> O_D5Decision
    O_D5Decision -- Full Refund 100% --> F_ProcessRefund --> C_RefundDone
    O_D5Decision -- Transfer Partner --> P_TransferAccept

    %% Flow: 6. Penanganan Disrupsi & Bencana
    A_DisruptionDesk -- 1. Cancel / Full Refund --> F_ProcessRefund
    A_DisruptionDesk -- 2. Reschedule (Paket Sama) --> S_PriceSnapshot
    A_DisruptionDesk -- 3. Switch Plan / Rute --> S_PriceSnapshot
    A_DisruptionDesk -- 4. Switch Package Lain --> F_ReconTransfer --> C_Rebooked

    %% Flow: 7. Pembatalan Mandiri Peserta
    C_Inq -. Permintaan Batal .-> A_IndivCancel
    A_IndivCancel --> F_ProcessRefund
```

---

## 4. Decision Gateways Summary

| Gateway | Penanggung Jawab | Kondisi & Cabang Keputusan |
|---|---|---|
| **G1: Evaluasi Kuota D-5** | System (Otomatis) | • **$\ge 20$ Peserta DP Valid:** Trip CONFIRMED $\rightarrow$ Terbitkan pelunasan.<br>• **$< 20$ Peserta DP Valid:** WAITING OWNER ACTION. |
| **G2: Meja Resolusi Disrupsi / Force Majeure** | Admin / Sales | • **1. Cancel:** Pengembalian dana darurat.<br>• **2. Reschedule:** Pindah tanggal 1:1.<br>• **3. Switch Plan:** Pindah rute alternatif.<br>• **4. Switch Package:** Pindah paket (Mode Standar vs Free Waiver). |
| **G3: Verifikasi DP Masuk** | Finance | • **Valid:** Booking status CONFIRMED, harga di-snapshot, kuota terkunci.<br>• **Tidak Valid:** Notifikasi ke Admin/Customer untuk perbaikan bukti bayar. |
| **G4: Keputusan Kuota Gagal D-5** | Owner / Executive | • **Full Refund 100%:** Dana dikembalikan utuh ke seluruh peserta.<br>• **Transfer Partner:** Manifest dan alokasi dana didelegasikan ke mitra. |
