# Technical Documentation Changelog

Semua perubahan dan riwayat versi dokumen di folder `technical/` (arsitektur, database schema, API contracts, dan FRD) dicatat secara terpusat dalam berkas ini.

Format pencatatan mengikuti panduan:
- `[YYYY-MM-DD] - [Document ID / Name] - Version X.X`
- Rincian perubahan (*Added, Changed, Deprecated, Removed, Fixed*).

## [2026-09-10]

### [DOMAIN-01] 00_DOMAIN_MODEL.md - Version 1.1
- **Status:** Approved
- **Author:** Product, Operations & Engineering Team
- **Changes:**
  - Menyelaraskan relasi `Customer` dan `Traveler` (peserta/pax) pada Bagian 2 (Modeling Decisions) dan Bagian 3 (Domain Glossary).
  - Menyelesaikan keputusan terbuka (*Open Decision #1*) pada Bagian 11 seiring implementasi `BOOK-VAULT-04` di mana satu booking komersial dapat meregistrasikan banyak traveler ke manifest keberangkatan.

---

## [2026-09-08]

### [DOMAIN-01] 00_DOMAIN_MODEL.md - Version 1.0
- **Status:** Approved
- **Author:** Product, Operations & Engineering Team
- **Changes:**
  - Persetujuan formal Conceptual & Functional Domain Model sebagai acuan arsitektur rekayasa teknis sistem TMS.

---

## [2026-08-28]

### [INIT] Technical Documentation Hub Initialized
- Inisialisasi direktori arsitektur teknis dan standarisasi rekayasa sistem TMS.
