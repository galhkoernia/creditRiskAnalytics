#
# Created on Mon Jul 13 2026
#
# Copyright (c) 2026 galhkoernia
#

import pandas as pd
import numpy as np


def export_dashboard_dataset(df, filepath='report/dashboard_dataset.csv'):
    """
    Export aggregated dataset for Power BI dashboard.
    """
    dashboard_df = _prepare_dashboard_data(df)
    dashboard_df.to_csv(filepath, index=False)
    print(f"Dashboard dataset exported: {dashboard_df.shape[0]} rows, {dashboard_df.shape[1]} columns")
    return dashboard_df


def _prepare_dashboard_data(df):
    """
    Prepare and aggregate data for dashboard.
    """
    dashboard_df = df.copy()
    
    dashboard_df = _add_aggregated_metrics(dashboard_df)
    dashboard_df = _add_risk_indicators(dashboard_df)
    dashboard_df = _add_trend_metrics(dashboard_df)
    dashboard_df = _select_dashboard_columns(dashboard_df)
    
    return dashboard_df


def _add_aggregated_metrics(df):
    """
    Add aggregated metrics for each customer.
    """
    df['Avg_Balance'] = df[['Balance Q1', 'Balance Q2', 'Balance Q3', 'Balance Q4']].mean(axis=1)
    df['Avg_Products'] = df[['NumOfProducts Q1', 'NumOfProducts Q2', 'NumOfProducts Q3', 'NumOfProducts Q4']].mean(axis=1)
    df['Avg_Active'] = df[['ActiveMember Q1', 'ActiveMember Q2', 'ActiveMember Q3', 'ActiveMember Q4']].mean(axis=1)
    df['Avg_CreditCard'] = df[['HasCrCard Q1', 'HasCrCard Q2', 'HasCrCard Q3', 'HasCrCard Q4']].mean(axis=1)
    
    df['Balance_Growth'] = ((df['Balance Q4'] - df['Balance Q1']) / (df['Balance Q1'] + 1)) * 100
    df['Product_Change'] = df['NumOfProducts Q4'] - df['NumOfProducts Q1']
    df['Activity_Trend'] = df['ActiveMember Q4'] - df['ActiveMember Q1']
    
    return df


def _add_risk_indicators(df):
    """
    Add risk categorization and indicators.
    """
    df['Balance_Risk_Level'] = pd.cut(
        df['Avg_Balance'],
        bins=[-np.inf, 100000, 500000, 1000000, np.inf],
        labels=['Very High Risk', 'High Risk', 'Medium Risk', 'Low Risk']
    )
    
    df['Income_Segment'] = pd.cut(
        df['Avg. Annual Income/Month'],
        bins=[-np.inf, 3000000, 6000000, 10000000, np.inf],
        labels=['Low Income', 'Medium Income', 'High Income', 'Very High Income']
    )
    
    df['Age_Group'] = pd.cut(
        df['Age'],
        bins=[-np.inf, 25, 35, 45, 55, np.inf],
        labels=['18-25', '26-35', '36-45', '46-55', '55+']
    )
    
    df['Product_Adoption'] = pd.cut(
        df['Avg_Products'],
        bins=[-np.inf, 1, 2, 3, np.inf],
        labels=['Low', 'Medium', 'High', 'Very High']
    )
    
    df['Activity_Status'] = df['Avg_Active'].apply(
        lambda x: 'Active' if x >= 0.5 else 'Inactive'
    )
    
    df['Risk_Score'] = _calculate_risk_score(df)
    df['Risk_Category'] = pd.cut(
        df['Risk_Score'],
        bins=[-np.inf, 0.3, 0.5, 0.7, np.inf],
        labels=['Low Risk', 'Medium Risk', 'High Risk', 'Very High Risk']
    )
    
    return df


def _calculate_risk_score(df):
    """
    Calculate composite risk score for each customer.
    """
    risk_score = pd.Series(index=df.index, dtype=float)
    risk_score = risk_score.fillna(0)
    
    risk_score += (1 - df['Avg_Balance'] / df['Avg_Balance'].max()) * 0.25
    risk_score += (1 - df['Avg_Products'] / df['Avg_Products'].max()) * 0.20
    risk_score += (1 - df['Avg_Active']) * 0.20
    risk_score += (1 - df['Avg_CreditCard']) * 0.15
    risk_score += (1 - df['Avg. Annual Income/Month'] / df['Avg. Annual Income/Month'].max()) * 0.20
    
    risk_score = risk_score / risk_score.max()
    
    return risk_score


def _add_trend_metrics(df):
    """
    Add quarterly trend metrics.
    """
    balance_cols = ['Balance Q1', 'Balance Q2', 'Balance Q3', 'Balance Q4']
    for i, col in enumerate(balance_cols):
        df[f'Balance_{i+1}_Log'] = np.log1p(df[col])
    
    df['Balance_Volatility'] = df[balance_cols].std(axis=1)
    df['Balance_Growth_Rate'] = df[balance_cols].pct_change(axis=1).mean(axis=1) * 100
    df['Max_Products'] = df[['NumOfProducts Q1', 'NumOfProducts Q2', 'NumOfProducts Q3', 'NumOfProducts Q4']].max(axis=1)
    df['Product_Diversity'] = df[['NumOfProducts Q1', 'NumOfProducts Q2', 'NumOfProducts Q3', 'NumOfProducts Q4']].nunique(axis=1)
    
    return df


def _select_dashboard_columns(df):
    """
    Select columns for dashboard export.
    """
    columns = [
        'Customer ID',
        'Branch Code',
        'City',
        'Age',
        'Age_Group',
        'Avg. Annual Income/Month',
        'Income_Segment',
        'Avg_Balance',
        'Balance_Risk_Level',
        'Balance_Volatility',
        'Balance_Growth',
        'Balance_Growth_Rate',
        'Avg_Products',
        'Product_Adoption',
        'Max_Products',
        'Product_Diversity',
        'Avg_CreditCard',
        'Avg_Active',
        'Activity_Status',
        'Activity_Trend',
        'Risk_Score',
        'Risk_Category',
        'Unpaid Tagging'
    ]
    
    available_columns = [col for col in columns if col in df.columns]
    return df[available_columns]


def generate_summary_metrics(df):
    """
    Generate summary metrics for dashboard header.
    """
    metrics = {
        'total_customers': len(df),
        'default_rate': (df['Unpaid Tagging'].sum() / len(df)) * 100,
        'avg_balance': df['Avg_Balance'].mean(),
        'avg_products': df['Avg_Products'].mean(),
        'avg_age': df['Age'].mean(),
        'avg_income': df['Avg. Annual Income/Month'].mean(),
        'active_rate': (df['Avg_Active'].mean()) * 100,
        'credit_card_rate': (df['Avg_CreditCard'].mean()) * 100,
        'high_risk_count': len(df[df['Risk_Category'] == 'Very High Risk']) if 'Risk_Category' in df.columns else 0,
        'default_by_city': df.groupby('City')['Unpaid Tagging'].mean().to_dict() if 'City' in df.columns else {}
    }
    
    return metrics


def save_summary_metrics(metrics, filepath='report/dashboard_metrics.json'):
    """
    Save summary metrics to JSON file.
    """
    import json
    with open(filepath, 'w') as f:
        json.dump(metrics, f, indent=2, default=str)
    print(f"Dashboard metrics saved to {filepath}")
    return metrics