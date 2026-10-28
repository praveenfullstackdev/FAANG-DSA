"""
LeetCode 202: Happy Number

Problem:
A happy number is a number defined by the following process:
- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it stays), or it loops endlessly in a cycle.
- Return True if n is a happy number, and False if not.

FAANG Pattern:
Fast & Slow Pointer Cycle Detection (Floyd's Algorithm in O(1) Space)
- Number transitions: n -> get_next(n) -> get_next(get_next(n))
- Either it terminates at 1, or it gets trapped in an infinite cycle!
- Using a Hash Set takes O(k) memory.
- Using Slow (1 step) and Fast (2 steps) pointers solves it in strict O(1) space!

Time Complexity: O(log N)
Space Complexity: O(1)
"""

def get_next(n: int) -> int:
    """Computes the sum of the squares of the digits."""
    total_sum = 0
    while n > 0:
        n, digit = divmod(n, 10)
        total_sum += digit ** 2
    return total_sum


def is_happy(n: int) -> bool:
    """
    Detects if n reaches 1 or falls into an infinite cycle using O(1) space.
    """
    slow = n
    fast = get_next(n)

    # Move slow by 1 step and fast by 2 steps until they meet or fast hits 1
    while fast != 1 and slow != fast:
        slow = get_next(slow)
        fast = get_next(get_next(fast))

    return fast == 1


if __name__ == "__main__":
    # Test 1: n = 19 -> True
    # 1^2 + 9^2 = 82
    # 8^2 + 2^2 = 68
    # 6^2 + 8^2 = 100
    # 1^2 + 0^2 + 0^2 = 1 (Happy!)
    assert is_happy(19) is True
    print("Test 1 (n=19): Passed (Happy Number)")

    # Test 2: n = 2 -> False
    # 2 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4 (Trapped in cycle!)
    assert is_happy(2) is False
    print("Test 2 (n=2): Passed (Unhappy Cycle Detected)")

    # Test 3: n = 7 -> True (7 -> 49 -> 97 -> 130 -> 10 -> 1)
    assert is_happy(7) is True
    print("Test 3 (n=7): Passed (Happy Number)")

    print("All tests for LeetCode 202 passed successfully!")
