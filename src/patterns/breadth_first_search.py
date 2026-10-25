"""Pattern 12 · Breadth-First Search (graphs).

Sections between `--8<-- [start:x]` / `[end:x]` markers are embedded
into docs/patterns/breadth-first-search.md, so every snippet shown there is tested.
"""

from collections import deque


# --8<-- [start:template]
def bfs_distances(graph: dict[int, list[int]], start: int) -> dict[int, int]:
    """Shortest number of edges from start to every reachable node."""
    dist = {start: 0}              # doubles as "visited"
    queue = deque([start])
    while queue:
        node = queue.popleft()     # FIFO -> nearest nodes first
        for nxt in graph.get(node, []):
            if nxt not in dist:    # mark when ENQUEUED, not when popped
                dist[nxt] = dist[node] + 1
                queue.append(nxt)
    return dist
# --8<-- [end:template]


# --8<-- [start:template_levels]
def bfs_levels(graph: dict[int, list[int]], start: int) -> list[list[int]]:
    """Same walk, but process one whole ring (level) at a time."""
    seen = {start}
    queue = deque([start])
    levels = []
    while queue:
        ring = []
        for _ in range(len(queue)):   # freeze the size: exactly this ring
            node = queue.popleft()
            ring.append(node)
            for nxt in graph.get(node, []):
                if nxt not in seen:
                    seen.add(nxt)
                    queue.append(nxt)
        levels.append(ring)
    return levels
# --8<-- [end:template_levels]


# --8<-- [start:open_the_lock]
def open_lock(deadends: list[str], target: str) -> int:  # LeetCode 752
    dead = set(deadends)
    if "0000" in dead:
        return -1
    seen = {"0000"}
    queue = deque([("0000", 0)])
    while queue:
        state, turns = queue.popleft()
        if state == target:
            return turns               # first time we reach it = fewest turns
        for i in range(4):
            d = int(state[i])
            for step in (1, -1):
                nxt = state[:i] + str((d + step) % 10) + state[i + 1:]
                if nxt not in seen and nxt not in dead:
                    seen.add(nxt)
                    queue.append((nxt, turns + 1))
    return -1
# --8<-- [end:open_the_lock]


# --8<-- [start:rotting_oranges]
def oranges_rotting(grid: list[list[int]]) -> int:  # LeetCode 994
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c))   # multi-source: ALL rotten start at minute 0
            elif grid[r][c] == 1:
                fresh += 1

    minutes = 0
    while queue and fresh:
        for _ in range(len(queue)):    # one level = one minute
            r, c = queue.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc))
        minutes += 1
    return minutes if fresh == 0 else -1
# --8<-- [end:rotting_oranges]


# --8<-- [start:shortest_path_binary_matrix]
def shortest_path_binary_matrix(grid: list[list[int]]) -> int:  # LeetCode 1091
    n = len(grid)
    if grid[0][0] or grid[n - 1][n - 1]:
        return -1
    queue = deque([(0, 0, 1)])         # (row, col, path length in cells)
    grid[0][0] = 1                     # mark visited in place
    while queue:
        r, c, length = queue.popleft()
        if (r, c) == (n - 1, n - 1):
            return length
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):      # 8 directions
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    grid[nr][nc] = 1
                    queue.append((nr, nc, length + 1))
    return -1
# --8<-- [end:shortest_path_binary_matrix]
