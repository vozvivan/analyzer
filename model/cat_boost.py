#!/usr/bin/python3
# -- Content-Encoding: UTF-8 --
"""
This bundle provides a component that is a simple implementation of the
Model service. It contains GradientBoostingClassifier.
"""

# iPOPO decorators
from pelix.ipopo.decorators import ComponentFactory, Property, Provides, \
    Validate, Invalidate, Instantiate

from sklearn.ensemble import GradientBoostingClassifier

from catboost import Pool, CatBoost

# Name the iPOPO component factory
@ComponentFactory("model_cat_boost_factory")
# This component provides a dictionary service
@Provides("model_service")
# It is the GradientBoostingClassifier
@Property("_name", "name", "CatBoost")
# Automatically instantiate a component when this factory is loaded
@Instantiate("model_cat_boost_instance")
class Model(object):
    """
    Implementation of a model GradientBoostingClassifier.
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

        print('A CatBoost has been added')

    @Invalidate
    def invalidate(self, context):
        """
        The component has been invalidated. This method is called right after
        the provided service has been removed from the framework.
        """
        self.model = None

    def fit(self, data):
        """
        ...

        @param Train_data.
        @return True if the word is in the dictionary, False otherwise.
        """
        self.model = CatBoost()
        try:
            p = Pool(data['X_train'], data['y_train'], data['cat_features'])
        except KeyError:
            print('Nothing know bout categorical features')
            p = Pool(data['X_train'], data['y_train'], [])

        self.model.fit(p, logging_level='Silent')

    def predict(self, data):
        """
        ...

        @param Test_data.
        @return tested
        """
        test = Pool(data['X_test'])
        return self.model.predict(test, prediction_type='Class') if self.model else -1
