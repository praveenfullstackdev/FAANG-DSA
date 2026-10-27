"""
LeetCode 141: Linked List Cycle (Boolean check)
LeetCode 142: Linked List Cycle II (Find Entry Node)

FAANG Pattern:
Floyd's Tortoise and Hare (Fast & Slow Pointers)
Mathematical Proof: L1 = n*C - d
Time: O(N), Space: O(1)
"""

from typing import Optional, Tuple

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


def has_cycle(head: Optional[ListNode]) -> bool:
    """
    LeetCode 141: Detect if cycle exists.
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


def detect_cycle_entry(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    LeetCode 142: Find the exact node where cycle begins.
    """
    slow = fast = head
    
    # Phase 1: Determine if meeting point exists
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None  # No cycle found

    # Phase 2: Collide head and slow to find cycle entry
    entry = head
    while entry != slow:
        entry = entry.next
        slow = slow.next

    return entry


if __name__ == "__main__":
    # Create list: 3 -> 2 -> 0 -> -4 -> points back to 2
    n1 = ListNode(3)
    n2 = ListNode(2)
    n3 = ListNode(0)
    n4 = ListNode(-4)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n2  # cycle at node 2

    assert has_cycle(n1) is True
    entry = detect_cycle_entry(n1)
    assert entry == n2
    print(f"Cycle detected! Entry node value: {entry.val}")

    # Test acyclic list: 1 -> 2 -> None
    a1 = ListNode(1)
    a2 = ListNode(2)
    a1.next = a2
    assert has_cycle(a1) is False
    assert detect_cycle_entry(a1) is None
    print("Acyclic test passed successfully!")
