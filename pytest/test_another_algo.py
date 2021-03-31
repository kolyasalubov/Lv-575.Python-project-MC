"""
Tests for somebody algo (pytest)
"""
import pytest
import algo


@pytest.mark.parametrize(
    "input_number, expected_number",
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
    ],
)
def test_task_with_one_int_validation_parameter_validate_data_right(input_number, expected_number):
    """
    Testing base class with validation method for correct number answer
    """
    assert algo.TaskWithOneIntValidationParameter.validate_data(input_number) == expected_number


@pytest.mark.parametrize(
    "input_number, expected_exception",
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
    ],
)
def test_task_with_one_int_validation_parameter_validate_data_exception(input_number, expected_exception):
    """
    Testing base class with validation method for exceptions
    """
    with pytest.raises(expected_exception):
        algo.TaskWithOneIntValidationParameter.validate_data(input_number)


@pytest.mark.parametrize(
    "input_value, expected_value",
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
    ],
)
def test_task88c(input_value, expected_value):
    """
    Testing task 88c class main logic (Swap the first and last digits of n)
    """
    assert algo.Task88c.main_logic(input_value) == expected_value


@pytest.mark.parametrize(
    "input_value, expected_value",
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
    ],
)
def test_task88d(input_value, expected_value):
    """
    Testing task 88d class main logic (Add the number 1 to the beginning and end of n)
    """
    assert algo.Task88d.main_logic(input_value) == expected_value


@pytest.mark.parametrize(
    "input_value, expected_value",
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
    ],
)
def test_task332(input_value, expected_value):
    """
    Testing task 332 class main logic (Find non-negative x1, x2, x3, x4 such that x1^2 + x2^2 + x3^2 + x4^2 = n)
    """
    assert algo.Task332.main_logic(input_value) == expected_value


@pytest.mark.parametrize(
    "number, quantity, expected_value",
    [
        ("49850", 2, 5),
        ("14", 2, 5),
        ("548736", 4, 24),
        ("5870", 1, 0),
        ("247845225", 1, 5),
        ("558062862", 5, 24),
    ],
)
def test_task87_main_logic(number, quantity, expected_value):
    """Testing task 87 class main logic"""
    assert algo.Task87.main_logic(number, quantity) == expected_value


@pytest.mark.parametrize(
    "number1, number2, expected_value",
    [
        (10, 3, []),
        (6, 15, [30, 60]),
        (250, 110, [2750, 5500, 8250, 11000, 13750, 16500, 19250, 22000, 24750]),
    ],
)
def test_task226_main_logic(number1, number2, expected_value):
    """Testing task 226 class main logic"""
    assert algo.Task226.main_logic(number1, number2) == expected_value


@pytest.mark.parametrize(
    "number, expected_value",
    [
        (126, [3, 7, 31]),
        (128, [3, 7, 31, 127]),
        (1, []),
        (8, [3, 7]),
        (8000, [3, 7, 31, 127]),
        (13172, [3, 7, 31, 127, 8191]),
    ],
)
def test_task559_main_logic(number, expected_value):
    """Testing task 559 class main logic"""
    assert algo.Task559.main_logic(number) == expected_value


# Testing task 107 class main logic (must return  the largest integer k, at which 4 ^k < m)
@pytest.mark.parametrize(
    "input_value, expected_value",
    [
        (1, 0),
        (3, 0),
        (4, 0),
        (16, 1),
        (17, 2),
        (45, 2),
        (64, 2),
        (65, 3),
        (100, 3),
        (256, 3),
        (257, 4),
    ],
)
def test_task107_main_logic(input_value, expected_value):
    assert algo.Task107.main_logic(input_value) == expected_value


# Testing task 243a class main logic (must return True if there are two numbers (x, y) that x ^2 + y ^2 = n)
@pytest.mark.parametrize(
    "number, expected_value",
    [
        (24, ()),
        (104, (10, 2)),
        (328, (18, 2)),
        (611, ()),
        (1920, ()),
        (2311, ()),
        (9945, (99, 12)),
        (41410, (197, 51)),
    ],
)
def test_task243a_main_logic(number, expected_value):
    assert algo.Task243a.main_logic(number) == expected_value


# Testing task 243a class main logic (must return True if there are two numbers (x, y) that x ^2 + y ^2 = n)
@pytest.mark.parametrize(
    "number, expected_value",
    [
        (24, []),
        (104, [(10, 2)]),
        (328, [(18, 2)]),
        (611, []),
        (2000, [(44, 8), (40, 20)]),
        (2311, []),
        (9945, [(99, 12), (96, 27), (93, 36), (72, 69)]),
        (41410, [(197, 51), (183, 89), (181, 93), (159, 127)]),
    ],
)
def test_task243b_main_logic(number, expected_value):
    assert algo.Task243b.main_logic(number) == expected_value


@pytest.mark.parametrize(
    "input_value, expected_value",
    [
        (5, 8),
        (16, 32),
        (1, 2),
        (65, 128),
        (8, 16),
        (55, 64),
        (256, 512),
        (1000, 1024),
        (13, 16),
        (2, 4),
    ],
)
def test_task108(input_value, expected_value):
    """
    Testing task 108 class main logic
    (must return the least number, that is bigger than n and is degree of number 2)
    """
    assert algo.Task108.main_logic(input_value) == expected_value


@pytest.mark.parametrize(
    "input_value, expected_value",
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
    ],
)
def test_task331a(input_value, expected_value):
    """
    Testing task 331a class main logic
    (must return number as a sum of 3 squared numbers)
    """
    assert algo.Task331a.main_logic(input_value) == expected_value


