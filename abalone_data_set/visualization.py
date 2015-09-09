__author__ = 'prabhath'

from main import MainCollection
import pandas as pd
import matplotlib.pyplot as plot

data = MainCollection()
df = data.get_data()

summary = df.describe()
minRings = summary.iloc[3, 7]
maxRings = summary.iloc[7, 7]
nrows = len(df.index)
print df.head()

for i in range(nrows):
    # Plot the data
    dataRow = df.iloc[i, 1:8]
    labelColor = (df.iloc[i, 8] - minRings)/(maxRings - minRings)
    dataRow.plot(color=plot.cm.RdYlBu(labelColor), alpha=0.5)

plot.xlabel("Attribute Index")
plot.ylabel("Attribute Values")
plot.savefig("Parallel_Coordinate_Plot_for_Abalone_Data")
plot.show()

import numpy as np

a = np.random.rand(1,10)
plot.plot(a)
plot.show()
