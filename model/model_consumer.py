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
@ComponentFactory("model_consumer_factory")
# Provide a model consuber service
@Provides("model_consumer_service")
# Consume all model consumer services available (aggregate them)
@Requires("_models", "model_service", aggregate=True)
# Automatic instantiation
@Instantiate("model_consumer_instance")
class ModelComsumer(object):
    """
    ...
    """

    def __init__(self):
        """
        Define class members
        """
        # the models, injected list
        self._models = []

        # the models, constructed
        self.models = {}

    @BindField('_models')
    def bind_dict(self, field, service, svc_ref):
        """
        Called by iPOPO when a spell dictionary service is bound to this
        component
        """
        # Extract the model from its properties
        model = svc_ref.get_property('name')

        # Store the service according to its model
        self.models[model] = service

    @UnbindField('_models')
    def unbind_dict(self, field, service, svc_ref):
        """
        Called by iPOPO when a dictionary service has gone away
        """
        # Extract the name of model from its properties
        model = svc_ref.get_property('name')

        # Remove it from the computed storage
        # The injected list of services is updated by iPOPO
        del self.models[model]

    @Validate
    def validate(self, context):
        """
        This consumer has been validated, i.e. at least one model
        has been bound.
        """
        # Set up internal members
        print('A model consumer has been started')

    @Invalidate
    def invalidate(self, context):
        """
        The component has been invalidated
        """
        print('A model consumer has been stopped')

    def check_model(self, data, all=True, model='GradientBoostingClassifier'):
        """
        ...

        :param ...
        :return: ...
        :raise ...
        """
        #df_predict = pd.DataFrame()
        if all:
            for model in self.models:
                self.models[model].fit(data)
                #df_predict[model] = self.models[model].predict(data['X_test'])
                yield {
                        'name':model,\
                        'predict': self.models[model].predict(data)
                }
        else:
            try:
                # Get the dictionary corresponding to the requested model
                self.models[model].fit(data)
                #df_predict[model] = self.models[model].predict(data['X_test'])
                yield {
                    'name': model, \
                    'predict': self.models[model].predict(data)
                }
            except KeyError:
                # Not found
                raise KeyError('Unknown model: {}'.format(model))

        #return df_predict