"""
Unitary tests for utproject/second_module.py

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

from utproject import second_module

class TestSecondModule(unittest.TestCase):
    """
    Unitary tests for utproject/second_module.py
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
        # Use the setup to create a fresh instance for each test
        self._my_test_module = second_module.SecondModule('tom', 25)

    def tearDown(self):
        """
        Test tearDown.
        """

    @classmethod
    def tearDownClass(cls):
        """
        Global tearDown.
        """

    def test_init_error(self):
        with self.assertRaises(TypeError) as err:
            second_module.SecondModule('tom', '25')
        self.assertTrue('age must be an integer' in str(err.exception))

    @mock.patch('logging.Logger.info')
    def test_print_name(self, mock_info):
        self._my_test_module.print_name()
        mock_info.assert_called_once_with('tom')

    @mock.patch('logging.Logger.info')
    @mock.patch('datetime.datetime')
    def test_print_year_of_birth(self, mock_datetime, mock_info):
        # now method returns an object, so we have to mock that
        date_instance = mock.Mock(year=2000)
        mock_datetime.now.return_value = date_instance
        self._my_test_module.print_year_of_birth()
        mock_info.assert_called_once_with('year of birth: %s', 1975)
        mock_datetime.now.assert_called_once_with()

    def test_print_all(self):
        # Just mock current instance methods
        self._my_test_module.print_name = mock.Mock()
        self._my_test_module.print_year_of_birth = mock.Mock()
        self._my_test_module.print_all()
        self._my_test_module.print_name.assert_called_once_with()
        self._my_test_module.print_year_of_birth.assert_called_once_with()

    # Look the difference between how the patching path is selected.

    @mock.patch('logging.Logger.debug')
    @mock.patch('utproject.second_module.first_module')
    def test_use_other_modules_sum(self, mock_first_module, mock_debug):
        mock_first_module.basic_sum.return_value = 5
        result = self._my_test_module.use_other_modules_sum(10, 20)
        self.assertEqual(result, 5)
        mock_debug.assert_called_once_with('the sum result is %d', 5)

    @mock.patch('logging.Logger.debug')
    @mock.patch('utproject.first_module')
    def test_use_other_modules_division(self, mock_first_module, mock_debug):
        mock_first_module.basic_division.return_value = 5
        result = self._my_test_module.use_other_modules_division(10, 20)
        self.assertEqual(result, 5)
        mock_debug.assert_called_once_with('the division result is %d', 5)
