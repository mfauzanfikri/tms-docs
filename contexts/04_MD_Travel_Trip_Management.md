# MD — Module Design / System Modules

## 1. Arsitektur Modul
```text
TRAVEL MANAGEMENT SYSTEM
├── Dashboard
├── Customer
├── Trip Management
├── Booking & Order
├── Participant
├── Finance
│   ├── Invoice Peserta
│   ├── Payment Peserta
│   ├── Refund
│   ├── Vendor Invoice
│   └── Vendor Payment
├── Operational
│   ├── Planning
│   ├── Itinerary
│   ├── Destination
│   ├── Activity
│   └── Tour Leader
├── Vendor
├── Travel Partner
├── Document Management
├── User & Role
└── Report
```

## 2. Trip sebagai pusat data
Satu Trip menghubungkan:
- Participants
- Booking
- Invoice
- Payment
- Refund/Transfer
- Itinerary
- Destination
- Activity
- Tour Leader
- Vendors
- Vendor payments
- Documents

## 3. Status Utama
### Trip
DRAFT → OPEN FOR BOOKING → H-5 VALIDATION → CONFIRMED → PREPARATION → DEPARTURE → ON TRIP → COMPLETED

Jika minimum gagal:
H-5 VALIDATION → CANCELLED → WAITING OWNER ACTION → REFUNDING → REFUNDED

atau:
H-5 VALIDATION → CANCELLED → WAITING OWNER ACTION → TRANSFERRED

### Booking/Participant
INQUIRY → ORDER → WAITING DP → DP PAID/CONFIRMED → FULLY PAID → JOINED TRIP → COMPLETED

### Payment
PENDING VERIFICATION → VERIFIED → ALLOCATED

### Refund
REQUESTED → APPROVED → PROCESSING → REFUNDED

## 4. Role
### Admin
Customer, booking, invoice, participant, dokumen, komunikasi operasional.

### Finance
Payment verification, refund, vendor payment, laporan keuangan.

### Operational
Planning, itinerary, vendor, Tour Leader.

### Tour Leader
Melihat detail trip, peserta, itinerary, dan kebutuhan operasional.

### Owner
Approval/decision penting, termasuk penanganan trip yang tidak mencapai minimum.

## 5. Modul H-5
Input:
- Trip
- Departure date
- Minimum participant
- DP verified count

Process:
1. Tentukan H-5.
2. Hitung participant dengan DP terverifikasi.
3. Bandingkan dengan minimum.
4. Jika >= minimum → Confirmed.
5. Jika < minimum → Cancelled/Waiting Owner Action.
6. Owner memilih Refund atau Transfer.

## 6. Modul Finance
### Participant Finance
Invoice → Payment(s) → Outstanding → Paid

### Trip Finance
Participant Revenue - Vendor Cost - Other Cost = Profit

### Cancellation Finance
Payment Received → Refund / Transfer

## 7. Modul Document
Semua dokumen dikaitkan dengan entitas:
Trip / Booking / Invoice / Payment / Vendor / Refund / Transfer.

## 8. Dashboard
- Trip aktif
- Trip H-5
- Trip yang belum memenuhi minimum
- Jumlah participant
- DP vs lunas
- Outstanding
- Vendor payable
- Revenue
- Cost
- Profit
