import pytest

from euler.problem004 import isPalindrome, reverse


@pytest.mark.parametrize(
    "input_val,expected",
    [(1, True), (11, True), (123, False), (101, True)],
)
def test_isPalindrome(input_val: int, expected: bool):
    assert isPalindrome(input_val) == expected


@pytest.mark.parametrize(
    "input_val,expected",
    [
        (1, 1),
        (11, 11),
        (123, 321),
    ],
)
def test_reverse(input_val: int, expected: int):
    assert reverse(input_val) == expected
