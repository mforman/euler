from typing import List

import pytest

from euler.problem008 import get_slices


@pytest.mark.parametrize(
    "input_val,size,expected",
    [("731671", 4, ["7316", "3167", "1671"]), ("7316712", 4, ["7316", "3167", "1671", "6712"])],
)
def test_get_slices(input_val: str, size: int, expected: List[str]):
    assert list(get_slices(input_val, size)) == expected


@pytest.mark.parametrize("input_val,size,expected", [("10234", 3, ["234"])])
def test_get_slices_drop_zeroes(input_val: str, size: int, expected: List[str]):
    assert list(get_slices(input_val, size, True)) == expected
