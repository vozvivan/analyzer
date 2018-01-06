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
import numpy as np
from defaut_classes.model_services import ModelService

# Name the iPOPO component factory
@ComponentFactory("model_gb_clf_factory")
# It is the GradientBoostingClassifier
@Property("_name", "name", "GradientBoostingClassifier")
# Automatically instantiate a component when this factory is loaded
@Instantiate("model_gb_clf_instance")
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

        self.model = GradientBoostingClassifier()

        print('A GradientBoostingClassifier has been added')




