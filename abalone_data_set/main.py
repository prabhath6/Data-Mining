__author__ = 'prabhath'

import pandas as pd


class MainCollection(object):

    target_url = ("http://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data")

    def get_data(self):

        abalone = pd.read_csv(MainCollection.target_url, header=None, prefix="V")
        abalone.columns = ['Sex', 'Length', 'Diameter', 'Height', 'Whole weight','Shucked weight',
                           'Viscera weight','Shell weight', 'Rings']

        return abalone