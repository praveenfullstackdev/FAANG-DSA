# FAANG DSA 🚀

A structured, production-grade repository containing Data Structures and Algorithms solutions, comprehensive mental models, and deep-dive technical interview guides in **Python** and **Java**.

---

## 📂 Repository Structure

```
FAANG DSA/
├── Arrays/
│   ├── MaxStockProfit.java         # Best Time to Buy and Sell Stock (O(n) Greedy / Kadane's variation)
│   ├── SubarraySum.java            # Subarray Sum Equals K (Prefix Sum + Hash Map)
│   └── TwoSumArrays.java           # Two Sum (Array / Two Pointers approach)
│
├── Hashing/
│   ├── ArraysAndHashing.md         # Comprehensive Study Guide: Mental models, time complexities, & 4 core patterns
│   ├── Sets_and_HashSets_Guide.md  # Deep dive into Sets, HashSets, BitSets & Redis intset optimization
│   ├── Python_Hashing_Methods_Guide.md # Python Hash Map & Set standard library cheat sheet
│   ├── ContainsDuplicate.py        # Check for duplicates using Hash Set (O(n) time, O(n) space)
│   ├── FirstUniqueCharacter.py     # First non-repeating character using Frequency Map
│   ├── GroupAnagrams.py            # Group Anagrams using Character Frequency Tuple / Sorted string key
│   ├── ransomnote.py               # Ransom Note string verification using Counter / Frequency Map
│   ├── TwoSum.py                   # Two Sum using complement lookup in Hash Map (O(n) time, O(n) space)
│   └── ValidAnagrams.py            # Valid Anagram check using Frequency Array / Counter
│
├── LinkedList/
│   ├── LinkedList_Guide.md         # Node structures, Cache line misses, Sentinel nodes & Redis quicklist
│   ├── LinkedList_Interview_Problems.md # FAANG Interview Guide: 10 Core LeetCode Problems & Pointer Surgery
│   ├── ReverseLinkedList.py        # LC 206 & LC 92 (Full & subsegment in-place reversals)
│   ├── LinkedListCycle.py          # LC 141 & LC 142 (Cycle detection & entry point with math proof)
│   ├── MiddleOfLinkedList.py       # LC 876 (Fast & slow pointer middle finding)
│   ├── RemoveNthFromEnd.py         # LC 19 (Sentinel node + fixed-distance window in 1 pass)
│   ├── MergeKSortedLists.py        # LC 21 & LC 23 (Divide & Conquer pairwise merge vs Min-Heap)
│   ├── ReorderList.py              # LC 143 (3-phase surgery: Midpoint -> Reverse -> Zipper merge)
│   ├── PalindromeLinkedList.py     # LC 234 (Midpoint -> Reverse second half -> O(1) space compare)
│   ├── FindDuplicateNumber.py      # LC 287 (Array as virtual linked list + Floyd's Cycle II)
│   ├── HappyNumber.py              # LC 202 (Fast & slow cycle detection on numbers in O(1) space)
│   └── LRUCache.py                 # LC 146 (O(1) Hash Map + Doubly Linked List with Sentinel bounds)
│
├── Trees/
│   └── RedBlackTree_Guide.md       # Self-balancing BSTs, Invariants, Rotations, std::map & Linux CFS
│
├── SkipList/
│   └── SkipList_and_ZSet_Guide.md  # Probabilistic express layers, Redis Sorted Set (ZSET) vs RB-Trees
│
├── .gitignore
└── README.md
```

---

## 📑 Problem Index

| # | Problem | Topic | Language | Pattern / Technique | Time Complexity | Space Complexity |
|---|---------|-------|----------|---------------------|-----------------|------------------|
| 1 | **Best Time to Buy and Sell Stock** | Arrays | Java | Single-pass Running Minimum | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ |
| 2 | **Subarray Sum Equals K** | Arrays / Hashing | Java | Prefix Sum + Frequency Map | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ |
| 3 | **Two Sum (Array)** | Arrays | Java | Two Pointers / Linear Scan | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ |
| 4 | **Two Sum** | Hashing | Python | Complements Mapping (`target - x`) | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ |
| 5 | **Contains Duplicate** | Hashing | Python | Visited Set Lookup | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ |
| 6 | **Valid Anagram** | Hashing | Python | Frequency Array / Counter | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ (alphabet size) |
| 7 | **Group Anagrams** | Hashing | Python | Fingerprint / 26-char Count Tuple Key | $\mathcal{O}(m \cdot k)$ | $\mathcal{O}(m \cdot k)$ |
| 8 | **Ransom Note** | Hashing | Python | Inventory / Decrement Frequency Map | $\mathcal{O}(m + n)$ | $\mathcal{O}(1)$ |
| 9 | **First Unique Character** | Hashing | Python | Two-pass Frequency Map | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ |
| 10 | **Reverse Linked List** (LC 206 & 92) | Linked List | Python | 3-Pointer Reversal & Head-Insertion | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ |
| 11 | **Linked List Cycle II** (LC 141 & 142) | Linked List | Python | Floyd's Fast & Slow + Entry Collision | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ |
| 12 | **Middle of the Linked List** (LC 876) | Linked List | Python | Fast & Slow Pointers (1x vs 2x) | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ |
| 13 | **Remove Nth Node From End** (LC 19) | Linked List | Python | Sentinel Dummy + Fixed Window ($N+1$) | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ |
| 14 | **Merge Two & K Sorted Lists** (LC 21 & 23) | Linked List | Python | Bottom-Up Divide & Conquer vs Min-Heap | $\mathcal{O}(n \log k)$ | $\mathcal{O}(1)$ |
| 15 | **Reorder List** (LC 143) | Linked List | Python | Midpoint $\to$ Reverse $\to$ Zipper Merge | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ |
| 16 | **Palindrome Linked List** (LC 234) | Linked List | Python | Mid $\to$ Reverse 2nd Half $\to$ Compare | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ |
| 17 | **Find the Duplicate Number** (LC 287) | Linked List / Array | Python | Virtual Linked List + Floyd's Cycle II | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ |
| 18 | **Happy Number** (LC 202) | Math / Fast & Slow | Python | Fast & Slow Cycle Detection on Sum of Squares | $\mathcal{O}(\log n)$ | $\mathcal{O}(1)$ |
| 19 | **LRU Cache** (LC 146) | Linked List / Design | Python | Hash Map + Doubly Linked List | $\mathcal{O}(1)$ | $\mathcal{O}(\text{capacity})$ |

