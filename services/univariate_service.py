#
# Created on Mon Jul 13 2026
#
# Copyright (c) 2026 Your Company
#

from analysis.univariate import (
    analyze_distribution,
    analyze_frequency
)

from config.constants import TARGET_COLUMN


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
    results["avg_balance"] = analyze_distribution(
        df,
        "Avg Balance"
    )

    # Product
    results["avg_products"] = analyze_distribution(
        df,
        "Avg Products"
    )

    # Activity
    results["activity_rate"] = analyze_distribution(
        df,
        "Activity Rate"
    )

    return results