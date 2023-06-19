import seaborn as sns
import matplotlib.pyplot as plt

def format_seaborn_plots():
    sns.set(style="whitegrid")
    sns.set_palette("rocket")
    sns.set_context("talk")
    plt.rcParams["figure.figsize"] = (8, 4)
    plt.rcParams["axes.titlesize"] = 14
    plt.rcParams["axes.labelsize"] = 12
    plt.rcParams["xtick.labelsize"] = 10
    plt.rcParams["ytick.labelsize"] = 10
    plt.rcParams["legend.fontsize"] = 8
    plt.rcParams["figure.autolayout"] = True