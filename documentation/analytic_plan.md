# Analytical Plan

## Business Theme 1 — Customer Profile Analysis

**Tujuan bisnis**

Memahami karakteristik dasar pelanggan FinanKu dan mengidentifikasi kelompok pelanggan yang lebih banyak mengalami unpaid.

| Business Question                                       | Kolom                | Analisis             | Visualisasi         | Insight yang Diharapkan           |
| ------------------------------------------------------- | -------------------- | -------------------- | ------------------- | --------------------------------- |
| Bagaimana distribusi pelanggan berdasarkan usia?        | Age                  | Distribution         | Histogram           | Mengetahui kelompok usia dominan  |
| Kelompok usia mana yang memiliki unpaid rate tertinggi? | Age, Unpaid Tagging  | Group Comparison     | Boxplot / Bar Chart | Menentukan kelompok usia berisiko |
| Bagaimana komposisi pelanggan berdasarkan kota?         | City                 | Frequency            | Bar Chart           | Mengetahui persebaran pelanggan   |
| Kota mana memiliki unpaid rate tertinggi?               | City, Unpaid Tagging | Groupby + Percentage | Horizontal Bar      | Menentukan prioritas wilayah      |

---

# Business Theme 2 — Financial Behaviour Analysis

**Tujuan bisnis**

Mengetahui apakah kondisi finansial pelanggan berkaitan dengan risiko gagal bayar.

| Business Question                                    | Kolom                   | Analisis           | Visualisasi         | Insight                                |
| ---------------------------------------------------- | ----------------------- | ------------------ | ------------------- | -------------------------------------- |
| Bagaimana distribusi saldo pelanggan?                | Balance Q1-Q4           | Distribution       | Histogram           | Memahami pola saldo                    |
| Apakah pelanggan unpaid memiliki saldo lebih rendah? | Balance, Unpaid Tagging | Mean Comparison    | Boxplot             | Menilai hubungan saldo dan unpaid      |
| Bagaimana perubahan saldo selama periode observasi?  | Balance Q1-Q4           | Trend per Customer | Line/Delta Analysis | Mengetahui perubahan kondisi finansial |

> **Catatan mentor:** Karena proyek ini berfokus pada analisis, kita akan lebih menekankan **rata-rata saldo (Mean Balance)** dan **perubahan saldo (Delta Balance)** sebagai metrik turunan yang mudah dipahami stakeholder.

---

# Business Theme 3 — Product Ownership Analysis

**Tujuan bisnis**

Memahami hubungan antara kepemilikan produk dengan status unpaid.

| Business Question                                           | Kolom                         | Analisis    | Visualisasi | Insight                    |
| ----------------------------------------------------------- | ----------------------------- | ----------- | ----------- | -------------------------- |
| Berapa rata-rata jumlah produk yang dimiliki pelanggan?     | NumOfProducts                 | Descriptive | Bar Chart   | Profil kepemilikan produk  |
| Apakah pelanggan dengan sedikit produk lebih sering unpaid? | NumOfProducts, Unpaid Tagging | Comparison  | Boxplot     | Loyalitas vs risiko        |
| Apakah kepemilikan kartu kredit berkaitan dengan unpaid?    | HasCrCard                     | Crosstab    | Stacked Bar | Hubungan kepemilikan kartu |

---

# Business Theme 4 — Customer Activity Analysis

**Tujuan bisnis**

Melihat apakah pelanggan yang aktif cenderung memiliki risiko lebih rendah.

| Business Question                                    | Kolom                        | Analisis  | Visualisasi | Insight                    |
| ---------------------------------------------------- | ---------------------------- | --------- | ----------- | -------------------------- |
| Bagaimana distribusi status keaktifan pelanggan?     | ActiveMember                 | Frequency | Bar Chart   | Profil aktivitas pelanggan |
| Apakah pelanggan aktif memiliki unpaid lebih rendah? | ActiveMember, Unpaid Tagging | Crosstab  | Stacked Bar | Aktivitas vs risiko        |

---

# Business Theme 5 — Credit Risk Profile

Ini adalah bagian terpenting dari seluruh EDA.

| Business Question                                           | Kolom                | Analisis             | Visualisasi             | Insight                   |
| ----------------------------------------------------------- | -------------------- | -------------------- | ----------------------- | ------------------------- |
| Siapa pelanggan yang paling berisiko?                       | Semua variabel utama | Segmentasi           | Heatmap / Summary Table | Profil pelanggan berisiko |
| Faktor apa yang paling sering muncul pada pelanggan unpaid? | Semua variabel       | Comparative Analysis | Ringkasan               | Dasar rekomendasi bisnis  |

---
