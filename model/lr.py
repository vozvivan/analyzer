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
import numpy as np

from defaut_classes.model_services import ModelService

# Name the iPOPO component factory
@ComponentFactory("model_lr_factory")
# It is the LogisticRegression
@Property("_name", "name", "LogisticRegression")
# Automatically instantiate a component when this factory is loaded
@Instantiate("model_lr_instance")
class Model(ModelService):
    """
    Implementation of a model Service LogisticRegression.
    """

    @Validate
    def validate(self, context):
        """
        The component is validated. This method is called right before the
        provided service is registered to the framework.
        """
        # All setup should be done here
        self.model = LogisticRegression()

        print('A LinearRegression has been added')



