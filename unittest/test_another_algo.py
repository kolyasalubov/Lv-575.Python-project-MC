import unittest
from parameterized import parameterized
import algo


class TestTaskWithOneIntValidationParameter(unittest.TestCase):

    @parameterized.expand([
        (1, 1), (+100, 100), (2048, 2048),
        ("8", 8), ("101", 101), ("1024", 1024),
        (" 56", 56), ("   +78     ", 78), ("+13   ", 13),
    ])
    def test_TaskWithOneIntValidationParameter_validate_data_right(self, input_number, expected_number):
        self.assertEqual(algo.TaskWithOneIntValidationParameter.validate_data(input_number), expected_number)

    @parameterized.expand([
        ("five", TypeError), (13.8, TypeError), (2 + 3j, TypeError),
        ("2+3j", TypeError), ("", TypeError), (None, TypeError),
        (-60, ValueError), ("  -12  ", ValueError), ("-1001", ValueError),
    ])
    def test_TaskWithOneIntValidationParameter_validate_data_exception(self, input_number, expected_exception):
        self.assertRaises(expected_exception, algo.TaskWithOneIntValidationParameter.validate_data, input_number)
