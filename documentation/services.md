# Services

Service layer bertugas mengorkestrasi workflow analisis.

## Service Diagram

main.py

↓

eda_service

├── univariate_service

├── bivariate_service

└── multivariate_service

---

## Responsibilities

eda_service

Mengatur seluruh proses EDA.

univariate_service

Menjalankan seluruh analisis univariate.

bivariate_service

Menjalankan seluruh analisis bivariate.

multivariate_service

Menjalankan correlation analysis.