"""Pattern 7 · Top-K Elements.

Sections between `--8<-- [start:x]` / `[end:x]` markers are embedded
into docs/patterns/top-k-elements.md, so every snippet shown there is tested.
"""

import heapq
from collections import Counter


# --8<-- [start:template]
def top_k_largest(nums: list[int], k: int) -> list[int]:
    """Keep a MIN-heap of size k: its root is the weakest of the current top k."""
    heap: list[int] = []
    for x in nums:
        heapq.heappush(heap, x)
        if len(heap) > k:
            heapq.heappop(heap)  # evict the smallest; the k largest survive
    return heap  # unordered; heap[0] is the k-th largest
# --8<-- [end:template]


# --8<-- [start:kth_largest]
def find_kth_largest(nums: list[int], k: int) -> int:  # LeetCode 215
    heap: list[int] = []
    for x in nums:
        heapq.heappush(heap, x)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]  # smallest of the k largest = k-th largest
# --8<-- [end:kth_largest]


# --8<-- [start:top_k_frequent]
def top_k_frequent(nums: list[int], k: int) -> list[int]:  # LeetCode 347
    counts = Counter(nums)
    heap: list[tuple[int, int]] = []  # (frequency, value)
    for value, freq in counts.items():
        heapq.heappush(heap, (freq, value))
        if len(heap) > k:
            heapq.heappop(heap)  # drop the least frequent
    return [value for _, value in heap]
# --8<-- [end:top_k_frequent]


# --8<-- [start:top_k_frequent_bucket]
def top_k_frequent_bucket(nums: list[int], k: int) -> list[int]:  # LeetCode 347, O(n)
    counts = Counter(nums)
    buckets: list[list[int]] = [[] for _ in range(len(nums) + 1)]  # index = frequency
    for value, freq in counts.items():
        buckets[freq].append(value)
    out: list[int] = []
    for freq in range(len(buckets) - 1, 0, -1):  # highest frequency first
        for value in buckets[freq]:
            out.append(value)
            if len(out) == k:
                return out
    return out
# --8<-- [end:top_k_frequent_bucket]


# --8<-- [start:k_closest]
def k_closest(points: list[list[int]], k: int) -> list[list[int]]:  # LeetCode 973
    heap: list[tuple[int, int, int]] = []  # (-distance, x, y): negate -> max-heap
    for x, y in points:
        heapq.heappush(heap, (-(x * x + y * y), x, y))
        if len(heap) > k:
            heapq.heappop(heap)  # evict the FARTHEST point
    return [[x, y] for _, x, y in heap]
# --8<-- [end:k_closest]
