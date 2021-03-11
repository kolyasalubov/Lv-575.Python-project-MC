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


class TestTask88c(unittest.TestCase):

    @parameterized.expand([
        (1, 1), (4, 4), (234, 432), (1646, 6641), (333, 333),
        (3093, 3093), (264537, 764532), (12, 21), (1435, 5431),
    ])
    def test_task88c(self, input_value, expected_value):
        self.assertEqual(algo.Task88c.main_logic(input_value), expected_value)


class TestTask88d(unittest.TestCase):

    @parameterized.expand([
        (1, 111), (4, 141), (234, 12341), (1646, 116461), (333, 13331),
        (3093, 130931), (264537, 12645371), (12, 1121), (1435, 114351),
    ])
    def test_task88d(self, input_value, expected_value):
        self.assertEqual(algo.Task88d.main_logic(input_value), expected_value)


class TestTask332(unittest.TestCase):

    @parameterized.expand([
        (1, [1, 0, 0, 0]), (4, [2, 0, 0, 0]), (234, [15, 3, 0, 0]),
        (1646, [40, 6, 3, 1]), (2141, [46, 5, 0, 0]), (2137, [46, 4, 2, 1]),
        (2149, [46, 5, 2, 2]), (12412, [111, 9, 3, 1]), (90475, [300, 21, 5, 3]),
    ])
    def test_task332(self, input_value, expected_value):
        self.assertEqual(algo.Task332.main_logic(input_value), expected_value)


class TestTask107(unittest.TestCase):

    @parameterized.expand([
        (1, 0), (3, 0), (4, 0), (16, 1), (17, 2), (45, 2), (64, 2), (65, 3),
        (95, 3), (100, 3), (256, 3), (257, 4)
    ])
    def test_task107(self, input_value, expected_value):
        self.assertEqual(algo.Task107.main_logic(input_value), expected_value)


class TestTask243a(unittest.TestCase):

    @parameterized.expand([
        (24, ()), (104, (10, 2)), (328, (18, 2)), (611, ()), (1920, ()), (2311, ()),
        (9945, (99, 12)), (41410, (197, 51))
    ])
    def test_task243a(self, input_value, expected_value):
        self.assertEqual(algo.Task243a.main_logic(input_value), expected_value)


class TestTask243b(unittest.TestCase):

    @parameterized.expand([
        (24, []), (104, [(10, 2)]), (328, [(18, 2)]), (611, []), (2000, [(44, 8), (40, 20)]), (2311, []),
        (9945, [(99, 12), (96, 27), (93, 36), (72, 69)]), (41410, [(197, 51), (183, 89), (181, 93), (159, 127)])
    ])
    def test_task243b(self, input_value, expected_value):
        self.assertEqual(algo.Task243b.main_logic(input_value), expected_value)


class TestTask108(unittest.TestCase):

    @parameterized.expand([
        (5, 8), (16, 32),
        (1, 2), (65, 128),
        (8, 16), (55, 64),
        (256, 512), (1000, 1024),
        (13, 16), (2, 4)
    ])
    def test_task108(self, input_value, expected_value):
        self.assertEqual(algo.Task108.main_logic(input_value), expected_value)


class TestTask331a(unittest.TestCase):

    @parameterized.expand([
        (20, False), (3, ["1^2 + 1^2 + 1^2"]),
        (26, ["1^2 + 3^2 + 4^2"]), (1, False),
        (42, ["1^2 + 4^2 + 5^2"]), (4, False),
        (7, False), (9, ["1^2 + 2^2 + 2^2"]),
        (6, ["1^2 + 1^2 + 2^2"]), (5, False)
    ])
    def test_task331a(self, input_value, expected_value):
        self.assertEqual(algo.Task331a.main_logic(input_value), expected_value)


class TestTask331b(unittest.TestCase):

    @parameterized.expand([
        (50, ['3^2 + 4^2 + 5^2', '3^2 + 5^2 + 4^2', '4^2 + 3^2 + 5^2', '4^2 + 5^2 + 3^2',
              '5^2 + 3^2 + 4^2', '5^2 + 4^2 + 3^2']),
        (45, ['2^2 + 4^2 + 5^2', '2^2 + 5^2 + 4^2', '4^2 + 2^2 + 5^2', '4^2 + 5^2 + 2^2',
              '5^2 + 2^2 + 4^2', '5^2 + 4^2 + 2^2']),
        (9, ['1^2 + 2^2 + 2^2', '2^2 + 1^2 + 2^2', '2^2 + 2^2 + 1^2']),
        (5, False), (1, False)
    ])
    def test_task331b(self, input_value, expected_value):
        self.assertEqual(algo.Task331b.main_logic(input_value), expected_value)

