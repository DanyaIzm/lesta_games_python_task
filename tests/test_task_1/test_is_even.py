import pytest
from task_1.main import is_even_classic, is_even_bitwise


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (1, False),
        (0, True),
        (2, True),
        (-1, False),
        (-2, True),
        (6, True),
        (-6, True),
        (7, False),
        (-7, False),
    ],
)
def test_is_even_classic(test_input, expected):
    assert is_even_classic(test_input) == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (1, False),
        (0, True),
        (2, True),
        (-1, False),
        (-2, True),
        (6, True),
        (-6, True),
        (7, False),
        (-7, False),
    ],
)
def test_is_even_bitwise(test_input, expected):
    assert is_even_bitwise(test_input) == expected