---

## 🧠 Study Guides & Mental Models

Included in this repository are in-depth guides designed for FAANG technical interviews:

1. **[Linked List FAANG Coding Interview Mastery Guide](LinkedList/LinkedList_Interview_Problems.md)**
   - The 4 Inviolable Rules of Linked List Interviews
   - 10 Core FAANG LeetCode questions categorized into 5 surgical archetypes
   - Step-by-step pointer state transitions, Floyd's mathematical proof, and complete Python/Java solutions

2. **[Linked Lists & Memory Internals Guide](LinkedList/LinkedList_Guide.md)**
   - Memory Mental Model: Memory Treasure Hunt vs Array Shelf
   - CPU Cache Line spatial locality penalties ($64$-byte cache lines & pointer chasing)
   - The Sentinel Node (Dummy Head/Tail) pattern & pointer manipulation mastery
   - Real-world production internals: Redis classic `adlist.c` memory bloat and modern `quicklist` (Doubly Linked List of ZipLists)

3. **[Arrays & Hashing Mental Models Guide](Hashing/ArraysAndHashing.md)**
   - When to use an Array vs. Hash Set vs. Hash Map
   - The 4 classic interview patterns: Visited, Complements, Frequency, Fingerprints
   - Visual ASCII and Mermaid architecture diagrams

4. **[Sets, HashSets, and BitSets Deep Dive](Hashing/Sets_and_HashSets_Guide.md)**
   - Uniqueness invariants, HashSet internals (HashMap with dummy values)
   - Set operations: Union, Intersection, Difference ($O(N)$ vs $O(N \log N)$)
   - Real-world production internals: Redis `intset` memory compression (87.5% RAM savings) & dynamic upgrade to `dict`

5. **[Self-Balancing Red-Black Trees Guide](Trees/RedBlackTree_Guide.md)**
   - The Degenerate BST problem ($O(N)$ skewed trees) & AVL vs Red-Black Tree trade-offs
   - The 5 Inviolable Rules of Red-Black Trees & the Black-Height Invariant ($\text{Max Height} \le 2\log_2(N+1)$)
   - Left & Right Rotations, recoloring, and insertion rebalancing cases
   - Real-world production internals: C++ STL `std::map`/`set`, Java `TreeMap`/`TreeSet`, Java 8 `HashMap` bucket treeification ($>8$ items), Linux Kernel CFS

6. **[SkipLists & Redis Sorted Sets (ZSET) Guide](SkipList/SkipList_and_ZSet_Guide.md)**
   - The Express Subway Train analogy & multi-level probabilistic skip architecture
   - Search, Insert, and Delete mechanics with coin-toss geometric distribution
   - **The Billion-Dollar Interview Question:** Why Redis creator Antirez chose SkipList over Red-Black Tree for ZSET (Range queries, lock-free concurrency, memory footprint, implementation simplicity)
   - Redis dual-engine architecture (`dict` for $O(1)$ point lookups + `zskiplist` for $O(\log N)$ range queries)
   - Complete Python implementation with full testing suite

7. **[Python Hashing Methods Deep Dive](Hashing/Python_Hashing_Methods_Guide.md)**
   - Complete reference for `dict`, `set`, `collections.defaultdict`, and `collections.Counter`
   - Common pitfalls (e.g., mutable dictionary keys, `KeyError` avoidance)
   - Idiomatic Pythonic patterns for competitive programming and interviews

---

## 🛠️ How to Run

### Python Solutions
Ensure you have Python 3.8+ installed:
```bash
# Linked List Solutions
python LinkedList/ReverseLinkedList.py
python LinkedList/LinkedListCycle.py
python LinkedList/MiddleOfLinkedList.py
python LinkedList/RemoveNthFromEnd.py
python LinkedList/MergeKSortedLists.py
python LinkedList/ReorderList.py
python LinkedList/PalindromeLinkedList.py
python LinkedList/FindDuplicateNumber.py
python LinkedList/HappyNumber.py
python LinkedList/LRUCache.py

# Hashing Solutions
python Hashing/GroupAnagrams.py
python Hashing/TwoSum.py
```

### Java Solutions
Compile and run with JDK 11+:
```bash
javac Arrays/MaxStockProfit.java
java Arrays.MaxStockProfit
```

---

## 🎯 Contributing & Future Modules
- [ ] Two Pointers & Sliding Window
- [ ] Stacks & Queues
- [ ] Binary Search
- [x] Linked Lists (Deep Dive Guide complete)
- [x] Trees & Balanced BSTs (Red-Black Trees Guide complete)
- [x] SkipLists & Sorted Sets (Complete)
- [ ] Graphs & Topological Sort
- [ ] Dynamic Programming & Backtracking
