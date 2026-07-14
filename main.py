#
# Created on Mon Jul 13 2026
#
# Copyright (c) 2026 galhkoernia
#

import pandas as pd
import os
import sys
import argparse
from datetime import datetime

from src.services.eda_service import run_complete_eda
from src.visualization.dashboard import save_dashboard
from src.report.insight_generator import generate_insights, save_insights
from src.report.recommendation_generator import generate_recommendations, save_recommendations
from src.report.dashboard_export import export_dashboard_dataset, generate_summary_metrics, save_summary_metrics
from src.report.executive_summary import save_executive_summary


def load_dataset(file_path):
    """
    Load dataset from CSV file.
    """
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return None
    
    df = pd.read_csv(file_path)
    print(f"Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")
    return df


def print_section(title):
    """
    Print section header.
    """
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def run_eda(df, output_dir='report'):
    """
    Run complete EDA pipeline.
    """
    print_section("Running Exploratory Data Analysis")
    results = run_complete_eda(df)
    print("EDA completed successfully.")
    return results


def run_insights(df, results, output_dir='report'):
    """
    Generate business insights.
    """
    print_section("Generating Business Insights")
    insights = generate_insights(df, results)
    save_insights(insights, f'{output_dir}/insights.txt')
    print(f"Generated {len(insights)} insights")
    return insights


def run_recommendations(insights, output_dir='report'):
    """
    Generate business recommendations.
    """
    print_section("Generating Business Recommendations")
    recommendations = generate_recommendations(insights)
    save_recommendations(recommendations, f'{output_dir}/recommendations.txt')
    print(f"Generated {len(recommendations)} recommendations")
    return recommendations


def run_dashboard(df, output_dir='report'):
    """
    Export dashboard dataset and create visualization.
    """
    print_section("Exporting Dashboard Dataset")
    dashboard_df = export_dashboard_dataset(df, f'{output_dir}/dashboard_dataset.csv')
    metrics = generate_summary_metrics(dashboard_df)
    save_summary_metrics(metrics, f'{output_dir}/dashboard_metrics.json')
    
    print_section("Creating Dashboard Visualization")
    save_dashboard(df, f'{output_dir}/dashboard.png')
    print("Dashboard created successfully.")
    return metrics


def run_executive_summary(df, insights, recommendations, metrics, output_dir='report'):
    """
    Generate executive summary.
    """
    print_section("Generating Executive Summary")
    save_executive_summary(df, insights, recommendations, metrics, f'{output_dir}/executive_summary.md')
    print("Executive summary generated successfully.")


def run_full_pipeline(file_path, output_dir='report'):
    """
    Run complete analytics pipeline.
    """
    start_time = datetime.now()
    print("=" * 60)
    print("FinanKu Credit Risk Analysis - Full Pipeline")
    print("=" * 60)
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    df = load_dataset(file_path)
    if df is None:
        print("Failed to load data. Exiting.")
        return
    
    print(f"\nDataset shape: {df.shape}")
    print(f"Columns: {df.columns.tolist()}")
    
    results = run_eda(df, output_dir)
    insights = run_insights(df, results, output_dir)
    recommendations = run_recommendations(insights, output_dir)
    metrics = run_dashboard(df, output_dir)
    run_executive_summary(df, insights, recommendations, metrics, output_dir)
    
    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()
    
    print_section("Pipeline Completed Successfully")
    print(f"Total execution time: {duration:.2f} seconds")
    print(f"All outputs saved to: {output_dir}/")
    print("=" * 60)


def main():
    """
    Main entry point with CLI support.
    """
    parser = argparse.ArgumentParser(
        description='FinanKu Credit Risk Analytics Pipeline',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py all                    # Run full pipeline
  python main.py eda                    # Run EDA only
  python main.py insights               # Generate insights only
  python main.py recommendations        # Generate recommendations only
  python main.py dashboard              # Export dashboard dataset
  python main.py summary                # Generate executive summary
  python main.py --file data.csv        # Use custom file
  python main.py --output reports/      # Set output directory
        """
    )
    
    parser.add_argument(
        'command',
        nargs='?',
        default='all',
        choices=['all', 'eda', 'insights', 'recommendations', 'dashboard', 'summary'],
        help='Command to execute (default: all)'
    )
    
    parser.add_argument(
        '--file',
        type=str,
        default='data/raw/FinanKu_Data_All.csv',
        help='Path to dataset file (default: data/raw/FinanKu_Data_All.csv)'
    )
    
    parser.add_argument(
        '--output',
        type=str,
        default='report',
        help='Output directory (default: report)'
    )
    
    args = parser.parse_args()
    
    if not os.path.exists(args.output):
        os.makedirs(args.output)
    
    df = load_dataset(args.file)
    if df is None:
        print("Failed to load data. Exiting.")
        sys.exit(1)
    
    print(f"\nDataset shape: {df.shape}")
    print("=" * 60)
    
    if args.command == 'all':
        run_full_pipeline(args.file, args.output)
    
    elif args.command == 'eda':
        results = run_eda(df, args.output)
    
    elif args.command == 'insights':
        results = run_eda(df, args.output)
        insights = run_insights(df, results, args.output)
    
    elif args.command == 'recommendations':
        results = run_eda(df, args.output)
        insights = run_insights(df, results, args.output)
        recommendations = run_recommendations(insights, args.output)
    
    elif args.command == 'dashboard':
        metrics = run_dashboard(df, args.output)
    
    elif args.command == 'summary':
        results = run_eda(df, args.output)
        insights = run_insights(df, results, args.output)
        recommendations = run_recommendations(insights, args.output)
        metrics = run_dashboard(df, args.output)
        run_executive_summary(df, insights, recommendations, metrics, args.output)


if __name__ == "__main__":
    main()