# 💡 Problem #474: Ones and Zeroes
**Link:** https://leetcode.com/problems/ones-and-zeroes/

---

## 🧠 Problem Understanding

You are given:
- A list of binary strings `strs`
- Two integers `m` (maximum zeros allowed) and `n` (maximum ones allowed)

Your task is to select **the maximum number of strings** such that:
- Total zeros used ≤ `m`
- Total ones used ≤ `n`

---

## ⚙️ Key Insight  
This is a **2D 0/1 knapsack** problem.

- Each string is an item.
- Its "cost" is `(zeros, ones)`.
- Its "value" is `1` (counting the number of strings included).
- We must maximize the number of strings without exceeding `(m, n)` capacity.

We cannot reorder or partially take a string → classic knapsack rules apply.

---

## 🧩 Dynamic Programming Strategy

Define:
dp[i][j] = maximum number of strings we can pick
using at most i zeros and j ones

For each string:
1. Count number of zeros and ones.
2. Traverse DP **backwards** to prevent overwriting required previous states:

for i in range(m, zeros - 1, -1):
for j in range(n, ones - 1, -1):
dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)


This ensures each string is considered **once** (0/1 knapsack).

---

## 🧠 Why Backwards Traversal?

If we go forward, we might use the same string multiple times.  
Going backward ensures each dp state is updated only from the previous iteration.

---

## 🧮 Example

```
strs = ["10","0001","111001","1","0"], m = 5, n = 3
```

Optimal selection picks:
- "10"
- "0001"
- "1"

Total = **3 strings**

---

## ⏱️ Complexity

### Time Complexity
- For each string, we update an `m × n` DP table  
→ **O(len(strs) × m × n)**

### Space Complexity
- DP table of size `(m+1) × (n+1)`  
→ **O(m × n)**

---

## 🔑 Key Insight  
This is a **two-constraint knapsack**, where each string consumes a 2D budget `(zeros, ones)` and contributes value `1`.



