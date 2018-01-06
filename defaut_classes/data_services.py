#!/usr/bin/python3
# -- Content-Encoding: UTF-8 --
"""
This bundle provides a component that is a simple implementation of the
Model service. It contains LogisticRegression.
"""

# iPOPO decorators
from pelix.ipopo.decorators import ComponentFactory, Property, Provides, \
    Validate, Invalidate, Instantiate, Requires

from sklearn.linear_model import LogisticRegression

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


@Provides("data_service")
@Requires("_kyoto_data", "data_kyoto_service")
@Property("_name", "name", "kyoto_defalut")
@Instantiate("data_kyoto_default_instance")
class KyotoDataService(object):

    def __init__(self):
        self.df = None
        self.data = {}

    @Validate
    def validate(self, context):

        print('A Kyoto Data Service has been added')

    @Invalidate
    def validate(self, context):
        self.df=None
        self.data={}
        print('A Kyoto Data Service has been removed')

    def split(self, **kwargs):
        X_train, X_test, y_train, y_test = train_test_split(self.df.drop(['_Label_'], axis=1), self.df['_Label_'],
                                                            **kwargs)
        self.data['X_train'], self.data['X_test'], self.data['y_train'], \
        self.data['y_test'] = X_train, X_test, y_train, y_test

        self.data['cat_features'] = [0, 1, 2]

    def get_data(self, **kwargs):
        self.df = self._kyoto_data.get_data()

        self.split()

        return self.data

