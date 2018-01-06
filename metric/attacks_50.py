#!/usr/bin/python3
# -- Content-Encoding: UTF-8 --
"""
This bundle provides a component that is a simple implementation of the
Model service. It contains GradientBoostingClassifier.
"""

# iPOPO decorators
from pelix.ipopo.decorators import ComponentFactory, Property, Provides, \
    Validate, Invalidate, Instantiate

from sklearn.metrics import accuracy_score
import pandas as pd

# Name the iPOPO component factory
@ComponentFactory("metric_attacks_50_factory")
# This component provides a dictionary service
@Provides("metric_service")
# It is the GradientBoostingClassifier
@Property("_name", "name", "Attacks 50")
# Automatically instantiate a component when this factory is loaded
@Instantiate("metric_attacks_50_instance")
class Metric(object):
    """
    Implementation of a model GradientBoostingClassifier.
    """

    @Validate
    def validate(self, context):
        """
        The component is validated. This method is called right before the
        provided service is registered to the framework.
        """

        print('A Attacks 50 has been added')

    @Invalidate
    def invalidate(self, context):
        """
        The component has been invalidated. This method is called right after
        the provided service has been removed from the framework.
        """
        print('A Attacks 50 has been removed')

    def evaluate(self, data, model):
        pred = pd.Series(model['model'].predict_by_proba(data['bank']))
        return 100*pred[pred==1].shape[0] / pred.shape[0]
