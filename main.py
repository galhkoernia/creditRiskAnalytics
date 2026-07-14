#
# Created on Mon Jul 13 2026
#
# Copyright (c) 2026 galhkoernia
#

import pandas as pd
import os
from src.services.eda_service import run_complete_eda
from src.visualization.dashboard import save_dashboard


def main():
    print("="*60)
    print("FinanKu Credit Risk Analysis")
    print("="*60)
    
    # Load data
    file_path = "data/raw/FinanKu_Data_All.csv"
    
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return
    
    df = pd.read_csv(file_path)
    
    print(f"\nDataset shape: {df.shape}")
    print("\nColumns in dataset:")
    print(df.columns.tolist())
    print("="*60)
    
    # Run EDA
    results = run_complete_eda(df)
    
    print("\n" + "="*60)
    print("EDA completed successfully.")
    print("="*60)
    
    # Save dashboard - pastikan menggunakan fungsi yang sudah diupdate
    try:
        save_dashboard(df, 'report/dashboard.png')
        print("\n✅ Dashboard saved to report/dashboard.png")
    except Exception as e:
        print(f"\n❌ Error creating dashboard: {e}")
        print("Please check that dashboard.py has been updated.")

if __name__ == "__main__":
    main()