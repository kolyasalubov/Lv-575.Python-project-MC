import unittest
from parameterized import parameterized
import algo


class TestTask86a(unittest.TestCase):

    @parameterized.expand([(1, 1), (5888, 4), (567, 3)])
    def test_main_logic(self, number, expected_value):
        self.assertEqual(Task86a.main_logic(number), expected_value)