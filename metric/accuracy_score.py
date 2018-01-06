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


# Name the iPOPO component factory
@ComponentFactory("metric_accuracy_score_factory")
# This component provides a dictionary service
@Provides("metric_service")
# It is the GradientBoostingClassifier
@Property("_name", "name", "Accuracy Score")
# Automatically instantiate a component when this factory is loaded
@Instantiate("metric_accuracy_score_instance")
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

        print('A Accuracy Score has been added')

    @Invalidate
    def invalidate(self, context):
        """
        The component has been invalidated. This method is called right after
        the provided service has been removed from the framework.
        """
        print('A Accuracy Score has been removed')

    def evaluate(self, data, model):
        return accuracy_score(data['y_test'], model['predict'])
