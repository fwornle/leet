"""Pattern 4 · Fast & Slow Pointers (Floyd's tortoise and hare).

Sections between `--8<-- [start:x]` / `[end:x]` markers are embedded
into docs/patterns/fast-slow-pointers.md, so every snippet shown there is tested.
"""

from __future__ import annotations

from patterns.structures import ListNode


# --8<-- [start:template]
def has_cycle(head: ListNode | None) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next          # 1 step
        fast = fast.next.next     # 2 steps
        if slow is fast:          # fast lapped slow -> there is a loop
            return True
    return False                  # fast fell off the end -> no loop
# --8<-- [end:template]


# --8<-- [start:linked_list_cycle]
def hasCycle(head: ListNode | None) -> bool:  # LeetCode 141
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False
# --8<-- [end:linked_list_cycle]


# --8<-- [start:middle_node]
def middleNode(head: ListNode | None) -> ListNode | None:  # LeetCode 876
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow  # fast went 2x as far -> slow is halfway
# --8<-- [end:middle_node]


# --8<-- [start:find_duplicate]
def findDuplicate(nums: list[int]) -> int:  # LeetCode 287
    # Treat i -> nums[i] as a linked list; the duplicate is the cycle entrance.
    slow = fast = nums[0]
    while True:                     # phase 1: meet somewhere inside the cycle
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    slow = nums[0]                  # phase 2: restart one pointer from the head
    while slow != fast:             # both at speed 1 -> they meet at the entrance
        slow = nums[slow]
        fast = nums[fast]
    return slow
# --8<-- [end:find_duplicate]


# --8<-- [start:happy_number]
def isHappy(n: int) -> bool:  # LeetCode 202
    def step(x: int) -> int:
        return sum(int(d) ** 2 for d in str(x))

    slow, fast = n, step(n)
    while fast != 1 and slow != fast:
        slow = step(slow)
        fast = step(step(fast))
    return fast == 1
# --8<-- [end:happy_number]
