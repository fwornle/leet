from patterns.sliding_window import (
    findMaxAverage,
    fixed_window_max_sum,
    lengthOfLongestSubstring,
    minWindow,
    variable_window_longest,
)


def test_fixed_window():
    assert fixed_window_max_sum([2, 1, 5, 1, 3, 2], 3) == 9
    assert fixed_window_max_sum([4], 1) == 4


def test_variable_window():
    assert variable_window_longest([3, 1, 2, 7, 4, 2, 1, 1, 5], 8) == 4
    assert variable_window_longest([10, 10], 5) == 0
    assert variable_window_longest([], 5) == 0


def test_max_average():
    assert findMaxAverage([1, 12, -5, -6, 50, 3], 4) == 12.75
    assert findMaxAverage([5], 1) == 5.0


def test_longest_unique():
    assert lengthOfLongestSubstring("abcabcbb") == 3
    assert lengthOfLongestSubstring("bbbbb") == 1
    assert lengthOfLongestSubstring("pwwkew") == 3
    assert lengthOfLongestSubstring("") == 0
    assert lengthOfLongestSubstring("abba") == 2


def test_min_window():
    assert minWindow("ADOBECODEBANC", "ABC") == "BANC"
    assert minWindow("a", "a") == "a"
    assert minWindow("a", "aa") == ""
