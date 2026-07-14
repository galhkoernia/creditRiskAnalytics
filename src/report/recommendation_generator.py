#
# Created on Mon Jul 13 2026
#
# Copyright (c) 2026 galhkoernia
#

import pandas as pd
import numpy as np


def generate_recommendations(insights):
    """
    Generate actionable business recommendations from insights.
    
    Parameters:
    -----------
    insights : list
        List of insight dictionaries from insight_generator
    
    Returns:
    --------
    list : List of recommendation dictionaries
    """
    recommendations = []
    
    recommendations.extend(_get_credit_risk_recommendations(insights))
    recommendations.extend(_get_customer_segmentation_recommendations(insights))
    recommendations.extend(_get_product_strategy_recommendations(insights))
    recommendations.extend(_get_engagement_recommendations(insights))
    recommendations.extend(_get_regional_strategy_recommendations(insights))
    
    return recommendations


def _get_credit_risk_recommendations(insights):
    recommendations = []
    
    for insight in insights:
        if insight['category'] == 'Credit Risk' and insight['severity'] == 'High':
            recommendations.append({
                'category': 'Credit Risk Management',
                'priority': 'High',
                'title': 'Strengthen Credit Assessment Process',
                'description': 'Implement stricter credit scoring for high-risk segments identified in analysis.',
                'action_items': [
                    'Review and update credit assessment criteria',
                    'Implement additional verification for high-risk applicants',
                    'Increase monitoring frequency for existing high-risk customers'
                ],
                'expected_impact': 'Reduce default rate by 15-20% within 6 months',
                'timeline': 'Short-term (0-3 months)'
            })
    
    recommendations.append({
        'category': 'Credit Risk Management',
        'priority': 'High',
        'title': 'Develop Early Warning System',
        'description': 'Create predictive model to identify customers at risk of default before it happens.',
        'action_items': [
            'Build machine learning model using historical data',
            'Set up automated alerts for risk indicators',
            'Define intervention protocols for different risk levels'
        ],
        'expected_impact': 'Identify 80% of potential defaults 3 months in advance',
        'timeline': 'Medium-term (3-6 months)'
    })
    
    return recommendations


def _get_customer_segmentation_recommendations(insights):
    recommendations = []
    
    age_insight = None
    income_insight = None
    
    for insight in insights:
        if insight['category'] == 'Demographic' and 'Age' in insight['title']:
            age_insight = insight
        if insight['category'] == 'Demographic' and 'Income' in insight['title']:
            income_insight = insight
    
    if age_insight and age_insight['severity'] == 'High':
        recommendations.append({
            'category': 'Customer Segmentation',
            'priority': 'High',
            'title': 'Implement Age-Based Risk Segmentation',
            'description': 'Develop targeted strategies for different age groups based on risk profile.',
            'action_items': [
                'Segment customers by age brackets (18-25, 26-35, 36-45, 46+)',
                'Design tailored products for each segment',
                'Adjust marketing and communication strategy per age group'
            ],
            'expected_impact': 'Increase risk-adjusted portfolio performance by 10%',
            'timeline': 'Medium-term (3-6 months)'
        })
    
    if income_insight and income_insight['severity'] == 'High':
        recommendations.append({
            'category': 'Customer Segmentation',
            'priority': 'High',
            'title': 'Develop Income-Based Product Tiers',
            'description': 'Create product packages aligned with income levels to improve affordability and reduce default.',
            'action_items': [
                'Design tiered product offerings based on income brackets',
                'Adjust credit limits and terms according to income profile',
                'Provide financial literacy programs for lower income segments'
            ],
            'expected_impact': 'Reduce default among low-income segment by 12-15%',
            'timeline': 'Short-term (0-3 months)'
        })
    
    return recommendations


