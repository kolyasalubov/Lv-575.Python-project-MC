import algo
import pytest


# Testing base class with validation method for corrext number answer
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


# Testing task 330 class  deviders func (must return set of all deviders of the number excpet number itself)
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


# Testing task 330 class main logic (must return number thats sum of deviders(from get_deviders) is equal to the number)
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


@pytest.mark.parametrize('number, expected_value', [
    (1, 0), (2, 0), (15, 1), (16, 1), (17, 2), (32, 2), (64, 2), (65, 3),
    (72, 3), (128, 3), (256, 3), (257, 4), (4000, 5), (10_000, 6),
])
def test_task107_main_logic(number, expected_value):
    assert algo.Task107.main_logic(number) == expected_value


@pytest.mark.parametrize('number, expected_value', [
    (1, ()), (7, ()), (13, (3, 2)), (272, (16, 4)), (317, (14, 11)), (300, ()),
    (6340, (78, 16)), (41410, (197, 51)), (67, ()), (32187, ()),
])
def test_task243a_main_logic(number, expected_value):
    assert algo.Task243a.main_logic(number) == expected_value


@pytest.mark.parametrize('number, expected_value', [
    (1, []), (7, []), (13, [(3, 2)]), (272, [(16, 4)]), (317, [(14, 11)]), (300, []),
    (6340, [(78, 16), (72, 34)]),
    (41410, [(197, 51), (183, 89), (181, 93), (159, 127)]),
    (100000, [(316, 12), (300, 100), (260, 180)]),
    (1000000000, [(31600, 1200), (30672, 7696), (30000, 10000), (26000, 18000), (24560, 19920)])
])
def test_task243b_main_logic(number, expected_value):
    assert algo.Task243b.main_logic(number) == expected_value
