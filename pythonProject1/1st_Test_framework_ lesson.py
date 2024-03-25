import pytest


def addition(a: int, b: int) -> int:
    return a + b


def test_addition():
    assert addition(7, 8) == 15


def test_addition2():
    assert addition(10, 8) == 18


if "__main__" == __name__:
    print(f'{addition(7, 8)}')
    pass
