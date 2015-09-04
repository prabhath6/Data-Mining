__author__ = 'prabhath'

from main import MainCollection
import matplotlib.pyplot as plot

data = MainCollection()
df = data.get_data()

# Summary
summary = df.describe()

# Box plot
plot.subplot(411)
array = df.iloc[:, 1:9].values
plot.boxplot(array)
plot.xlabel("Attribute Index")
plot.ylabel("Quartile Ranges")


# Box plot by removing abnormalities
plot.subplot(412)
array1 = df.iloc[:, 1:8].values
plot.boxplot(array1)
plot.xlabel("Attribute Index")
plot.ylabel("Quartile Ranges")


# Normalizing the abnormal values

""" 1. Rescaling. """
df_ = df
min_ = min(df["Rings"])
max_ = max(df["Rings"])


for i in range(4177):
    df_.loc[i, 9] = float(df_.iloc[i, 8] - min_) / (max_ + min_)

plot.subplot(413)
array2 = df_.iloc[:, 1:10].values
plot.boxplot(array2)
plot.xlabel("Attribute Index")
plot.ylabel("Quartile Ranges")
plot.title("Rescaled plot")


"""
renormalize columns to zero mean and unit standard deviation
this is a common normalization and desirable for other operations
(subtract feature with mean and divide by variance)
"""

abaloneNormalized = df.iloc[:, 1:9]

for i in range(8):
    mean = summary.iloc[1, i]
    sd = summary.iloc[2, i]

    abaloneNormalized.iloc[:, i:(i+1)] = (abaloneNormalized.iloc[:,i:(1+i)] - mean)/sd

plot.subplot(414)
array3 = abaloneNormalized.values
plot.boxplot(array3)
plot.xlabel("Attribute Index")
plot.ylabel("Quartile Ranges")
plot.title("renormalized plots")
plot.show()