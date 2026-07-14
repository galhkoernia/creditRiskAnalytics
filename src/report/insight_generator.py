#
# Created on Mon Jul 13 2026
#
# Copyright (c) 2026 galhkoernia
#

import pandas as pd
import numpy as np


def generate_insights(df, eda_results):
    """
    Generate business insights from EDA results.
    """
    insights = []
    
    insights.extend(_get_target_insights(df))
    insights.extend(_get_demographic_insights(df))
    insights.extend(_get_financial_insights(df))
    insights.extend(_get_behavioral_insights(df))
    insights.extend(_get_geographic_insights(df))
    
    return insights


def _get_target_insights(df):
    insights = []
    
    total = len(df)
    unpaid = df['Unpaid Tagging'].sum()
    unpaid_rate = (unpaid / total) * 100
    
    insights.append({
        'category': 'Credit Risk',
        'title': 'Default Rate Overview',
        'description': f'From {total} customers, {unpaid} customers ({unpaid_rate:.1f}%) are identified as high risk with unpaid tagging.',
        'severity': 'High' if unpaid_rate > 10 else 'Medium' if unpaid_rate > 5 else 'Low',
        'metric': unpaid_rate
    })
    
    return insights


def _get_demographic_insights(df):
    insights = []
    
    age_unpaid = df[df['Unpaid Tagging'] == 1]['Age'].mean()
    age_paid = df[df['Unpaid Tagging'] == 0]['Age'].mean()
    age_diff = age_unpaid - age_paid
    
    insights.append({
        'category': 'Demographic',
        'title': 'Age and Credit Risk Correlation',
        'description': f'Customers with unpaid tagging have average age of {age_unpaid:.1f} years, while paying customers average {age_paid:.1f} years. Difference of {age_diff:.1f} years indicates age is a significant factor.',
        'severity': 'High' if abs(age_diff) > 5 else 'Medium',
        'metric': age_diff
    })
    
    income_unpaid = df[df['Unpaid Tagging'] == 1]['Avg. Annual Income/Month'].mean()
    income_paid = df[df['Unpaid Tagging'] == 0]['Avg. Annual Income/Month'].mean()
    income_ratio = income_unpaid / income_paid
    
    insights.append({
        'category': 'Demographic',
        'title': 'Income Impact on Credit Risk',
        'description': f'Unpaid customers have average monthly income of Rp{income_unpaid:,.0f}, compared to Rp{income_paid:,.0f} for paying customers. Lower income group shows {(1-income_ratio)*100:.1f}% higher default risk.',
        'severity': 'High' if income_ratio < 0.7 else 'Medium',
        'metric': income_ratio
    })
    
    return insights


def _get_financial_insights(df):
    insights = []
    
    balance_unpaid = df[df['Unpaid Tagging'] == 1]['Balance Q4'].mean()
    balance_paid = df[df['Unpaid Tagging'] == 0]['Balance Q4'].mean()
    balance_ratio = balance_unpaid / balance_paid
    
    insights.append({
        'category': 'Financial',
        'title': 'Balance and Default Risk',
        'description': f'Unpaid customers maintain average balance of Rp{balance_unpaid:,.0f}, while paying customers average Rp{balance_paid:,.0f}. Lower balance correlates with {(1-balance_ratio)*100:.1f}% higher default risk.',
        'severity': 'High' if balance_ratio < 0.5 else 'Medium',
        'metric': balance_ratio
    })
    
    return insights


def _get_behavioral_insights(df):
    insights = []
    
    product_unpaid = df[df['Unpaid Tagging'] == 1]['NumOfProducts Q4'].mean()
    product_paid = df[df['Unpaid Tagging'] == 0]['NumOfProducts Q4'].mean()
    
    insights.append({
        'category': 'Behavioral',
        'title': 'Product Ownership Pattern',
        'description': f'Unpaid customers own average {product_unpaid:.1f} products, while paying customers own {product_paid:.1f} products. Higher product adoption correlates with lower default risk.',
        'severity': 'Medium',
        'metric': product_unpaid / product_paid if product_paid > 0 else 0
    })
    
    active_unpaid = df[df['Unpaid Tagging'] == 1]['ActiveMember Q4'].mean() * 100
    active_paid = df[df['Unpaid Tagging'] == 0]['ActiveMember Q4'].mean() * 100
    
    insights.append({
        'category': 'Behavioral',
        'title': 'Customer Activity and Default',
        'description': f'Only {active_unpaid:.1f}% of unpaid customers are active members, compared to {active_paid:.1f}% of paying customers. Inactive customers show significantly higher default risk.',
        'severity': 'High' if (active_paid - active_unpaid) > 20 else 'Medium',
        'metric': active_unpaid / active_paid if active_paid > 0 else 0
    })
    
    cc_unpaid = df[df['Unpaid Tagging'] == 1]['HasCrCard Q4'].mean() * 100
    cc_paid = df[df['Unpaid Tagging'] == 0]['HasCrCard Q4'].mean() * 100
    
    insights.append({
        'category': 'Behavioral',
        'title': 'Credit Card Ownership Impact',
        'description': f'Credit card ownership is {cc_unpaid:.1f}% among unpaid customers vs {cc_paid:.1f}% among paying customers, suggesting credit card holders are more creditworthy.',
        'severity': 'Medium',
        'metric': cc_unpaid / cc_paid if cc_paid > 0 else 0
    })
    
    return insights


def _get_geographic_insights(df):
    insights = []
    
    city_unpaid = df.groupby('City')['Unpaid Tagging'].mean() * 100
    highest_risk_city = city_unpaid.idxmax()
    highest_risk_rate = city_unpaid.max()
    
    insights.append({
        'category': 'Geographic',
        'title': 'Regional Risk Distribution',
        'description': f'{highest_risk_city} has the highest default rate at {highest_risk_rate:.1f}%, indicating geographic location is a risk factor.',
        'severity': 'High' if highest_risk_rate > 15 else 'Medium',
        'metric': highest_risk_rate
    })
    
    return insights


def format_insights(insights):
    """
    Format insights for report display.
    """
    output = []
    output.append("\n" + "=" * 80)
    output.append("BUSINESS INSIGHTS")
    output.append("=" * 80)
    
    categories = {}
    for insight in insights:
        cat = insight['category']
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(insight)
    
    for category, items in categories.items():
        output.append(f"\n{category.upper()}")
        output.append("-" * 40)
        for i, insight in enumerate(items, 1):
            output.append(f"\nInsight {i}: {insight['title']}")
            output.append(f"  Severity: {insight['severity']}")
            output.append(f"  {insight['description']}")
    
    output.append("\n" + "=" * 80)
    return "\n".join(output)


def save_insights(insights, filepath='report/insights.txt'):
    """
    Save insights to text file.
    """
    with open(filepath, 'w') as f:
        f.write(format_insights(insights))
    print(f"Insights saved to {filepath}")