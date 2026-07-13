#
# Created on Mon Jul 13 2026
#
# Copyright (c) 2026 galhkoernia
#

from visualization.plotter import (
    plot_heatmap
)


def correlation_analysis(
    df,
    columns
):
    """
    Generate correlation matrix.
    """

    correlation = (
        df[columns]
        .corr()
    )

    plot_heatmap(
        correlation
    )

    return correlation