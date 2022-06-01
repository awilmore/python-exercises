"""
Parent class to exercise implementations.
"""

import logging


class Exercise:
    """
    Parent class to exercise implementations.
    """

    def __init__(self, module_name, module_number):
        self.module_name = module_name
        self.module_number = module_number

    def run(self):
        """To be implemented by Exercise subclass"""
        self.log_exercise()

    def log_exercise(self):
        """Show info about exercise"""
        logging.info("Exercise: %s ({%s})", self.module_name, self.module_number)
