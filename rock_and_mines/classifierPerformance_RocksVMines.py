__author__ = 'prabhath'

import pylab as pl
import numpy as np
from sklearn import linear_model, datasets
from sklearn.metrics import roc_curve, auc
import urllib2

"""
Structure involved.
1. Define Confusion Matrix.
2. Read the Data
3. Arrange the data to divide into training(2/3) and testing(1/3)
4. Training and predicting
5. Ploting ROC graphs using pylab.
"""


# 1. Confusion matrix
def confusionmatrix(predicted, actual, threshold):

    """
    :param predicted:
    :param actual:
    :param threshold:
    :return:
    """
    """ Length of predicted should be same as actual. """
    if len(predicted) != len(actual):
        return -1

    # Values
    tp = 0.0
    fp = 0.0
    tn = 0.0
    fn = 0.0

    for i in range(len(actual)):
        if actual[i] > 0.5:
            if predicted[i] > threshold:
                tp += 1.0 # Correctly predicted positive.
            else:
                fn += 1.0 # Incorrectly predicted negative.
        else:
            if predicted[i] < threshold:
                tn += 1.0 # Correctly predicted negative.
            else:
                fp += 1.0 # Incorrectly predicted positive.

    rtn = [tp, fp, tn, fn]
    return rtn


# 2. Get the data
target_url = ("https://archive.ics.uci.edu/ml/machine-learning-"
"databases/undocumented/connectionist-bench/sonar/sonar.all-data")
data = urllib2.urlopen(target_url)


# 3. Arrange the data to divide into training(2/3) and testing(1/3)

labels = []
xlists = []

for i in data:
    row = i.strip().split(',')
    # Add data into labels
    if (row[-1] == 'M'):
        labels.append(1.0)
    elif (row[-1] == 'R'):
        labels.append(0.0)
    # Remove the label from row
    row.pop()
    floatrow = [float(x) for x in row]
    xlists.append(floatrow)

# Divide the attribute matrix and label into train(2/3) and test(1/3)
index = range(len(xlists))
xlisttest = [xlists[i] for i in index if (i % 3) == 0]
xlisttrain = [xlists[i] for i in index if (i % 3) != 0]
labeltest = [labels[i] for i in index if (i % 3) == 0]
labeltrain = [labels[i] for i in index if (i % 3) != 0]

# Convert them into arrays to pass into scikit learn linear_model.
xTrain = np.array(xlisttrain)
yTrain = np.array(labeltrain)
xTest = np.array(xlisttest)
yTest = np.array(labeltest)

print "Shape of xTrain {0} and yTrain {1}" .format(xTrain.shape, yTrain.shape)
print "Shape of xTest {0} and yTest {1}" .format(xTest.shape, yTest.shape)

# 4. Training and predicting.

""" Train linear regression Model. """
rockvmines = linear_model.LinearRegression()
rockvmines.fit(xTrain, yTrain)

# Generate predictions on in-sample error
trainingpredictions = rockvmines.predict(xTrain)
print "Some predicted values {} - {}" .format(trainingpredictions[0:5], trainingpredictions[-6:-1])

# Generate confusion matrix for predictions on training set (in-sample)
confusionmatrixtrain = confusionmatrix(trainingpredictions, yTrain, 0.5)
tp = confusionmatrixtrain[0]
fp = confusionmatrixtrain[1]
tn = confusionmatrixtrain[2]
fn = confusionmatrixtrain[3]

print "tp = {0}, fp = {1}, tn = {2}, fn = {3}" .format(tp, fp, tn, fn)

# Generate predictions on out-of-sample error
testpredictions = rockvmines.predict(xTest)
print "Some predicted values on testing data set {} - {}" .format(trainingpredictions[0:5], trainingpredictions[-6:-1])

# Generate confusion matrix for predictions on training set (in-sample)
confusionmatrixtrain = confusionmatrix(testpredictions, yTest, 0.5)
tp_ = confusionmatrixtrain[0]
fp_ = confusionmatrixtrain[1]
tn_ = confusionmatrixtrain[2]
fn_ = confusionmatrixtrain[3]

print "tp = {0}, fp = {1}, tn = {2}, fn = {3}" .format(tp_, fp_, tn_, fn_)

# 5. Plotting Roc curve
""" Roc curve for in-sample data. """
fpr, tpr, threshold = roc_curve(yTrain, trainingpredictions)
auc_value = auc(fpr, tpr)

print "Auc for in-sample roc curve is {}" .format(auc_value)

# Plot roc curve
pl.clf()
pl.plot(fpr, tpr, label="Roc curve area {}" .format(auc_value))
pl.plot([0, 1], [0, 1], 'k-')
pl.xlim([0.0, 1.0])
pl.ylim([0.0, 1.0])
pl.xlabel('False positive rate.')
pl.ylabel('True positive rate.')
pl.title("In sample ROC rocks versus mines")
pl.legend(loc="lower right")
pl.savefig("In sample ROC rocks versus mines")
pl.show()

""" Roc curve for out of sample curve. """
fpr_, tpr_, threshold = roc_curve(yTest, testpredictions)
auc_value_ = auc(fpr_, tpr_)

print "Auc for out_sample-sample roc curve is {}" .format(auc_value_)

# Plot roc curve
pl.clf()
pl.plot(fpr_, tpr_, label="Roc curve area {}" .format(auc_value_))
pl.plot([0, 1], [0, 1], 'k-')
pl.xlim([0.0, 1.0])
pl.ylim([0.0, 1.0])
pl.xlabel('False positive rate.')
pl.ylabel('True positive rate.')
pl.title("Out of sample ROC rocks versus mines")
pl.legend(loc="lower right")
pl.savefig("Out of sample ROC rocks versus mines")
pl.show()
