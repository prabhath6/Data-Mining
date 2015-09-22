__author__ = 'prabhath'

from main import MainCollection
import matplotlib.pyplot as plt
import pandas as pd

data = MainCollection()
df = data.get_data()
df.columns = ['Id', 'RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe', 'Type']


def boxplot(df):
    """
    :param df:
    :return: box plot
    """

    df = df.iloc[:, 1:len(df.columns)]
    summary = df.describe()
    normalizedvalues = df

    ncols = len(df.columns)

    for i in range(ncols):
        mean = summary.iloc[1, i]
        sd = summary.iloc[2, i]

        normalizedvalues.iloc[:, i:(i+1)] = (normalizedvalues.iloc[:, i:(i+1)] - mean) / sd

    plt.boxplot(normalizedvalues.values[0:len(normalizedvalues.values)])
    plt.xlabel("Attribute Index")
    plt.ylabel("Quartile Ranges - Normalized ")
    plt.savefig("Box plot")
    plt.show()


def coordinateplot(df):
    """
    :param df:
    :return: parallel coordinate plot.
    """

    df = df.iloc[:, 1:len(df.columns)]
    summary = df.describe()
    normalizedvalues = df

    ncols = len(df.columns)
    nrows = len(df.index)

    for i in range(ncols):
        mean = summary.iloc[1, i]
        sd = summary.iloc[2, i]

        normalizedvalues.iloc[:, i:(i+1)] = (normalizedvalues.iloc[:, i:(i+1)] - mean) / sd

    for i in range(nrows):
        data_df = normalizedvalues.iloc[i, 1 : (ncols - 1)]
        colorlabel = normalizedvalues.iloc[i, (ncols - 1)]/7.0
        data_df.plot(color=plt.cm.RdYlBu(colorlabel), alpha=0.5)

    plt.xlabel("Attribute Index")
    plt.ylabel(("Attribute Values"))
    plt.savefig("Co-ordinate plot")
    plt.show()


def colorplot(df):
    """
    :param df:
    :return: heat map
    """
    df = df.iloc[:, 1:len(df.columns)]
    summary = df.describe()
    normalizedvalues = df

    ncols = len(df.columns)

    for i in range(ncols):
        mean = summary.iloc[1, i]
        sd = summary.iloc[2, i]

        normalizedvalues.iloc[:, i:(i+1)] = (normalizedvalues.iloc[:, i:(i+1)] - mean) / sd

    colr = normalizedvalues.iloc[:, 1:10].corr()
    plt.pcolor(colr)
    plt.title("Heat map")
    plt.savefig("Heat map")
    plt.show()


if __name__ == "__main__":
    boxplot(df)
    coordinateplot(df)
    colorplot(df)