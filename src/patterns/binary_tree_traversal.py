"""Pattern 10 · Binary Tree Traversal.

Sections between `--8<-- [start:x]` / `[end:x]` markers are embedded
into docs/patterns/binary-tree-traversal.md, so every snippet shown there is tested.
"""

from __future__ import annotations

from collections import deque

from patterns.structures import TreeNode


# --8<-- [start:recursive]
def preorder(root: TreeNode | None) -> list[int]:  # node, left, right
    return [root.val] + preorder(root.left) + preorder(root.right) if root else []


def inorder(root: TreeNode | None) -> list[int]:  # left, node, right
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []


def postorder(root: TreeNode | None) -> list[int]:  # left, right, node
    return postorder(root.left) + postorder(root.right) + [root.val] if root else []
# --8<-- [end:recursive]


# --8<-- [start:inorder_iterative]
def inorder_traversal(root: TreeNode | None) -> list[int]:  # LeetCode 94
    out: list[int] = []
    stack: list[TreeNode] = []
    node = root
    while node or stack:
        while node:  # dive left, remembering the path
            stack.append(node)
            node = node.left
        node = stack.pop()  # leftmost unvisited node
        out.append(node.val)
        node = node.right  # then explore its right subtree
    return out
# --8<-- [end:inorder_iterative]


# --8<-- [start:level_order]
def level_order(root: TreeNode | None) -> list[list[int]]:  # LeetCode 102
    if not root:
        return []
    levels: list[list[int]] = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):  # exactly the nodes of this level
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        levels.append(level)
    return levels
# --8<-- [end:level_order]


# --8<-- [start:max_depth]
def max_depth(root: TreeNode | None) -> int:  # LeetCode 104
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))  # postorder: children first
# --8<-- [end:max_depth]


# --8<-- [start:kth_smallest]
def kth_smallest(root: TreeNode | None, k: int) -> int:  # LeetCode 230
    stack: list[TreeNode] = []
    node = root
    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        k -= 1
        if k == 0:  # inorder of a BST is sorted: the k-th visit is the answer
            return node.val
        node = node.right
    raise ValueError("k is larger than the tree")
# --8<-- [end:kth_smallest]
