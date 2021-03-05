import pytest
import sys
import os
sys.path.append(
    '..')

from algo import *


@pytest.mark.parametrize('number, expected_value', [(1, 1), (5888, 4), (567, 3)], )
def test_task86_main_logic(number, expected_value):
    assert Task86a.main_logic(number) == expected_value


@pytest.mark.parametrize('number, expected_value', [(1, 1), (5888, 5888), (3, 3), ], )
def test_task86_validate_data(number, expected_value):
    assert Task86a.validate_data(number) == expected_value


@pytest.mark.parametrize('number, expected_value', [('1.2', TypeError), ('-3sdhv', TypeError), ('0', ValueError), ], )
def test_task86_validate_exceptions(number, expected_value):
    with pytest.raises(expected_value):
        Task86a.validate_data(number)
