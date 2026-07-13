# Development Guidelines

## General Principles

- Business question menjadi dasar seluruh analisis.
- Setiap notebook hanya memiliki satu tanggung jawab utama.
- Seluruh business logic ditempatkan pada module Python.
- Notebook digunakan sebagai media analisis dan presentasi.
- Hindari duplikasi kode.
- Gunakan reusable function.
- Setiap visualisasi harus menjawab business question.
- Jangan melakukan data cleaning tanpa justifikasi.
- Feature engineering harus memiliki tujuan bisnis.
- Seluruh insight harus didukung oleh hasil analisis.
- Seluruh recommendation harus berbasis evidence.

## Code Style

- Gunakan snake_case.
- Berikan docstring pada setiap fungsi.
- Hindari hardcoded value.
- Pisahkan configuration dan business logic.
- Gunakan struktur modular.

## Visualization

- Gunakan style yang konsisten.
- Selalu tampilkan judul yang informatif.
- Sertakan statistik pendukung sebelum interpretasi.
- Hindari visualisasi yang tidak menjawab business question.

## Documentation

- Seluruh notebook harus memiliki Project Overview.
- Setiap analisis harus memiliki Business Question, Objective, Method, Visualization, Interpretation, dan Business Insight.
- README harus menggambarkan proyek secara menyeluruh.