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
│   └── LinkedList_Guide.md         # Node structures, Cache line misses, Sentinel nodes & Redis quicklist
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

---

## 🧠 Study Guides & Mental Models

Included in this repository are in-depth guides designed for FAANG technical interviews:

1. **[Arrays & Hashing Mental Models Guide](Hashing/ArraysAndHashing.md)**
   - When to use an Array vs. Hash Set vs. Hash Map
   - The 4 classic interview patterns: Visited, Complements, Frequency, Fingerprints
   - Visual ASCII and Mermaid architecture diagrams

2. **[Sets, HashSets, and BitSets Deep Dive](Hashing/Sets_and_HashSets_Guide.md)**
   - Uniqueness invariants, HashSet internals (HashMap with dummy values)
   - Set operations: Union, Intersection, Difference ($O(N)$ vs $O(N \log N)$)
   - Real-world production internals: Redis `intset` memory compression (87.5% RAM savings) & dynamic upgrade to `dict`

3. **[Linked Lists & Memory Internals Guide](LinkedList/LinkedList_Guide.md)**
   - Memory Mental Model: Memory Treasure Hunt vs Array Shelf
   - CPU Cache Line spatial locality penalties ($64$-byte cache lines & pointer chasing)
   - The Sentinel Node (Dummy Head/Tail) pattern & pointer manipulation mastery
   - Real-world production internals: Redis classic `adlist.c` memory bloat and modern `quicklist` (Doubly Linked List of ZipLists)

4. **[Self-Balancing Red-Black Trees Guide](Trees/RedBlackTree_Guide.md)**
   - The Degenerate BST problem ($O(N)$ skewed trees) & AVL vs Red-Black Tree trade-offs
   - The 5 Inviolable Rules of Red-Black Trees & the Black-Height Invariant ($\text{Max Height} \le 2\log_2(N+1)$)
   - Left & Right Rotations, recoloring, and insertion rebalancing cases
   - Real-world production internals: C++ STL `std::map`/`set`, Java `TreeMap`/`TreeSet`, Java 8 `HashMap` bucket treeification ($>8$ items), Linux Kernel CFS

5. **[SkipLists & Redis Sorted Sets (ZSET) Guide](SkipList/SkipList_and_ZSet_Guide.md)**
   - The Express Subway Train analogy & multi-level probabilistic skip architecture
   - Search, Insert, and Delete mechanics with coin-toss geometric distribution
   - **The Billion-Dollar Interview Question:** Why Redis creator Antirez chose SkipList over Red-Black Tree for ZSET (Range queries, lock-free concurrency, memory footprint, implementation simplicity)
   - Redis dual-engine architecture (`dict` for $O(1)$ point lookups + `zskiplist` for $O(\log N)$ range queries)
   - Complete Python implementation with full testing suite

6. **[Python Hashing Methods Deep Dive](Hashing/Python_Hashing_Methods_Guide.md)**
   - Complete reference for `dict`, `set`, `collections.defaultdict`, and `collections.Counter`
   - Common pitfalls (e.g., mutable dictionary keys, `KeyError` avoidance)
   - Idiomatic Pythonic patterns for competitive programming and interviews

---

## 🛠️ How to Run

### Python Solutions & SkipList
Ensure you have Python 3.8+ installed:
```bash
python Hashing/GroupAnagrams.py
python Hashing/TwoSum.py
python SkipList/SkipList_and_ZSet_Guide.md  # Includes runnable Python code blocks
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
