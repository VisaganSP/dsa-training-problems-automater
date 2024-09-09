
## Introduction to Sliding Window and Binary Search 🚀

#### Day 5 - 09-09-2024

#### **📖 Concepts of Sliding Window and Binary Search**

### Sliding Window
The Sliding Window technique involves creating a window that can expand or contract as needed to find the optimal solution to a problem. This method is especially useful for problems that require working with contiguous subarrays or substrings. It can efficiently handle problems related to finding the minimum or maximum values within a sliding window.

#### 🔍 Real-time Example
Using Sliding Window to find the maximum sum of any contiguous subarray of size k.

### Binary Search
Binary Search is an efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing the search interval in half. If the value of the search key is less than the item in the middle of the interval, the algorithm narrows the interval to the lower half, otherwise to the upper half. This method is useful for searching in sorted data and optimizing algorithms involving sorted arrays or lists.

#### 🔍 Real-time Example
Binary Search can be used to find the position of a target value in a sorted array.

#### **✨ Advantages of Sliding Window and Binary Search**

- **_Sliding Window_**:
  - Reduces the time complexity of problems involving subarrays from O(n²) to O(n).
  - Efficient for problems related to contiguous subarray or substring.
- **_Binary Search_**:
  - Provides O(log n) time complexity for search operations in sorted arrays.
  - Efficient for problems involving sorted data and range queries.

#### **🌟 Use Cases**

- **_Sliding Window_**:
  - Finding the maximum sum of a fixed-size subarray.
  - Determining the longest substring without repeating characters.
- **_Binary Search_**:
  - Searching for an element in a sorted array.
  - Finding the first or last occurrence of an element in a sorted list.

#### **🛠️ Implementing Sliding Window and Binary Search**

**_Maximum Sum Subarray of Size K_**

Given an array of integers and a number k, find the maximum sum of any contiguous subarray of size k.

**_Constraints_**:

- 1 ≤ `arr.length` ≤ 10⁵
- 1 ≤ `k` ≤ `arr.length`

**_Examples_**:

**_Example 1_**:

```java
Input: arr = [1, 2, 3, 4, 5], k = 3
Output: 12
Explanation: The maximum sum subarray of size 3 is [3, 4, 5], and its sum is 12.
```

**_Example 2_**:

```java
Input: arr = [2, 1, 5, 1, 3, 2], k = 3
Output: 9
Explanation: The maximum sum subarray of size 3 is [5, 1, 3], and its sum is 9.
```

**_Solve Here to Get Credits_**: [Maximum Sum Subarray of Size K](https://leetcode.com/problems/maximum-sum-of-subarray-of-size-k/)

**_Binary Search on Sorted Array_**

Given a sorted array and a target value, return the index of the target if it exists in the array, otherwise return -1.

**_Constraints_**:

- 1 ≤ `arr.length` ≤ 10⁵
- `arr` is sorted in ascending order.

**_Examples_**:

**_Example 1_**:

```java
Input: arr = [1, 2, 3, 4, 5], target = 3
Output: 2
Explanation: The target value 3 is located at index 2.
```

**_Example 2_**:

```java
Input: arr = [1, 2, 3, 4, 5], target = 6
Output: -1
Explanation: The target value 6 does not exist in the array.
```

**_Solve Here to Get Credits_**: [Binary Search on Sorted Array](https://leetcode.com/problems/binary-search/)


#### **❓ Practice Problems**

1. **_Maximum Sum Subarray of Size K_**:
   - **_Objective_**: Find the maximum sum of a contiguous subarray of size k using the Sliding Window technique.
   - **_Key Concept_**: Use Sliding Window to maintain and update the sum of the current window.

2. **_Binary Search on Sorted Array_**:
   - **_Objective_**: Implement Binary Search to efficiently find an element in a sorted array.
   - **_Key Concept_**: Use Binary Search to divide the array and find the target value.


#### **📚 Suggested Reading**

- [Sliding Window Technique Explained](https://www.geeksforgeeks.org/sliding-window-maximum-using-deque/)
- [Introduction to Binary Search](https://www.geeksforgeeks.org/binary-search/)

---
