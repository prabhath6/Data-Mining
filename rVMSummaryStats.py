__author__ = 'prabhath'

import urllib2
import sys
import numpy as np
import matplotlib.pyplot as plt

# Reading data
target_url = ("""https://archive.ics.uci.edu/ml/machine-learning-\
databases/undocumented/connectionist-bench/sonar/sonar.all-data""")


data = urllib2.urlopen(target_url)

# Arranging data
xList = []
labels = []

for line in data:
    row = line.strip().split(',')
    xList.append(row)

nrow = len(xList)
ncol = len(xList[1])

type = [0] * 3
colCounts = []

# Generating summary statistics for column 3
col = 3
colData = []
for row in xList:
    colData.append(float(row[col]))

# Converting into array
colAry = np.array(colData)
colMean = np.mean(colAry)
colSTD = np.std(colAry)
colVar = np.var(colAry)

sys.stdout.write("\nMean: {} \nStandard deviation: {}\nVariance: {}\n" .format(colMean, colSTD, colVar))


def quantile(ntiles):
    """
    :param ntiles:
    :return: list of quantiles
    """
    result = []

    for i in range(ntiles + 1):
        result.append(np.percentile(colAry, i * (100)/ ntiles))
    return result

sys.stdout.write("\nBoundaries for 4 Equal Percentiles \n")
percentBdry_4 = quantile(4)
print(percentBdry_4)
sys.stdout.write(" \n")

sys.stdout.write("\nBoundaries for 10 Equal Percentiles \n")
percentBdry_10 = quantile(10)
print(percentBdry_10)
sys.stdout.write(" \n")

# Analyzing the last column of the data i.e the character coloumn

col = 60
colData_ = []

for row in xList:
    colData_.append(row[col])

colCount_ = list(set(colData_))
final = {colCount_[0]: colData_.count(colCount_[0]), colCount_[1]: colData_.count(colCount_[1])}

print "Counts for Each Value of Categorical Label\n{}." .format(final)

""" Visualization """
plt.bar(range(len(final)), final.values())
plt.xticks(range(len(final)), list(final.keys()))
plt.title("R and M Summary")
plt.savefig("R and M Summary")
plt.show()
