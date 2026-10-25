"""Pattern 11 · Depth-First Search (graphs).

Sections between `--8<-- [start:x]` / `[end:x]` markers are embedded
into docs/patterns/depth-first-search.md, so every snippet shown there is tested.
"""

from __future__ import annotations


# --8<-- [start:template_recursive]
def dfs_recursive(graph: dict[int, list[int]], start: int) -> list[int]:
    """Return nodes in DFS visit order. graph = adjacency list."""
    visited: set[int] = set()
    order: list[int] = []

    def dfs(node: int) -> None:
        visited.add(node)          # mark on entry -> never visit twice
        order.append(node)
        for nxt in graph.get(node, []):
            if nxt not in visited:
                dfs(nxt)           # go deep before going wide

    dfs(start)
    return order
# --8<-- [end:template_recursive]


# --8<-- [start:template_iterative]
def dfs_iterative(graph: dict[int, list[int]], start: int) -> list[int]:
    visited: set[int] = set()
    order: list[int] = []
    stack = [start]                # explicit stack replaces the call stack
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        for nxt in reversed(graph.get(node, [])):  # reversed -> same order as recursion
            if nxt not in visited:
                stack.append(nxt)
    return order
# --8<-- [end:template_iterative]


# --8<-- [start:clone_graph]
class Node:
    def __init__(self, val: int = 0, neighbors: list[Node] | None = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node: Node | None) -> Node | None:  # LeetCode 133
    clones: dict[Node, Node] = {}  # original -> copy (doubles as "visited")

    def dfs(orig: Node) -> Node:
        if orig in clones:
            return clones[orig]
        copy = Node(orig.val)
        clones[orig] = copy            # register BEFORE recursing (handles cycles)
        copy.neighbors = [dfs(n) for n in orig.neighbors]
        return copy

    return dfs(node) if node else None
# --8<-- [end:clone_graph]


# --8<-- [start:number_of_provinces]
def find_circle_num(is_connected: list[list[int]]) -> int:  # LeetCode 547
    n = len(is_connected)
    visited = [False] * n

    def dfs(city: int) -> None:
        visited[city] = True
        for other in range(n):
            if is_connected[city][other] and not visited[other]:
                dfs(other)

    provinces = 0
    for city in range(n):
        if not visited[city]:      # every fresh DFS start = one new component
            dfs(city)
            provinces += 1
    return provinces
# --8<-- [end:number_of_provinces]


# --8<-- [start:course_schedule]
def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:  # LeetCode 207
    graph: list[list[int]] = [[] for _ in range(num_courses)]
    for course, pre in prerequisites:
        graph[pre].append(course)

    WHITE, GREY, BLACK = 0, 1, 2   # unvisited / on current path / finished
    colour = [WHITE] * num_courses

    def has_cycle(node: int) -> bool:
        colour[node] = GREY
        for nxt in graph[node]:
            if colour[nxt] == GREY:            # back edge -> cycle
                return True
            if colour[nxt] == WHITE and has_cycle(nxt):
                return True
        colour[node] = BLACK
        return False

    return not any(colour[c] == WHITE and has_cycle(c) for c in range(num_courses))
# --8<-- [end:course_schedule]
