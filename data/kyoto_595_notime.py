#!/usr/bin/python3
# -- Content-Encoding: UTF-8 --
"""
This bundle provides a component that is a simple implementation of the
Model service. It contains LogisticRegression.
"""

# iPOPO decorators
from pelix.ipopo.decorators import ComponentFactory, Property, Provides, \
    Validate, Invalidate, Instantiate, Requires


from sklearn.model_selection import train_test_split
from defaut_classes.data_services import KyotoDataService

# Name the iPOPO component factory
@ComponentFactory("data_kyoto_595_notime")
@Property("_name", "name", "Kyoto 5:95 NoTime")
@Instantiate("data_kyoto_595_notime_instance")
class Data(KyotoDataService):
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

        print('A Kyoto Data 5:95 No Time has been added')


    def get_data(self, **kwargs):
        self.df = self._kyoto_data.get_data(p_attacks=.05, time=False)

        self.split()

        return self.data

