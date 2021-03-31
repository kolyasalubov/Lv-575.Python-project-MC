"""
Tests for algo (pytest)
"""
import algo
import pytest


@pytest.mark.parametrize(
    "number, expected_value",
    [
        (1, 1),
        (5888, 5888),
        (3, 3),
        ("0002", 2),
        ("+99999", 99999),
        ("  067 ", 67),
        (" 12", 12),
    ],
)
def test_task_with_one_int_validation_parameter_validate_data(number, expected_value):
    """
    Testing base class with validation method for correct number answer
    """

    assert algo.TaskWithOneIntValidationParameter.validate_data(number) == expected_value


@pytest.mark.parametrize(
    "number, expected_value",
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
    ],
)
def test_task_with_one_int_validation_parameter_validate_exceptions(number, expected_value):
    """
    Testing base class with validation method for exceptions
    """

    with pytest.raises(expected_value):
        algo.TaskWithOneIntValidationParameter.validate_data(number)


# Testing task 86a class main logic (must return  amount of digits in number)
@pytest.mark.parametrize("number, expected_value", [(1, 1), (5888, 4), ("567", 3), (1111111111, 10)])
def test_task86a_main_logic(number, expected_value):
    """
    Testing task 86b class main logic (must return sum of digits in number)
    """
    assert algo.Task86a.main_logic(number) == expected_value


# Testing task 86b class main logic (must return sum of digits in number)
@pytest.mark.parametrize("number, expected_value", [(1, 1), (5888, 29), ("567", 18), (1111101111, 9)])
def test_task86b_main_logic(number, expected_value):
    """
    Testing task 86b class main logic (must return sum of digits in number)
    """
    assert algo.Task86b.main_logic(number) == expected_value


# Testing task 330 class  dividers func (must return set of all dividers of the number expect number itself)
@pytest.mark.parametrize(
    "number, expected_value",
    [
        (1, {1}),
        (100, {1, 2, 4, 5, 10, 20, 25, 50}),
        (30, {1, 2, 3, 5, 6, 10, 15}),
        (47, {1}),
        (90, {1, 2, 3, 5, 6, 9, 10, 15, 18, 30, 45}),
        (198, {1, 2, 3, 6, 9, 11, 18, 22, 33, 66, 99}),
    ],
)
def test_task330_get_dividers(number, expected_value):
    assert algo.Task330.get_dividers(number) == expected_value


# Testing task 330 class main logic (must return number thats sum of dividers(from get_dividers) is equal to the number)
@pytest.mark.parametrize(
    "number, expected_value",
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
def test_task330_main_logic(number, expected_value):
    """
    Testing task 330 class  dividers func (must return set of all dividers of the number expect number itself)
    """
    assert list(algo.Task330.main_logic(number)) == expected_value


@pytest.mark.parametrize(
    "sequence, expected_value",
    [
        ([5], 0),
        ([9], 1),
        ([4, 5], 0),
        ([9, 13], 1),
        ([9, 12, 18, 21], 4),
        ([1, 5, 10, 15], 0),
    ],
)
def test_task178b_main_logic(sequence, expected_value):
    """
    Testing task 178b class main logic
    (must find the least number, that is bigger than n and is degree of number 2)
    """
    assert algo.Task178b.main_logic(sequence) == expected_value


@pytest.mark.parametrize(
    "sequence, expected_value",
    [
        ([5], 0),
        ([100], 1),
        ([4, 5], 1),
        ([9, 13], 0),
        ([4, 16, 36, 64], 4),
        ([1, 2, 10, 15], 0),
    ],
)
def test_task178c_main_logic(sequence, expected_value):
    """
    Testing task 178c class main logic
    (must return amount of numbers which are the square of the even number)
    """
    assert algo.Task178c.main_logic(sequence) == expected_value


@pytest.mark.parametrize(
    "input_value, expected_value",
    [
        ([18, 3, 17], 1),
        ([9, 12, 3], 0),
        ([12, 13, 13, 14], 1),
        ([16, 16, 16, 16], 0),
    ],
)
def test_task178d(input_value, expected_value):
    """
    Testing task 178d class main logic
    (find amount of elements, which satisfy the condition\nAk < (Ak-1 + Ak+1) / 2.)
    """
    assert algo.Task178d.main_logic(input_value) == expected_value


@pytest.mark.parametrize(
    "input_value, expected_value",
    [
        ([22, 33, 13, 19], 1),
        ([3, 6, 9, 8, 21, 37], 0),
        ([40, 60], 0),
        ([8, 8, 8], 0),
    ],
)
def test_task178e(input_value, expected_value):
    """
    Testing task 178e class main logic (find amount of elements, which satisfy the condition\n2**k < Ak < k!)
    """
    assert algo.Task178e.main_logic(input_value) == expected_value


@pytest.mark.parametrize("input_value, expected_value",
                         [
                             (1, [1, '\n']),
                             (2, [1, '\n', 1, 1, '\n', ]),
                             (4, [1, '\n', 1, 1, '\n', 1, 2,
                                  1, '\n', 1, 3, 3, 1, '\n']),
                             (5, [1, '\n', 1, 1, '\n', 1, 2, 1, '\n', 1, 3, 3, 1,
                                  '\n', 1, 4, 6, 4, 1, '\n',]),
                         ])
def test_task555(input_value, expected_value):
    """
    Testing task 555 class main logic (build first n rows of Pascal's triangle)
    """
    assert list(algo.Task555.main_logic(input_value)) == expected_value


@pytest.mark.parametrize(
    "number, expected_value",
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
    ],
)
def test_task554_main_logic(number, expected_value):
    """
    Testing task 554 class main logic
    (must return list of pythagorean triplets)
    """
    assert algo.Task554.main_logic(number + 1) == expected_value


