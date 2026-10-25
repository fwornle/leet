from patterns.matrix_traversal import flood, flood_fill, num_islands, rotate, spiral_order


def test_flood_template():
    grid = [list("110"), list("100"), list("001")]
    flood(grid, 0, 0, "1", "x")
    assert grid == [list("xx0"), list("x00"), list("001")]


def test_num_islands():
    grid = [
        list("11110"),
        list("11010"),
        list("11000"),
        list("00000"),
    ]
    assert num_islands(grid) == 1
    grid = [
        list("11000"),
        list("11000"),
        list("00100"),
        list("00011"),
    ]
    assert num_islands(grid) == 3
    assert num_islands([["0"]]) == 0


def test_flood_fill():
    assert flood_fill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2) == [
        [2, 2, 2],
        [2, 2, 0],
        [2, 0, 1],
    ]
    assert flood_fill([[0, 0, 0], [0, 0, 0]], 0, 0, 0) == [[0, 0, 0], [0, 0, 0]]


def test_spiral_order():
    assert spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert spiral_order([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [
        1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7,
    ]
    assert spiral_order([[1], [2], [3]]) == [1, 2, 3]
    assert spiral_order([[7]]) == [7]


def test_rotate():
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate(m)
    assert m == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    m = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    rotate(m)
    assert m == [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