def _get_product_strategy_recommendations(insights):
    recommendations = []
    
    product_insight = None
    
    for insight in insights:
        if insight['category'] == 'Behavioral' and 'Product' in insight['title']:
            product_insight = insight
    
    recommendations.append({
        'category': 'Product Strategy',
        'priority': 'Medium',
        'title': 'Increase Product Cross-Selling',
        'description': 'Encourage customers to adopt more products to increase engagement and reduce default risk.',
        'action_items': [
            'Create product bundles with incentives',
            'Develop targeted cross-selling campaigns',
            'Offer loyalty rewards for multi-product customers'
        ],
        'expected_impact': 'Increase average products per customer by 25%',
        'timeline': 'Medium-term (3-6 months)'
    })
    
    recommendations.append({
        'category': 'Product Strategy',
        'priority': 'Medium',
        'title': 'Enhance Credit Card Offerings',
        'description': 'Expand credit card portfolio to attract more customers and improve creditworthiness.',
        'action_items': [
            'Design credit card products for different segments',
            'Introduce rewards program for good payers',
            'Provide credit education for card users'
        ],
        'expected_impact': 'Increase credit card adoption by 20%',
        'timeline': 'Medium-term (3-6 months)'
    })
    
    return recommendations


def _get_engagement_recommendations(insights):
    recommendations = []
    
    active_insight = None
    
    for insight in insights:
        if insight['category'] == 'Behavioral' and 'Activity' in insight['title']:
            active_insight = insight
    
    recommendations.append({
        'category': 'Customer Engagement',
        'priority': 'High',
        'title': 'Activate Inactive Customers',
        'description': 'Implement engagement programs to increase customer activity and reduce default risk.',
        'action_items': [
            'Create reactivation campaigns for inactive customers',
            'Develop customer engagement score system',
            'Implement personalized communication strategy'
        ],
        'expected_impact': 'Increase active member rate by 20%',
        'timeline': 'Short-term (0-3 months)'
    })
    
    return recommendations


def _get_regional_strategy_recommendations(insights):
    recommendations = []
    
    regional_insight = None
    
    for insight in insights:
        if insight['category'] == 'Geographic':
            regional_insight = insight
    
    if regional_insight and regional_insight['severity'] == 'High':
        recommendations.append({
            'category': 'Regional Strategy',
            'priority': 'High',
            'title': 'Optimize Regional Risk Management',
            'description': 'Develop region-specific strategies to address geographic risk variations.',
            'action_items': [
                'Conduct in-depth analysis of high-risk regions',
                'Adjust credit policies for different regions',
                'Develop local partnerships for collections'
            ],
            'expected_impact': 'Reduce default rate in high-risk regions by 18%',
            'timeline': 'Medium-term (3-6 months)'
        })
    
    return recommendations


def format_recommendations(recommendations):
    """
    Format recommendations for report display.
    """
    output = []
    output.append("\n" + "=" * 80)
    output.append("BUSINESS RECOMMENDATIONS")
    output.append("=" * 80)
    
    high_priority = [r for r in recommendations if r['priority'] == 'High']
    medium_priority = [r for r in recommendations if r['priority'] == 'Medium']
    
    all_priority = high_priority + medium_priority
    
    for i, rec in enumerate(all_priority, 1):
        output.append(f"\nRecommendation {i}: {rec['title']}")
        output.append(f"  Priority: {rec['priority']}")
        output.append(f"  Category: {rec['category']}")
        output.append(f"  Timeline: {rec['timeline']}")
        output.append(f"  Expected Impact: {rec['expected_impact']}")
        output.append(f"  Description: {rec['description']}")
        output.append("  Action Items:")
        for item in rec['action_items']:
            output.append(f"    - {item}")
    
    output.append("\n" + "=" * 80)
    return "\n".join(output)


def save_recommendations(recommendations, filepath='report/recommendations.txt'):
    """
    Save recommendations to text file.
    """
    with open(filepath, 'w') as f:
        f.write(format_recommendations(recommendations))
    print(f"Recommendations saved to {filepath}")