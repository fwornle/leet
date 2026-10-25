from patterns.breadth_first_search import (
    bfs_distances,
    bfs_levels,
    open_lock,
    oranges_rotting,
    shortest_path_binary_matrix,
)

GRAPH = {1: [2, 3], 2: [4, 5], 3: [6], 4: [], 5: [6], 6: []}


def test_bfs_distances():
    assert bfs_distances(GRAPH, 1) == {1: 0, 2: 1, 3: 1, 4: 2, 5: 2, 6: 2}


def test_bfs_levels():
    assert bfs_levels(GRAPH, 1) == [[1], [2, 3], [4, 5, 6]]
    assert bfs_levels({0: []}, 0) == [[0]]


def test_open_lock():
    assert open_lock(["0201", "0101", "0102", "1212", "2002"], "0202") == 6
    assert open_lock(["8888"], "0009") == 1
    assert open_lock(
        ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], "8888"
    ) == -1
    assert open_lock(["0000"], "8888") == -1
    assert open_lock([], "0000") == 0


def test_oranges_rotting():
    assert oranges_rotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4
    assert oranges_rotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1
    assert oranges_rotting([[0, 2]]) == 0
    assert oranges_rotting([[0]]) == 0


def test_shortest_path_binary_matrix():
    assert shortest_path_binary_matrix([[0, 1], [1, 0]]) == 2
    assert shortest_path_binary_matrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]) == 4
    assert shortest_path_binary_matrix([[1, 0, 0], [1, 1, 0], [1, 1, 0]]) == -1
    assert shortest_path_binary_matrix([[0]]) == 1
