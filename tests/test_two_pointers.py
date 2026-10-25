from patterns.two_pointers import (
    maxArea,
    threeSum,
    twoSum,
    two_pointers_opposite,
    two_pointers_same_direction,
)


def test_template_opposite():
    assert two_pointers_opposite([1, 3, 4, 6, 8, 11], 10) == (2, 3)
    assert two_pointers_opposite([1, 2, 3], 100) is None
    assert two_pointers_opposite([], 0) is None


def test_template_same_direction():
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = two_pointers_same_direction(nums)
    assert k == 5
    assert nums[:k] == [0, 1, 2, 3, 4]
    assert two_pointers_same_direction([]) == 0


def test_two_sum_sorted():
    assert twoSum([2, 7, 11, 15], 9) == [1, 2]
    assert twoSum([2, 3, 4], 6) == [1, 3]
    assert twoSum([-1, 0], -1) == [1, 2]


def test_three_sum():
    assert sorted(threeSum([-1, 0, 1, 2, -1, -4])) == [[-1, -1, 2], [-1, 0, 1]]
    assert threeSum([0, 1, 1]) == []
    assert threeSum([0, 0, 0, 0]) == [[0, 0, 0]]


def test_max_area():
    assert maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert maxArea([1, 1]) == 1
