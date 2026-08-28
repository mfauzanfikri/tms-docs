# Product Documentation Changelog

Semua perubahan dan riwayat versi dokumen di folder `product/` (serta PRD rilis) dicatat secara terpusat dalam berkas ini.

Format pencatatan mengikuti panduan:
- `[YYYY-MM-DD] - [Document ID / Name] - Version X.X`
- Rincian perubahan (*Added, Changed, Deprecated, Removed, Fixed*).

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
