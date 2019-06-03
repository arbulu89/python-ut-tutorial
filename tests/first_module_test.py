"""
Unitary tests for utproject/first_module.py

:author: xarbulu
:organization: SUSE Linux GmbH
:contact: xarbulu@suse.de

:since: 2019-06-02
"""

# pylint:disable=C0103,C0111,W0212,W0611

import sys
import logging
import unittest

try:
    from unittest import mock
except ImportError:
    import mock

from utproject import first_module

class TestFirstModule(unittest.TestCase):
    """
    Unitary tests for utproject/first_module.py
    """

    @classmethod
    def setUpClass(cls):
        """
        Global setUp.
        """

        logging.basicConfig(level=logging.INFO)

    def setUp(self):
        """
        Test setUp.
        """

    def tearDown(self):
        """
        Test tearDown.
        """

    @classmethod
    def tearDownClass(cls):
        """
        Global tearDown.
        """

    def test_sum(self):
        result = first_module.basic_sum(5, 6)
        expected = 11
        # Try to use the correct order -> test values, expected value
        self.assertEqual(result, expected)

    def test_basic_division(self):
        result = first_module.basic_division(10, 5)
        expected = 2
        # Try to use the correct order -> test values, expected value
        self.assertEqual(result, expected)

    def test_basic_division_error(self):
        with self.assertRaises(ZeroDivisionError) as err:
            first_module.basic_division(10, 0)

        if sys.version_info.major == 2:
            self.assertTrue('integer division or modulo by zero' in err.exception)
        else:
            self.assertTrue('division by zero' in str(err.exception))

    def test_custom_exception(self):
        result = first_module.custom_exception(20, 5)
        expected = 4
        # Try to use the correct order -> test values, expected value
        self.assertEqual(result, expected)

    def test_custom_exception_error(self):
        with self.assertRaises(first_module.MyCustomError) as err:
            first_module.custom_exception(10, 0)
        self.assertTrue('custom err' in str(err.exception))

    # Next two test show how we need to mock other methods in order to isolate the current
    # method under test
    # The first approach would be incorrect as we depend in user_other_method

    def test_use_other_method_wrong(self):
        result = first_module.use_other_method(4, 6)
        self.assertEqual(result, 10)

    # Use the absolute path to create the patch. You need to patch exactly basic_sum from this
    # module

    @mock.patch('utproject.first_module.basic_sum')
    def test_use_other_method_good(self, mock_basic_sum):
        mock_basic_sum.return_value = 50 # Use return_value to only return 1 value
        result = first_module.use_other_method(4, 6)
        self.assertEqual(result, 50)
        mock_basic_sum.assert_called_once_with(4, 6) # Check if basi_sum was called only once

    @mock.patch('utproject.first_module.basic_sum')
    def test_loop_method(self, mock_basic_sum):
        mock_basic_sum.side_effect = [5, 7, 9] # basic_sum called 3 times
        result = first_module.loop_method()
        self.assertEqual(result, 5+7+9)
        mock_basic_sum.assert_has_calls([ # Check if basi_sum was called 3 times
            mock.call(0, 1),
            mock.call(1, 2),
            mock.call(2, 3)
        ])

    @mock.patch('utproject.first_module.basic_sum')
    def test_loop_method_error(self, mock_basic_sum):
        mock_basic_sum.side_effect = [5, 7, first_module.MyCustomError] # basic_sum called 3 times
        with self.assertRaises(first_module.MyCustomError):
            first_module.loop_method()
        mock_basic_sum.assert_has_calls([ # Check if basi_sum was called 3 times
            mock.call(0, 1),
            mock.call(1, 2)
        ])

    # Always mock methods such a time and sleep. The UT must be fast
    # REMEMBER! You need to mock the exact method
    # Look how it is different if we use from keyword to import or not
    # @mock.patch('time.sleep') would fail as it is not the same sleep method

    @mock.patch('time.time')
    @mock.patch('utproject.first_module.sleep')
    def test_use_other_modules(self, mock_sleep, mock_time):
        mock_time.return_value = 5
        result = first_module.use_other_modules()
        self.assertEqual(result, 5)
        mock_time.assert_called_once_with()
        mock_sleep.assert_called_once_with(3)
