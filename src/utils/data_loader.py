#
# Created on Mon Jul 13 2026
#
# Copyright (c) 2026 galhkoernia
#

import pandas as pd


def load_dataset(path):
    """
    Load dataset from CSV file.

    Parameters
    ----------
    path : str or Path
        Dataset path.

    Returns
    -------
    pandas.DataFrame
    """

    return pd.read_csv(path)


def save_dataset(df, path):
    """
    Save dataframe to CSV.
    """

    df.to_csv(path, index=False)