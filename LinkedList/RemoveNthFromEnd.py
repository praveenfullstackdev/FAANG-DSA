"""
LeetCode 19: Remove Nth Node From End of List

FAANG Pattern:
Sentinel (Dummy) Node + Fixed-Distance Fast/Slow Window (1-pass)
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


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    Remove nth node from end in a single pass.
    """
    dummy = ListNode(0, head)
    fast = slow = dummy

    # 1. Advance fast pointer by n + 1 steps to establish gap
    for _ in range(n + 1):
        if fast is None:
            return head
        fast = fast.next

    # 2. Advance both pointers until fast hits None
    while fast:
        slow = slow.next
        fast = fast.next

    # 3. Delete target node (slow is resting directly before it)
    slow.next = slow.next.next

    return dummy.next


if __name__ == "__main__":
    # Case 1: Standard middle deletion [1, 2, 3, 4, 5], n = 2 -> [1, 2, 3, 5]
    l1 = ListNode.from_list([1, 2, 3, 4, 5])
    res1 = remove_nth_from_end(l1, 2)
    print("Deleted 2nd from end:", res1.to_list())
    assert res1.to_list() == [1, 2, 3, 5]

    # Case 2: Deleting head node [1, 2], n = 2 -> [2]
    l2 = ListNode.from_list([1, 2])
    res2 = remove_nth_from_end(l2, 2)
    print("Deleted head node:", res2.to_list())
    assert res2.to_list() == [2]

    # Case 3: Single element list [1], n = 1 -> []
    l3 = ListNode.from_list([1])
    res3 = remove_nth_from_end(l3, 1)
    print("Deleted sole node:", res3.to_list() if res3 else [])
    assert res3 is None
    print("All tests passed successfully!")
