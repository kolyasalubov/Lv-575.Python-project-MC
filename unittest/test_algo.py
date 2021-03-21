import unittest
from parameterized import parameterized
import algo


class TestTaskWithOneIntValidationParameter(unittest.TestCase):

    # Testing base class with validation method for corrext number answer
    @parameterized.expand(
        [
            (1, 1),
            (5888, 5888),
            (3, 3),
            ("0002", 2),
            ("+99999", 99999),
            ("  067 ", 67),
            (" 12", 12),
        ]
    )
    def test_main_logic(self, number, expected_value):
        self.assertEqual(algo.TaskWithOneIntValidationParameter.validate_data(number), expected_value)

    # Testing base class with validation method for exceptions
    @parameterized.expand(
        [
            ("1.2", TypeError),
            ("-3sdhv", TypeError),
            (0, ValueError),
            (1.2, TypeError),
            ("0o2", TypeError),
            ("-2", ValueError),
            ("-0.2", TypeError),
            ("-0", ValueError),
            ("-566", ValueError),
            (" ", TypeError),
            ("0  067 ", TypeError),
            ("+7m", TypeError),
        ]
    )
    def test_main_logic(self, number, expected_value):
        self.assertRaises(expected_value, algo.TaskWithOneIntValidationParameter.validate_data, number)


class TestTask86a(unittest.TestCase):

    # Testing task 86a class main logic (must return  amount of digits in number)
    @parameterized.expand([(1, 1), (5888, 4), ("567", 3), (1111111111, 10)])
    def test_main_logic(self, number, expected_value):
        self.assertEqual(algo.Task86a.main_logic(number), expected_value)


class TestTask86b(unittest.TestCase):

    # Testing task 86b class main logic (must return sum of digits in number)
    @parameterized.expand([(1, 1), (5888, 29), ("567", 18), (1111011111, 9)])
    def test_main_logic(self, number, expected_value):
        self.assertEqual(algo.Task86b.main_logic(number), expected_value)


class TestTask330(unittest.TestCase):

    # Testing task 330 class  deviders func (must return set of all deviders of the number excpet number itself)
    @parameterized.expand(
        [
            (1, {1}),
            (100, {1, 2, 4, 5, 10, 20, 25, 50}),
            (30, {1, 2, 3, 5, 6, 10, 15}),
            (47, {1}),
            (90, {1, 2, 3, 5, 6, 9, 10, 15, 18, 30, 45}),
            (198, {1, 2, 3, 6, 9, 11, 18, 22, 33, 66, 99}),
        ],
    )
    def test_get_dividers(self, number, expected_value):
        self.assertEqual(algo.Task330._get_dividers(number), expected_value)

    # Testing task 330 class main logic (must return number thats sum of deviders(from get_deviders) is equal to the number)
    @parameterized.expand(
        [
            (10, [6]),
            (100, [6, 28]),
            (400, [6, 28]),
            (1000, [6, 28, 496]),
            (5000, [6, 28, 496]),
            (10000, [6, 28, 496, 8128]),
            (50000, [6, 28, 496, 8128]),
            (100000, [6, 28, 496, 8128]),
        ],
    )
    def test_main_logic(self, number, expected_value):
        self.assertEqual([res for res in algo.Task330.main_logic(number)], expected_value)


class TestTask178b(unittest.TestCase):

    # Testing task 178b class main logic (must return amount of numbers divided by 3 and not divided by 5 in a sequence)
    @parameterized.expand(
        [
            ([5], 0),
            ([9], 1),
            ([4, 5], 0),
            ([9, 13], 1),
            ([9, 12, 18, 21], 4),
            ([1, 5, 10, 15], 0),
        ]
    )
    def test_main_logic(self, sequence, expected_value):
        self.assertEqual(algo.Task178b.main_logic(sequence), expected_value)


class TestTask178c(unittest.TestCase):

    # Testing task 178c class main logic (must return amount of numbers which are the square of the even number)
    @parameterized.expand(
        [
            ([5], 0),
            ([100], 1),
            ([4, 5], 1),
            ([9, 13], 0),
            ([4, 16, 36, 64], 4),
            ([1, 2, 10, 15], 0),
        ]
    )
    def test_main_logic(self, sequence, expected_value):
        self.assertEqual(algo.Task178c.main_logic(sequence), expected_value)


