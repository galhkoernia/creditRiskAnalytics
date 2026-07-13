#
# Created on Mon Jul 13 2026
#
# Copyright (c) 2026 Your Company
#

import pandas as pd


def create_average_balance(df):
    """
    Create average balance feature.
    """

    df["Avg Balance"] = (
        df[
            [
                "Balance Q1",
                "Balance Q2",
                "Balance Q3",
                "Balance Q4"
            ]
        ]
        .mean(axis=1)
    )

    return df


def create_balance_change(df):
    """
    Create balance change feature.
    """

    df["Balance Change"] = (
        df["Balance Q4"] -
        df["Balance Q1"]
    )

    return df


def create_average_products(df):
    """
    Create average products feature.
    """

    df["Avg Products"] = (
        df[
            [
                "NumOfProducts Q1",
                "NumOfProducts Q2",
                "NumOfProducts Q3",
                "NumOfProducts Q4"
            ]
        ]
        .mean(axis=1)
    )

    return df


def create_activity_rate(df):
    """
    Create activity rate feature.
    """

    df["Activity Rate"] = (
        df[
            [
                "ActiveMember Q1",
                "ActiveMember Q2",
                "ActiveMember Q3",
                "ActiveMember Q4"
            ]
        ]
        .mean(axis=1)
    )

    return df


def build_features(df):
    """
    Execute all feature engineering steps.
    """

    df = create_average_balance(df)
    df = create_balance_change(df)
    df = create_average_products(df)
    df = create_activity_rate(df)

    return df