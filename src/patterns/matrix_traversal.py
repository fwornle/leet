"""Pattern 13 · Matrix Traversal.

Sections between `--8<-- [start:x]` / `[end:x]` markers are embedded
into docs/patterns/matrix-traversal.md, so every snippet shown there is tested.
"""


# --8<-- [start:template]
DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))  # down, up, right, left


def flood(grid: list[list[str]], r: int, c: int, target: str, mark: str) -> None:
    """Grid = graph: each cell is a node, its 4 neighbours are its edges."""
    rows, cols = len(grid), len(grid[0])
    if not (0 <= r < rows and 0 <= c < cols):   # 1. in bounds?
        return
    if grid[r][c] != target:                     # 2. right kind of cell / not visited?
        return
    grid[r][c] = mark                            # 3. mark visited (in place)
    for dr, dc in DIRS:                          # 4. recurse into neighbours
        flood(grid, r + dr, c + dc, target, mark)
# --8<-- [end:template]


# --8<-- [start:number_of_islands]
def num_islands(grid: list[list[str]]) -> int:  # LeetCode 200
    rows, cols = len(grid), len(grid[0])

    def sink(r: int, c: int) -> None:
        if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] != "1":
            return
        grid[r][c] = "0"               # sink the land -> it is never counted again
        for dr, dc in DIRS:
            sink(r + dr, c + dc)

    islands = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":      # unvisited land = a brand-new island
                islands += 1
                sink(r, c)
    return islands
# --8<-- [end:number_of_islands]


# --8<-- [start:flood_fill]
def flood_fill(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:  # LeetCode 733
    original = image[sr][sc]
    if original == color:              # nothing to do (and avoids infinite recursion)
        return image
    rows, cols = len(image), len(image[0])

    def paint(r: int, c: int) -> None:
        if not (0 <= r < rows and 0 <= c < cols) or image[r][c] != original:
            return
        image[r][c] = color
        for dr, dc in DIRS:
            paint(r + dr, c + dc)

    paint(sr, sc)
    return image
# --8<-- [end:flood_fill]


# --8<-- [start:spiral_matrix]
def spiral_order(matrix: list[list[int]]) -> list[int]:  # LeetCode 54
    out = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    while top <= bottom and left <= right:
        for c in range(left, right + 1):           # → along the top row
            out.append(matrix[top][c])
        top += 1
        for r in range(top, bottom + 1):           # ↓ down the right column
            out.append(matrix[r][right])
        right -= 1
        if top <= bottom:
            for c in range(right, left - 1, -1):   # ← along the bottom row
                out.append(matrix[bottom][c])
            bottom -= 1
        if left <= right:
            for r in range(bottom, top - 1, -1):   # ↑ up the left column
                out.append(matrix[r][left])
            left += 1
    return out
# --8<-- [end:spiral_matrix]


# --8<-- [start:rotate_image]
def rotate(matrix: list[list[int]]) -> None:  # LeetCode 48
    n = len(matrix)
    for r in range(n):                 # 1. transpose: swap across the main diagonal
        for c in range(r + 1, n):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
    for row in matrix:                 # 2. mirror each row
        row.reverse()
# --8<-- [end:rotate_image]
