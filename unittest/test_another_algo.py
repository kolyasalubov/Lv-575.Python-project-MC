"""
Tests for somebody algo (unittest)
"""
import unittest
from parameterized import parameterized
import algo


class TestTaskWithOneIntValidationParameter(unittest.TestCase):
    """Class for testing tasks with one int validation parameter"""

    @parameterized.expand(
        [
            (1, 1),
            (+100, 100),
            (2048, 2048),
            ("8", 8),
            ("101", 101),
            ("1024", 1024),
            (" 56", 56),
            ("   +78     ", 78),
            ("+13   ", 13),
        ]
    )
    def test_task_with_one_int_validation_parameter_validate_data_right(self, input_number, expected_number):
        """Testing base class with validation method for correct number answer"""
        self.assertEqual(algo.TaskWithOneIntValidationParameter.validate_data(input_number), expected_number)

    @parameterized.expand(
        [
            ("five", TypeError),
            (13.8, TypeError),
            (2 + 3j, TypeError),
            ("2+3j", TypeError),
            ("", TypeError),
            (None, TypeError),
            (-60, ValueError),
            ("  -12  ", ValueError),
            ("-1001", ValueError),
        ]
    )
    def test_task_with_one_int_validation_parameter_validate_data_exception(self, input_number, expected_exception):
        """Testing base class with validation method for exceptions"""
        self.assertRaises(expected_exception, algo.TaskWithOneIntValidationParameter.validate_data, input_number)


class TestTask88c(unittest.TestCase):
    """Testing task 88c class main logic"""

    @parameterized.expand(
        [
            (1, 1),
            (4, 4),
            (234, 432),
            (1646, 6641),
            (333, 333),
            (3093, 3093),
            (264537, 764532),
            (12, 21),
            (1435, 5431),
        ]
    )
    def test_task88c(self, input_value, expected_value):
        """Swap the first and last digits of n"""
        self.assertEqual(algo.Task88c.main_logic(input_value), expected_value)


class TestTask88d(unittest.TestCase):
    """Testing task 88d class main logic"""

    @parameterized.expand(
        [
            (1, 111),
            (4, 141),
            (234, 12341),
            (1646, 116461),
            (333, 13331),
            (3093, 130931),
            (264537, 12645371),
            (12, 1121),
            (1435, 114351),
        ]
    )
    def test_task88d(self, input_value, expected_value):
        """Add the number 1 to the beginning and end of n"""
        self.assertEqual(algo.Task88d.main_logic(input_value), expected_value)


class TestTask332(unittest.TestCase):
    """esting task 332 class main logic"""

    @parameterized.expand(
        [
            (1, [1, 0, 0, 0]),
            (4, [2, 0, 0, 0]),
            (234, [15, 3, 0, 0]),
            (1646, [40, 6, 3, 1]),
            (2141, [46, 5, 0, 0]),
            (2137, [46, 4, 2, 1]),
            (2149, [46, 5, 2, 2]),
            (12412, [111, 9, 3, 1]),
            (90475, [300, 21, 5, 3]),
        ]
    )
    def test_task332(self, input_value, expected_value):
        """Find non-negative x1, x2, x3, x4 such that x1^2 + x2^2 + x3^2 + x4^2 = n"""
        self.assertEqual(algo.Task332.main_logic(input_value), expected_value)


class TestTask87(unittest.TestCase):
    @parameterized.expand(
        [("49850", 2, 5), ("14", 2, 5), ("548736", 4, 24), ("5870", 1, 0), ("247845225", 1, 5), ("558062862", 5, 24)]
    )
    def test_main_logic(self, number, quantity, expected_value):
        self.assertEqual(algo.Task87.main_logic(number, quantity), expected_value)


class TestTask226(unittest.TestCase):
    @parameterized.expand(
        [
            (10, 3, []),
            (6, 15, [30, 60]),
            (250, 110, [2750, 5500, 8250, 11000, 13750, 16500, 19250, 22000, 24750]),
            (71, 140, []),
        ]
    )
    def test_main_logic(self, number1, number2, expected_value):
        self.assertEqual(algo.Task226.main_logic(number1, number2), expected_value)


