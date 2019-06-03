"""
Unitary tests for utproject/third_module.py

:author: xarbulu
:organization: SUSE Linux GmbH
:contact: xarbulu@suse.de

:since: 2019-06-02
"""

# pylint:disable=C0103,C0111,W0212,W0611

import sys
import logging
import unittest
import string

try:
    from unittest import mock
except ImportError:
    import mock

from utproject import third_module

class TestThirdModule(unittest.TestCase):
    """
    Unitary tests for utproject/third_module.py
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
        self._my_test_module = third_module.ThirdModule()

    def tearDown(self):
        """
        Test tearDown.
        """

    @classmethod
    def tearDownClass(cls):
        """
        Global tearDown.
        """

    # Some exceptional cases we can use the original module instead of mocking it (constans for instance)

    @mock.patch('random.choice')
    def test_random_string(self, mock_choice):
        mock_choice.side_effect = ['a', 'b', 'c', 'd', 'e']
        my_str = third_module.ThirdModule.random_string(5)
        self.assertEqual(my_str, 'abcde')
        mock_choice.assert_has_calls([
            mock.call(string.ascii_lowercase),
            mock.call(string.ascii_lowercase),
            mock.call(string.ascii_lowercase),
            mock.call(string.ascii_lowercase),
            mock.call(string.ascii_lowercase)
        ])

    # Use return_value when the method is executed only once

    @mock.patch('logging.Logger.info')
    @mock.patch('utproject.second_module.SecondModule')
    def test_use_other_classes(self, mock_second_module, mock_logger):
        mock_instance = mock.Mock()
        mock_second_module.return_value = mock_instance

        self._my_test_module.use_other_classes('tom', 25)

        mock_second_module.assert_called_once_with('tom', 25)
        mock_instance.print_name.assert_called_once_with()
        mock_instance.print_year_of_birth.assert_called_once_with()

        mock_logger.assert_has_calls([
            mock.call('using other module classes'),
            mock.call('method execution finished')
        ])

    # Use side_effect when the method is executed several times or to raise an exception
    # Check here how a returned value might be a mock too

    @mock.patch('random.randint')
    @mock.patch('utproject.second_module.SecondModule')
    @mock.patch('utproject.third_module.ThirdModule.random_string')
    def test_use_other_classes_multiple(self, mock_random_string, mock_second_module, mock_randint):
        mock_instance_first = mock.Mock()
        mock_instance_second = mock.Mock()
        mock_instance_third = mock.Mock()

        mock_second_module.side_effect = [
            mock_instance_first, mock_instance_second, mock_instance_third]
        mock_random_string.side_effect = ['abc', 'def', 'ghi']
        mock_randint.side_effect = [5, 10 ,15]

        # Method under test
        result = self._my_test_module.use_other_classes_multiple(3)

        self.assertListEqual(result, [
            mock_instance_first, mock_instance_second, mock_instance_third])

        mock_second_module.assert_has_calls([
            mock.call('abc', 5),
            mock.call('def', 10),
            mock.call('ghi', 15),
        ])

        mock_randint.assert_has_calls([
            mock.call(1, 100),
            mock.call(1, 100),
            mock.call(1, 100)
        ])

        mock_random_string.assert_has_calls([
            mock.call(5),
            mock.call(5),
            mock.call(5)
        ])

        mock_instance_first.print_name.assert_called_once_with()
        mock_instance_first.print_year_of_birth.assert_called_once_with()

        mock_instance_second.print_name.assert_called_once_with()
        mock_instance_second.print_year_of_birth.assert_called_once_with()

        mock_instance_third.print_name.assert_called_once_with()
        mock_instance_third.print_year_of_birth.assert_called_once_with()
