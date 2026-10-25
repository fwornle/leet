from patterns.linked_list_reversal import reverse, reverseBetween, reverseList, swapPairs
from patterns.structures import list_from, to_list


def test_template_and_206():
    for fn in (reverse, reverseList):
        assert to_list(fn(list_from([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]
        assert to_list(fn(list_from([1, 2]))) == [2, 1]
        assert fn(None) is None


def test_reverse_between():
    assert to_list(reverseBetween(list_from([1, 2, 3, 4, 5]), 2, 4)) == [1, 4, 3, 2, 5]
    assert to_list(reverseBetween(list_from([5]), 1, 1)) == [5]
    assert to_list(reverseBetween(list_from([3, 5]), 1, 2)) == [5, 3]


def test_swap_pairs():
    assert to_list(swapPairs(list_from([1, 2, 3, 4]))) == [2, 1, 4, 3]
    assert to_list(swapPairs(list_from([1, 2, 3]))) == [2, 1, 3]
    assert to_list(swapPairs(list_from([1]))) == [1]
    assert swapPairs(None) is None
