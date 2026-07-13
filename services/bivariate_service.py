#
# Created on Mon Jul 13 2026
#
# Copyright (c) 2026 Your Company
#

from analysis.bivariate import (
    compare_with_target,
    analyze_unpaid_rate
)

from config.constants import TARGET_COLUMN


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

    results["avg_balance"] = compare_with_target(
        df,
        "Avg Balance",
        TARGET_COLUMN
    )

    results["balance_change"] = compare_with_target(
        df,
        "Balance Change",
        TARGET_COLUMN
    )

    results["avg_products"] = compare_with_target(
        df,
        "Avg Products",
        TARGET_COLUMN
    )

    results["activity_rate"] = compare_with_target(
        df,
        "Activity Rate",
        TARGET_COLUMN
    )

    return results