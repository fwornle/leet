"""Pattern 2 · Two Pointers.

Sections between `--8<-- [start:x]` / `[end:x]` markers are embedded
into docs/patterns/two-pointers.md, so every snippet shown there is tested.
"""


# --8<-- [start:template]
def two_pointers_opposite(nums: list[int], target: int) -> tuple[int, int] | None:
    """Sorted input: find i < j with nums[i] + nums[j] == target."""
    left, right = 0, len(nums) - 1
    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            return left, right
        if s < target:
            left += 1   # need a bigger sum -> move the small end up
        else:
            right -= 1  # need a smaller sum -> move the big end down
    return None


def two_pointers_same_direction(nums: list[int]) -> int:
    """Sorted input: remove duplicates in place, return new length (LeetCode 26)."""
    write = 0                      # slow: next slot to keep
    for read in range(len(nums)):  # fast: scans everything
        if read == 0 or nums[read] != nums[read - 1]:
            nums[write] = nums[read]
            write += 1
    return write
# --8<-- [end:template]


# --8<-- [start:two_sum_sorted]
def twoSum(numbers: list[int], target: int) -> list[int]:  # LeetCode 167
    left, right = 0, len(numbers) - 1
    while left < right:
        s = numbers[left] + numbers[right]
        if s == target:
            return [left + 1, right + 1]  # 1-indexed answer
        if s < target:
            left += 1
        else:
            right -= 1
    return []
# --8<-- [end:two_sum_sorted]


# --8<-- [start:three_sum]
def threeSum(nums: list[int]) -> list[list[int]]:  # LeetCode 15
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # skip duplicate anchors
        left, right = i + 1, len(nums) - 1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s < 0:
                left += 1
            elif s > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1  # skip duplicate second values
    return result
# --8<-- [end:three_sum]


# --8<-- [start:container_water]
def maxArea(height: list[int]) -> int:  # LeetCode 11
    left, right = 0, len(height) - 1
    best = 0
    while left < right:
        width = right - left
        best = max(best, width * min(height[left], height[right]))
        # The shorter wall limits the area; moving the taller one can't help.
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return best
# --8<-- [end:container_water]
