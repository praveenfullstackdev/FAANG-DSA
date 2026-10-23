"""
Problem: LeetCode 49 - Group Anagrams
Difficulty: Medium
Category: Arrays & Hashing

Given an array of strings `strs`, group the anagrams together.
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a
different word or phrase, typically using all the original letters exactly once.
"""

from collections import defaultdict


# ==============================================================================
# APPROACH 1: Canonical Sorted String using Standard Dictionary
# ==============================================================================
def group_anagrams_basic_dict(strs: list[str]) -> list[list[str]]:
    """
    Time Complexity:  O(N * K log K)
        - N: Number of strings in strs
        - K: Maximum length of a string in strs
        - Sorting each word takes O(K log K), done for N words.
    Space Complexity: O(N * K)
        - Stores all N words and keys inside the hash map.
    """
    anagram_dict = {}
    for s in strs:
        sorted_s = "".join(sorted(s))
        if sorted_s not in anagram_dict:
            anagram_dict[sorted_s] = []
        anagram_dict[sorted_s].append(s)
    return list(anagram_dict.values())


# ==============================================================================
# APPROACH 2: Canonical Sorted String using defaultdict (Clean & Idiomatic)
# ==============================================================================
def group_anagrams_sorted(strs: list[str]) -> list[list[str]]:
    """
    Time Complexity:  O(N * K log K)
    Space Complexity: O(N * K)
    
    Idiomatic improvement over Approach 1:
    - defaultdict(list) automatically handles key initialization,
      reducing boilerplate and avoiding double dictionary lookups.
    """
    groups = defaultdict(list)
    for s in strs:
        groups["".join(sorted(s))].append(s)
    return list(groups.values())


# ==============================================================================
# APPROACH 3: Character Frequency Count Tuple (Asymptotically Optimal)
# ==============================================================================
def group_anagrams_count_tuple(strs: list[str]) -> list[list[str]]:
    """
    Time Complexity:  O(N * K)  [Optimal Lower Bound]
        - Scanning each string of length K takes O(K) time.
        - Constructing the 26-element tuple takes O(26) = O(1) time.
        - Total time: O(N * (K + 26)) = O(N * K).
    Space Complexity: O(N * K)
        - Stores all words and tuple keys. Keys take O(26) = O(1) extra space.
    """
    groups = defaultdict(list)
    for s in strs:
        count = [0] * 26  # 26 slots for 'a' through 'z'
        for char in s:
            count[ord(char) - ord("a")] += 1
        # Lists are mutable and unhashable -> convert to immutable tuple
        groups[tuple(count)].append(s)
    return list(groups.values())


# ==============================================================================
# APPROACH 4: Prime Product Hashing (Mathematical Alternative)
# ==============================================================================
def group_anagrams_prime_hash(strs: list[str]) -> list[list[str]]:
    """
    Time Complexity:  O(N * K)
    Space Complexity: O(N * K)

    Concept:
    - Fundamental Theorem of Arithmetic: Every integer > 1 is either prime
      itself or can be represented as the unique product of prime numbers.
    - Map each letter 'a'-'z' to a unique prime number.
    - The product of prime values for any anagram group will be IDENTICAL.
    - Non-anagrams will always produce distinct products (no hash collisions!).

    Note on Trade-offs:
    - In Python: Integers have arbitrary precision, so no 32/64-bit overflow.
    - In C++/Java: Large strings cause integer overflow unless using BigInteger
      or modular hashing (which introduces collision risk).
    """
    # 26 prime numbers for 'a' through 'z'
    primes = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
        43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101
    ]

    groups = defaultdict(list)
    for s in strs:
        product = 1
        for char in s:
            product *= primes[ord(char) - ord("a")]
        groups[product].append(s)

    return list(groups.values())


# ==============================================================================
# MAIN & VERIFICATION
# ==============================================================================
def main():
    test_cases = [
        ["eat", "tea", "tan", "ate", "nat", "bat"],
        [""],
        ["a"],
    ]

    for i, words in enumerate(test_cases, 1):
        print(f"--- Test Case {i}: {words} ---")
        print("Approach 1 (Basic dict):", group_anagrams_basic_dict(words))
        print("Approach 2 (Sorted):    ", group_anagrams_sorted(words))
        print("Approach 3 (Tuple 26):  ", group_anagrams_count_tuple(words))
        print("Approach 4 (Prime Hash):", group_anagrams_prime_hash(words))
        print()


if __name__ == "__main__":
    main()

"""
================================================================================
INTERVIEW PLAYBOOK & STRATEGY GUIDE (TIER-1 / FAANG)
================================================================================

1. Can any approach be faster than O(N * K)?
   - NO. The theoretical lower bound for this problem is Omega(N * K).
   - Reason: In the worst case, you must inspect every character of every
     word at least once to know its letters. Therefore, O(N * K) is optimal.

2. Interview Communication Script:
   -----------------------------------------------------------------------------
   Step 1: Clarify the Inputs & Edge Cases
   - "Can the strings contain uppercase letters, spaces, or special symbols?"
     (Assuming lowercase English 'a'-'z' unless told otherwise).
   - "What if the input array is empty or contains empty strings?" (strs = [""]).

   Step 2: Propose the Baseline Solution (Approach 2)
   - "We can group words by their canonical form. If we sort each word
     alphabetically, all anagrams produce the exact same string (e.g. 'eat',
     'tea' -> 'aet')."
   - "Using a hash map (defaultdict), we map this sorted string to a list of
     original words."
   - State Complexity: "Time is O(N * K log K), Space is O(N * K)."

   Step 3: Proactively Offer the Optimization (Approach 3)
   - "We can eliminate the O(K log K) sorting cost by noticing the alphabet
     is fixed to 26 characters."
   - "Instead of sorting, we count the frequency of each character in an
     array of size 26. Since lists are mutable and unhashable in Python,
     we convert this array into an immutable tuple to use as our dictionary key."
   - State Complexity: "This brings the time complexity down to O(N * K),
     which is theoretically optimal."

   Step 4: The Senior Engineer Nuance (Real-World vs Theoretical)
   - "Even though Approach 3 is asymptotically superior (O(N * K) vs O(N * K log K)),
     in real-world Python execution with typical short English words (K < 15),
     Approach 2 (sorted) can actually run faster in practice.
     Why? Timsort in Python runs in highly-optimized C, whereas constructing
     26-element tuples in pure Python introduces higher constant-factor overhead."
   - (Interviewers LOVE this discussion!).

3. Summary Comparison Table:
+------------+----------------------+---------------+---------------+-----------------------------+
| Approach   | Strategy             | Time          | Space         | Key Hash Type               |
+------------+----------------------+---------------+---------------+-----------------------------+
| Approach 1 | Manual dict + Sort   | O(N * K log K)| O(N * K)      | str                         |
| Approach 2 | defaultdict + Sort   | O(N * K log K)| O(N * K)      | str                         |
| Approach 3 | 26-Count Tuple       | O(N * K)      | O(N * K)      | tuple[int, ...] (26 ints)   |
| Approach 4 | Prime Multiplication | O(N * K)      | O(N * K)      | int (unique prime product)  |
+------------+----------------------+---------------+---------------+-----------------------------+
================================================================================
"""