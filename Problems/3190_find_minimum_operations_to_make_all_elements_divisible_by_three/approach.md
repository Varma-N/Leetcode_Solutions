# 💡 Problem #3190: Find Minimum Operations to Make All Elements Divisible by Three
**Link:** https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/

---

## 🧠 Problem Understanding

You are given an integer array `nums`.

In one operation, you can **add or subtract 1** from any element.

Goal:  
Make **every element divisible by 3** using the **minimum number of operations**.

---

## ⚙️ Key Insight

Any integer `x` falls into one of these modulo classes:

- `x % 3 == 0` → already divisible → **0 operations**
- `x % 3 == 1` → needs **1 operation** (subtract 1)
- `x % 3 == 2` → needs **1 operation** (add 1)

👉 **Every number that is not divisible by 3 needs exactly one operation.**

So the problem reduces to:
> Count how many elements are **not divisible by 3**.

---

## 🧩 Example

`nums = [3, 6, 1, 4, 2]`

`Divisible by 3: 3, 6`
`Not divisible: 1, 4, 2`

`Answer = 3`


---

## ⏱️ Complexity

- **Time:** O(n)
- **Space:** O(1)

---

## 🔑 Key Insight  
Each non-divisible element contributes exactly **one** required operation — no greedy or DP needed.
