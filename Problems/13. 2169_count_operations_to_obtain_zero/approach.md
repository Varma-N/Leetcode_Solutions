# 💡 Problem #2169: Count Operations to Obtain Zero
**Link:** https://leetcode.com/problems/count-operations-to-obtain-zero/

---

## 🧠 Problem Understanding

You are given two integers `num1` and `num2`.  
You must repeatedly perform the following operation until either becomes `0`:

- If `num1 >= num2`: `num1 = num1 - num2`
- Else: `num2 = num2 - num1`

You must return the **total number of operations performed**.

---

## ⚙️ Intuition

This process is effectively a **repeated subtraction version** of the Euclidean algorithm (similar to computing GCD via subtraction instead of modulo).

Each operation reduces the larger number while keeping both values non-negative.  
Eventually one number becomes zero, and the loop ends.

---

## 🧩 Example Walkthrough

Example:  
```
num1 = 5, num2 = 3

Step 1: 5 >= 3 → 5 - 3 = 2 → (2, 3)
Step 2: 3 >= 2 → 3 - 2 = 1 → (2, 1)
Step 3: 2 >= 1 → 2 - 1 = 1 → (1, 1)
Step 4: 1 >= 1 → 1 - 1 = 0 → (0, 1)
```

Operations = **4**

---

## ⏱️ Time Complexity

- Worst case: **O(max(num1, num2))**
- Each step reduces one number, so runtime depends on value size.

Space: **O(1)**

---

## 🔑 Key Insight

This directly simulates the described process — no optimization or math trick is required unless constraints demand it.
