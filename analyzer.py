#!/usr/bin/python
# -- Content-Encoding: UTF-8 --
"""
...
"""

# iPOPO decorators
from pelix.ipopo.decorators import ComponentFactory, Provides, \
    Validate, Invalidate, Requires, Instantiate

# Specification of a command service for the Pelix shell
from pelix.shell import SHELL_COMMAND_SPEC

# Name the component factory
@ComponentFactory("analyzer_factory")
# Consume a single model_consumer_service
@Requires("_model_consumer", "model_consumer_service")
@Requires("_data_consumer", "data_consumer_service")
@Requires("_metric_consumer", "metric_consumer_service")
# Provide a shell command service
@Provides(SHELL_COMMAND_SPEC)
# Automatic instantiation
@Instantiate("analyzer_instance")
class Analyzer(object):
    """
    A component that provides a shell command (spell.spell), using a
    model_consumer_service
    """

    def __init__(self):
        """
        Defines class members
        """
        # the spell checker service
        self._model_consumer = None
        self._data_consumer = None
        self._metric_consumer = None

    @Validate
    def validate(self, context):
        """
        Component validated, just print a trace to visualize the event.
        Between this call and the call to invalidate, the _model_consumer member
        will point to a valid model_consumer_service.
        """
        print('A analyzer has been started')

    @Invalidate
    def invalidate(self, context):
        """
        Component invalidated, just print a trace to visualize the event
        """
        print('A analyzer has been stopped')

    def get_namespace(self):
        """
        analyze
        """
        return "analyze"

    def get_methods(self):
        """
        Retrieves the list of (command, method) tuples for all shell commands
        provided by this component.
        Look at the shell tutorial for more information.
        """
        return [("analyze", self.analyze)]

    def analyze(self, io_handler):
        """

        :param io_handler: A utility object given by the shell to interact with
                           the user.
        """

        passage = None
        all = io_handler.prompt("Please enter all models or not: ")

        while passage != 'quit':
            # Request the text to check
            passage = io_handler.prompt(
                "Please enter 'quit' to exit:\n")

            if passage and passage != 'quit':

                # A text has been given: call the spell checker, which have been
                # injected by iPOPO.

                try:
                    for data in self._data_consumer.get_data(test_size=0.1):
                        try:
                            for model in self._model_consumer.check_model(data, bool(all)):
                                try:
                                    for metric in self._metric_consumer.evaluate(data, model):
                                        print('{} is {} for {} in {}'.format(\
                                            metric['name'], metric['value'], model['name'], data['name']))
                                except Exception as ex:
                                    print(str(ex))
                        except Exception as ex:
                            print(str(ex))
                except Exception as ex:
                    print(str(ex))
                #print(self._data_sber.get_data())