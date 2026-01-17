# 💡 Problem #1351: Count Negative Numbers in a Sorted Matrix
**Link:** [Problem](https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/)

---

## 🧠 Problem Understanding

You are given a matrix `grid` where:
- Each row is sorted in **non-increasing order**
- Each column is sorted in **non-increasing order**

Your task is to count how many elements in the matrix are **negative**.

---

## ⚙️ Simple & Correct Approach

The most straightforward way to solve this problem is:
- Iterate through every element in the matrix
- Count how many values are `< 0`

This approach is:
- Easy to implement
- Easy to understand
- Guaranteed to work for all valid inputs

---

## 🧩 Algorithm Steps

1. Initialize a counter to `0`
2. Loop through each row in the matrix
3. Loop through each value in the row
4. If the value is negative, increment the counter
5. Return the counter

---

## 🧮 Example

```
grid = [
[4, 3, 2, -1],
[3, 2, 1, -1],
[1, 1, -1, -2],
[-1, -1, -2, -3]
]

Negative numbers = 8
```

---

## 🧠 Why This Works

- The matrix size is small enough for direct iteration
- No need for complex logic when clarity is preferred
- This solution is often accepted in interviews for correctness first

---

## ⏱️ Complexity

- **Time:** O(m × n)
- **Space:** O(1)

Where:
- `m` = number of rows
- `n` = number of columns

---

## 🔑 Key Insight  
When constraints allow, a direct scan is the clearest and safest solution.
