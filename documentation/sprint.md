# Sprint Documentation — Python Application Migration

# Milestone

```text
Notebook-Based Analysis
        │
        ▼
Python Modular Architecture
        │
        ▼
Automated Analytics Pipeline
        │
        ▼
Business Reporting
        │
        ▼
Dashboard Dataset
```

---

# Sprint Tasks

## Task 1 — Refactor Project Architecture

### Objective

Menyusun ulang struktur project agar seluruh business logic berada pada module Python.

### Deliverables

```text
src/
│
├── analysis/
├── config/
├── report/
├── services/
├── utils/
└── visualization/
```

Status

```text
Completed
```

---

## Task 2 — Build Configuration Layer

### Objective

Memusatkan seluruh konfigurasi project.

### Modules

```text
settings.py
constants.py
```

Deliverables

* Dataset path
* Output path
* Figure configuration
* Constants

Status

```text
Completed
```

---

## Task 3 — Build Utility Layer

### Objective

Menyediakan reusable utility function.

Modules

```text
data_loader.py

statistics.py

validator.py

formatter.py
```

Deliverables

* Load dataset
* Save dataset
* Summary statistics
* Validation
* Formatting

Status

```text
Completed
```

---

## Task 4 — Build Visualization Layer

### Objective

Menyediakan reusable plotting.

Modules

```text
plotter.py

style.py
```

Functions

```text
plot_histogram()

plot_boxplot()

plot_countplot()

plot_bar()

plot_heatmap()
```

Status

```text
Completed
```

---

## Task 5 — Build Analysis Layer

### Objective

Memindahkan seluruh business logic dari notebook.

Modules

```text
feature_engineering.py

univariate.py

bivariate.py

multivariate.py

insight.py

recommendation.py
```

Status

```text
Completed
```

---

## Task 6 — Build Service Layer

### Objective

Mengatur workflow analisis.

Modules

```text
eda_service.py

univariate_service.py

bivariate_service.py

multivariate_service.py
```

Status

```text
Completed
```

---

## Task 7 — Build Application Entry Point

### Objective

Menjadikan project dapat dijalankan melalui satu entry point.

File

```text
main.py
```

Workflow

```text
Load Dataset

↓

Run EDA

↓

Generate Output
```

Status

```text
In Progress
```

---

# Sprint Berikutnya

---

## Task 8 — Business Insight Engine

### Objective

Menghasilkan insight bisnis secara otomatis berdasarkan hasil EDA.

Module

```text
src/report/
```

```text
insight_generator.py
```

Output

```text
Business Insight
```

Status

```text
Planned
```

---

## Task 9 — Recommendation Engine

### Objective

Menghasilkan rekomendasi bisnis berdasarkan insight.

Module

```text
recommendation_generator.py
```

Output

```text
Business Recommendation
```

Status

```text
Planned
```

---

## Task 10 — Dashboard Dataset Generator

### Objective

Menghasilkan dataset yang siap dikonsumsi oleh Power BI.

Module

```text
dashboard_export.py
```

Output

```text
dashboard_dataset.csv
```

Status

```text
Planned
```

---

## Task 11 — Executive Summary Generator

### Objective

Menyusun ringkasan hasil analisis dalam format yang siap dibaca oleh stakeholder.

Module

```text
executive_summary.py
```

Output

```text
Executive Summary
```

Status

```text
Planned
```

---

## Task 12 — Project Automation

### Objective

Menyediakan command-line interface (CLI) untuk menjalankan pipeline analitik.

Contoh penggunaan

```bash
python main.py eda
python main.py insight
python main.py recommendation
python main.py dashboard
python main.py all
```

Status

```text
Planned
```

---

# Final Project Workflow

```text
Raw Dataset
      │
      ▼
Data Validation
      │
      ▼
Feature Engineering
      │
      ▼
Exploratory Data Analysis
      │
      ▼
Business Insight Generation
      │
      ▼
Business Recommendation Generation
      │
      ▼
Dashboard Dataset Export
      │
      ▼
Power BI Dashboard
      │
      ▼
Executive Summary
```

---