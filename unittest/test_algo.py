import unittest
from parameterized import parameterized
import algo


class TestTask86a(unittest.TestCase):

    @parameterized.expand([(1, 1), (5888, 4), ('567', 3), (1111111111, 10)])
    def test_main_logic(self, number, expected_value):
        self.assertEqual(algo.Task86a.main_logic(number), expected_value)

    @parameterized.expand([(1, 1), (5888, 5888), (3, 3), ('0002', 2),
                           ('+99999', 99999), ('  067 ', 67), (' 12', 12)])
    def test_main_logic(self, number, expected_value):
        self.assertEqual(algo.Task86a.validate_data(number), expected_value)

    @parameterized.expand([('1.2', TypeError), ('-3sdhv', TypeError), (0, ValueError),
                           (1.2, TypeError), ('0o2',
                                              TypeError), ('-2', ValueError),
                           ('-0.2', TypeError), ('-0',
                                                 ValueError), ('-566', ValueError),
                           (' ', TypeError), ('0  067 ', TypeError), ('+7m', TypeError)])
    def test_main_logic(self, number, expected_value):
        self.assertRaises(expected_value, algo.Task86a.validate_data, number)
