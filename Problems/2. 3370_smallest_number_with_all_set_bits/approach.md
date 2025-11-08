# 💡 Problem #3370: Smallest Number With All Set Bits
**Link:** [LeetCode #3370](https://leetcode.com/problems/smallest-number-with-all-set-bits/)

---

## 🧠 Approach

### 🔍 Understanding the Problem
We are given an integer `n`.  
We need to find the smallest number that:
1. Has **all bits set to 1** (e.g., `1`, `3`, `7`, `15`, `31`, …)
2. Is **greater than or equal to `n`**

Example:  
If `n = 6` → next number with all bits set is `7 (111 in binary)`  
If `n = 8` → next number with all bits set is `15 (1111 in binary)`

---

### ⚙️ Thought Process
- Start from `x = 1` (which is `1` in binary).
- Keep setting the next bit to 1 until `x` becomes greater than or equal to `n`.
- This can be achieved by the operation:
  ```python
  x = (x << 1) | 1
This left-shifts x (adds a zero bit to the right) and then sets that bit to 1.
Continue until x >= n, then return x.

---

### 🧩 Example Walkthrough

For n = 6:
```
x = 1  (1)
x = 3  (11)
x = 7  (111) → 7 >= 6 → return 7
```

For n = 10:
```
x = 1 → 3 → 7 → 15 → return 15
```

---

⏱️ Time Complexity

O(log n) - since we double x each iteration until it surpasses n.

💾 Space Complexity

O(1) - constant extra space.
