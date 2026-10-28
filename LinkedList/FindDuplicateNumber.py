"""
LeetCode 287: Find the Duplicate Number

Problem:
Given an array of integers 'nums' containing n + 1 integers where each integer is 
in the range [1, n] inclusive.
Prove that at least one duplicate number must exist, and find that duplicate.

FAANG Constraints:
1. You must not modify the array (sorting or marking negative is forbidden).
2. You must use only constant O(1) extra space (Hash Set is forbidden).
3. Runtime must be O(N) (nested loop O(N^2) is forbidden).

The "Aha!" Moment (Array as a Virtual Linked List):
- Because values are 1..n and indices are 0..n:
  Treat each index as a NODE, and the value nums[i] as the POINTER to the next node!
  i  ──►  nums[i]
- By Pigeonhole Principle, two different indices will point to the SAME value.
- Multiple pointers pointing to the same node creates a CYCLE!
- The duplicate value is the EXACT ENTRY POINT of the cycle!
- This is secretly Floyd's Cycle Detection II (LeetCode 142)!

Time Complexity: O(N)
Space Complexity: O(1)
"""

from typing import List

def find_duplicate(nums: List[int]) -> int:
    """
    Finds the duplicate integer in O(N) time and O(1) auxiliary space
    using Floyd's Tortoise and Hare cycle detection algorithm.
    """
    # Phase 1: Detect collision point inside cycle
    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]              # 1 step: slow.next
        fast = nums[nums[fast]]        # 2 steps: fast.next.next
        if slow == fast:
            break

    # Phase 2: Find the entrance to the cycle (the duplicate number)
    entry = nums[0]
    while entry != slow:
        entry = nums[entry]            # 1 step
        slow = nums[slow]              # 1 step

    return entry


if __name__ == "__main__":
    # Test 1: [1, 3, 4, 2, 2] -> duplicate is 2
    # Node 0 -> 1 -> 3 -> 2 -> 4 -> points back to 2 (Cycle entry at 2!)
    test1 = [1, 3, 4, 2, 2]
    dup1 = find_duplicate(test1)
    print("Test 1 Result:", dup1)
    assert dup1 == 2

    # Test 2: [3, 1, 3, 4, 2] -> duplicate is 3
    test2 = [3, 1, 3, 4, 2]
    dup2 = find_duplicate(test2)
    print("Test 2 Result:", dup2)
    assert dup2 == 3

    # Test 3: [3, 3, 3, 3, 3] -> duplicate is 3
    test3 = [3, 3, 3, 3, 3]
    dup3 = find_duplicate(test3)
    print("Test 3 Result:", dup3)
    assert dup3 == 3

    print("All tests for LeetCode 287 passed successfully!")
