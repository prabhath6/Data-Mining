__author__ = 'prabhath'

import pandas as pd

class MainCollection(object):

    target_url = ("https://archive.ics.uci.edu/ml/machine-"\
"learning-databases/glass/glass.data")

    def get_data(self):
        return pd.read_csv(MainCollection.target_url, prefix='V')

if __name__ == "__main__":
    a = MainCollection()
    b = a.get_data()
    b.columns = ['Id', 'RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe', 'Type']
    print b.columns[1:len(b.columns)]
    print b.head()