@pytest.mark.parametrize(
    "number, expected_value",
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
    ],
)
def test_task107_main_logic(number, expected_value):
    """
    Testing task 107 class main logic (must return  the largest integer k, at which 4 ^k < m)
    """
    assert algo.Task107.main_logic(number) == expected_value


@pytest.mark.parametrize(
    "number, expected_value",
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
    ],
)
def test_task243a_main_logic(number, expected_value):
    """
    Testing task 243a class main logic (must return True if there are two numbers (x, y) that x ^2 + y ^2 = n)
    """
    assert algo.Task243a.main_logic(number) == expected_value


@pytest.mark.parametrize(
    "number, expected_value",
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
    ],
)
def test_task243b_main_logic(number, expected_value):
    """
    Testing task 243a class main logic (must return True if there are two numbers (x, y) that x ^2 + y ^2 = n)
    """
    assert algo.Task243b.main_logic(number) == expected_value


# Testing task 108 class main logic ( must return the least number, that is bigger than n and is degree of number 2)
@pytest.mark.parametrize("number, expected_value", [(2, 4), (123, 128), (1034, 2048), (100020, 131072)])
def test_task108_main_logic(number, expected_value):
    """
    Testing task 108 class main logic ( must return the least number,
    that is bigger than n and is degree of number 2)
    :param: int
    :return: int
    """
    assert algo.Task108.main_logic(number) == expected_value


# Testing task 331a class main logic ( must return the sum of 3 integers in power 2, that is equal to n)
@pytest.mark.parametrize(
    "number, expected_value",
    [(19, ["1^2 + 3^2 + 3^2"]), (20, []), (75, ["1^2 + 5^2 + 7^2"]), (4, [])],
)
def test_task331a_main_logic(number, expected_value):
    """
    Testing task 331a class main logic ( must return the sum of 3 integers in power 2,
    that is equal to n)
    :param: int
    :return: list
    """
    assert algo.Task331a.main_logic(number) == expected_value


# Testing task 331b class main logic ( must return the array of sums of 3 integers in power 2, that is equal to n)
@pytest.mark.parametrize(
    "number, expected_value",
    [
        (19, ["1^2 + 3^2 + 3^2", "3^2 + 1^2 + 3^2", "3^2 + 3^2 + 1^2"]),
        (20, []),
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
        (4, []),
    ],
)
def test_task331b_main_logic(number, expected_value):
    """
    Testing task 331b class main logic ( must return the array of sums of 3 integers in power 2,
    that is equal to n)
    :param: int
    :return: list
    """
    assert algo.Task331b.main_logic(number) == expected_value


@pytest.mark.parametrize(
    "data, expected_value",
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
    ],
)
def test_task_with_two_int_validation_parameters_validate_exceptions_task87(data, expected_value):
    """
    Testing base class with validation method for exceptions
    """

    with pytest.raises(expected_value):
        algo.Task87.validate_data(data)


