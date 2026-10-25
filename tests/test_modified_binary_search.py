import bisect

from patterns.modified_binary_search import lower_bound, min_eating_speed, search, search_rotated


def test_lower_bound_matches_bisect():
    nums = [1, 3, 3, 5, 8]
    for target in range(0, 10):
        got = lower_bound(0, len(nums) - 1, lambda i: nums[i] >= target)
        assert got == bisect.bisect_left(nums, target)


def test_search():
    assert search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert search([-1, 0, 3, 5, 9, 12], 2) == -1
    assert search([5], 5) == 0
    assert search([], 1) == -1


def test_search_rotated():
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert search_rotated([1], 0) == -1
    assert search_rotated([3, 1], 1) == 1
    assert search_rotated([5, 1, 3], 5) == 0


def test_min_eating_speed():
    assert min_eating_speed([3, 6, 7, 11], 8) == 4
    assert min_eating_speed([30, 11, 23, 4, 20], 5) == 30
    assert min_eating_speed([30, 11, 23, 4, 20], 6) == 23
