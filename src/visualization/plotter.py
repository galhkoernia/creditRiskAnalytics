#
# Created on Mon Jul 13 2026
#
# Copyright (c) 2026 galhkoernia
#

import matplotlib.pyplot as plt
import seaborn as sns

from .style import set_plot_style

def plot_histogram(
    data,
    column,
    bins=30,
    title=None
):
    """
    Plot histogram.
    """

    set_plot_style()

    plt.figure()

    sns.histplot(
        data=data,
        x=column,
        bins=bins,
        kde=True
    )

    plt.title(title or column)
    plt.xlabel(column)
    plt.ylabel("Frequency")

    plt.tight_layout()
    plt.show()

def plot_boxplot(
    data,
    x=None,
    y=None,
    title=None
):
    """
    Plot boxplot.
    """

    set_plot_style()

    plt.figure()

    sns.boxplot(
        data=data,
        x=x,
        y=y
    )

    plt.title(title)

    plt.tight_layout()
    plt.show()

def plot_countplot(
    data,
    column,
    title=None,
    rotation=0
):
    """
    Plot countplot.
    """

    set_plot_style()

    plt.figure()

    ax = sns.countplot(
        data=data,
        x=column
    )

    total = len(data)

    for patch in ax.patches:

        percentage = (
            patch.get_height() /
            total
        ) * 100

        ax.annotate(
            f"{percentage:.1f}%",
            (
                patch.get_x() + patch.get_width() / 2,
                patch.get_height()
            ),
            ha="center",
            va="bottom"
        )

    plt.xticks(rotation=rotation)

    plt.title(title or column)

    plt.tight_layout()
    plt.show()

def plot_bar(
    data,
    x,
    y,
    title=None,
    rotation=0
):
    """
    Plot barplot.
    """

    set_plot_style()

    plt.figure()

    sns.barplot(
        data=data,
        x=x,
        y=y
    )

    plt.xticks(rotation=rotation)

    plt.title(title)

    plt.tight_layout()
    plt.show()

def plot_heatmap(
    correlation,
    title="Correlation Matrix"
):
    """
    Plot correlation heatmap.
    """

    set_plot_style()

    plt.figure(figsize=(8, 6))

    sns.heatmap(
        correlation,
        annot=True,
        cmap="RdBu_r",
        fmt=".2f",
        square=True
    )

    plt.title(title)

    plt.tight_layout()
    plt.show()

