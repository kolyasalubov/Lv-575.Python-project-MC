import algo
import pytest


@pytest.mark.parametrize('number, expected_value', [(1, 1), (5888, 4), ('567', 3), (1111111111, 10)])
def test_task86_main_logic(number, expected_value):
    assert algo.Task86a.main_logic(number) == expected_value


@pytest.mark.parametrize('number, expected_value', [(1, 1), (5888, 5888), (3, 3), ('0002', 2),
                                                    ('+99999', 99999), ('  067 ', 67), (' 12', 12)], )
def test_task86_validate_data(number, expected_value):
    assert algo.Task86a.validate_data(number) == expected_value


@pytest.mark.parametrize('number, expected_value', [('1.2', TypeError), ('-3sdhv', TypeError), (0, ValueError),
                                                    (1.2, TypeError), ('0o2',
                                                                       TypeError), ('-2', ValueError),
                                                    ('-0.2', TypeError), ('-0',
                                                                          ValueError), ('-566', ValueError),
                                                    (' ', TypeError), ('0  067 ', TypeError), ('+7m', TypeError)], )
def test_task86_validate_exceptions(number, expected_value):
    with pytest.raises(expected_value):
        algo.Task86a.validate_data(number)
