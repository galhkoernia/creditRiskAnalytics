#
# Created on Mon Jul 13 2026
#
# Copyright (c) 2026 galhkoernia
#

import pandas as pd


def summary_statistics(df, columns=None):
    """
    Generate descriptive statistics.
    """

    if columns is None:
        return df.describe(include="all").T

    return df[columns].describe().T


def frequency_table(df, column):
    """
    Generate frequency table.
    """

    return (
        df[column]
        .value_counts(dropna=False)
        .reset_index(name="Count")
        .rename(columns={"index": column})
    )


def unpaid_rate(df, group_column, target):
    """
    Calculate unpaid rate.
    """

    result = (
        df.groupby(group_column)[target]
        .agg(
            Total="count",
            Unpaid="sum",
            Unpaid_Rate="mean"
        )
        .reset_index()
    )

    result["Unpaid_Rate"] *= 100

    return result.sort_values(
        "Unpaid_Rate",
        ascending=False
    )