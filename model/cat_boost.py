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

from defaut_classes.model_services import ModelService

# Name the iPOPO component factory
@ComponentFactory("model_cat_boost_factory")
# It is the GradientBoostingClassifier
@Property("_name", "name", "CatBoost")
# Automatically instantiate a component when this factory is loaded
@Instantiate("model_cat_boost_instance")
class Model(ModelService):
    """
    Implementation of a model GradientBoostingClassifier.
    """


    @Validate
    def validate(self, context):
        """
        The component is validated. This method is called right before the
        provided service is registered to the framework.
        """
        # All setup should be done here

        print('A CatBoost has been added')


    def fit(self, data):
        """
        ...

        @param Train_data.
        @return True if the word is in the dictionary, False otherwise.
        """
        self.model = CatBoost()
        try:
            self.features = list(data['X_train'].columns)
        except:
            print('Warning\nHAVE NO INFO ABOUT FEATURES')
            self.features = []
        try:
            p = Pool(data['X_train'], data['y_train'], data['cat_features'])
        except KeyError:
            print('Nothing know bout categorical features')
            p = Pool(data['X_train'], data['y_train'], [])

        self.model.fit(p, logging_level='Silent')

    def predict(self, data):
        test = Pool(data['X_test'])
        return self.model.predict(test, prediction_type='Class') if self.model else -1
