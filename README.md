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
│   ├── Python_Hashing_Methods_Guide.md # Python Hash Map & Set standard library cheat sheet
│   ├── ContainsDuplicate.py        # Check for duplicates using Hash Set (O(n) time, O(n) space)
│   ├── FirstUniqueCharacter.py     # First non-repeating character using Frequency Map
│   ├── GroupAnagrams.py            # Group Anagrams using Character Frequency Tuple / Sorted string key
│   ├── ransomnote.py               # Ransom Note string verification using Counter / Frequency Map
│   ├── TwoSum.py                   # Two Sum using complement lookup in Hash Map (O(n) time, O(n) space)
│   └── ValidAnagrams.py            # Valid Anagram check using Frequency Array / Counter
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
   - The 4 classic interview patterns:
     1. *Visited / Duplicates* (`set()`)
     2. *Complements* (`dict()` with `target - num`)
     3. *Frequency / Inventory* (`dict()` or `Counter`)
     4. *Fingerprint Grouping* (`dict()` with immutable key)
   - Visual ASCII and Mermaid architecture diagrams

2. **[Python Hashing Methods Deep Dive](Hashing/Python_Hashing_Methods_Guide.md)**
   - Complete reference for `dict`, `set`, `collections.defaultdict`, and `collections.Counter`
   - Common pitfalls (e.g., mutable dictionary keys, `KeyError` avoidance)
   - Idiomatic Pythonic patterns for competitive programming and interviews

---

## 🛠️ How to Run

### Python Solutions
Ensure you have Python 3.8+ installed:
```bash
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
- [ ] Linked Lists
- [ ] Trees & Graphs
- [ ] Dynamic Programming & Backtracking
