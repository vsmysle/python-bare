""" Bare module."""
import logging


class BareClass:
    """ Sample class."""

    def __init__(self, debug=False):
        """ Bare class initialization method.

        :param debug: Debug flag (used for logging).
        :type debug: bool
        """
        self.debug = debug
