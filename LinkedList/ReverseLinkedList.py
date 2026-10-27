"""
LeetCode 206: Reverse Linked List
LeetCode 92: Reverse Linked List II

FAANG Patterns:
1. 3-Pointer Iteration (prev, curr, nxt)
2. In-Place Head-Insertion for Subsegment Reversal
"""

from typing import Optional, List

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

    @staticmethod
    def from_list(values: List[int]) -> Optional['ListNode']:
        dummy = ListNode(0)
        curr = dummy
        for v in values:
            curr.next = ListNode(v)
            curr = curr.next
        return dummy.next

    def to_list(self) -> List[int]:
        res = []
        curr = self
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    LeetCode 206: Reverse Linked List
    Time: O(N), Space: O(1)
    """
    prev = None
    curr = head

    while curr is not None:
        next_node = curr.next  # 1. Save the lifeline
        curr.next = prev       # 2. Flip the arrow backward
        prev = curr            # 3. Advance prev to curr
        curr = next_node       # 4. Advance curr to the lifeline

    return prev                # prev is now standing on the new head


def reverse_between(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    """
    LeetCode 92: Reverse Linked List II (subsegment [left, right] in 1-pass)
    Time: O(N), Space: O(1)
    """
    if not head or left == right:
        return head

    # Phase 1: Setup dummy and walk to the cut point
    dummy = ListNode(0, head)
    before_left = dummy

    for _ in range(left - 1):
        before_left = before_left.next

    # Plant bookmarks and initialize the 3-pointer crew
    curr = before_left.next
    sublist_tail = curr
    prev = None

    # Phase 2: Standard 3-pointer reversal for (right - left + 1) nodes
    for _ in range(right - left + 1):
        next_node = curr.next  # 1. Save the lifeline
        curr.next = prev       # 2. Flip the arrow backward
        prev = curr            # 3. Advance prev to curr
        curr = next_node       # 4. Advance curr to the lifeline

    # Phase 3: The Two-Wire Weld
    before_left.next = prev    # Connect Node 1 -> Node 4
    sublist_tail.next = curr   # Connect Node 2 -> Node 5

    return dummy.next


if __name__ == "__main__":
    # Test LC 206
    l1 = ListNode.from_list([1, 2, 3, 4, 5])
    rev = reverse_list(l1)
    print("Reversed List:", rev.to_list())
    assert rev.to_list() == [5, 4, 3, 2, 1]

    # Test LC 92
    l2 = ListNode.from_list([1, 2, 3, 4, 5])
    rev_sub = reverse_between(l2, 2, 4)
    print("Reversed Sublist (2 to 4):", rev_sub.to_list())
    assert rev_sub.to_list() == [1, 4, 3, 2, 5]
    print("All tests passed successfully!")
