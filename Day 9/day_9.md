
## Introduction to Binary Tree and Union-Find 🚀

#### Day 9 - 23-09-2024

#### **📖 Concepts of Binary Tree and Union-Find**

### Binary Tree
A Binary Tree is a hierarchical data structure where each node has at most two children referred to as the left child and the right child. Binary trees are foundational in computer science and are used in various applications, such as binary search trees, heaps, and expression parsing.

#### 🔍 Real-time Example
Using a binary tree to implement a binary search tree (BST) for efficient searching and sorting.

### Union-Find
Union-Find (or Disjoint Set Union) is a data structure used to keep track of a partition of a set into disjoint subsets. It supports two primary operations: union (to merge two subsets) and find (to identify which subset a particular element is in). This structure is commonly used in network connectivity and clustering problems.

#### 🔍 Real-time Example
Using Union-Find to determine if two elements are in the same connected component of a graph.

#### **✨ Advantages of Binary Tree and Union-Find**

- **_Binary Tree_**:
  - Facilitates efficient data retrieval and manipulation.
  - Supports various types of tree-based algorithms and data structures.
- **_Union-Find_**:
  - Efficiently handles dynamic connectivity queries.
  - Optimized for union and find operations with near constant time complexity using path compression and union by rank.

#### **🌟 Use Cases**

- **_Binary Tree_**:
  - Implementing binary search trees for efficient data searching.
  - Parsing and evaluating expressions in compilers.
- **_Union-Find_**:
  - Finding connected components in a graph.
  - Handling equivalence classes in clustering algorithms.

#### **🛠️ Implementing Binary Tree and Union-Find**

**_Lowest Common Ancestor of a Binary Tree_**

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes. The LCA is defined as the lowest node in the tree that has both nodes as descendants.

**_Constraints_**:

- The number of nodes in the tree is between 1 and 10⁵.
- Each node has a unique value.

**_Examples_**:

**_Example 1_**:

```java
Input: root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], p = 5, q = 1
Output: 3
Explanation: The lowest common ancestor of nodes 5 and 1 is node 3.
```

**_Solve Here to Get Credits_**: [Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)

**_Number of Connected Components in an Undirected Graph_**

Given an undirected graph and a list of edges, find the number of connected components in the graph. A connected component is a subset of the graph where there is a path between any two vertices.

**_Constraints_**:

- 1 ≤ `n` ≤ 10⁴
- 1 ≤ `edges.length` ≤ 10⁵

**_Examples_**:

**_Example 1_**:

```java
Input: n = 5, edges = [[0, 1], [1, 2], [3, 4]]
Output: 2
Explanation: There are two connected components: {0, 1, 2} and {3, 4}.
```

**_Solve Here to Get Credits_**: [Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/)


#### **❓ Practice Problems**

1. **_Lowest Common Ancestor of a Binary Tree_**:
   - **_Objective_**: Find the lowest common ancestor in a binary tree.
   - **_Key Concept_**: Use traversal techniques to find the LCA by checking paths or using recursion.

2. **_Number of Connected Components in an Undirected Graph_**:
   - **_Objective_**: Count the number of connected components using Union-Find or DFS.
   - **_Key Concept_**: Use Union-Find to track and merge connected components.


#### **📚 Suggested Reading**

- [Understanding Binary Trees](https://www.geeksforgeeks.org/binary-tree-data-structure/)
- [Union-Find Algorithm and Its Applications](https://www.geeksforgeeks.org/union-find/)

---
