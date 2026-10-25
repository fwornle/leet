from patterns.monotonic_stack import (
    dailyTemperatures,
    largestRectangleArea,
    nextGreaterElement,
    next_greater,
)


def test_template():
    assert next_greater([2, 1, 2, 4, 3]) == [4, 2, 4, -1, -1]
    assert next_greater([]) == []
    assert next_greater([5, 4, 3]) == [-1, -1, -1]


def test_daily_temperatures():
    assert dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
    assert dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
    assert dailyTemperatures([30, 60, 90]) == [1, 1, 0]


def test_next_greater_element():
    assert nextGreaterElement([4, 1, 2], [1, 3, 4, 2]) == [-1, 3, -1]
    assert nextGreaterElement([2, 4], [1, 2, 3, 4]) == [3, -1]


def test_largest_rectangle():
    assert largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10
    assert largestRectangleArea([2, 4]) == 4
    assert largestRectangleArea([1]) == 1
    assert largestRectangleArea([2, 2, 2]) == 6
