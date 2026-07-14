#
# Created on Mon Jul 13 2026
#
# Copyright (c) 2026 Your Company
#

from src.analysis.multivariate import (
    correlation_analysis
)

from src.config.constants import TARGET_COLUMN


def run_multivariate(df):
    """
    Execute all multivariate analyses.
    """

    results = {}

    numeric_cols = [
        "Age",
        "Avg. Annual Income/Month",
        "Balance Q1",
        "Balance Q2",
        "Balance Q3",
        "Balance Q4",
        "NumOfProducts Q1",
        "NumOfProducts Q2",
        "NumOfProducts Q3",
        "NumOfProducts Q4",
        "HasCrCard Q1",
        "HasCrCard Q2",
        "HasCrCard Q3",
        "HasCrCard Q4",
        "ActiveMember Q1",
        "ActiveMember Q2",
        "ActiveMember Q3",
        "ActiveMember Q4"
    ]

    results["correlation"] = correlation_analysis(
        df,
        numeric_cols
    )

    return results