@pytest.mark.parametrize(
    "number, quantity, expected_value",
    [
        ("78451", 2, 6),
        ("421", 3, 7),
        ("1234567890", 10, 45),
        ("52138", 4, 14),
        ("17", 2, 8),
        ("32", 1, 2),
    ],
)
def test_task87_main_logic(number, quantity, expected_value):
    """
    Testing task 87 class main logic
    """
    assert algo.Task87.main_logic(number, quantity) == expected_value


@pytest.mark.parametrize(
    "data, expected_value",
    [
        ("1.2", ValueError),
        ("-3ssss", ValueError),
        ("0", ValueError),
        ("445", ValueError),
        ("7m 456", TypeError),
        ("7115m 4", TypeError),
        ("124 4d56", TypeError),
        ("7,5555 456", TypeError),
    ],
)
def test_task_with_two_int_validation_parameters_validate_exceptions_task226(data, expected_value):
    """
    Testing base class with validation method for exceptions
    """

    with pytest.raises(expected_value):
        algo.TaskWithTwoIntValidationParameters.validate_data(data)


@pytest.mark.parametrize(
    "number1, number2, expected_value",
    [
        (12, 36, [36, 72, 108, 144, 180, 216, 252, 288, 324, 360, 396]),
        (78, 5, []),
        (78, 12, [156, 312, 468, 624, 780]),
        (444, 822, [60828, 121656, 182484, 243312, 304140]),
        (77, 127, []),
    ],
)
def test_task226_main_logic(number1, number2, expected_value):
    """
    Testing task 226 class main logic
    """
    assert algo.Task226.main_logic(number1, number2) == expected_value


@pytest.mark.parametrize(
    "data, expected_value",
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
    ],
)
def test_task_with_two_int_validation_parameters_validate_exceptions_task559(data, expected_value):
    """
    Testing base class with validation method for exceptions
    """
    with pytest.raises(expected_value):
        algo.TaskWithOneIntValidationParameter.validate_data(data)


# Testing eratosthenes function in task 559
@pytest.mark.parametrize(
    "number, expected_value",
    [
        (24, [2, 3, 5, 7, 11, 13, 17, 19, 23]),
        (50, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]),
        (62, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]),
        (88, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83]),
    ],
)
def test_task559_eratosthenes(number, expected_value):
    """
    Testing eratosthenes function in task 559
    """
    assert algo.Task559.eratosthenes(number) == expected_value


@pytest.mark.parametrize(
    "number, expected_value",
    [
        (24, [3, 7, 15]),
        (50, [3, 7, 15, 31]),
        (61, [3, 7, 15, 31]),
        (88, [3, 7, 15, 31, 63]),
        (7700, [3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095]),
    ],
)
def test_task559_mersen_number(number, expected_value):
    """
    Testing mersen_numbers function in task 559
    """
    assert algo.Task559.mersen_numbers(number) == expected_value


@pytest.mark.parametrize(
    "number, expected_value",
    [
        (456, [3, 7, 31, 127]),
        (1234, [3, 7, 31, 127]),
        (2, []),
        (100000, [3, 7, 31, 127, 8191]),
        (748452, [3, 7, 31, 127, 8191, 131071, 524287]),
        (12, [3, 7]),
        (6, [3]),
    ],
)
def test_task559_main_logic(number, expected_value):
    """
    Testing task 559 class main logic
    """
    assert algo.Task559.main_logic(number) == expected_value


@pytest.mark.parametrize("number, expected_value", [(3, "NO"), (6, "YES"), (18, "YES"), (13, "NO")])
def test_task88a_main_logic(number, expected_value):
    """
    Testing task 88a class main logic ( input number n, we should check, if 3 is in n^2 number)
    """
    assert algo.Task88a.main_logic(number) == expected_value


@pytest.mark.parametrize(
    "number, expected_value",
    [(3, 3), (121, 121), (1222, 2221), (1250, 521), (54789, 98745)],
)
def test_task88b_main_logic(number, expected_value):
    """
    Testing task 88b class main logic ( input number n, we should revert it)
    """
    assert algo.Task88b.main_logic(number) == expected_value
