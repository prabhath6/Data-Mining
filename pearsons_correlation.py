__author__ = 'prabhath'

from main import MainCollection
import numpy as np

data = MainCollection()
df = data.get_data()


def correlation_caluclation():
    """
    :return:
    """

    # Calucalte correlation between real valued attributes.
    dataRow2 = df.iloc[1, 0:60]
    dataRow3 = df.iloc[2, 0:60]
    dataRow21 = df.iloc[20, 0:60]

    # Mean
    mean2 = np.mean(dataRow2)
    mean3 = np.mean(dataRow3)
    mean21 = np.mean(dataRow21)

    # variance
    var2 = np.var(dataRow2)
    var3 = np.mean(dataRow3)
    var21 = np.mean(dataRow21)

    # correlation
    corr23 = 0.0
    corr221 = 0.0

    for i in range(len(dataRow2)):
        corr23 += ((dataRow2[i] - mean2) * (dataRow3[i] - mean3)) / (np.sqrt(var2 * var3) * (len(dataRow2)))
        corr221 += ((dataRow2[i] - mean2) * (dataRow21[i] - mean21)) / (np.sqrt(var2 * var21) * (len(dataRow2)))

    print "Correlation of 2 & 3 {}" .format(corr23)
    print "Correlation of 2 & 21 {}" .format(corr221)

if __name__ == "__main__":
    correlation_caluclation()
