"""
LeetCode 143: Reorder List

Problem:
Reorder L0 -> L1 -> ... -> Ln-1 -> Ln into:
L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 ... in-place.

FAANG Pattern:
3-Step Composite Surgery:
1. Fast & Slow Pointers to find midpoint
2. Reverse second half (severing midpoint pointer!)
3. Alternating zipper merge of both halves
Time: O(N), Space: O(1)
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


def reorder_list(head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    if not head or not head.next:
        return

    # 1. Find midpoint (slow will end at middle/left-middle)
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # 2. Reverse second half
    prev = None
    curr = slow.next
    slow.next = None  # CRUCIAL: Sever the first half to avoid infinite cycles!

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    second = prev  # Head of reversed second half

    # 3. Zipper merge first and second half
    first = head
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2


if __name__ == "__main__":
    # Test even length: [1, 2, 3, 4] -> [1, 4, 2, 3]
    l1 = ListNode.from_list([1, 2, 3, 4])
    reorder_list(l1)
    print("Reordered even list:", l1.to_list())
    assert l1.to_list() == [1, 4, 2, 3]

    # Test odd length: [1, 2, 3, 4, 5] -> [1, 5, 2, 4, 3]
    l2 = ListNode.from_list([1, 2, 3, 4, 5])
    reorder_list(l2)
    print("Reordered odd list:", l2.to_list())
    assert l2.to_list() == [1, 5, 2, 4, 3]
    print("All tests passed successfully!")
