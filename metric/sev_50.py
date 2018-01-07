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
from defaut_classes.metric_services import SevMetricService

# Name the iPOPO component factory
@ComponentFactory("metric_sev_50_factory")
# It is the GradientBoostingClassifier
@Property("_name", "name", "Sev 50")
# Automatically instantiate a component when this factory is loaded
@Instantiate("metric_sev_50_instance")
class Metric(SevMetricService):
    """
    Implementation of a model GradientBoostingClassifier.
    """

    @Validate
    def validate(self, context):
        """
        The component is validated. This method is called right before the
        provided service is registered to the framework.
        """

        print('A Sev 50 has been added')
