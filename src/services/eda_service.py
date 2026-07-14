#
# Created on Mon Jul 13 2026
#
# Copyright (c) 2026 Your Company
#

from src.services.univariate_service import (
    run_univariate
)

from src.services.bivariate_service import (
    run_bivariate
)

from src.services.multivariate_service import (
    run_multivariate
)


def run_complete_eda(df):
    """
    Execute complete EDA workflow.
    """

    results = {}

    print("=" * 60)
    print("Running Univariate Analysis")
    print("=" * 60)

    results["univariate"] = run_univariate(df)

    print("=" * 60)
    print("Running Bivariate Analysis")
    print("=" * 60)

    results["bivariate"] = run_bivariate(df)

    print("=" * 60)
    print("Running Multivariate Analysis")
    print("=" * 60)

    results["multivariate"] = run_multivariate(df)

    return results