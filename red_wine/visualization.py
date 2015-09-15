__author__ = 'prabhath'

from main import MainCollection
import math
import matplotlib.pyplot as plt


data = MainCollection()
df = data.get_data()


def boxplot(df):
    """
    :param df:
    :return: Plot returned with normalized values.
    """

    summary = df.describe()
    normalizedValues = df

    ncols = len(normalizedValues.columns)

    for i in range(ncols):
        mean = summary.iloc[1, i]
        sd = summary.iloc[2, i]

        normalizedValues.iloc[:, i:(i+1)] = (normalizedValues.iloc[:, i:(i+1)] - mean) / sd

    array = normalizedValues.values
    plt.boxplot(array)
    plt.xlabel("Attribute Index")
    plt.ylabel(("Quartile Ranges - Normalized "))
    plt.savefig("Boxplot")
    plt.show()


def coordinateplot(df):
    """
    :param df:
    :return: coordinate plot taste of wine.
    """

    """ Normalizing the values to work on. """
    normalizedvalues = df
    ncol = len(normalizedvalues.columns)
    summary = df.describe()
    nDataCol = len(df.columns) - 1

    for i in range(ncol):
        mean = summary.iloc[1, i]
        sd = summary.iloc[2, i]
        normalizedvalues.iloc[:,i:(i + 1)] = (normalizedvalues.iloc[:,i:(i + 1)] - mean) / sd

    """ Plotting with different colors. """
    for j in range(len(normalizedvalues.index)):
        dataRow = normalizedvalues.iloc[j, 1:nDataCol]
        normTarget = normalizedvalues.iloc[j, nDataCol]
        labelColor = 1.0/(1.0 + math.exp(-normTarget))
        dataRow.plot(color=plt.cm.RdYlBu(labelColor), alpha=0.5)

    plt.xlabel("Attribute Index")
    plt.ylabel(("Attribute Values"))
    plt.savefig("Co-ordinate plot")
    plt.show()

def corelationplot(df):
    """
    :param df:
    :return: correlation plot
    """

    corm = df.iloc[:, 0:12].corr()
    plt.pcolor(corm)
    plt.savefig("HeatMap.png")
    plt.show()


if __name__ == "__main__":
    boxplot(df)
    coordinateplot(df)
    corelationplot(df)