class TestTask554(unittest.TestCase):

    # Testing task 554 class main logic (must return list of pythagorean triplets)
    @parameterized.expand(
        [
            (
                20,
                [
                    [3, 4, 5],
                    [6, 8, 10],
                    [9, 12, 15],
                    [12, 16, 20],
                    [5, 12, 13],
                    [8, 15, 17],
                ],
            ),
            (5, [[3, 4, 5]]),
            (10, [[3, 4, 5], [6, 8, 10]]),
            (1, []),
        ]
    )
    def test_main_logic(self, number, expected_value):
        self.assertEqual(algo.Task554.main_logic(number + 1), expected_value)


class TestTask107(unittest.TestCase):

    # Testing task 107 class main logic (must return  the largest integer k, at which 4 ^k < m)
    @parameterized.expand(
        [
            (1, 0),
            (2, 0),
            (15, 1),
            (16, 1),
            (17, 2),
            (32, 2),
            (64, 2),
            (65, 3),
            (72, 3),
            (128, 3),
            (256, 3),
            (257, 4),
            (4000, 5),
            (10_000, 6),
        ]
    )
    def test_main_logic(self, number, expected_value):
        self.assertEqual(algo.Task107.main_logic(number), expected_value)


class TestTask243a(unittest.TestCase):

    # Testing task 243a class main logic (must return True if there are two numbers (x, y) that x ^2 + y ^2 = n)
    @parameterized.expand(
        [
            (1, ()),
            (7, ()),
            (13, (3, 2)),
            (272, (16, 4)),
            (317, (14, 11)),
            (300, ()),
            (6340, (78, 16)),
            (41410, (197, 51)),
            (67, ()),
            (32187, ()),
        ]
    )
    def test_main_logic(self, number, expected_value):
        self.assertEqual(algo.Task243a.main_logic(number), expected_value)


class TestTask243b(unittest.TestCase):

    # Testing task 243b class main logic (must return all of the two numbers (x, y) that x ^2 + y ^2 = n)
    @parameterized.expand(
        [
            (1, []),
            (7, []),
            (13, [(3, 2)]),
            (272, [(16, 4)]),
            (317, [(14, 11)]),
            (300, []),
            (6340, [(78, 16), (72, 34)]),
            (41410, [(197, 51), (183, 89), (181, 93), (159, 127)]),
            (100000, [(316, 12), (300, 100), (260, 180)]),
            (
                1000000000,
                [
                    (31600, 1200),
                    (30672, 7696),
                    (30000, 10000),
                    (26000, 18000),
                    (24560, 19920),
                ],
            ),
        ]
    )
    def test_task243b_main_logic(self, number, expected_value):
        self.assertEqual(algo.Task243b.main_logic(number), expected_value)


class TestTask108(unittest.TestCase):
    @parameterized.expand([(2, 4), (123, 128), (1034, 2048), (100020, 131072)])
    def test_task108_main_logic(self, number, expected_value):
        self.assertEqual(algo.Task108.main_logic(number), expected_value)


class TestTask331a(unittest.TestCase):
    @parameterized.expand([(19, ["1^2 + 3^2 + 3^2"]), (20, False), (75, ["1^2 + 5^2 + 7^2"]), (4, False)])
    def test_task331a_main_logic(self, number, expected_value):
        self.assertEqual(algo.Task331a.main_logic(number), expected_value)


class TestTask331b(unittest.TestCase):
    @parameterized.expand(
        [
            (19, ["1^2 + 3^2 + 3^2", "3^2 + 1^2 + 3^2", "3^2 + 3^2 + 1^2"]),
            (20, False),
            (
                75,
                [
                    "1^2 + 5^2 + 7^2",
                    "1^2 + 7^2 + 5^2",
                    "5^2 + 1^2 + 7^2",
                    "5^2 + 5^2 + 5^2",
                    "5^2 + 7^2 + 1^2",
                    "7^2 + 1^2 + 5^2",
                    "7^2 + 5^2 + 1^2",
                ],
            ),
            (4, False),
        ]
    )
    def test_task331b_main_logic(self, number, expected_value):
        self.assertEqual(algo.Task331b.main_logic(number), expected_value)


