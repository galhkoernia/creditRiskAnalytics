#
# Created on Mon Jul 13 2026
#
# Copyright (c) 2026 Your Company
#

from src.analysis.bivariate import (
    compare_with_target,
    analyze_unpaid_rate
)

from src.config.constants import TARGET_COLUMN


def run_bivariate(df):
    """
    Execute all bivariate analyses.
    """

    results = {}

    results["age"] = compare_with_target(
        df,
        "Age",
        TARGET_COLUMN
    )

    results["income"] = compare_with_target(
        df,
        "Avg. Annual Income/Month",
        TARGET_COLUMN
    )

    results["city"] = analyze_unpaid_rate(
        df,
        "City",
        TARGET_COLUMN
    )

    results["balance_q4"] = compare_with_target(
        df,
        "Balance Q4",
        TARGET_COLUMN
    )

    results["products_q4"] = compare_with_target(
        df,
        "NumOfProducts Q4",
        TARGET_COLUMN
    )

    results["credit_card_q4"] = compare_with_target(
        df,
        "HasCrCard Q4",
        TARGET_COLUMN
    )

    results["active_q4"] = compare_with_target(
        df,
        "ActiveMember Q4",
        TARGET_COLUMN
    )

    return results