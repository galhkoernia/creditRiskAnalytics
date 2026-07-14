#
# Created on Mon Jul 13 2026
#
# Copyright (c) 2026 galhkoernia
#

from src.utils.statistics import (
    summary_statistics,
    frequency_table
)

from src.visualization.plotter import (
    plot_histogram,
    plot_countplot
)


def analyze_distribution(
    df,
    column,
    bins=30
):
    """
    Perform univariate analysis for numerical variables.
    """

    plot_histogram(
        data=df,
        column=column,
        bins=bins,
        title=f"Distribution of {column}"
    )

    return summary_statistics(
        df,
        [column]
    )


def analyze_frequency(
    df,
    column
):
    """
    Perform univariate analysis for categorical variables.
    """

    plot_countplot(
        data=df,
        column=column,
        title=f"{column} Distribution"
    )

    return frequency_table(
        df,
        column
    )