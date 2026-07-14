#
# Created on Mon Jul 13 2026
#
# Copyright (c) 2026 galhkoernia
#

from src.utils.statistics import unpaid_rate

from src.visualization.plotter import (
    plot_boxplot,
    plot_bar
)


def compare_with_target(
    df,
    feature,
    target
):
    """
    Compare numerical feature against target.
    """

    plot_boxplot(
        data=df,
        x=target,
        y=feature,
        title=f"{feature} vs {target}"
    )

    return (
        df
        .groupby(target)[feature]
        .describe()
    )


def analyze_unpaid_rate(
    df,
    group_column,
    target
):
    """
    Calculate unpaid rate by category.
    """

    result = unpaid_rate(
        df,
        group_column,
        target
    )

    plot_bar(
        data=result,
        x=group_column,
        y="Unpaid_Rate",
        title=f"Unpaid Rate by {group_column}"
    )

    return result