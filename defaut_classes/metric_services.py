#!/usr/bin/python3
# -- Content-Encoding: UTF-8 --
"""
This bundle provides a component that is a simple implementation of the
Model service. It contains GradientBoostingClassifier.
"""

# iPOPO decorators
from pelix.ipopo.decorators import ComponentFactory, Property, Provides, \
    Validate, Invalidate, Instantiate

import pandas as pd

# Name the iPOPO component factory
@ComponentFactory("metric_attacks_default_factory")
# This component provides a dictionary service
@Provides("metric_service")
# It is the GradientBoostingClassifier
@Property("_name", "name", "Default Attacks")
# Automatically instantiate a component when this factory is loaded
@Instantiate("metric_attacks_defalut_instance")
class AttacksMetricService(object):
    """
    Implementation of a model GradientBoostingClassifier.
    """

    @Validate
    def validate(self, context):
        """
        The component is validated. This method is called right before the
        provided service is registered to the framework.
        """

        print('A Attacks Default has been added')

    @Invalidate
    def invalidate(self, context):
        """
        The component has been invalidated. This method is called right after
        the provided service has been removed from the framework.
        """
        print('A Attacks Default has been removed')

    def perc_attacks(self, data, model, p_value=.5):
        pred = pd.Series(model['model'].predict_by_proba(data['bank'], p_value))
        return 100 * pred[pred == 1].shape[0] / pred.shape[0]

    def evaluate(self, data, model):
        return self.perc_attacks(data, model)


# Name the iPOPO component factory
@ComponentFactory("metric_sev_default_factory")
# This component provides a dictionary service
@Provides("metric_service")
# It is the GradientBoostingClassifier
@Property("_name", "name", "Sev Default")
# Automatically instantiate a component when this factory is loaded
@Instantiate("metric_sev_default_instance")
class SevMetricService(object):
    """
    Implementation of a model GradientBoostingClassifier.
    """

    @Validate
    def validate(self, context):
        """
        The component is validated. This method is called right before the
        provided service is registered to the framework.
        """

        print('A Sev Default has been added')

    @Invalidate
    def invalidate(self, context):
        """
        The component has been invalidated. This method is called right after
        the provided service has been removed from the framework.
        """
        print('A Sev Default has been removed')

    def perc_sev10_in_attacks(self, data, model, p_value=.5):
        df = pd.DataFrame()
        df['sev'] = pd.Series(data['bank']['sev'])
        df['predict'] = pd.Series(model['model'].predict_by_proba(data['bank'], p_value))

        return 100 * (df[(df['sev'] == 10) & (df['predict'] == 1)].shape[0]) / df[(df['sev'] == 10)].shape[0]

    def evaluate(self, data, model):
        return self.perc_sev10_in_attacks(data, model)