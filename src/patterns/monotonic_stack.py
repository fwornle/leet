"""Pattern 6 · Monotonic Stack.

Sections between `--8<-- [start:x]` / `[end:x]` markers are embedded
into docs/patterns/monotonic-stack.md, so every snippet shown there is tested.
"""


# --8<-- [start:template]
def next_greater(nums: list[int]) -> list[int]:
    """For each element, the next element to its right that is larger (-1 if none)."""
    result = [-1] * len(nums)
    stack: list[int] = []  # indices; their values are decreasing bottom -> top
    for i, x in enumerate(nums):
        while stack and nums[stack[-1]] < x:  # x is the answer for everyone smaller
            result[stack.pop()] = x
        stack.append(i)                       # x waits for its own answer
    return result
# --8<-- [end:template]


# --8<-- [start:daily_temperatures]
def dailyTemperatures(temperatures: list[int]) -> list[int]:  # LeetCode 739
    answer = [0] * len(temperatures)
    stack: list[int] = []  # indices of days still waiting for a warmer day
    for i, t in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < t:
            j = stack.pop()
            answer[j] = i - j  # days waited
        stack.append(i)
    return answer
# --8<-- [end:daily_temperatures]


# --8<-- [start:next_greater_element]
def nextGreaterElement(nums1: list[int], nums2: list[int]) -> list[int]:  # LeetCode 496
    greater: dict[int, int] = {}
    stack: list[int] = []  # values (all distinct), decreasing
    for x in nums2:
        while stack and stack[-1] < x:
            greater[stack.pop()] = x
        stack.append(x)
    return [greater.get(x, -1) for x in nums1]
# --8<-- [end:next_greater_element]


# --8<-- [start:largest_rectangle]
def largestRectangleArea(heights: list[int]) -> int:  # LeetCode 84
    stack: list[int] = []  # indices with increasing heights
    best = 0
    for i, h in enumerate(heights + [0]):  # sentinel 0 flushes the stack at the end
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            left = stack[-1] + 1 if stack else 0  # first bar >= height on the left
            best = max(best, height * (i - left))  # i is the first shorter bar on the right
        stack.append(i)
    return best
# --8<-- [end:largest_rectangle]
