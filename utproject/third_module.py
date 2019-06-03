"""
Python module storing a class object

:author: xarbulu
:organization: SUSE LLC
:contact: xarbulu@suse.com

:since: 2019-06-02
"""

import logging
import random
import string

from utproject import second_module


class ThirdModule(object):
    """
    Python basic class
    """

    def __init__(self):
        self._logger = logging.getLogger(__name__)

    @staticmethod
    def random_string(length=10):
        """
        Random string generator
        """
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    def use_other_classes(self, name, age):
        """
        Use other module classes
        """
        self._logger.info('using other module classes')
        sec_mod = second_module.SecondModule(name, age)
        sec_mod.print_name()
        sec_mod.print_year_of_birth()
        self._logger.info('method execution finished')

    def use_other_classes_multiple(self, count):
        """
        Run other class methods in a loop
        """
        instances = []
        for _ in range(count):
            age = random.randint(1, 100)
            name = self.random_string(5)
            sec_mod = second_module.SecondModule(name, age)
            sec_mod.print_name()
            sec_mod.print_year_of_birth()
            instances.append(sec_mod)
        return instances
