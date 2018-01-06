#!/usr/bin/python3
# -- Content-Encoding: UTF-8 --
"""
Starts a Pelix framework and installs the analyzer models bundles
"""

# Pelix framework module and utility methods
import pelix.framework
from pelix.utilities import use_service


def main():
    """
    Starts a Pelix framework and waits for it to stop
    """
    # Prepare the framework, with iPOPO and the shell console
    # Warning: we only use the first argument of this method, a list of bundles
    framework = pelix.framework.create_framework((
        # iPOPO
        "pelix.ipopo.core",
        # Shell core (engine)
        "pelix.shell.core",
        # Text console
        "pelix.shell.console"))

    # Start the framework, and the pre-installed bundles
    framework.start()

    # Get the bundle context of the framework, i.e. the link between the
    # framework starter and its content.
    context = framework.get_bundle_context()

    # Start the model bundles, which provide the ml models
    context.install_bundle("model_gb_clf").start()
    context.install_bundle("model_lr").start()

    # Start the model_consumer bundle, which provides the model consumer service.
    context.install_bundle("model_consumer").start()

    # Start the model bundles, which provide the ml models
    context.install_bundle("data_iris").start()
    context.install_bundle("data_breast_cancer").start()

    # Start the model_consumer bundle, which provides the model consumer service.
    context.install_bundle("data_consumer").start()

    # Start the analyzer bundle, which provides a shell command
    context.install_bundle("analyzer").start()

    # Wait for the framework to stop
    framework.wait_for_stop()


# Classic entry point...
if __name__ == "__main__":
    main()
