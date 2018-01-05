#!/usr/bin/python3
# -- Content-Encoding: UTF-8 --
"""
This bundle provides a component that is a simple implementation of the
Model service. It contains LinearRegression.
"""

# iPOPO decorators
from pelix.ipopo.decorators import ComponentFactory, Property, Provides, \
    Validate, Invalidate, Instantiate

from sklearn.linear_model import LinearRegression


# Name the iPOPO component factory
@ComponentFactory("model_lr_factory")
# This component provides a dictionary service
@Provides("model_service")
# It is the GradientBoostingClassifier
@Property("_name", "name", "LinearRegression")
# Automatically instantiate a component when this factory is loaded
@Instantiate("model_lr_instance")
class Model(object):
    """
    Implementation of a model Service LinearRegression.
    """

    def __init__(self):
        """
        Declares members, to respect PEP-8.
        """
        self.model = None

    @Validate
    def validate(self, context):
        """
        The component is validated. This method is called right before the
        provided service is registered to the framework.
        """
        # All setup should be done here
        self.model = LinearRegression()

        print('A LinearRegression has been added')

    @Invalidate
    def invalidate(self, context):
        """
        The component has been invalidated. This method is called right after
        the provided service has been removed from the framework.
        """
        self.model = None

    def fit(self, X_train):
        """
        ...

        @param Train_data.
        @return True if the word is in the dictionary, False otherwise.
        """
        self.model.fit(X_train)

    def predict(self, X_test):
        """
        ...

        @param Test_data.
        @return tested
        """

        return self.model.predict(X_test) if self.model else -1
