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
    plt.show()

if __name__ == "__main__":
    boxplot(df)