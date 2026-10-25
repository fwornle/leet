"""Pattern 14 · Backtracking.

Sections between `--8<-- [start:x]` / `[end:x]` markers are embedded
into docs/patterns/backtracking.md, so every snippet shown there is tested.
"""


# --8<-- [start:template]
def backtrack_template(choices: list[int]) -> list[list[int]]:
    results: list[list[int]] = []
    path: list[int] = []

    def backtrack(start: int) -> None:
        if is_solution(path):
            results.append(path[:])        # COPY: path keeps mutating
            return                         # (drop this return to keep extending)
        for i in range(start, len(choices)):
            if not is_valid(path, choices[i]):
                continue                   # PRUNE: skip a whole subtree
            path.append(choices[i])        # 1. choose
            backtrack(i + 1)               # 2. explore
            path.pop()                     # 3. un-choose

    def is_solution(p: list[int]) -> bool:
        return len(p) == 2                 # example goal: all pairs

    def is_valid(p: list[int], x: int) -> bool:
        return True                        # example: no constraint

    backtrack(0)
    return results
# --8<-- [end:template]


# --8<-- [start:subsets]
def subsets(nums: list[int]) -> list[list[int]]:  # LeetCode 78
    results: list[list[int]] = []
    path: list[int] = []

    def backtrack(start: int) -> None:
        results.append(path[:])        # every node in the tree is a valid subset
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1)           # i + 1: never reuse, never look back
            path.pop()

    backtrack(0)
    return results
# --8<-- [end:subsets]


# --8<-- [start:permutations]
def permute(nums: list[int]) -> list[list[int]]:  # LeetCode 46
    results: list[list[int]] = []
    path: list[int] = []
    used = [False] * len(nums)

    def backtrack() -> None:
        if len(path) == len(nums):     # only LEAVES are answers
            results.append(path[:])
            return
        for i in range(len(nums)):     # order matters -> always scan from 0
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            backtrack()
            path.pop()
            used[i] = False

    backtrack()
    return results
# --8<-- [end:permutations]


# --8<-- [start:combination_sum]
def combination_sum(candidates: list[int], target: int) -> list[list[int]]:  # LeetCode 39
    candidates = sorted(candidates)    # sorted -> we can stop early
    results: list[list[int]] = []
    path: list[int] = []

    def backtrack(start: int, remaining: int) -> None:
        if remaining == 0:
            results.append(path[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remaining:
                break                  # PRUNE: every later candidate is bigger too
            path.append(candidates[i])
            backtrack(i, remaining - candidates[i])   # i (not i + 1): reuse allowed
            path.pop()

    backtrack(0, target)
    return results
# --8<-- [end:combination_sum]
