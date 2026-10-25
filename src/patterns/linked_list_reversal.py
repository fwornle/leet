"""Pattern 5 · Linked List In-place Reversal.

Sections between `--8<-- [start:x]` / `[end:x]` markers are embedded
into docs/patterns/linked-list-reversal.md, so every snippet shown there is tested.
"""

from __future__ import annotations

from patterns.structures import ListNode


# --8<-- [start:template]
def reverse(head: ListNode | None) -> ListNode | None:
    prev, curr = None, head
    while curr:
        nxt = curr.next   # 1. save the rest of the list
        curr.next = prev  # 2. flip the arrow
        prev = curr       # 3. advance prev
        curr = nxt        # 4. advance curr
    return prev           # prev is the new head
# --8<-- [end:template]


# --8<-- [start:reverse_list]
def reverseList(head: ListNode | None) -> ListNode | None:  # LeetCode 206
    prev, curr = None, head
    while curr:
        curr.next, prev, curr = prev, curr, curr.next
    return prev
# --8<-- [end:reverse_list]


# --8<-- [start:reverse_between]
def reverseBetween(head: ListNode | None, left: int, right: int) -> ListNode | None:  # LeetCode 92
    dummy = ListNode(0, head)
    before = dummy
    for _ in range(left - 1):        # walk to the node just before position `left`
        before = before.next
    prev, curr = None, before.next
    for _ in range(right - left + 1):  # reverse exactly the sublist
        nxt = curr.next
        curr.next = prev
        prev, curr = curr, nxt
    tail = before.next               # old first node is now the sublist's tail
    before.next = prev               # reconnect front -> reversed head
    tail.next = curr                 # reconnect reversed tail -> rest
    return dummy.next
# --8<-- [end:reverse_between]


# --8<-- [start:swap_pairs]
def swapPairs(head: ListNode | None) -> ListNode | None:  # LeetCode 24
    dummy = ListNode(0, head)
    prev = dummy
    while prev.next and prev.next.next:
        a, b = prev.next, prev.next.next
        a.next = b.next   # a skips over b
        b.next = a        # b points back to a
        prev.next = b     # front now points at b
        prev = a          # a is the tail of this pair
    return dummy.next
# --8<-- [end:swap_pairs]
