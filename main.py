__author__ = 'prabhath'

import pandas as pd


class MainCollection(object):

    target_url = ("""https://archive.ics.uci.edu/ml/machine-learning-\
databases/undocumented/connectionist-bench/sonar/sonar.all-data""")

    def get_data(self):
        return pd.read_csv(MainCollection.target_url, header=None, prefix="A")

