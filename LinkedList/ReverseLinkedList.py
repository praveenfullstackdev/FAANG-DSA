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
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


def reverse_between(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    """
    LeetCode 92: Reverse Linked List II (subsegment [left, right] in 1-pass)
    Time: O(N), Space: O(1)
    """
    if not head or left == right:
        return head

    dummy = ListNode(0, head)
    pre = dummy

    # 1. Walk pre to the node right before 'left'
    for _ in range(left - 1):
        pre = pre.next

    start = pre.next  # First node of reversed subsegment
    then = start.next # Node being pulled to front of subsegment

    # 2. In-place head-insertion
    for _ in range(right - left):
        start.next = then.next
        then.next = pre.next
        pre.next = then
        then = start.next

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
