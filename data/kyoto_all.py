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

from defaut_classes.data_services import KyotoDataService

@ComponentFactory("data_kyoto_all")
@Property("_name", "name", "kyoto_all")
@Instantiate("data_kyoto_all_instance")
class Data(KyotoDataService):


    @Validate
    def validate(self, context):

        print('A Kyoto Data All has been added')

