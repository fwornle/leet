"""Pattern 3 · Sliding Window.

Sections between `--8<-- [start:x]` / `[end:x]` markers are embedded
into docs/patterns/sliding-window.md, so every snippet shown there is tested.
"""

from collections import Counter


# --8<-- [start:template]
def fixed_window_max_sum(nums: list[int], k: int) -> int:
    """Max sum of any window of exactly k elements."""
    window = sum(nums[:k])
    best = window
    for right in range(k, len(nums)):
        window += nums[right] - nums[right - k]  # add the new one, drop the oldest
        best = max(best, window)
    return best


def variable_window_longest(nums: list[int], limit: int) -> int:
    """Longest window with sum <= limit (non-negative nums)."""
    left = window = best = 0
    for right, x in enumerate(nums):
        window += x                    # 1. expand: take nums[right]
        while window > limit:          # 2. shrink until valid again
            window -= nums[left]
            left += 1
        best = max(best, right - left + 1)  # 3. record the valid window
    return best
# --8<-- [end:template]


# --8<-- [start:max_average]
def findMaxAverage(nums: list[int], k: int) -> float:  # LeetCode 643
    window = sum(nums[:k])
    best = window
    for right in range(k, len(nums)):
        window += nums[right] - nums[right - k]
        best = max(best, window)
    return best / k
# --8<-- [end:max_average]


# --8<-- [start:longest_unique]
def lengthOfLongestSubstring(s: str) -> int:  # LeetCode 3
    last_seen: dict[str, int] = {}
    left = best = 0
    for right, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1  # jump past the earlier copy
        last_seen[ch] = right
        best = max(best, right - left + 1)
    return best
# --8<-- [end:longest_unique]


# --8<-- [start:min_window]
def minWindow(s: str, t: str) -> str:  # LeetCode 76
    need = Counter(t)
    missing = len(t)          # chars of t still not covered
    left = 0
    best = (0, float("inf"))  # (start, end) of best window
    for right, ch in enumerate(s):
        if need[ch] > 0:
            missing -= 1
        need[ch] -= 1
        while missing == 0:   # valid: try to shrink from the left
            if right - left < best[1] - best[0]:
                best = (left, right)
            need[s[left]] += 1
            if need[s[left]] > 0:
                missing += 1  # we just dropped a needed char
            left += 1
    start, end = best
    return "" if end == float("inf") else s[start:end + 1]
# --8<-- [end:min_window]
