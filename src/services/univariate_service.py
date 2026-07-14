#
# Created on Mon Jul 13 2026
#
# Copyright (c) 2026 Your Company
#

from src.analysis.univariate import (
    analyze_distribution,
    analyze_frequency
)

from src.config.constants import TARGET_COLUMN


def run_univariate(df):
    """
    Execute all univariate analyses.
    """

    results = {}

    # Credit Risk Overview
    results["target_distribution"] = analyze_frequency(
        df,
        TARGET_COLUMN
    )

    # Customer Profile
    results["age"] = analyze_distribution(
        df,
        "Age"
    )

    results["income"] = analyze_distribution(
        df,
        "Avg. Annual Income/Month"
    )

    # Geographic
    results["city"] = analyze_frequency(
        df,
        "City"
    )

    # Financial
    results["balance_q4"] = analyze_distribution(
        df,
        "Balance Q4"
    )

    # Product 
    results["products_q4"] = analyze_distribution(
        df,
        "NumOfProducts Q4"
    )

    # Activity
    results["active_q4"] = analyze_frequency(
        df,
        "ActiveMember Q4"
    )

    # Credit Card
    results["credit_card_q4"] = analyze_frequency(
        df,
        "HasCrCard Q4"
    )

    return results