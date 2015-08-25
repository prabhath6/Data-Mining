import urllib2
import pandas
import sys
from pandas.io.common import urlopen


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
ncol = len(xList[0])

print "Number of rows: {}" .format(nrow)
print "Number of columns: {}" .format(ncol)


#   ############################# Another way of dealing ##############################
# test = []
#
# with urlopen(target_url) as p:
#
#   for i in p:
#       q = i.strip().split(',')
#       test.append(q)
#   ############################# ----------------------- ##############################

""" Modifying to view the data based on the columns. """

type = [0] * 3
colCounts = []

for col in range(ncol):
    for row in xList:
        try:
            a = float(row[col])
            if isinstance(a, float):
                type[0] += 1
        except ValueError:
            if len(row[col]) > 0:
                type[1] += 1
            else:
                type[2] += 1
    colCounts.append(type)

    type = [0] * 3

sys.stdout.write("Col#" + "\t" + "Number" + "\t" + "strings" + "\t" + "Other\n")

iCol = 0

for types in colCounts:
    sys.stdout.write(str(iCol) + "\t\t" + str(types[0]) + "\t\t" + str(types[1]) + "\t\t" + str(type[2]) + "\n")

    iCol += 1
