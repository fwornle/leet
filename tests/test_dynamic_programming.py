from patterns.dynamic_programming import (
    climb_stairs,
    coin_change,
    fib_memo,
    fib_table,
    longest_common_subsequence,
    rob,
)


def test_fib():
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    assert [fib_memo(i) for i in range(10)] == expected
    assert [fib_table(i) for i in range(10)] == expected
    assert fib_memo(80) == fib_table(80) == 23416728348467685


def test_climb_stairs():
    assert climb_stairs(1) == 1
    assert climb_stairs(2) == 2
    assert climb_stairs(3) == 3
    assert climb_stairs(5) == 8
    assert climb_stairs(45) == 1836311903


def test_rob():
    assert rob([1, 2, 3, 1]) == 4
    assert rob([2, 7, 9, 3, 1]) == 12
    assert rob([5]) == 5
    assert rob([2, 1, 1, 2]) == 4


def test_coin_change():
    assert coin_change([1, 2, 5], 11) == 3
    assert coin_change([2], 3) == -1
    assert coin_change([1], 0) == 0
    assert coin_change([186, 419, 83, 408], 6249) == 20


def test_lcs():
    assert longest_common_subsequence("abcde", "ace") == 3
    assert longest_common_subsequence("abc", "abc") == 3
    assert longest_common_subsequence("abc", "def") == 0
