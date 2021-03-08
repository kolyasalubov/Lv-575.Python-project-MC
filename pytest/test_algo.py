# import algo
import pytest
import sys

sys.path.append(
    '..')
import algo


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
def test_task330_get_deviders(number, expected_value):
    assert algo.Task330._get_deviders(number) == expected_value


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
def test_task178c_main_logic(number, expected_value):
    assert algo.Task554.main_logic(number + 1) == expected_value
