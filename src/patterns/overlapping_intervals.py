"""Pattern 8 · Overlapping Intervals.

Sections between `--8<-- [start:x]` / `[end:x]` markers are embedded
into docs/patterns/overlapping-intervals.md, so every snippet shown there is tested.
"""


# --8<-- [start:template]
def merge(intervals: list[list[int]]) -> list[list[int]]:  # LeetCode 56
    intervals.sort(key=lambda iv: iv[0])  # 1. sort by start
    merged: list[list[int]] = []
    for start, end in intervals:
        if merged and start <= merged[-1][1]:  # 2. overlaps the last one?
            merged[-1][1] = max(merged[-1][1], end)  #    extend it
        else:
            merged.append([start, end])  # 3. otherwise start a new block
    return merged
# --8<-- [end:template]


# --8<-- [start:insert_interval]
def insert(intervals: list[list[int]], new: list[int]) -> list[list[int]]:  # LeetCode 57
    out: list[list[int]] = []
    i, n = 0, len(intervals)
    while i < n and intervals[i][1] < new[0]:  # entirely before `new`
        out.append(intervals[i])
        i += 1
    start, end = new
    while i < n and intervals[i][0] <= end:  # overlapping: absorb into `new`
        start = min(start, intervals[i][0])
        end = max(end, intervals[i][1])
        i += 1
    out.append([start, end])
    out.extend(intervals[i:])  # entirely after
    return out
# --8<-- [end:insert_interval]


# --8<-- [start:non_overlapping]
def erase_overlap_intervals(intervals: list[list[int]]) -> int:  # LeetCode 435
    intervals.sort(key=lambda iv: iv[1])  # sort by END: greedy keeps earliest finisher
    removed = 0
    prev_end = float("-inf")
    for start, end in intervals:
        if start >= prev_end:  # fits after the last kept one
            prev_end = end
        else:
            removed += 1  # overlaps: drop it (it ends later)
    return removed
# --8<-- [end:non_overlapping]
