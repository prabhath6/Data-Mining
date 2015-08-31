__author__ = 'prabhath'

from random import uniform

import matplotlib.pyplot as plot
import pandas as pd

from rock_and_mines.main import MainCollection


# Getting data

data = MainCollection()
df = data.get_data()


def correlation_(df):

    """
    Scatter Plot to caluclate relation between any two real valued
    attributes.
    It tells how one attibute relates to other.

    :param df: dataFrame
    :return: plot
    """
    dataRow2 = df.iloc[1, 0:60]
    dataRow3 = df.iloc[2, 0:60]
    dataRow30 = df.iloc[31, 0:60]

    plot.subplot(121)
    plot.scatter(dataRow2, dataRow3)
    plot.xlabel("2nd Attribute")
    plot.ylabel("3rd Attribute")
    plot.title("Cross plot between 2nd and 3rd attribute")

    plot.subplot(122)
    plot.scatter(dataRow2, dataRow30)
    plot.xlabel("2nd Attribute")
    plot.ylabel("30th Attribute")
    plot.title("Cross plot between 2nd and 30th attribute")

    plot.show()


def correlation__(df):
    """
        Scatter between unreal attribute(61) and 35th attribute.
    :param df:
    :return:
    """

    # target = []
    # for i in range(208):
    #     if df.iat[i, 60] == "M":
    #         target.append(1 + uniform(-0.1, 0.1))
    #     elif df.iat[i, 60] == "R":
    #         target.append(0 + uniform(-0.1, 0.1))

    target = [(1 + uniform(-0.1, 0.1)) if df.iat[i, 60] == "M" else (0 + uniform(-0.1, 0.1)) for i in range(208)]

    # 35th attribute
    dataRow = df.iloc[0:208, 35]

    plot.scatter(dataRow, target, alpha=0.5, s=120)
    plot.xlabel("Attribute avlue")
    plot.ylabel("Target value")
    plot.title("Cross plot between target and attribute")
    plot.show()


def heat_plot(df):
    """Heat plot of correlation using pandas"""
    cor_plot = pd.DataFrame(df.corr())

    plot.pcolor(cor_plot)
    plot.title("Heat map showing attributes cross correlation")
    plot.show()




if __name__ == "__main__":

    correlation_(df)
    correlation__(df)
    heat_plot(df)