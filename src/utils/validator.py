#
# Created on Mon Jul 13 2026
#
# Copyright (c) 2026 galhkoernia
#

def validate_columns(df, required_columns):
    """
    Validate required columns.
    """

    missing = [
        column
        for column in required_columns
        if column not in df.columns
    ]

    if missing:
        raise ValueError(
            f"Missing columns: {missing}"
        )

    return True


def validate_dataframe(df):
    """
    Validate dataframe object.
    """

    if df.empty:
        raise ValueError(
            "DataFrame is empty."
        )

    return True