class TestTask559(unittest.TestCase):
    @parameterized.expand(
        [
            (126, [3, 7, 31]),
            (128, [3, 7, 31, 127]),
            (1, []),
            (8, [3, 7]),
            (8000, [3, 7, 31, 127]),
            (5, [3]),
            (13172, [3, 7, 31, 127, 8191]),
        ],
    )
    def test_main_logic(self, number, expected_value):
        self.assertEqual(algo.Task559.main_logic(number), expected_value)


class TestTask107(unittest.TestCase):
    @parameterized.expand(
        [(1, 0), (3, 0), (4, 0), (16, 1), (17, 2), (45, 2), (64, 2), (65, 3), (95, 3), (100, 3), (256, 3), (257, 4)]
    )
    def test_task107(self, input_value, expected_value):
        self.assertEqual(algo.Task107.main_logic(input_value), expected_value)


class TestTask243a(unittest.TestCase):
    @parameterized.expand(
        [
            (24, ()),
            (104, (10, 2)),
            (328, (18, 2)),
            (611, ()),
            (1920, ()),
            (2311, ()),
            (9945, (99, 12)),
            (41410, (197, 51)),
        ]
    )
    def test_task243a(self, input_value, expected_value):
        self.assertEqual(algo.Task243a.main_logic(input_value), expected_value)


class TestTask243b(unittest.TestCase):
    @parameterized.expand(
        [
            (24, []),
            (104, [(10, 2)]),
            (328, [(18, 2)]),
            (611, []),
            (2000, [(44, 8), (40, 20)]),
            (2311, []),
            (9945, [(99, 12), (96, 27), (93, 36), (72, 69)]),
            (41410, [(197, 51), (183, 89), (181, 93), (159, 127)]),
        ]
    )
    def test_task243b(self, input_value, expected_value):
        self.assertEqual(algo.Task243b.main_logic(input_value), expected_value)


class TestTask108(unittest.TestCase):
    """Test class for task 108"""

    @parameterized.expand(
        [(5, 8), (16, 32), (1, 2), (65, 128), (8, 16), (55, 64), (256, 512), (1000, 1024), (13, 16), (2, 4)]
    )
    def test_task108(self, input_value, expected_value):
        """
        Testing task 108 class main logic
        (must find the least number, that is bigger than n and is degree of number 2)
        """
        self.assertEqual(algo.Task108.main_logic(input_value), expected_value)


class TestTask331a(unittest.TestCase):
    """Test class for task 331a"""

    @parameterized.expand(
        [
            (20, []),
            (3, ["1^2 + 1^2 + 1^2"]),
            (26, ["1^2 + 3^2 + 4^2"]),
            (1, []),
            (42, ["1^2 + 4^2 + 5^2"]),
            (4, []),
            (7, []),
            (9, ["1^2 + 2^2 + 2^2"]),
            (6, ["1^2 + 1^2 + 2^2"]),
            (5, []),
        ]
    )
    def test_task331a(self, input_value, expected_value):
        """
        Testing task 331a class main logic
        (must return number as a sum of 3 squared numbers)
        """
        self.assertEqual(algo.Task331a.main_logic(input_value), expected_value)


class TestTask331b(unittest.TestCase):
    """Test class for task 331b"""

    @parameterized.expand(
        [
            (
                    50,
                    [
                        "3^2 + 4^2 + 5^2",
                        "3^2 + 5^2 + 4^2",
                        "4^2 + 3^2 + 5^2",
                        "4^2 + 5^2 + 3^2",
                        "5^2 + 3^2 + 4^2",
                        "5^2 + 4^2 + 3^2",
                    ],
            ),
            (
                    45,
                    [
                        "2^2 + 4^2 + 5^2",
                        "2^2 + 5^2 + 4^2",
                        "4^2 + 2^2 + 5^2",
                        "4^2 + 5^2 + 2^2",
                        "5^2 + 2^2 + 4^2",
                        "5^2 + 4^2 + 2^2",
                    ],
            ),
            (9, ["1^2 + 2^2 + 2^2", "2^2 + 1^2 + 2^2", "2^2 + 2^2 + 1^2"]),
            (5, []),
            (1, []),
        ]
    )
    def test_task331b(self, input_value, expected_value):
        """
        Testing task 331b class main logic
        (must return number as all of combinations of sums of 3 squared numbers)
        """
        self.assertEqual(algo.Task331b.main_logic(input_value), expected_value)


