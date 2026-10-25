from patterns.fast_slow_pointers import (
    findDuplicate,
    hasCycle,
    has_cycle,
    isHappy,
    middleNode,
)
from patterns.structures import list_from, to_list


def make_cycle(values: list[int], pos: int):
    """Build a list whose tail links back to index `pos` (-1 = no cycle)."""
    head = list_from(values)
    if pos < 0 or head is None:
        return head
    entry, tail, i = None, head, 0
    node = head
    while node:
        if i == pos:
            entry = node
        tail = node
        node = node.next
        i += 1
    tail.next = entry
    return head


def test_template_and_141():
    for fn in (has_cycle, hasCycle):
        assert fn(make_cycle([3, 2, 0, -4], 1)) is True
        assert fn(make_cycle([1, 2], 0)) is True
        assert fn(make_cycle([1], -1)) is False
        assert fn(None) is False


def test_middle_node():
    assert to_list(middleNode(list_from([1, 2, 3, 4, 5]))) == [3, 4, 5]
    assert to_list(middleNode(list_from([1, 2, 3, 4, 5, 6]))) == [4, 5, 6]
    assert middleNode(None) is None


def test_find_duplicate():
    assert findDuplicate([1, 3, 4, 2, 2]) == 2
    assert findDuplicate([3, 1, 3, 4, 2]) == 3
    assert findDuplicate([3, 3, 3, 3, 3]) == 3


def test_happy_number():
    assert isHappy(19) is True
    assert isHappy(2) is False
    assert isHappy(1) is True