class TestTask87(unittest.TestCase):
    """Testing all methods of task 87 class"""

    @parameterized.expand(
        [
            ("1.2", ValueError),
            ("-3ssss", ValueError),
            ("0", ValueError),
            ("445", ValueError),
            ("7m 456", TypeError),
            ("7115m 4", TypeError),
            ("124 4d56", TypeError),
            ("7,5555 456", TypeError),
            ("7 456", algo.InvalidInput),
            ("44894 10", algo.InvalidInput),
            ("5555 5", algo.InvalidInput),
        ]
    )
    def test_exceptions(self, data, expected_value):
        """Testing base class with validation method for exceptions"""
        self.assertRaises(expected_value, algo.Task87.validate_data, data)

    @parameterized.expand(
        [
            ("78451", 2, 6),
            ("421", 3, 7),
            ("1234567890", 10, 45),
            ("52138", 4, 14),
            ("17", 2, 8),
            ("32", 1, 2),
        ]
    )
    def test_main_logic(self, number, quantity, expected_value):
        """Testing task 87 class main logic"""
        self.assertEqual(algo.Task87.main_logic(number, quantity), expected_value)


class TestTask226(unittest.TestCase):
    """Testing all methods of task 226 class"""

    @parameterized.expand(
        [
            ("1.2", ValueError),
            ("-3ssss", ValueError),
            ("0", ValueError),
            ("445", ValueError),
            ("7m 456", TypeError),
            ("7115m 4", TypeError),
            ("124 4d56", TypeError),
            ("7,5555 456", TypeError),
        ]
    )
    def test_exceptions(self, data, expected_value):
        """Testing base class with validation method for exceptions"""
        self.assertRaises(expected_value, algo.TaskWithTwoIntValidationParameters.validate_data, data)

    @parameterized.expand(
        [
            (12, 36, [36, 72, 108, 144, 180, 216, 252, 288, 324, 360, 396]),
            (78, 5, []),
            (78, 12, [156, 312, 468, 624, 780]),
            (444, 822, [60828, 121656, 182484, 243312, 304140]),
            (77, 127, []),
        ]
    )
    def test_main_logic(self, number1, number2, expected_value):
        """Testing task 226 class main logic"""
        self.assertEqual(algo.Task226.main_logic(number1, number2), expected_value)


class TestTask559(unittest.TestCase):
    """Testing all methods of task 559 class"""

    @parameterized.expand(
        [
            ("1.2", TypeError),
            ("lol", TypeError),
            (1.2, TypeError),
            ("40o", TypeError),
            ("-2", ValueError),
            ("-0.2", TypeError),
            ("-0", ValueError),
            ("-566", ValueError),
            (" ", TypeError),
            ("0  02223 ", TypeError),
            ("+777m", TypeError),
        ]
    )
    def test_exceptions(self, number, expected_value):
        """Test task 559 for exceptions"""
        self.assertRaises(expected_value, algo.TaskWithOneIntValidationParameter.validate_data, number)

    # Testing eratosthenes function in task 559
    @parameterized.expand(
        [
            (24, [2, 3, 5, 7, 11, 13, 17, 19, 23]),
            (50, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]),
            (62, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]),
            (88, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83]),
        ],
    )
    def test_eratosthenes_function(self, number, expected_value):
        """Testing eratosthenes function in task 559"""
        self.assertEqual(algo.Task559.eratosthenes(number), expected_value)

    @parameterized.expand(
        [
            (24, [3, 7, 15]),
            (50, [3, 7, 15, 31]),
            (61, [3, 7, 15, 31]),
            (88, [3, 7, 15, 31, 63]),
            (7700, [3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095]),
        ],
    )
    def test_mersen_function(self, number, expected_value):
        """Testing mersen_numbers function in task 559"""
        self.assertEqual(algo.Task559.mersen_numbers(number), expected_value)

    @parameterized.expand(
        [
            (456, [3, 7, 31, 127]),
            (1234, [3, 7, 31, 127]),
            (2, []),
            (100000, [3, 7, 31, 127, 8191]),
            (748452, [3, 7, 31, 127, 8191, 131071, 524287]),
            (12, [3, 7]),
            (6, [3]),
        ]
    )
    def test_main_logic(self, number, expected_value):
        """Testing task 559 class main logic"""
        self.assertEqual(algo.Task559.main_logic(number), expected_value)


class TestTask88a(unittest.TestCase):
    @parameterized.expand([(3, "NO"), (6, "YES"), (18, "YES"), (13, "NO")])
    def test_task88a_main_logic(self, number, expected_value):
        self.assertEqual(algo.Task88a.main_logic(number), expected_value)


class TestTask88b(unittest.TestCase):
    @parameterized.expand([(3, 3), (121, 121), (1222, 2221), (1250, 521), (54789, 98745)])
    def test_task88b_main_logic(self, number, expected_value):
        self.assertEqual(algo.Task88b.main_logic(number), expected_value)
