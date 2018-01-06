#!/usr/bin/python3
# -- Content-Encoding: UTF-8 --
"""
This bundle provides a component that is a simple implementation of the
Model service. It contains LogisticRegression.
"""

# iPOPO decorators
from pelix.ipopo.decorators import ComponentFactory, Property, Provides, \
    Validate, Invalidate, Instantiate

from sklearn.linear_model import LogisticRegression

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Name the iPOPO component factory
@ComponentFactory("data_iris")
# This component provides a dictionary service
@Provides("data_service")
# It is the LogisticRegression
@Property("_name", "name", "iris")
# Automatically instantiate a component when this factory is loaded
@Instantiate("data_iris_instance")
class Data(object):
    """
    Implementation of a model Service LogisticRegression.
    """

    def __init__(self):
        """
        Declares members, to respect PEP-8.
        """
        self.X = None
        self.y = None

    @Validate
    def validate(self, context):
        """
        The component is validated. This method is called right before the
        provided service is registered to the framework.
        """
        # All setup should be done here
        iris = load_iris()
        self.X, self.y = iris.data[:, :2], iris.target

        print('A Iris Data has been added')

    @Invalidate
    def invalidate(self, context):
        """
        The component has been invalidated. This method is called right after
        the provided service has been removed from the framework.
        """
        self.X = None
        self.y = None

    def get_data(self, **kwargs):

        data = {}

        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, *kwargs)

        data['name'] = 'iris'

        data['X_train'], data['X_test'], data['y_train'],\
            data['y_test'] = X_train, X_test, y_train, y_test

        return data

