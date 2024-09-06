
## Introduction to Two Pointers new and Hashmap 🚀

#### Day 5 - 06-09-2024

#### **📖 Concepts of Two Pointers new and Hashmap**

### Two Pointers new
The Two Pointers technique involves using two indices to traverse a data structure (typically an array or a string). This method can help reduce the time complexity of problems that require checking pairs or managing subarray ranges. It is particularly useful for problems related to sorted arrays, linked lists, and searching pairs in linear time.

#### 🔍 Real-time Example
Two pointers can efficiently solve the problem of finding pairs in a sorted array that sum up to a target value.

### Hashmap
A Hashmap is a data structure that maps keys to values for highly efficient lookups. It allows storing data in key-value pairs, where each key is unique, and is often used to solve problems involving frequency counting, caching, and quick data retrieval.

#### 🔍 Real-time Example
Using a Hashmap, you can count the frequency of words in a document or keep track of the inventory in an e-commerce application.

#### **✨ Advantages of Two Pointers new and Hashmap**

- **_Two Pointers_**:
  - Reduces time complexity from O(n²) to O(n) for certain problems.
  - Efficiently handles problems involving subsequences and sorted data.
- **_Hashmap_**:
  - Provides average O(1) time complexity for insertions and lookups.
  - Useful for counting, grouping, and solving problems involving unique identification.

#### **🌟 Use Cases**

- **_Two Pointers_**:
  - Finding pairs with a given sum in a sorted array.
  - Merging two sorted arrays.
- **_Hashmap_**:
  - Frequency counting in strings and arrays.
  - Implementing caches for faster access.

#### **🛠️ Implementing Two Pointers new and Hashmap**

**_Lemonade Change_**

You have a lemonade stand, and each lemonade costs $5. Customers are standing in a queue to buy from you, and each pays with either a $5, $10, or $20 bill. You must provide each customer with the correct change, ensuring your cash register has the right bills at all times. Return `true` if you can provide the correct change to every customer, otherwise return `false`.

**_Constraints_**:

- 1 ≤ `bills.length` ≤ 10⁵
- `bills[i]` is either `5`, `10`, or `20`.

**_Examples_**:

**_Example 1_**:

```java
Input: bills = [5, 5, 5, 10, 20]
Output: true
Explanation: You provide change using available $5 and $10 bills.
```

**_Example 2_**:

```java
Input: bills = [5, 5, 10, 10, 20]
Output: false
Explanation: You cannot provide change for the last customer.
```

**_Solve Here to Get Credits_**: [Lemonade Change](https://leetcode.com/problems/lemonade-change/)

**_Roman to Integer_**

Given a string `s` representing a Roman numeral, convert it to an integer. Roman numerals are typically written largest to smallest from left to right. The numeral system includes instances where subtraction is used (e.g., IV for 4). Your task is to correctly parse and sum these values to produce the integer result.

**_Constraints_**:

- 1 ≤ `s.length` ≤ 15
- `s` consists of characters: 'I', 'V', 'X', 'L', 'C', 'D', 'M'.
- `s` is guaranteed to be a valid Roman numeral representing a number in the range [1, 3999].

**_Examples_**:

**_Example 1_**:

```java
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90, IV = 4.
```

**_Example 2_**:

```java
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V = 5, III = 3.
```

**_Solve Here to Get Credits_**: [Roman to Integer](https://leetcode.com/problems/roman-to-integer/)


#### **❓ Practice Problems**

1. **_Lemonade Change_**:
   - **_Objective_**: Manage your change effectively using a greedy algorithm approach.
   - **_Key Concept_**: Use Hashmap for counting and Two Pointers for managing cash flow.

2. **_Roman to Integer_**:
   - **_Objective_**: Parse and convert Roman numerals into integers.
   - **_Key Concept_**: Use Hashmap to map Roman symbols to their respective values.


#### **📚 Suggested Reading**

- [Two Pointers Technique: A Complete Guide](https://www.geeksforgeeks.org/two-pointers-technique/)
- [Understanding Hashmaps and Their Applications](https://www.geeksforgeeks.org/hash-map-in-java/)

---
