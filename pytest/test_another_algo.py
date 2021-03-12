import pytest
import algo


@pytest.mark.parametrize("input_number, expected_number", [
    (1, 1), (+100, 100), (2048, 2048),
    ("8", 8), ("101", 101), ("1024", 1024),
    (" 56", 56), ("   +78     ", 78), ("+13   ", 13),
])
def test_TaskWithOneIntValidationParameter_validate_data_right(input_number, expected_number):
    assert algo.TaskWithOneIntValidationParameter.validate_data(
        input_number) == expected_number


@pytest.mark.parametrize("input_number, expected_exception", [
    ("five", TypeError), (13.8, TypeError), (2 + 3j, TypeError),
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


# Testing task 87 class main logic
@pytest.mark.parametrize('number, quantity, expected_value', [
    ('49850', 2, 5), ('14', 2, 5), ('548736', 4, 24), ('5870', 1, 0), ('247845225', 1, 5), ('558062862', 5, 24)])
def test_task87_main_logic(number, quantity, expected_value):
    assert algo.Task87.main_logic(number, quantity) == expected_value


# Testing task 226 class main logic
@pytest.mark.parametrize('number1, number2, expected_value', [
    (10, 3, []), (6, 15, [30, 60]), (250, 110, [2750, 5500, 8250, 11000, 13750, 16500, 19250, 22000, 24750]), (71, 140, [])],)
def test_task226_main_logic(number1, number2, expected_value):
    assert algo.Task226.main_logic(number1, number2) == expected_value


# Testing task 559 class main logic
@pytest.mark.parametrize('number, expected_value', [
    (126, [3, 7, 31]), (128, [3, 7, 31, 127]), (1, []), (8, [3, 7]),
    (8000, [3, 7, 31, 127]), (5, [3]), (13172, [3, 7, 31, 127, 8191])],)
def test_task559_main_logic(number, expected_value):
    assert algo.Task559.main_logic(number) == expected_value


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
    (24, []), (104, [(10, 2)]), (328, [(18, 2)]), (611,
                                                   []), (2000, [(44, 8), (40, 20)]), (2311, []),
    (9945, [(99, 12), (96, 27), (93, 36), (72, 69)]), (41410,
                                                       [(197, 51), (183, 89), (181, 93), (159, 127)])
])
def test_task243b_main_logic(number, expected_value):
    assert algo.Task243b.main_logic(number) == expected_value


@pytest.mark.parametrize("input_value, expected_value",
                         [
                             (5, 8), (16, 32),
                             (1, 2), (65, 128),
                             (8, 16), (55, 64),
                             (256, 512), (1000, 1024),
                             (13, 16), (2, 4)
                         ])
def test_task108(input_value, expected_value):
    assert algo.Task108.main_logic(input_value) == expected_value


@pytest.mark.parametrize("input_value, expected_value",
                         [
                             (20, False), (3, ["1^2 + 1^2 + 1^2"]),
                             (26, ["1^2 + 3^2 + 4^2"]), (1, False),
                             (42, ["1^2 + 4^2 + 5^2"]), (4, False),
                             (7, False), (9, ["1^2 + 2^2 + 2^2"]),
                             (6, ["1^2 + 1^2 + 2^2"]), (5, False)
                         ])
def test_task331a(input_value, expected_value):
    assert algo.Task331a.main_logic(input_value) == expected_value


@pytest.mark.parametrize("input_value, expected_value",
                         [
                             (50, ['3^2 + 4^2 + 5^2', '3^2 + 5^2 + 4^2', '4^2 + 3^2 + 5^2', '4^2 + 5^2 + 3^2',
                                   '5^2 + 3^2 + 4^2', '5^2 + 4^2 + 3^2']),
                             (45, ['2^2 + 4^2 + 5^2', '2^2 + 5^2 + 4^2', '4^2 + 2^2 + 5^2', '4^2 + 5^2 + 2^2',
                                   '5^2 + 2^2 + 4^2', '5^2 + 4^2 + 2^2']),
                             (9, ['1^2 + 2^2 + 2^2',
                                  '2^2 + 1^2 + 2^2', '2^2 + 2^2 + 1^2']),
                             (5, False), (1, False)
                         ])
def test_task331b(input_value, expected_value):
    assert algo.Task331b.main_logic(input_value) == expected_value


@pytest.mark.parametrize("input_value, expected_value",
                         [
                             ([9, 12, 3], 0),
                             ([18, 3, 17], 1),
                             ([18, 3, 17, 78], 2),
                             ([18, 3, 17, 0], 1),
                             ([17, 17, 17, 17], 0)
                         ])
def test_task178d(input_value, expected_value):
    assert algo.Task178d.main_logic(input_value) == expected_value


@pytest.mark.parametrize("input_value, expected_value",
                         [
                             ([12, 45, 3, 8], 2),
                             ([2, 4, 6, 8, 4], 3),
                             ([1, 45], 1),
                             ([2, 2, 2], 1),
                         ])
def test_task178e(input_value, expected_value):
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
    assert [*algo.Task555.main_logic(input_value)] == expected_value
