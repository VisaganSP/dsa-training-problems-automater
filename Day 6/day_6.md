
## Introduction to Dynamic Programming and Backtracking 🚀

#### Day 6 - 10-09-2024

#### **📖 Concepts of Dynamic Programming and Backtracking**

### Dynamic Programming
Dynamic Programming (DP) is a technique for solving complex problems by breaking them down into simpler overlapping subproblems. It is used when the problem can be divided into smaller subproblems that are solved independently and combined to get the final solution. DP can be applied using either memoization (top-down) or tabulation (bottom-up) approaches.

#### 🔍 Real-time Example
Using DP to find the minimum cost path in a grid.

### Backtracking
Backtracking is a method for solving problems by exploring all potential solutions and eliminating those that do not meet the criteria. It involves trying out different possibilities and undoing or 'backtracking' when a choice leads to an invalid solution. This method is often used for constraint satisfaction problems and combinatorial problems.

#### 🔍 Real-time Example
Using backtracking to solve the N-Queens problem.

#### **✨ Advantages of Dynamic Programming and Backtracking**

- **_Dynamic Programming_**:
  - Transforms exponential time problems into polynomial time solutions.
  - Effective for problems with optimal substructure and overlapping subproblems.
- **_Backtracking_**:
  - Useful for problems where all potential solutions need to be explored.
  - Effective for constraint satisfaction and combinatorial problems.

#### **🌟 Use Cases**

- **_Dynamic Programming_**:
  - Finding the longest common subsequence.
  - Calculating the maximum profit from stock trading.
- **_Backtracking_**:
  - Generating permutations and combinations.
  - Solving puzzles like Sudoku and crosswords.

#### **🛠️ Implementing Dynamic Programming and Backtracking**

**_Coin Change_**

Given a set of coin denominations and a total amount, find the minimum number of coins needed to make up that amount. If it is not possible to make up the amount, return -1.

**_Constraints_**:

- 1 ≤ `coins.length` ≤ 12
- 1 ≤ `amount` ≤ 10⁴

**_Examples_**:

**_Example 1_**:

```java
Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: The minimum number of coins is 3 (5 + 5 + 1).
```

**_Example 2_**:

```java
Input: coins = [2], amount = 3
Output: -1
Explanation: It is not possible to make the amount using only coin 2.
```

**_Solve Here to Get Credits_**: [Coin Change](https://leetcode.com/problems/coin-change/)

**_Subsets_**

Given a set of distinct integers, return all possible subsets (the power set). The solution set must not contain duplicate subsets.

**_Constraints_**:

- 1 ≤ `nums.length` ≤ 10
- `nums` consists of distinct integers.

**_Examples_**:

**_Example 1_**:

```java
Input: nums = [1, 2, 3]
Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
Explanation: All possible subsets of the given set are returned.
```

**_Solve Here to Get Credits_**: [Subsets](https://leetcode.com/problems/subsets/)


#### **❓ Practice Problems**

1. **_Coin Change_**:
   - **_Objective_**: Find the minimum number of coins required to make up the given amount using DP.
   - **_Key Concept_**: Use DP to keep track of the minimum coins needed for each amount.

2. **_Subsets_**:
   - **_Objective_**: Generate all possible subsets using backtracking.
   - **_Key Concept_**: Use backtracking to explore all possible combinations.


#### **📚 Suggested Reading**

- [Dynamic Programming: A Comprehensive Guide](https://www.geeksforgeeks.org/dynamic-programming/)
- [Backtracking Algorithm: An Introduction](https://www.geeksforgeeks.org/backtracking/)

---
