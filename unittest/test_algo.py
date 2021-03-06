import unittest
from parameterized import parameterized
import algo


class TestTaskWithOneIntValidationParameter(unittest.TestCase):

    # Testing base class with validation method for corrext number answer
    @parameterized.expand([(1, 1), (5888, 5888), (3, 3), ('0002', 2),
                           ('+99999', 99999), ('  067 ', 67), (' 12', 12)])
    def test_main_logic(self, number, expected_value):
        self.assertEqual(algo.TaskWithOneIntValidationParameter.validate_data(
            number), expected_value)

    # Testing base class with validation method for exceptions
    @parameterized.expand([('1.2', TypeError), ('-3sdhv', TypeError), (0, ValueError),
                           (1.2, TypeError), ('0o2',
                                              TypeError), ('-2', ValueError),
                           ('-0.2', TypeError), ('-0',
                                                 ValueError), ('-566', ValueError),
                           (' ', TypeError), ('0  067 ', TypeError), ('+7m', TypeError)])
    def test_main_logic(self, number, expected_value):
        self.assertRaises(
            expected_value, algo.TaskWithOneIntValidationParameter.validate_data, number)


class TestTask86a(unittest.TestCase):

    # Testing task 86a class main logic (must return  amount of digits in number)
    @parameterized.expand([(1, 1), (5888, 4), ('567', 3), (1111111111, 10)])
    def test_main_logic(self, number, expected_value):
        self.assertEqual(algo.Task86a.main_logic(number), expected_value)


class TestTask86b(unittest.TestCase):

    # Testing task 86b class main logic (must return sum of digits in number)
    @parameterized.expand([(1, 1), (5888, 29), ('567', 18), (1111011111, 9)])
    def test_main_logic(self, number, expected_value):
        self.assertEqual(algo.Task86b.main_logic(number), expected_value)


class TestTask330(unittest.TestCase):

    # Testing task 330 class  deviders func (must return set of all deviders of the number excpet number itself)
    @parameterized.expand([(1, {1}),
                           (100, {1, 2, 4, 5, 10, 20, 25, 50}),
                           (30, {1, 2, 3, 5, 6, 10, 15}),
                           (47, {1}),
                           (90, {1, 2, 3, 5, 6, 9, 10, 15, 18, 30, 45}),
                           (198, {1, 2, 3, 6, 9, 11, 18, 22, 33, 66, 99})],
                          )
    def test_get_deviders(self, number, expected_value):
        self.assertEqual(algo.Task330._get_dividers(number), expected_value)

    # Testing task 330 class main logic (must return number thats sum of deviders(from get_deviders) is equal to the number)
    @parameterized.expand([(10, [6]),
                           (100, [6, 28]),
                           (400, [6, 28]),
                           (1000, [6, 28, 496]),
                           (5000, [6, 28, 496]),
                           (10000, [6, 28, 496, 8128]),
                           (50000, [6, 28, 496, 8128]),
                           (100000, [6, 28, 496, 8128])],
                          )
    def test_main_logic(self, number, expected_value):
        self.assertEqual(
            [res for res in algo.Task330.main_logic(number)], expected_value)
