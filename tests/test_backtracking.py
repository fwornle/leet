from patterns.backtracking import backtrack_template, combination_sum, permute, subsets


def _norm(lists):
    return sorted(sorted(x) for x in lists)


def test_template_pairs():
    assert backtrack_template([1, 2, 3]) == [[1, 2], [1, 3], [2, 3]]


def test_subsets():
    assert _norm(subsets([1, 2, 3])) == _norm(
        [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    )
    assert subsets([0]) == [[], [0]]
    assert len(subsets([1, 2, 3, 4])) == 16


def test_permute():
    assert sorted(permute([1, 2, 3])) == sorted(
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    )
    assert permute([1]) == [[1]]
    assert len(permute([1, 2, 3, 4])) == 24


def test_combination_sum():
    assert _norm(combination_sum([2, 3, 6, 7], 7)) == _norm([[2, 2, 3], [7]])
    assert _norm(combination_sum([2, 3, 5], 8)) == _norm([[2, 2, 2, 2], [2, 3, 3], [3, 5]])
    assert combination_sum([2], 1) == []
