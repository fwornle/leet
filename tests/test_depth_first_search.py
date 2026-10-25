from patterns.depth_first_search import (
    Node,
    can_finish,
    clone_graph,
    dfs_iterative,
    dfs_recursive,
    find_circle_num,
)

GRAPH = {1: [2, 3], 2: [4, 5], 3: [6], 4: [], 5: [6], 6: []}


def test_dfs_orders_match():
    assert dfs_recursive(GRAPH, 1) == [1, 2, 4, 5, 6, 3]
    assert dfs_iterative(GRAPH, 1) == [1, 2, 4, 5, 6, 3]


def test_dfs_handles_cycles():
    cyclic = {0: [1], 1: [2], 2: [0]}
    assert dfs_recursive(cyclic, 0) == [0, 1, 2]
    assert dfs_iterative(cyclic, 0) == [0, 1, 2]


def test_clone_graph():
    # LeetCode example: 1-2, 1-4, 2-3, 3-4
    n1, n2, n3, n4 = Node(1), Node(2), Node(3), Node(4)
    n1.neighbors = [n2, n4]
    n2.neighbors = [n1, n3]
    n3.neighbors = [n2, n4]
    n4.neighbors = [n1, n3]
    c1 = clone_graph(n1)
    assert c1 is not n1 and c1.val == 1
    assert [n.val for n in c1.neighbors] == [2, 4]
    c2 = c1.neighbors[0]
    assert c2 is not n2
    assert c2.neighbors[0] is c1  # cycle preserved inside the copy
    assert clone_graph(None) is None


def test_find_circle_num():
    assert find_circle_num([[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2
    assert find_circle_num([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 3
    assert find_circle_num([[1]]) == 1


def test_can_finish():
    assert can_finish(2, [[1, 0]]) is True
    assert can_finish(2, [[1, 0], [0, 1]]) is False
    assert can_finish(4, [[1, 0], [2, 1], [3, 2]]) is True
    assert can_finish(3, [[0, 1], [1, 2], [2, 0]]) is False
    assert can_finish(1, []) is True
