#
# Created on Mon Jul 13 2026
#
# Copyright (c) 2026 galhkoernia
#

import matplotlib.pyplot as plt
import seaborn as sns


def set_plot_style():
    """
    Apply global visualization style.
    """

    sns.set_theme(
        style="whitegrid",
        palette="deep"
    )

    plt.rcParams["figure.figsize"] = (8, 5)
    plt.rcParams["figure.dpi"] = 100
    plt.rcParams["axes.titlesize"] = 11
    plt.rcParams["axes.labelsize"] = 10
    plt.rcParams["xtick.labelsize"] = 8
    plt.rcParams["ytick.labelsize"] = 8