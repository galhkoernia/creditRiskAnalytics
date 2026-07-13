## Roadmap yang akan kita gunakan

Saya sedikit memodifikasi roadmap Anda agar lebih mendekati workflow Data Analyst di perusahaan.

### 1. Business Understanding

Output yang harus dihasilkan:

* Business Background
* Business Problem
* Business Objective
* Stakeholder
* Success Metrics
* Business Questions

Contoh pertanyaan bisnis:

* Berapa proporsi nasabah yang mengalami unpaid?
* Kota mana yang memiliki risiko tertinggi?
* Kelompok umur mana yang paling berisiko?
* Apakah saldo rendah berkaitan dengan unpaid?
* Produk apa yang sering dimiliki nasabah yang gagal bayar?

Belum menyentuh coding.

---

### 2. Data Understanding

Output:

* Data Dictionary
* Tipe data
* Jumlah observasi
* Missing value
* Duplicate
* Distribusi target
* Statistik deskriptif

Di tahap ini kita mulai membuat notebook yang rapi.

## Data Types
```

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
```

---

### 3. Data Cleaning

Output:

* Missing value treatment
* Duplicate handling
* Data type correction
* Outlier analysis
* Consistency check

Yang saya inginkan nanti bukan sekadar:

```python
df.dropna()
```

tetapi menjawab

> Kenapa dihapus?
> Kenapa tidak diimputasi?
> Apa dampaknya terhadap insight bisnis?

---

### 4. Exploratory Data Analysis (Bagian Terbesar)

Ini nanti sekitar 60–70% isi project.

Saya ingin setiap visualisasi selalu mengikuti pola:

Business Question

↓

Visualisasi

↓

Insight

↓

Business Interpretation

Misalnya

Business Question

> Apakah pelanggan dengan income rendah lebih sering unpaid?

Visualisasi

Boxplot

Insight

Median income pelanggan unpaid lebih rendah.

Business Interpretation

FinanKu dapat mempertimbangkan evaluasi limit kredit pada kelompok income tertentu.

Ini jauh lebih kuat daripada sekadar menampilkan grafik.

---

### 5. Business Insight & Recommendation

Di sinilah nilai seorang Data Analyst muncul.

Misalnya:

Insight

35% unpaid berasal dari Jakarta.

Recommendation

* review approval policy Jakarta
* monitoring lebih ketat
* reminder lebih awal

Semua rekomendasi harus berasal dari data.

---

### 6. Dashboard Power BI

Dashboard bukan kumpulan chart.

Harus mampu menjawab pertanyaan stakeholder.

Minimal terdiri dari:

Halaman 1

Executive Overview

Halaman 2

Customer Profile

Halaman 3

Credit Risk Analysis

Halaman 4

Business Recommendation

---

### 7. Executive Summary

Ini yang nantinya recruiter biasanya baca paling dulu.

Isinya:

Business Problem

↓

Key Findings

↓

Business Impact

↓

Recommendation

↓

Next Action

---

### Bonus

Kalau nanti memang ingin,

baru kita tambahkan

> Logistic Regression untuk melihat faktor yang paling memengaruhi unpaid.

Tetapi ini hanya bonus.

Portfolio tetap selesai walaupun tidak ada machine learning.

---

# Perbedaan penting dengan artikel MySkill

Ada beberapa bagian dari artikel tersebut yang **tidak akan kita ikuti** karena kurang relevan untuk Data Analyst.

| Artikel MySkill                | Project Kita                                      |
| ------------------------------ | ------------------------------------------------- |
| Fokus membangun model prediksi | Fokus menghasilkan insight bisnis                 |
| Feature Engineering untuk ML   | Feature Engineering hanya jika membantu analisis  |
| StandardScaler                 | Tidak diperlukan untuk EDA                        |
| Train-test split               | Tidak diperlukan                                  |
| Hyperparameter tuning          | Tidak diperlukan                                  |
| GridSearchCV                   | Tidak diperlukan                                  |
| Recall, Accuracy               | Tidak diperlukan                                  |
| Feature Importance ML          | Diganti dengan analisis statistik dan visualisasi |
| Evaluation model               | Diganti evaluasi insight dan rekomendasi bisnis   |
| Deployment model               | Diganti Dashboard Power BI                        |

Dengan kata lain, sekitar **70% materi machine learning pada artikel tersebut tidak akan menjadi bagian utama portfolio Anda**. Datasetnya tetap sama, tetapi tujuan analisisnya berbeda.

---

## Standar yang akan saya gunakan

Saya akan menilai setiap tahap berdasarkan empat aspek:

1. **Business relevance** — Apakah analisis menjawab kebutuhan stakeholder?
2. **Analytical correctness** — Apakah metode yang digunakan tepat?
3. **Code quality** — Apakah notebook rapi, mudah dibaca, dan dapat direproduksi?
4. **Storytelling** — Apakah hasil analisis membentuk narasi yang logis hingga menghasilkan rekomendasi?
