import pytest
import algo


@pytest.mark.parametrize("input_number, expected_number", [
    (1, 1), (+100, 100), (2048, 2048),
    ("8", 8), ("101", 101), ("1024", 1024),
    (" 56", 56), ("   +78     ", 78), ("+13   ", 13),
])
def test_TaskWithOneIntValidationParameter_validate_data_right(input_number, expected_number):
    assert algo.TaskWithOneIntValidationParameter.validate_data(input_number) == expected_number


@pytest.mark.parametrize("input_number, expected_exception", [
    ("five", TypeError), (13.8, TypeError), (2+3j, TypeError),
    ("2+3j", TypeError), ("", TypeError), (None, TypeError),
    (-60, ValueError), ("  -12  ", ValueError), ("-1001", ValueError),
])
def test_TaskWithOneIntValidationParameter_validate_data_exception(input_number, expected_exception):
    with pytest.raises(expected_exception):
        algo.TaskWithOneIntValidationParameter.validate_data(input_number)


@pytest.mark.parametrize("input_value, expected_value", [
    (1, 1), (4, 4), (234, 432), (1646, 6641), (333, 333),
    (3093, 3093), (264537, 764532), (12, 21), (1435, 5431),
])
def test_task88c(input_value, expected_value):
    assert algo.Task88c.main_logic(input_value) == expected_value


@pytest.mark.parametrize("input_value, expected_value", [
    (1, 111), (4, 141), (234, 12341), (1646, 116461), (333, 13331),
    (3093, 130931), (264537, 12645371), (12, 1121), (1435, 114351),
])
def test_task88d(input_value, expected_value):
    assert algo.Task88d.main_logic(input_value) == expected_value


@pytest.mark.parametrize("input_value, expected_value", [
    (1, [1, 0, 0, 0]), (4, [2, 0, 0, 0]), (234, [15, 3, 0, 0]),
    (1646, [40, 6, 3, 1]), (2141, [46, 5, 0, 0]), (2137, [46, 4, 2, 1]),
    (2149, [46, 5, 2, 2]), (12412, [111, 9, 3, 1]), (90475, [300, 21, 5, 3]),
])
def test_task332(input_value, expected_value):
    assert algo.Task332.main_logic(input_value) == expected_value


@pytest.mark.parametrize('input_value, expected_value', [
    (1, 0), (3, 0), (4, 0), (16, 1), (17, 2), (45, 2), (64, 2), (65, 3),
    (95, 3), (100, 3), (256, 3), (257, 4)
])
def test_task107_main_logic(input_value, expected_value):
    assert algo.Task107.main_logic(input_value) == expected_value


@pytest.mark.parametrize('number, expected_value', [
    (24, ()), (104, (10, 2)), (328, (18, 2)), (611, ()), (1920, ()), (2311, ()),
    (9945, (99, 12)), (41410, (197, 51))
])
def test_task243a_main_logic(number, expected_value):
    assert algo.Task243a.main_logic(number) == expected_value


@pytest.mark.parametrize('number, expected_value', [
    (24, []), (104, [(10, 2)]), (328, [(18, 2)]), (611, []), (2000, [(44, 8), (40, 20)]), (2311, []),
    (9945, [(99, 12), (96, 27), (93, 36), (72, 69)]), (41410, [(197, 51), (183, 89), (181, 93), (159, 127)])
])
def test_task243b_main_logic(number, expected_value):
    assert algo.Task243b.main_logic(number) == expected_value
