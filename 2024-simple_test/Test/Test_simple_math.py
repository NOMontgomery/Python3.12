import pytest
from Src.simple_math import reverse_str, addition, substraction


def test_reverse_str():
    assert reverse_str("abc") == "cba"


@pytest.mark.parametrize("x, y", [
                           (3, 5),
                           (-3, 5),
                           (-15, 7),
                       ])
def test_addition_simple(x, y):
    assert addition(x, y) == 7


@pytest.mark.parametrize("x, y, expected", [
                           (3, 5),
                           (-3, 5),
                           (-15, 7),
                       ])
def test_addition_simple_expected(x, y, expected):
    assert addition(x, y) == expected


@pytest.mark.parametrize("string, expected", [
        ("abc", "cba"),
        ("abc xyz", "zyx cba"),
        ("abc123", "321cba"),
])
def test_reverse_string(string, expected):
    assert reverse_str(string) == expected