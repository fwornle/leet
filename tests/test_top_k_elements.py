from patterns.top_k_elements import (
    find_kth_largest,
    k_closest,
    top_k_frequent,
    top_k_frequent_bucket,
    top_k_largest,
)


def test_top_k_largest():
    assert sorted(top_k_largest([3, 1, 5, 12, 2, 11], 3)) == [5, 11, 12]
    assert top_k_largest([7], 1) == [7]


def test_find_kth_largest():
    assert find_kth_largest([3, 2, 1, 5, 6, 4], 2) == 5
    assert find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    assert find_kth_largest([1], 1) == 1


def test_top_k_frequent():
    assert sorted(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    assert top_k_frequent([1], 1) == [1]
    assert sorted(top_k_frequent_bucket([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    assert top_k_frequent_bucket([4, 4, 5], 1) == [4]


def test_k_closest():
    assert k_closest([[1, 3], [-2, 2]], 1) == [[-2, 2]]
    assert sorted(k_closest([[3, 3], [5, -1], [-2, 4]], 2)) == [[-2, 4], [3, 3]]
