#!/usr/bin/python
# -- Content-Encoding: UTF-8 --
"""
Consumer of ml models
"""

# iPOPO decorators
from pelix.ipopo.decorators import ComponentFactory, Provides, \
    Validate, Invalidate, Requires, Instantiate, BindField, UnbindField

# Standard library
import re


# Name the component factory
@ComponentFactory("metric_consumer_factory")
# Provide a model consuber service
@Provides("metric_consumer_service")
# Consume all model consumer services available (aggregate them)
@Requires("_metrics", "metric_service", aggregate=True)
# Automatic instantiation
@Instantiate("metric_consumer_instance")
class MetricComsumer(object):
    """
    ...
    """

    def __init__(self):
        """
        Define class members
        """
        # the models, injected list
        self._metrics = []

        # the models, constructed
        self.metrics = {}

    @BindField('_metrics')
    def bind_dict(self, field, service, svc_ref):
        """
        Called by iPOPO when a spell dictionary service is bound to this
        component
        """
        # Extract the model from its properties
        metric = svc_ref.get_property('name')

        # Store the service according to its model
        self.metrics[metric] = service

    @UnbindField('_metrics')
    def unbind_dict(self, field, service, svc_ref):
        """
        Called by iPOPO when a dictionary service has gone away
        """
        # Extract the name of model from its properties
        metric = svc_ref.get_property('name')

        # Remove it from the computed storage
        # The injected list of services is updated by iPOPO
        del self.metrics[metric]

    @Validate
    def validate(self, context):
        """
        This consumer has been validated, i.e. at least one model
        has been bound.
        """
        # Set up internal members
        print('A metric consumer has been started')

    @Invalidate
    def invalidate(self, context):
        """
        The component has been invalidated
        """
        print('A metric consumer has been stopped')

    def evaluate(self, data, model):

        for metric in self.metrics:
            yield {
                'name': metric,\
                'value': self.metrics[metric].evaluate(data, model)
            }
