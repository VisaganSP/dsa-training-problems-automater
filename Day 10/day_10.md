
## Introduction to Hashing and Segment Tree 🚀

#### Day 10 - 24-09-2024

#### **📖 Concepts of Hashing and Segment Tree**

### Hashing
Hashing is a technique used to map data of arbitrary size to fixed-size values. It involves the use of a hash function to convert input data into a hash code, which can then be used to index data in a hash table. Hashing is commonly used for fast data retrieval and to handle collisions in hash tables.

#### 🔍 Real-time Example
Using hashing to quickly find duplicates in an array.

### Segment Tree
A Segment Tree is a data structure that allows for efficient range queries and updates. It is used to perform operations on intervals or segments of an array, such as range sum queries or range minimum queries, with logarithmic time complexity for both updates and queries.

#### 🔍 Real-time Example
Using a Segment Tree to calculate the sum of elements within a given range of an array.

#### **✨ Advantages of Hashing and Segment Tree**

- **_Hashing_**:
  - Provides constant time complexity for average case lookups, insertions, and deletions.
  - Efficient for handling large datasets and frequent queries.
- **_Segment Tree_**:
  - Allows efficient range queries and updates.
  - Handles complex range operations like sum, minimum, maximum, and greatest common divisor.

#### **🌟 Use Cases**

- **_Hashing_**:
  - Implementing hash tables and hash maps.
  - Detecting duplicates in data and checking membership.
- **_Segment Tree_**:
  - Range queries and updates in arrays.
  - Handling dynamic array operations efficiently.

#### **🛠️ Implementing Hashing and Segment Tree**

**_Find All Anagrams in a String_**

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s. Strings consist of lowercase English letters only.

**_Constraints_**:

- 1 ≤ `s.length`, `p.length` ≤ 10⁴

**_Examples_**:

**_Example 1_**:

```java
Input: s = "cbaebabacd", p = "abc"
Output: [0, 6]
Explanation: The anagrams of 'abc' in 'cbaebabacd' start at indices 0 and 6.
```

**_Solve Here to Get Credits_**: [Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/)

**_Range Sum Query - Mutable_**

Given an integer array nums and an integer array updates, implement a segment tree that supports range sum queries and range updates. Perform a series of updates and queries on the array.

**_Constraints_**:

- 1 ≤ `nums.length` ≤ 10⁵
- 1 ≤ `updates.length` ≤ 10⁵

**_Examples_**:

**_Example 1_**:

```java
Input: nums = [1, 3, 5], updates = [[1, 2, 2], [0, 1, 1]]
Output: The final array after updates and queries.
Explanation: The segment tree is used to efficiently process range updates and queries.
```

**_Solve Here to Get Credits_**: [Range Sum Query - Mutable](https://leetcode.com/problems/range-sum-query-mutable/)


#### **❓ Practice Problems**

1. **_Find All Anagrams in a String_**:
   - **_Objective_**: Find all starting indices of p's anagrams in s using hashing.
   - **_Key Concept_**: Use a hash table to track character frequencies and sliding window for efficient searching.

2. **_Range Sum Query - Mutable_**:
   - **_Objective_**: Implement a Segment Tree for efficient range updates and queries.
   - **_Key Concept_**: Use Segment Tree to handle range queries and updates with logarithmic time complexity.


#### **📚 Suggested Reading**

- [Hashing: Concepts and Applications](https://www.geeksforgeeks.org/hash-table/)
- [Segment Tree Explained](https://www.geeksforgeeks.org/segment-tree-set-1-sum-of-given-range/)

---
