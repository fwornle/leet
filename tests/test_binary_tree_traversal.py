from patterns.binary_tree_traversal import (
    inorder,
    inorder_traversal,
    kth_smallest,
    level_order,
    max_depth,
    postorder,
    preorder,
)
from patterns.structures import tree_from

#        1
#      /   \
#     2     3
#    / \     \
#   4   5     6
SAMPLE = [1, 2, 3, 4, 5, None, 6]


def test_recursive_orders():
    root = tree_from(SAMPLE)
    assert preorder(root) == [1, 2, 4, 5, 3, 6]
    assert inorder(root) == [4, 2, 5, 1, 3, 6]
    assert postorder(root) == [4, 5, 2, 6, 3, 1]
    assert preorder(None) == []


def test_inorder_iterative():
    assert inorder_traversal(tree_from(SAMPLE)) == [4, 2, 5, 1, 3, 6]
    assert inorder_traversal(tree_from([1, None, 2, 3])) == [1, 3, 2]
    assert inorder_traversal(None) == []


def test_level_order():
    assert level_order(tree_from([3, 9, 20, None, None, 15, 7])) == [[3], [9, 20], [15, 7]]
    assert level_order(tree_from([1])) == [[1]]
    assert level_order(None) == []


def test_max_depth():
    assert max_depth(tree_from([3, 9, 20, None, None, 15, 7])) == 3
    assert max_depth(tree_from([1, None, 2])) == 2
    assert max_depth(None) == 0


def test_kth_smallest():
    assert kth_smallest(tree_from([3, 1, 4, None, 2]), 1) == 1
    assert kth_smallest(tree_from([5, 3, 6, 2, 4, None, None, 1]), 3) == 3
