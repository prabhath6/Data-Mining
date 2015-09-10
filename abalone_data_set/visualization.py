__author__ = 'prabhath'

from main import MainCollection
import matplotlib.pyplot as plot

fig = plot.gcf()

data = MainCollection()
df = data.get_data()

summary = df.describe()
minRings = summary.iloc[3, 7]
maxRings = summary.iloc[7, 7]
nrows = len(df.index)

for i in range(nrows):
    # Plot the data
    dataRow = df.iloc[i, 1:8]
    labelColor = (df.iloc[i, 8] - minRings)/(maxRings - minRings)
    dataRow.plot(color=plot.cm.RdYlBu(labelColor), alpha=0.5)

plot.xlabel("Attribute Index")
plot.ylabel("Attribute Values")
plot.savefig("Parallel_Coordinate_Plot_for_Abalone_Data")
plot.show()

# Heat Map (relation between the targets and values)
colMat = df.iloc[:, 1:9].corr()
plot.pcolor(colMat)
plot.savefig("HeatMap.png")
plot.show()