# Product Documentation Changelog

Semua perubahan dan riwayat versi dokumen di folder `product/` (serta PRD rilis) dicatat secara terpusat dalam berkas ini.

Format pencatatan mengikuti panduan:
- `[YYYY-MM-DD] - [Document ID / Name] - Version X.X`
- Rincian perubahan (*Added, Changed, Deprecated, Removed, Fixed*).

---

## [2026-09-08]

### [DOCS-APPROVAL] Product Documentation Baseline Approved
- **Status:** Approved
- **Documents:**
  - `01_BUSINESS_ANALYSIS.md` (Version 1.2) - Status: Approved
  - `02_BRD.md` (Version 1.3) - Status: Approved
  - `03_FEATURE_CATALOG_AND_SCOPE.md` (Version 1.0) - Status: Approved
- **Changes:**
  - Persetujuan formal dokumen fondasi bisnis, BRD, dan Feature Catalog sebagai acuan normatif rilis MVP-1.
  - Penegasan evaluasi ambang batas kuota minimum dinamis (`minQuota`, default 20 pax) pada `OPS-GATE-04`.

---

## [2026-09-01]

### [BRD-01] 02_BRD.md - Version 1.3
- **Status:** In Review
- **Changes:** Menyatukan vocabulary status, memperjelas gate H-5, memisahkan quota failure dan force majeure, serta memformalkan aturan finansial dan scope late-joiner MVP.

### [BA-01] 01_BUSINESS_ANALYSIS.md - Version 1.3
- **Status:** In Review
- **Changes:** Memperjelas bahwa late joiner ditolak secara default pada MVP dan otomatisasi late-joiner berada di Phase 3.

---

## [2026-09-01]

### [BA-01] 01_BUSINESS_ANALYSIS.md - Version 1.2
- **Status:** In Review
- **Changes:** Menambahkan model BEP dinamis, pemisahan Open/Private Tour, milestone operasional, KPI governance, dan batasan MVP.

### [BRD-01] 02_BRD.md - Version 1.2
- **Status:** In Review
- **Changes:** Menambahkan requirement IDs, traceability, acceptance rules, financial controls, data governance, serta policy boundaries.

## [2026-08-29]

### [BA-01] 01_BUSINESS_ANALYSIS.md - Version 1.1
- **Status:** In Review
- **Author:** Product & Operations Team
- **Changes:**
  - Menambahkan ranah analisis risiko penambahan peserta di tengah perjalanan (*Mid-Trip / Late-Joiner Addition*).
  - Memperbarui diagram Mermaid alur tantangan operasional dengan menambahkan node $P7$, $I4$, dan solusi sistemik $S7$ (*Emergency Add-Traveler Engine & Instant Waiver*).

### [BRD-01] 02_BRD.md - Version 1.1
- **Status:** In Review
- **Author:** Product & Operations Team
- **Changes:**
  - Menambahkan aturan bisnis formal **Rule 4.7 (Mid-Trip Addition Policy)** yang mencakup 4 kriteria kelayakan mutlak (*Gatekeeper*), larangan transaksi tunai lapangan, formula *dynamic pricing late-joiner*, dan otomatisasi sinkronisasi *Live Manifest* serta revisi PO vendor.
  - Memperbarui dekomposisi modul fungsional makro (Modul 03, 04, 06, 07, 08, dan 09) untuk mendukung alur *Emergency Add-Traveler*.

### [REG-01] Product Metadata.md - Version 1.1
- **Status:** In Review
- **Author:** Product & Operations Team
- **Changes:**
  - Pemutakhiran status dokumen `01_BUSINESS_ANALYSIS.md` dan `02_BRD.md` menjadi Version 1.1 (In Review).

---

## [2026-08-28]

### [BA-01] 01_BUSINESS_ANALYSIS.md - Version 1.0
- **Status:** Draft
- **Author:** Product & Operations Team
- **Changes:**
  - Inisialisasi dokumen Business Analysis & Strategic Discovery.
  - Dokumentasi Operating Model agensi sebagai *Tour Operator / Orchestrator*.
  - Pemetaan struktur biaya *Fixed Costs* vs *Variable Costs* serta rasionalisasi kuota minimum $N \ge 20$.
  - Penyusunan matriks analisis masalah operasional eksisting dan risiko potensial masa depan (*race conditions, floating funds, fraud, vendor default*).
  - Penetapan stakeholder matrix dan sasaran strategis/KPI.

### [BRD-01] 02_BRD.md - Version 1.0
- **Status:** Draft
- **Author:** Product & Operations Team
- **Changes:**
  - Inisialisasi dokumen formal Business Requirements Document (BRD).
  - Dekomposisi konsep inti domain: *Tour Package Blueprint* vs *Tour Departure Instance*, BOM fasilitas, *Price Snapshotting*, dan *Perks Overlay*.
  - Pemetaan taksonomi 8 aktor dan matriks hak akses (*RBAC*).
  - Formalisasi master aturan bisnis (*Price Immutability, Temporary Seat Hold, Evaluasi Kuota H-5, Matriks Disrupsi 4 Jalur, S&K Pembatalan Mandiri*).
  - Perancangan diagram alur operasional *end-to-end* To-Be & BPMN *swimlane*.
  - Dekomposisi 10 modul sistem makro.

### [REG-01] Product Metadata.md - Version 1.0
- **Status:** Draft
- **Author:** Product & Operations Team
- **Changes:**
  - Inisialisasi master mapping dokumen terhadap target rilis produk `v1.0 (TMS Core Operations MVP)`.
