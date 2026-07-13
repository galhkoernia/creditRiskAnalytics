#
# Created on Mon Jul 13 2026
#
# Copyright (c) 2026 galhkoernia
#


from pathlib import Path

# Project root
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Directories
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

NOTEBOOK_DIR = PROJECT_ROOT / "notebooks"
REPORT_DIR = PROJECT_ROOT / "reports"
DASHBOARD_DIR = PROJECT_ROOT / "dashboard"
IMAGE_DIR = PROJECT_ROOT / "images"

# Dataset
RAW_DATASET = RAW_DATA_DIR / "credit_risk.csv"
PROCESSED_DATASET = PROCESSED_DATA_DIR / "credit_risk_feature_engineered.csv"

# Figure configuration
DEFAULT_FIGSIZE = (10, 6)
DEFAULT_DPI = 120

# Random seed
RANDOM_STATE = 42