#!/usr/bin/python
# -- Content-Encoding: UTF-8 --
"""
Consumer of ml models
"""

# iPOPO decorators
from pelix.ipopo.decorators import ComponentFactory, Provides, \
    Validate, Invalidate, Requires, Instantiate, BindField, UnbindField

import pandas as pd

# Standard library
import re


# Name the component factory
@ComponentFactory("data_consumer_factory")
# Provide a model consuber service
@Provides("data_consumer_service")
# Consume all model consumer services available (aggregate them)
@Requires("_datasets", "data_service", aggregate=True)
# Automatic instantiation
@Instantiate("data_consumer_instance")
class DataComsumer(object):
    """
    ...
    """

    def __init__(self):
        """
        Define class members
        """
        # the models, injected list
        self._datasets = []

        # the models, constructed
        self.datasets = {}

    @BindField('_datasets')
    def bind_dict(self, field, service, svc_ref):
        """
        Called by iPOPO when a spell dictionary service is bound to this
        component
        """
        # Extract the model from its properties
        data_name = svc_ref.get_property('name')

        # Store the service according to its model
        self.datasets[data_name] = service

    @UnbindField('_data')
    def unbind_dict(self, field, service, svc_ref):
        """
        Called by iPOPO when a dictionary service has gone away
        """
        # Extract the name of model from its properties
        data_name = svc_ref.get_property('name')

        # Remove it from the computed storage
        # The injected list of services is updated by iPOPO
        del self.datasets[data_name]

    @Validate
    def validate(self, context):
        """
        This consumer has been validated, i.e. at least one model
        has been bound.
        """
        # Set up internal members
        print('A data consumer has been started')

    @Invalidate
    def invalidate(self, context):
        """
        The component has been invalidated
        """
        print('A data consumer has been stopped')

    def get_data(self, **kwargs):

        for data in self.datasets:
            yield self.datasets[data].get_data(*kwargs)
