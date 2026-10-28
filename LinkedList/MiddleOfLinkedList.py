"""
LeetCode 876: Middle of the Linked List

Problem:
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

FAANG Pattern:
Fast & Slow Pointers (Floyd's Tortoise & Hare)
- slow moves 1 step per tick: slow = slow.next
- fast moves 2 steps per tick: fast = fast.next.next
- When fast reaches None (or fast.next is None), slow is EXACTLY at the middle!

Time Complexity: O(N) — Single pass
Space Complexity: O(1) — No extra memory
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


def middle_node(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Returns the middle node of a singly linked list.
    If even number of nodes, returns the second middle node.
    """
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


if __name__ == "__main__":
    # Test 1: Odd length [1, 2, 3, 4, 5] -> Middle is 3
    odd_list = ListNode.from_list([1, 2, 3, 4, 5])
    mid_odd = middle_node(odd_list)
    print("Odd List Middle Node:", mid_odd.val, "Remaining:", mid_odd.to_list())
    assert mid_odd.val == 3
    assert mid_odd.to_list() == [3, 4, 5]

    # Test 2: Even length [1, 2, 3, 4, 5, 6] -> Second middle is 4
    even_list = ListNode.from_list([1, 2, 3, 4, 5, 6])
    mid_even = middle_node(even_list)
    print("Even List Middle Node:", mid_even.val, "Remaining:", mid_even.to_list())
    assert mid_even.val == 4
    assert mid_even.to_list() == [4, 5, 6]

    # Test 3: Single element [1] -> Middle is 1
    single = ListNode.from_list([1])
    mid_single = middle_node(single)
    assert mid_single.val == 1

    print("All tests for LeetCode 876 passed successfully!")
