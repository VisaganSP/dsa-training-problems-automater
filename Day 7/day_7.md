
## Introduction to Greedy Algorithms and Graph Traversal 🚀

#### Day 7 - 16-09-2024

#### **📖 Concepts of Greedy Algorithms and Graph Traversal**

### Greedy Algorithms
Greedy Algorithms build up a solution piece by piece, always choosing the next piece that offers the most immediate benefit. The greedy choice is made with the hope that this local optimization will lead to a global optimum. Greedy algorithms are used for optimization problems where a series of local optimal choices lead to a global solution.

#### 🔍 Real-time Example
Using a greedy algorithm to find the minimum number of coins needed for a given amount.

### Graph Traversal
Graph Traversal refers to techniques for visiting all the nodes in a graph systematically. Common traversal methods include Depth-First Search (DFS) and Breadth-First Search (BFS). These methods are used to explore nodes and edges of a graph and are foundational for many graph-related algorithms.

#### 🔍 Real-time Example
Using BFS to find the shortest path in an unweighted graph.

#### **✨ Advantages of Greedy Algorithms and Graph Traversal**

- **_Greedy Algorithms_**:
  - Often provides a simple and intuitive approach to optimization problems.
  - Can be more efficient than other methods for certain types of problems.
- **_Graph Traversal_**:
  - Essential for solving problems related to paths, connectivity, and graph components.
  - Provides foundational techniques for many advanced graph algorithms.

#### **🌟 Use Cases**

- **_Greedy Algorithms_**:
  - Huffman coding for data compression.
  - Activity selection problem.
- **_Graph Traversal_**:
  - Finding the shortest path in unweighted graphs.
  - Solving puzzles like mazes and Sudoku.

#### **🛠️ Implementing Greedy Algorithms and Graph Traversal**

**_Activity Selection_**

Given a set of activities with start and end times, select the maximum number of activities that don't overlap.

**_Constraints_**:

- 1 ≤ `n` ≤ 10⁵
- Activities are given with their start and end times.

**_Examples_**:

**_Example 1_**:

```java
Input: activities = [[1, 4], [2, 6], [5, 7], [8, 9]]
Output: 3
Explanation: Select activities [1, 4], [5, 7], and [8, 9] for maximum count without overlap.
```

**_Solve Here to Get Credits_**: [Activity Selection](https://www.geeksforgeeks.org/activity-selection-problem-greedy-algo-1/)

**_Shortest Path in an Unweighted Graph_**

Given an unweighted graph and a starting node, find the shortest path to all other nodes using BFS.

**_Constraints_**:

- 1 ≤ `nodes` ≤ 10⁵
- Graph is represented using an adjacency list.

**_Examples_**:

**_Example 1_**:

```java
Input: graph = {0: [1, 2], 1: [2], 2: [3], 3: []}, start = 0
Output: [0, 1, 1, 2]
Explanation: Shortest paths from node 0 are [0, 1, 1, 2] to nodes 0, 1, 2, and 3 respectively.
```

**_Solve Here to Get Credits_**: [Shortest Path in an Unweighted Graph](https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/)


#### **❓ Practice Problems**

1. **_Activity Selection_**:
   - **_Objective_**: Select the maximum number of non-overlapping activities using a greedy approach.
   - **_Key Concept_**: Use greedy choice to select the earliest finishing activity that is compatible with the previously selected activities.

2. **_Shortest Path in an Unweighted Graph_**:
   - **_Objective_**: Find the shortest path in an unweighted graph using BFS.
   - **_Key Concept_**: Use BFS to explore nodes level by level, ensuring the shortest path is found.


#### **📚 Suggested Reading**

- [Greedy Algorithms and Their Applications](https://www.geeksforgeeks.org/greedy-algorithms/)
- [Graph Traversal Techniques](https://www.geeksforgeeks.org/graph-traversal-techniques/)

---
