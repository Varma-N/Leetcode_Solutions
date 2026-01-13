# 960. Delete Columns to Make Sorted III
**Link:** [Problem](https://leetcode.com/problems/delete-columns-to-make-sorted-iii/)

## Problem Summary

You are given an array of equal-length strings `strs`.

You may delete some columns so that the resulting strings are in **non-decreasing lexicographical order**.

Return the **minimum number of columns to delete**.

---

## Key Insight

Instead of thinking about which columns to delete, think about:

> **Which columns can be kept in order**

This becomes a **Longest Increasing Subsequence (LIS)**–style problem over columns.

---

## Column Ordering Rule

Column `i` can come before column `j` **if and only if**:

`For every row r:`
`strs[r][i] <= strs[r][j]`

This ensures lexicographical order is preserved across all strings.

---

## Dynamic Programming Approach

Let:
- `m` = number of columns
- `dp[j]` = length of the longest valid column sequence ending at column `j`

### Transition

For every column `j`:
- Check all previous columns `i < j`
- If column `i` can precede column `j`, then:
`dp[j] = max(dp[j], dp[i] + 1)`

### Initialization

`dp[j] = 1 (each column alone is valid)`

---

## Final Answer

`minimum deletions = m - max(dp)`

---

## Complexity Analysis

- Time Complexity: `O(m² × n)`
  - `m` columns
  - `n` strings
- Space Complexity: `O(m)`

---

## Why This Works

- We keep the **largest possible valid column subsequence**
- Deleting the rest minimizes deletions
- This avoids brute-force column removal

---

## Related Concepts

- Longest Increasing Subsequence (LIS)
- Dynamic Programming
- Lexicographical ordering

---
