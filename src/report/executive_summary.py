#
# Created on Mon Jul 13 2026
#
# Copyright (c) 2026 galhkoernia
#

import pandas as pd
import json
from datetime import datetime


def generate_executive_summary(df, insights, recommendations, metrics):
    """
    Generate executive summary in markdown format.
    """
    sections = []
    
    sections.append(_get_header())
    sections.append(_get_executive_overview(metrics))
    sections.append(_get_key_findings(insights))
    sections.append(_get_recommendations_summary(recommendations))
    sections.append(_get_risk_analysis(df))
    sections.append(_get_next_steps(recommendations))
    sections.append(_get_footer())
    
    return "\n\n".join(sections)


def _get_header():
    return f"""# Executive Summary
## FinanKu Credit Risk Analysis
### Report Date: {datetime.now().strftime('%B %d, %Y')}

---

"""


def _get_executive_overview(metrics):
    return f"""## 1. Executive Overview

### Portfolio Summary
| Metric | Value |
|--------|-------|
| Total Customers | {metrics['total_customers']:,} |
| Default Rate | {metrics['default_rate']:.1f}% |
| Average Balance | Rp{metrics['avg_balance']:,.0f} |
| Average Products per Customer | {metrics['avg_products']:.1f} |
| Average Age | {metrics['avg_age']:.1f} years |
| Average Monthly Income | Rp{metrics['avg_income']:,.0f} |
| Active Member Rate | {metrics['active_rate']:.1f}% |
| Credit Card Ownership Rate | {metrics['credit_card_rate']:.1f}% |

### Key Insights
- {metrics['default_rate']:.1f}% of customers are at risk of default
- {metrics['high_risk_count']} customers identified as very high risk
- {'Jakarta' if 'Jakarta' in metrics.get('default_by_city', {}) else 'Highest'} region shows highest default rate

---"""


def _get_key_findings(insights):
    output = ["## 2. Key Findings"]
    output.append("")
    
    high_severity = [i for i in insights if i['severity'] == 'High']
    medium_severity = [i for i in insights if i['severity'] == 'Medium']
    
    output.append("### High Priority Findings")
    for i, insight in enumerate(high_severity[:3], 1):
        output.append(f"{i}. **{insight['title']}**")
        output.append(f"   {insight['description']}")
        output.append("")
    
    if medium_severity:
        output.append("### Additional Findings")
        for i, insight in enumerate(medium_severity[:3], 1):
            output.append(f"{i}. **{insight['title']}**")
            output.append(f"   {insight['description']}")
            output.append("")
    
    output.append("---")
    return "\n".join(output)


def _get_recommendations_summary(recommendations):
    output = ["## 3. Strategic Recommendations"]
    output.append("")
    
    high_priority = [r for r in recommendations if r['priority'] == 'High']
    medium_priority = [r for r in recommendations if r['priority'] == 'Medium']
    
    output.append("### Immediate Actions (Priority High)")
    for i, rec in enumerate(high_priority[:3], 1):
        output.append(f"{i}. **{rec['title']}**")
        output.append(f"   - Expected Impact: {rec['expected_impact']}")
        output.append(f"   - Timeline: {rec['timeline']}")
        output.append("")
    
    if medium_priority:
        output.append("### Short to Medium Term Actions")
        for i, rec in enumerate(medium_priority[:3], 1):
            output.append(f"{i}. **{rec['title']}**")
            output.append(f"   - Expected Impact: {rec['expected_impact']}")
            output.append(f"   - Timeline: {rec['timeline']}")
            output.append("")
    
    output.append("---")
    return "\n".join(output)


def _get_risk_analysis(df):
    output = ["## 4. Risk Analysis"]
    output.append("")
    
    if 'Risk_Category' in df.columns:
        output.append("### Risk Distribution")
        risk_counts = df['Risk_Category'].value_counts()
        for category, count in risk_counts.items():
            percentage = (count / len(df)) * 100
            output.append(f"- {category}: {count:,} customers ({percentage:.1f}%)")
        output.append("")
    
    if 'City' in df.columns:
        output.append("### Geographic Risk Distribution")
        city_risk = df.groupby('City')['Unpaid Tagging'].mean().sort_values(ascending=False)
        for city, risk_rate in city_risk.items():
            output.append(f"- {city}: {risk_rate*100:.1f}% default rate")
        output.append("")
    
    if 'Income_Segment' in df.columns:
        output.append("### Risk by Income Segment")
        income_risk = df.groupby('Income_Segment')['Unpaid Tagging'].mean().sort_values(ascending=False)
        for segment, risk_rate in income_risk.items():
            output.append(f"- {segment}: {risk_rate*100:.1f}% default rate")
        output.append("")
    
    output.append("---")
    return "\n".join(output)


def _get_next_steps(recommendations):
    output = ["## 5. Next Steps"]
    output.append("")
    
    output.append("### Implementation Roadmap")
    output.append("")
    output.append("| Timeline | Action | Owner | Priority |")
    output.append("|----------|--------|-------|----------|")
    
    for rec in recommendations[:5]:
        output.append(f"| {rec['timeline']} | {rec['title']} | TBD | {rec['priority']} |")
    
    output.append("")
    output.append("### Critical Success Factors")
    output.append("")
    output.append("1. **Executive Sponsorship**: Ensure leadership commitment to implement recommendations")
    output.append("2. **Data Infrastructure**: Strengthen data collection and integration capabilities")
    output.append("3. **Team Capability**: Build analytics and risk management expertise")
    output.append("4. **Technology Investment**: Deploy predictive models and monitoring systems")
    output.append("5. **Change Management**: Develop communication and training programs")
    output.append("")
    output.append("---")
    return "\n".join(output)


def _get_footer():
    return f"""## 6. Appendix

### Methodology
- Data Period: Quarterly data from Q1 to Q4
- Sample Size: 7,561 customers
- Analysis Methods: Univariate, Bivariate, Multivariate analysis
- Risk Scoring: Composite score based on financial and behavioral indicators

### Contact Information
**Prepared By:** Galuh Kurnia Pratama
**Email:** galuhkoernia@gmail.com
**LinkedIn:** https://www.linkedin.com/in/galuh-kurnia-pratama-a25b9b325/

---

*This report is confidential and intended for internal use only.*

---
"""


def save_executive_summary(df, insights, recommendations, metrics, 
                          filepath='report/executive_summary.md'):
    """
    Save executive summary to markdown file.
    """
    summary = generate_executive_summary(df, insights, recommendations, metrics)
    
    with open(filepath, 'w') as f:
        f.write(summary)
    
    print(f"Executive summary saved to {filepath}")
    return summary