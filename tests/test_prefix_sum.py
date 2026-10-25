from patterns.prefix_sum import (
    NumArray,
    build_prefix,
    find_max_length,
    range_sum,
    subarray_sum,
)


def test_build_prefix_and_range_sum():
    nums = [2, 4, 1, 3, 5]
    prefix = build_prefix(nums)
    assert prefix == [0, 2, 6, 7, 10, 15]
    assert range_sum(prefix, 1, 3) == 8
    assert range_sum(prefix, 0, 4) == 15


def test_num_array():
    arr = NumArray([-2, 0, 3, -5, 2, -1])
    assert arr.sumRange(0, 2) == 1
    assert arr.sumRange(2, 5) == -1
    assert arr.sumRange(0, 5) == -3


def test_subarray_sum():
    assert subarray_sum([1, 1, 1], 2) == 2
    assert subarray_sum([1, 2, 3], 3) == 2
    assert subarray_sum([1, -1, 0], 0) == 3


def test_find_max_length():
    assert find_max_length([0, 1]) == 2
    assert find_max_length([0, 1, 0]) == 2
    assert find_max_length([0, 0, 1, 0, 0, 0, 1, 1]) == 6
