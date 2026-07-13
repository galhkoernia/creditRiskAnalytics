#
# Created on Mon Jul 13 2026
#
# Copyright (c) 2026 galhkoernia
#

import pandas as pd


def percentage(series):
    """
    Convert numeric values to percentage.
    """

    return series.round(2).astype(str) + "%"


def currency(series):
    """
    Format currency.
    """

    return series.map(
        lambda x: f"Rp{x:,.2f}"
    )


def integer(series):
    """
    Format integer.
    """

    return series.map(
        lambda x: f"{int(x):,}"
    )