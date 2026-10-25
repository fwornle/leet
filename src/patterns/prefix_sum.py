"""Pattern 1 · Prefix Sum.

Sections between `--8<-- [start:x]` / `[end:x]` markers are embedded
into docs/patterns/prefix-sum.md, so every snippet shown there is tested.
"""

from collections import defaultdict


# --8<-- [start:template]
def build_prefix(nums: list[int]) -> list[int]:
    """prefix[i] = sum(nums[:i]); prefix has len(nums) + 1 entries."""
    prefix = [0] * (len(nums) + 1)
    for i, x in enumerate(nums):
        prefix[i + 1] = prefix[i] + x
    return prefix


def range_sum(prefix: list[int], i: int, j: int) -> int:
    """Sum of nums[i..j] inclusive, in O(1)."""
    return prefix[j + 1] - prefix[i]
# --8<-- [end:template]


# --8<-- [start:range_sum_query]
class NumArray:  # LeetCode 303
    def __init__(self, nums: list[int]):
        self.prefix = build_prefix(nums)  # O(n) once

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]  # O(1) per query
# --8<-- [end:range_sum_query]


# --8<-- [start:subarray_sum_k]
def subarray_sum(nums: list[int], k: int) -> int:  # LeetCode 560
    seen = defaultdict(int)
    seen[0] = 1  # the empty prefix
    running = count = 0
    for x in nums:
        running += x
        count += seen[running - k]  # earlier prefixes that leave exactly k
        seen[running] += 1
    return count
# --8<-- [end:subarray_sum_k]


# --8<-- [start:contiguous_array]
def find_max_length(nums: list[int]) -> int:  # LeetCode 525
    first_seen = {0: -1}  # balance -> earliest index
    balance = best = 0
    for i, x in enumerate(nums):
        balance += 1 if x == 1 else -1
        if balance in first_seen:
            best = max(best, i - first_seen[balance])
        else:
            first_seen[balance] = i
    return best
# --8<-- [end:contiguous_array]
