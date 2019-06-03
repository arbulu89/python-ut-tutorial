"""
Python module storing independent methods

:author: xarbulu
:organization: SUSE LLC
:contact: xarbulu@suse.com

:since: 2019-06-02
"""

from time import sleep
import time


class MyCustomError(Exception):
    """
    Custom exception
    """


def basic_sum(first_value, second_value):
    """
    Sum 2 values
    """
    return first_value + second_value


def basic_division(first_value, second_value):
    """
    Division
    """
    return first_value / second_value


def custom_exception(first_value, second_value):
    """
    Custom execption
    """
    try:
        return first_value / second_value
    except ZeroDivisionError:
        raise MyCustomError('custom err')


def use_other_method(first_value, second_value):
    """
    Method using other methods
    """
    return basic_sum(first_value, second_value)


def loop_method():
    """
    Method with a loop
    """
    total = 0
    for i in range(3):
        my_sum = basic_sum(i, i+1)
        total = total + my_sum
    return total


def use_other_modules():
    """
    Use other modules methods
    """
    sleep(3)
    return time.time()
