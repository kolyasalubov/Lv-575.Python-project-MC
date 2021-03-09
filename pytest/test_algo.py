import algo
import pytest
import sys


# Testing base class with validation method for correct number answer
@pytest.mark.parametrize('number, expected_value', [(1, 1), (5888, 5888), (3, 3), ('0002', 2),
                                                    ('+99999', 99999), ('  067 ', 67), (' 12', 12)], )
def test_TaskWithOneIntValidationParameter_validate_data(number, expected_value):
    assert algo.TaskWithOneIntValidationParameter.validate_data(
        number) == expected_value


# Testing base class with validation method for exceptions
@pytest.mark.parametrize('number, expected_value', [('1.2', TypeError), ('-3sdhv', TypeError), (0, ValueError),
                                                    (1.2, TypeError), ('0o2',
                                                                       TypeError), ('-2', ValueError),
                                                    ('-0.2', TypeError), ('-0',
                                                                          ValueError), ('-566', ValueError),
                                                    (' ', TypeError), ('0  067 ', TypeError), ('+7m', TypeError)], )
def test_TaskWithOneIntValidationParameter_validate_exceptions(number, expected_value):
    with pytest.raises(expected_value):
        algo.TaskWithOneIntValidationParameter.validate_data(number)


# Testing task 86a class main logic (must return  amount of digits in number)
@pytest.mark.parametrize('number, expected_value', [(1, 1), (5888, 4), ('567', 3), (1111111111, 10)])
def test_task86a_main_logic(number, expected_value):
    assert algo.Task86a.main_logic(number) == expected_value


# Testing task 86b class main logic (must return sum of digits in number)
@pytest.mark.parametrize('number, expected_value', [(1, 1), (5888, 29), ('567', 18), (1111101111, 9)])
def test_task86b_main_logic(number, expected_value):
    assert algo.Task86b.main_logic(number) == expected_value


# Testing task 330 class  dividers func (must return set of all dividers of the number expect number itself)
@pytest.mark.parametrize('number, expected_value',
                         [(1, {1}),
                          (100, {1, 2, 4, 5, 10, 20, 25, 50}),
                          (30, {1, 2, 3, 5, 6, 10, 15}),
                          (47, {1}),
                          (90, {1, 2, 3, 5, 6, 9, 10, 15, 18, 30, 45}),
                          (198, {1, 2, 3, 6, 9, 11, 18, 22, 33, 66, 99})],
                         )
def test_task330_get_dividers(number, expected_value):
    assert algo.Task330._get_dividers(number) == expected_value


# Testing task 330 class main logic (must return number thats sum of dividers(from get_dividers) is equal to the number)
@pytest.mark.parametrize('number, expected_value',
                         [(10, [6]),
                          (100, [6, 28]),
                          (400, [6, 28]),
                          (1000, [6, 28, 496]),
                          (5000, [6, 28, 496]),
                          (10000, [6, 28, 496, 8128]),
                          (50000, [6, 28, 496, 8128]),
                          (100000, [6, 28, 496, 8128])],
                         )
def test_task330_main_logic(number, expected_value):
    assert [res for res in algo.Task330.main_logic(number)] == expected_value


# Testing task 178b class main logic (must return amount of numbers divided by 3 and not divided by 5 in a sequence)
@pytest.mark.parametrize('sequence, expected_value',
                         [([5], 0),
                          ([9], 1),
                          ([4, 5], 0),
                          ([9, 13], 1),
                          ([9, 12, 18, 21], 4),
                          ([1, 5, 10, 15], 0)]
                         )
def test_task178b_main_logic(sequence, expected_value):
    assert algo.Task178b.main_logic(sequence) == expected_value


# Testing task 178c class main logic (must return amount of numbers which are the square of the even number)
@pytest.mark.parametrize('sequence, expected_value',
                         [([5], 0),
                          ([100], 1),
                          ([4, 5], 1),
                          ([9, 13], 0),
                          ([4, 16, 36, 64], 4),
                          ([1, 2, 10, 15], 0)]
                         )
