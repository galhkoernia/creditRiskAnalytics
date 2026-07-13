# Project Architecture

## Overview

Project menggunakan pendekatan modular sehingga notebook hanya digunakan sebagai media analisis, sedangkan seluruh business logic berada pada module Python.

Architecture

main.py

↓

services

↓

analysis

↓

visualization

↓

utils

↓

config

---

## Layer Responsibilities

### main.py

Entry point project.

Tanggung jawab

- Load dataset
- Menjalankan workflow
- Menampilkan output

---

### Services

Workflow orchestration.

Tidak berisi business logic.

Services hanya mengatur urutan proses analisis.

---

### Analysis

Business logic.

Semua proses analisis data berada di layer ini.

---

### Visualization

Reusable plotting.

Semua visualisasi berada di layer ini.

---

### Utils

Utility function.

Contoh

- loader
- statistics
- validator
- formatter

---

### Config

Konfigurasi project.

Tidak berisi proses analisis.