@pytest.mark.parametrize(
    "input_value, expected_value",
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
    ],
)
def test_task331b(input_value, expected_value):
    """
    Testing task 331b class main logic
    (must return number as all of combinations of sums of 3 squared numbers)
    """
    assert algo.Task331b.main_logic(input_value) == expected_value


@pytest.mark.parametrize(
    "input_value, expected_value",
    [
        ([9, 12, 3], 0),
        ([18, 3, 17], 1),
        ([18, 3, 17, 78], 2),
        ([18, 3, 17, 0], 1),
        ([17, 17, 17, 17], 0),
    ],
)
def test_task178d(input_value, expected_value):
    """Testing task 178d class main logic
    (find amount of elements, which satisfy the condition\nAk < (Ak-1 + Ak+1) / 2.)"""
    assert algo.Task178d.main_logic(input_value) == expected_value


@pytest.mark.parametrize(
    "input_value, expected_value",
    [
        ([12, 45, 3, 19], 1),
        ([2, 4, 6, 8, 21, 34], 0),
        ([1, 45], 0),
        ([2, 2, 2], 0),
    ],
)
def test_task178e(input_value, expected_value):
    """Testing task 178e class main logic (find amount of elements, which satisfy the condition\n2**k < Ak < k!)"""
    assert algo.Task178e.main_logic(input_value) == expected_value


@pytest.mark.parametrize("input_value, expected_value",
                         [
                             (1, [1, '\n']),
                             (2, [1, '\n', 1, 1, '\n', ]),
                             (4, [1, '\n', 1, 1, '\n', 1, 2,
                                  1, '\n', 1, 3, 3, 1, '\n', ]),
                             (6, [1, '\n', 1, 1, '\n', 1, 2, 1, '\n', 1, 3, 3, 1,
                                  '\n', 1, 4, 6, 4, 1, '\n', 1, 5, 10, 10, 5, 1, '\n', ]),
                         ])
def test_task555(input_value, expected_value):
    """Testing task 555 class main logic (build first n rows of Pascal's triangle)"""
    assert list(algo.Task555.main_logic(input_value)) == expected_value


@pytest.mark.parametrize(
    "input_value, expected_value",
    [
        ([3, 6, 9, 12], 4),
        ([9, 15, 21, 33], 3),
        ([1, 45], 0),
        ([15, 2, 4], 0),
    ],
)
def test_task178b(input_value, expected_value):
    """Testing task 178b class main logic (Find numbers which are multiples of 3 and not multiples of 5)"""
    assert algo.Task178b.main_logic(input_value) == expected_value


@pytest.mark.parametrize(
    "input_value, expected_value",
    [
        ([4, 4, 4, 4], 4),
        ([16, 36], 2),
        ([1, 3], 0),
        ([16, 13, 4], 2),
    ],
)
def test_task178c(input_value, expected_value):
    """Testing task 178c class main logic (Find numbers which are squares of even numbers)"""
    assert algo.Task178c.main_logic(input_value) == expected_value


@pytest.mark.parametrize(
    "input_value, expected_value",
    [
        (
            10,
            [
                [3, 4, 5],
                [6, 8, 10],
            ],
        ),
        (6, [[3, 4, 5]]),
        (11, [[3, 4, 5], [6, 8, 10]]),
        (2, []),
    ],
)
def test_task554(input_value, expected_value):
    """Testing task 554 class main logic (return list of pythagorean triplets)"""
    assert algo.Task554.main_logic(input_value + 1) == expected_value


@pytest.mark.parametrize(
    "number, expected_value",
    [(15, 2), (441, 3), (9, 1), (123456798, 9), (15263, 5), (10526374859632104512, 20)],
)
def test_task86a_main_logic(number, expected_value):
    """Testing task 86a class main logic (must return  amount of digits in number)"""
    assert algo.Task86a.main_logic(number) == expected_value


@pytest.mark.parametrize(
    "number, expected_value",
    [
        (15, 6),
        (441, 9),
        (9, 9),
        (123456798, 45),
        (15263, 17),
        (0, 0),
        (10000, 1),
        (11111, 5),
        (1991, 20),
    ],
)
def test_task86b_main_logic(number, expected_value):
    """Testing task 86b class main logic (must return sum of digits in number)"""
    assert algo.Task86b.main_logic(number) == expected_value


@pytest.mark.parametrize(
    "number, expected_value",
    [
        (15, {1, 3, 5}),
        (441, {1, 3, 7, 9, 49, 147, 21, 63}),
        (9, {1, 3}),
        (1, {1}),
        (127, {1}),
        (254, {1, 2, 127}),
        (1000, {1, 2, 4, 5, 100, 200, 8, 10, 40, 50, 500, 20, 25, 250, 125}),
    ],
)
def test_task330_get_dividers(number, expected_value):
    """Testing task 330 class  dividers func (must return set of all dividers of the number expect number itself)"""
    assert algo.Task330.get_dividers(number) == expected_value


@pytest.mark.parametrize(
    "number, expected_value",
    [
        (15, [6]),
        (441, [6, 28]),
        (9, [6]),
        (123456, [6, 28, 496, 8128]),
        (15263, [6, 28, 496, 8128]),
        (1000, [6, 28, 496]),
    ],
)
def test_task330_main_logic(number, expected_value):
    """Testing task 330 main logic (must return number that's sum of dividers is equal to the number)"""
    assert list(algo.Task330.main_logic(number)) == expected_value