def test_task178c_main_logic(sequence, expected_value):
    assert algo.Task178c.main_logic(sequence) == expected_value


# Testing task 554 class main logic (must return list of pythagorean triplets)
@pytest.mark.parametrize('number, expected_value',
                         [(20, [[3, 4, 5],
                                [6, 8, 10],
                                [9, 12, 15],
                                [12, 16, 20],
                                [5, 12, 13],
                                [8, 15, 17]]),

                          (5, [[3, 4, 5]]),

                          (10, [[3, 4, 5],
                                [6, 8, 10]]),

                          (1, [])]
                         )
def test_task554_main_logic(number, expected_value):
    assert algo.Task554.main_logic(number + 1) == expected_value


# Testing task 107 class main logic (must return  the largest integer k, at which 4 ^k < m)
@pytest.mark.parametrize('number, expected_value', [
    (1, 0), (2, 0), (15, 1), (16, 1), (17, 2), (32, 2), (64, 2), (65, 3),
    (72, 3), (128, 3), (256, 3), (257, 4), (4000, 5), (10_000, 6),
])
def test_task107_main_logic(number, expected_value):
    assert algo.Task107.main_logic(number) == expected_value


# Testing task 243a class main logic (must return True if there are two numbers (x, y) that x ^2 + y ^2 = n)
@pytest.mark.parametrize('number, expected_value', [
    (1, ()), (7, ()), (13, (3, 2)), (272, (16, 4)), (317, (14, 11)), (300, ()),
    (6340, (78, 16)), (41410, (197, 51)), (67, ()), (32187, ()),
])
def test_task243a_main_logic(number, expected_value):
    assert algo.Task243a.main_logic(number) == expected_value


# Testing task 243b class main logic (must return all of the two numbers (x, y) that x ^2 + y ^2 = n)
@pytest.mark.parametrize('number, expected_value', [
    (1, []), (7, []), (13, [(3, 2)]), (272, [(16, 4)]), (317, [(14, 11)]), (300, []),
    (6340, [(78, 16), (72, 34)]),
    (41410, [(197, 51), (183, 89), (181, 93), (159, 127)]),
    (100000, [(316, 12), (300, 100), (260, 180)]),
    (1000000000, [(31600, 1200), (30672, 7696), (30000, 10000), (26000, 18000), (24560, 19920)])
])
def test_task243b_main_logic(number, expected_value):
    assert algo.Task243b.main_logic(number) == expected_value


# Testing task 108 class main logic ( must return the least number, that is bigger than n and is degree of number 2)
@pytest.mark.parametrize('number, expected_value', [(2, 4), (123, 128), (1034, 2048), (100020, 131072)])
def test_task108_main_logic(number, expected_value):
    assert algo.Task108.main_logic(number) == expected_value


# Testing task 331a class main logic ( must return the sum of 3 integers in power 2, that is equal to n)
@pytest.mark.parametrize('number, expected_value', [
    (19, ['1^2 + 3^2 + 3^2']),
    (20, False),
    (75, ['1^2 + 5^2 + 7^2']),
    (4, False)])
def test_task331a_main_logic(number, expected_value):
    assert algo.Task331a.main_logic(number) == expected_value


# Testing task 331b class main logic ( must return the array of sums of 3 integers in power 2, that is equal to n)
@pytest.mark.parametrize('number, expected_value', [
    (19, ['1^2 + 3^2 + 3^2', '3^2 + 1^2 + 3^2', '3^2 + 3^2 + 1^2']),
    (20, False),
    (75, ['1^2 + 5^2 + 7^2', '1^2 + 7^2 + 5^2', '5^2 + 1^2 + 7^2', '5^2 + 5^2 + 5^2', '5^2 + 7^2 + 1^2', '7^2 + 1^2 + 5^2', '7^2 + 5^2 + 1^2']),
    (4, False)])
def test_task331b_main_logic(number, expected_value):
    assert algo.Task331b.main_logic(number) == expected_value