class TestTask178d(unittest.TestCase):
    """Testing task class 178d """

    @parameterized.expand(
        [([9, 12, 3], 0), ([18, 3, 17], 1), ([18, 3, 17, 78], 2), ([18, 3, 17, 0], 1), ([17, 17, 17, 17], 0)]
    )
    def test_task178d(self, input_value, expected_value):
        """Testing task 178d class main logic
        (find amount of elements, which satisfy the condition\nAk < (Ak-1 + Ak+1) / 2.)"""
        self.assertEqual(algo.Task178d.main_logic(input_value), expected_value)


class TestTask178e(unittest.TestCase):
    """Testing task class 178e """

    @parameterized.expand(
        [
            ([12, 45, 3, 8], 2),
            ([2, 4, 6, 8, 4], 3),
            ([1, 45], 1),
            ([2, 2, 2], 1),
        ]
    )
    def test_task178e(self, input_value, expected_value):
        """Testing task 178e class main logic (find amount of elements, which satisfy the condition\n2**k < Ak < k!)"""
        self.assertEqual(algo.Task178e.main_logic(input_value), expected_value)


class TestTask555(unittest.TestCase):
    """Testing task class 555 """

    @parameterized.expand([
        (1, [1, '\n']),
        (2, [1, '\n', 1, 1, '\n', ]),
        (4, [1, '\n', 1, 1, '\n', 1, 2,
             1, '\n', 1, 3, 3, 1, '\n', ]),
        (6, [1, '\n', 1, 1, '\n', 1, 2, 1, '\n', 1, 3, 3, 1,
             '\n', 1, 4, 6, 4, 1, '\n', 1, 5, 10, 10, 5, 1, '\n', ]),
    ])
    def test_task555(self, input_value, expected_value):
        """Testing task 555 class main logic (build first n rows of Pascal's triangle)"""
        self.assertEqual([*algo.Task555.main_logic(input_value)], expected_value)


class TestTask86a(unittest.TestCase):
    """Testing all methods of task 86a class"""

    @parameterized.expand([(15, 2), (441, 3), (9, 1), (123456798, 9), (15263, 5), (10526374859632104512, 20)])
    def test_task86a(self, input_value, expected_value):
        """Testing task 86a class main logic (must return  amount of digits in number)"""
        self.assertEqual(algo.Task86a.main_logic(input_value), expected_value)


class TestTask86b(unittest.TestCase):
    """Testing all methods of task 86b class"""

    @parameterized.expand(
        [(15, 6), (441, 9), (9, 9), (123456798, 45), (15263, 17), (0, 0), (10000, 1), (11111, 5), (1991, 20)]
    )
    def test_task86b(self, input_value, expected_value):
        """Testing task 86b class main logic (must return sum of digits in number)"""
        self.assertEqual(algo.Task86b.main_logic(input_value), expected_value)


class TestTask330(unittest.TestCase):
    """Testing all methods of task 330 class"""

    @parameterized.expand(
        [
            (15, {1, 3, 5}),
            (441, {1, 3, 7, 9, 49, 147, 21, 63}),
            (9, {1, 3}),
            (1, {1}),
            (127, {1}),
            (254, {1, 2, 127}),
            (1000, {1, 2, 4, 5, 100, 200, 8, 10, 40, 50, 500, 20, 25, 250, 125}),
        ]
    )
    def test_task330_get_dividers(self, number, expected_value):
        """Testing task 330 class  dividers func (must return set of all dividers of the number expect number itself)"""
        self.assertEqual(algo.Task330.get_dividers(number), expected_value)

    @parameterized.expand(
        [
            (15, [6]),
            (441, [6, 28]),
            (9, [6]),
            (123456, [6, 28, 496, 8128]),
            (15263, [6, 28, 496, 8128]),
            (1000, [6, 28, 496]),
        ]
    )
    def test_task330_main_logic(self, number, expected_value):
        """Testing task 330 main logic (must return number that's sum of dividers is equal to the number)"""
        self.assertEqual(list(algo.Task330.main_logic(number)), expected_value)
