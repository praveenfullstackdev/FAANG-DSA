"""
LeetCode 234: Palindrome Linked List

Problem:
Given the head of a singly linked list, return True if it is a palindrome, or False otherwise.

FAANG Pattern:
Composite Fast & Slow Pointer + In-Place Reversal (O(1) Auxiliary Space)
1. Find middle of list using Fast & Slow pointers (LC 876)
2. Reverse the second half in-place (LC 206)
3. Two-pointer comparison of first half vs second half
4. (Senior FAANG Bar): Restore the list back to its original state before returning!

Time Complexity: O(N) — Two passes
Space Complexity: O(1) — No arrays allocated
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


def is_palindrome(head: Optional[ListNode]) -> bool:
    """
    Checks if linked list is palindrome in O(N) time and strict O(1) memory.
    """
    if not head or not head.next:
        return True

    # Phase 1: Find end of first half (left middle for even lengths)
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # Phase 2: Reverse second half starting after slow
    def reverse(curr_node):
        prev = None
        curr = curr_node
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    second_half_head = reverse(slow.next)

    # Phase 3: Compare first half and reversed second half
    p1 = head
    p2 = second_half_head
    is_palin = True

    while is_palin and p2:
        if p1.val != p2.val:
            is_palin = False
        p1 = p1.next
        p2 = p2.next

    # Phase 4 (Senior Polish): Restore the list so caller's data isn't corrupted
    slow.next = reverse(second_half_head)

    return is_palin


if __name__ == "__main__":
    # Test 1: Even length palindrome [1, 2, 2, 1] -> True
    p1 = ListNode.from_list([1, 2, 2, 1])
    assert is_palindrome(p1) is True
    print("Test 1 [1, 2, 2, 1]: Passed! Restored list:", p1.to_list())

    # Test 2: Odd length palindrome [1, 2, 3, 2, 1] -> True
    p2 = ListNode.from_list([1, 2, 3, 2, 1])
    assert is_palindrome(p2) is True
    print("Test 2 [1, 2, 3, 2, 1]: Passed! Restored list:", p2.to_list())

    # Test 3: Non-palindrome [1, 2, 3] -> False
    np1 = ListNode.from_list([1, 2, 3])
    assert is_palindrome(np1) is False
    print("Test 3 [1, 2, 3]: Passed!")

    # Test 4: Single element [7] -> True
    single = ListNode.from_list([7])
    assert is_palindrome(single) is True
    print("Test 4 [7]: Passed!")

    print("All tests for LeetCode 234 passed successfully!")
