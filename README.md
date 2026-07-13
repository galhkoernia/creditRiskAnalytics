# Analisis Risiko Kredit FinanKu

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0+-green.svg)](https://pandas.pydata.org/)
[![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow.svg)](https://powerbi.microsoft.com/)

---

## Ringkasan Eksekutif

<!-- 
PERTANYAAN KRITIS:
1. Ceritakan dalam 3-4 kalimat: Apa masalahnya, apa yang Anda lakukan, dan apa hasilnya?
2. Sebutkan satu insight paling penting yang ditemukan.
3. Berikan 1 rekomendasi bisnis utama.
-->

**Tulis jawaban Anda di sini.**

---

## Latar Belakang & Problem Statement

<!-- 
PERTANYAAN KRITIS:
1. Siapa FinanKu dan apa bisnis utamanya?
2. Apa tantangan spesifik yang mereka hadapi?
3. Mengapa masalah ini penting untuk diselesaikan?
4. Apa tujuan utama proyek ini (dalam bahasa bisnis)?
-->

**Tulis jawaban Anda di sini.**

---

## Tools & Technologies

<!--
PERTANYAAN KRITIS:
1. Tools apa saja yang Anda gunakan? (Python, Pandas, Seaborn, Scikit-learn, Power BI, dll)
2. Mengapa memilih tools tersebut?
-->

| **Kategori** | **Tools** | **Fungsi** |
|--------------|-----------|------------|
| **Analisis Data** | Python, Pandas, NumPy | ... |
| **Visualisasi** | Matplotlib, Seaborn | ... |
| **Dashboard** | Power BI | ... |
| **Machine Learning** | Scikit-learn, XGBoost | ... |

---

## Struktur Proyek

<!-- 
PERTANYAAN KRITIS:
1. Bagaimana struktur folder proyek Anda?
2. Apa isi setiap folder?
-->

```
FinanKu-Credit-Risk-Analysis/
│
├── data/
│   ├── raw/                  # Data mentah
│   ├── processed/            # Data setelah preprocessing
│   └── validation/           # Data validasi
│
├── notebooks/
│   ├── 01_EDA.ipynb          # Exploratory Data Analysis
│   ├── 02_Modeling.ipynb     # Machine Learning
│   └── 03_Dashboard_Link.txt # Link Power BI
│
├── dashboard/
│   └── finansial_dashboard.pbix
│
├── reports/
│   └── executive_summary.pdf
│
├── README.md
└── requirements.txt
```

---

## Data Understanding

### **Sumber Data**
<!-- 
PERTANYAAN KRITIS:
1. Dari mana data berasal?
2. Berapa periode data? (Q1-Q4 2023)
3. Berapa jumlah total nasabah?
-->

**Tulis jawaban Anda di sini.**

| Kolom               | Dtype Sekarang | Perlakuan Analisis             |
| ------------------- | -------------- | ------------------------------ |
| Customer ID         | int64          | Identifier (jangan dianalisis) |
| Branch Code         | int64          | Categorical                    |
| City                | object         | Categorical                    |
| Age                 | int64          | Numerical                      |
| Income              | int64          | Numerical                      |
| Balance Q1-Q4       | float64        | Numerical                      |
| NumOfProducts Q1-Q4 | int64          | Numerical/Ordinal              |
| HasCrCard Q1-Q4     | int64          | Binary                         |
| ActiveMember Q1-Q4  | int64          | Binary                         |
| Unpaid Tagging      | int64          | Target                         |


### **Variabel Utama**

<!-- 
PERTANYAAN KRITIS:
1. Sebutkan variabel-variabel kunci dan jelaskan artinya.
2. Mana yang menjadi target variabel (label)?
-->

### **Struktur Data**

Dataset terdiri dari **7.561 nasabah** dengan **22 variabel** yang mencakup informasi demografi, keuangan, dan perilaku nasabah selama 4 kuartal (Q1-Q4).

| **#** | **Nama Kolom** | **Tipe Data** | **Deskripsi** | **Periode** |
|-------|----------------|---------------|---------------|-------------|
| 0 | Customer ID | Integer | ID unik nasabah | - |
| 1 | Branch Code | Integer | Kode cabang tempat nasabah terdaftar | - |
| 2 | City | Object (Kategorikal) | Kota domisili nasabah (Jakarta, Bandung, Surabaya) | - |
| 3 | Age | Integer | Usia nasabah (tahun) | - |
| 4 | Avg. Annual Income/Month | Integer | Rata-rata penghasilan per bulan (dalam Rupiah) | - |
| 5 | Balance Q1 | Float | Saldo mengendap akhir kuartal 1 | Q1 |
| 6 | NumOfProducts Q1 | Integer | Jumlah produk yang dimiliki kuartal 1 | Q1 |
| 7 | HasCrCard Q1 | Integer (0/1) | Status kepemilikan kartu kredit kuartal 1 | Q1 |
| 8 | ActiveMember Q1 | Integer (0/1) | Status keaktifan nasabah kuartal 1 | Q1 |
| 9 | Balance Q2 | Float | Saldo mengendap akhir kuartal 2 | Q2 |
| 10 | NumOfProducts Q2 | Integer | Jumlah produk yang dimiliki kuartal 2 | Q2 |
| 11 | HasCrCard Q2 | Integer (0/1) | Status kepemilikan kartu kredit kuartal 2 | Q2 |
| 12 | ActiveMember Q2 | Integer (0/1) | Status keaktifan nasabah kuartal 2 | Q2 |
| 13 | Balance Q3 | Float | Saldo mengendap akhir kuartal 3 | Q3 |
| 14 | NumOfProducts Q3 | Integer | Jumlah produk yang dimiliki kuartal 3 | Q3 |
| 15 | HasCrCard Q3 | Integer (0/1) | Status kepemilikan kartu kredit kuartal 3 | Q3 |
| 16 | ActiveMember Q3 | Integer (0/1) | Status keaktifan nasabah kuartal 3 | Q3 |
| 17 | Balance Q4 | Float | Saldo mengendap akhir kuartal 4 | Q4 |
| 18 | NumOfProducts Q4 | Integer | Jumlah produk yang dimiliki kuartal 4 | Q4 |
| 19 | HasCrCard Q4 | Integer (0/1) | Status kepemilikan kartu kredit kuartal 4 | Q4 |
| 20 | ActiveMember Q4 | Integer (0/1) | Status keaktifan nasabah kuartal 4 | Q4 |
| 21 | Unpaid Tagging | Integer (0/1) | **Target Variabel:** Status gagal bayar (1 = Gagal Bayar, 0 = Lancar) | - |

### **Kualitas Data**

<!-- 
PERTANYAAN KRITIS:
1. Apakah ada data yang hilang? Berapa banyak?
2. Apakah ada data duplikat?
3. Apakah data seimbang antara kelas 'gagal bayar' dan 'lancar'? (Ini penting!)
-->

**Tulis jawaban Anda di sini.**

---

## Data Preparation & Feature Engineering

### **Proses Pembersihan Data**

<!-- 
PERTANYAAN KRITIS:
1. Langkah-langkah apa yang Anda lakukan?
2. Mengapa Anda melakukan itu?
-->

**Tulis jawaban Anda di sini.**

### **Feature Engineering**

<!-- 
PERTANYAAN KRITIS:
1. Fitur baru apa yang Anda buat? (Mean Balance, Delta Balance, Diff PH, Vintage_CR)
2. Mengapa fitur ini penting secara bisnis?
3. Berikan contoh formula perhitungannya.
-->

**Tulis jawaban Anda di sini.**

---

## Exploratory Data Analysis (EDA)

<!-- 
PERTANYAAN KRITIS:
1. Apa saja pertanyaan bisnis yang ingin Anda jawab melalui EDA?
2. Untuk setiap visualisasi, tuliskan insight bisnisnya.
3. JANGAN hanya menampilkan grafik, tapi CERITAKAN maknanya.
-->

### **1. Distribusi Nasabah Berdasarkan Lokasi**

<!-- Tambahkan screenshot grafik Anda di sini -->

**Insight:**
- **Tulis insight Anda di sini.**

### **2. Profil Nasabah Berdasarkan Usia**

<!-- Tambahkan screenshot grafik Anda di sini -->

**Insight:**
- **Tulis insight Anda di sini.**

### **3. Analisis Saldo & Risiko Gagal Bayar**

<!-- Tambahkan screenshot grafik Anda di sini -->

**Insight:**
- **Tulis insight Anda di sini.**

### **4. Analisis Kepemilikan Produk**

<!-- Tambahkan screenshot grafik Anda di sini -->

**Insight:**
- **Tulis insight Anda di sini.**

---

## Business Insights & Recommendations

<!-- 
PERTANYAAN KRITIS:
1. Dari EDA, apa 3-5 insight paling penting untuk bisnis?
2. Berikan rekomendasi konkret untuk setiap insight.
3. Bagaimana cara mengimplementasikannya?
4. Apa dampak bisnis yang diharapkan?
-->

### **Insight 1: [Judul Insight Anda]**

- **Temuan:** ...
- **Rekomendasi:** ...
- **Dampak yang Diharapkan:** ...

### **Insight 2: [Judul Insight Anda]**

- **Temuan:** ...
- **Rekomendasi:** ...
- **Dampak yang Diharapkan:** ...

### **Insight 3: [Judul Insight Anda]**

- **Temuan:** ...
- **Rekomendasi:** ...
- **Dampak yang Diharapkan:** ...

---

## Dashboard Power BI

<!-- 
PERTANYAAN KRITIS:
1. Apa tujuan dashboard ini?
2. Metrik apa saja yang ditampilkan?
3. Siapa pengguna dashboard ini?
-->

**Tulis jawaban Anda di sini.**

<!-- Tambahkan screenshot dashboard Anda di sini -->

### **Fitur Dashboard:**
- ...
- ...
- ...

---

## Machine Learning (Bonus)

### **Tujuan**

<!-- 
PERTANYAAN KRITIS:
1. Mengapa Anda menambahkan ML?
2. Apa yang ingin Anda capai?
-->

**Tulis jawaban Anda di sini.**

### **Algoritma yang Digunakan**

<!-- 
PERTANYAAN KRITIS:
1. Algoritma apa saja yang dicoba? (Logistic Regression, Random Forest, XGBoost)
2. Mengapa memilih algoritma tersebut?
-->

**Tulis jawaban Anda di sini.**

### **Evaluasi Model**

<!-- 
PERTANYAAN KRITIS:
1. Metrik apa yang digunakan? (Accuracy, Recall, Precision)
2. Mengapa Recall penting di sini?
3. Apa hasil terbaik?
4. Mengapa menurut Anda model belum optimal?
-->

| **Model** | **Accuracy** | **Recall** | **Precision** | **F1-Score** |
|-----------|--------------|------------|---------------|--------------|
| Logistic Regression | ... | ... | ... | ... |
| Random Forest | ... | ... | ... | ... |
| XGBoost | ... | ... | ... | ... |

**Interpretasi:**
**Tulis interpretasi Anda di sini.**

### **Feature Importance**

<!-- Tambahkan screenshot feature importance -->

**Insight dari Feature Importance:**
**Tulis insight Anda di sini.**

---

## Kesimpulan & Next Steps

### **Kesimpulan**

<!-- 
PERTANYAAN KRITIS:
1. Apa pencapaian utama proyek ini?
2. Apakah tujuan awal tercapai?
3. Apa batasan dari analisis ini?
-->

**Tulis jawaban Anda di sini.**

### **Rekomendasi Pengembangan**

<!-- 
PERTANYAAN KRITIS:
1. Apa yang bisa ditingkatkan?
2. Data tambahan apa yang dibutuhkan?
3. Pendekatan lain apa yang bisa dicoba?
-->

**Tulis jawaban Anda di sini.**

---

## Cara Menjalankan Proyek

### **1. Clone Repository**
```bash
git clone https://github.com/username/finanku-credit-risk-analysis.git
cd finanku-credit-risk-analysis
```

### **2. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3. Jalankan Notebook**
```bash
jupyter notebook notebooks/01_EDA.ipynb
```

### **4. Buka Dashboard**
- Buka file `dashboard/finansial_dashboard.pbix` dengan Power BI Desktop

---

## Referensi

<!-- 
PERTANYAAN KRITIS:
1. Sumber data atau inspirasi apa yang Anda gunakan?
2. Apakah ada artikel, buku, atau dataset yang dirujuk?
-->

**Tulis jawaban Anda di sini.**

---

## Kontak

**Nama:** [Galuh Kurnia Pratama]  
**LinkedIn:** [https://www.linkedin.com/in/galuh-kurnia-pratama-a25b9b325/]  
**Email:** [galuhkoernia@gmail.com]  
**Portofolio:** [https://www.galhkoernia.my.id/]

---

## Lisensi

[MIT](https://www.galhkoernia.my.id/) © [2026] [galhkoernia]
```

---