"""
Python module storing a class object

:author: xarbulu
:organization: SUSE LLC
:contact: xarbulu@suse.com

:since: 2019-06-02
"""

import logging
import datetime

from utproject import first_module
import utproject.first_module


class SecondModule(object):
    """
    Python basic class
    """

    def __init__(self, name, age):
        self._logger = logging.getLogger(__name__)
        self._name = name
        if not isinstance(age, int):
            raise TypeError('age must be an integer')
        self._age = age

    def print_name(self):
        """
        Log name
        """
        self._logger.info(self._name)

    def print_year_of_birth(self):
        """
        Log year of birth
        """
        year = datetime.datetime.now()
        self._logger.info('year of birth: %s', year.year - self._age)

    def print_all(self):
        """
        Log all the information
        """
        self.print_name()
        self.print_year_of_birth()

    def use_other_modules_sum(self, first_value, second_value):
        """
        Use methods from other modules
        """
        result = first_module.basic_sum(first_value, second_value)
        self._logger.debug('the sum result is %d', result)
        return result

    def use_other_modules_division(self, first_value, second_value):
        """
        Use methods from other modules
        """
        result = utproject.first_module.basic_division(first_value, second_value)
        self._logger.debug('the division result is %d', result)
        return result
