"""Pattern 9 · Modified Binary Search.

Sections between `--8<-- [start:x]` / `[end:x]` markers are embedded
into docs/patterns/modified-binary-search.md, so every snippet shown there is tested.
"""

import math
from typing import Callable


# --8<-- [start:template]
def lower_bound(lo: int, hi: int, ok: Callable[[int], bool]) -> int:
    """Smallest x in [lo, hi] with ok(x) True, given ok is False...False True...True.
    Returns hi + 1 if ok is never True."""
    hi += 1  # search the half-open range [lo, hi)
    while lo < hi:
        mid = (lo + hi) // 2
        if ok(mid):
            hi = mid  # mid might be the answer: keep it
        else:
            lo = mid + 1  # mid is definitely not: discard it
    return lo
# --8<-- [end:template]


# --8<-- [start:binary_search]
def search(nums: list[int], target: int) -> int:  # LeetCode 704
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1  # target is in the right half
        else:
            hi = mid - 1  # target is in the left half
    return -1
# --8<-- [end:binary_search]


# --8<-- [start:rotated]
def search_rotated(nums: list[int], target: int) -> int:  # LeetCode 33
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[lo] <= nums[mid]:  # left half [lo..mid] is sorted
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:  # right half [mid..hi] is sorted
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1
# --8<-- [end:rotated]


# --8<-- [start:koko]
def min_eating_speed(piles: list[int], h: int) -> int:  # LeetCode 875
    def can_finish(speed: int) -> bool:  # monotone: faster always works if slower does
        return sum(math.ceil(p / speed) for p in piles) <= h

    return lower_bound(1, max(piles), can_finish)  # search the ANSWER space
# --8<-- [end:koko]
