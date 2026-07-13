#
# Created on Mon Jul 13 2026
#
# Copyright (c) 2026 Your Company
#

from analysis.multivariate import (
    correlation_analysis
)

from config.constants import (
    CORRELATION_COLUMNS
)


def run_multivariate(df):
    """
    Execute multivariate analysis.
    """

    correlation = correlation_analysis(
        df,
        CORRELATION_COLUMNS
    )

    return {
        "correlation": correlation
    }