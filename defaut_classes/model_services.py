#!/usr/bin/python3
# -- Content-Encoding: UTF-8 --
"""
This bundle provides a component that is a simple implementation of the
Model service. It contains GradientBoostingClassifier.
"""

# iPOPO decorators
from pelix.ipopo.decorators import ComponentFactory, Property, Provides, \
    Validate, Invalidate, Instantiate

import numpy as np

@ComponentFactory("def_model_factory")
@Provides("model_service")
@Property("_name", "name", "Default Model Service")
@Instantiate("def_model_instance")
class ModelService(object):

    def __init__(self):
        self.model = None
        self.features = None

    @Validate
    def validate(self, context):

        print('A Default Model Service has been added')

    @Invalidate
    def invalidate(self, context):
        self.model = None
        self.features = None

    def fit(self, data):
        """
        ...

        @param Train_data.
        @return True if the word is in the dictionary, False otherwise.
        """
        try:
            self.model.fit(data['X_train'], data['y_train'])
        except Exception as ex:
            raise Exception('{} for {}'.format(str(ex), self._name))
        try:
            self.features = list(data['X_train'].columns)
        except:
            print('Warning: HAVE NO INFO ABOUT FEATURES when fitting {} on {}'.format(self._name, data['name']))
            self.features = []

    def predict(self, data):
        try:
            if self.features:
                pred=self.model.predict_proba(data['X_test'][self.features])
            else:
                print('Try to predict with no info bout binding of fetures in {} on {}'.format(self._name, data['name']))
                pred = self.model.predict(data['X_test'])
            return self.model.predict(data['X_test'])
        except Exception as ex:
            raise Exception('Cannot predict')

    def predict_by_proba(self, data, p_value=0.5):
        """
        ...

        @param Test_data.
        @return tested
        """
        pred = []
        try:
            if self.features:
                pred=self.model.predict_proba(data['X_test'][self.features])
            else:
                print('Try to predict with no info bout binding of fetures in {} on {}'.format(self._name, data['name']))
                pred = self.model.predict_proba(data['X_test'])
        except Exception as ex :
            raise Exception('Cannot predict')
        else:
            return np.apply_along_axis(lambda x: 1 if x[0] > p_value else 0, 1, pred)



