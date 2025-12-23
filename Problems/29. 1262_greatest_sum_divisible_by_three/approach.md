# 💡 Problem #1262: Greatest Sum Divisible by Three
**Link:** https://leetcode.com/problems/greatest-sum-divisible-by-three/

---

## 🧠 Problem Understanding

You are given an integer array `nums`.

You may choose **any subset of elements** (possibly empty).  
Your task is to find the **maximum possible sum** of chosen elements such that:

`sum % 3 == 0`


Return that maximum sum.

---

## ⚙️ Key Insight

Divisibility by 3 depends **only on the remainder modulo 3**, not on the exact values.

So instead of tracking all possible sums, we track **only the best sum for each remainder**:

`dp[r] = maximum sum achievable with remainder r (mod 3)`


There are only **3 states**:
- remainder 0
- remainder 1
- remainder 2

This keeps the solution extremely efficient.

---

## 🧩 Dynamic Programming Strategy

### Initialization
`dp = [0, -∞, -∞]`


Meaning:
- Sum 0 is achievable with remainder 0
- Other remainders are initially impossible

---

### Transition
For each number `num`:
1. Copy current dp → `new_dp`
2. For each remainder `r`:
   - If `dp[r]` is valid:
     ```
     new_sum = dp[r] + num
     new_r = new_sum % 3
     new_dp[new_r] = max(new_dp[new_r], new_sum)
     ```
3. Replace `dp` with `new_dp`

This ensures each number is used **at most once**.

---

## 🧮 Example

`nums = [3, 6, 5, 1, 8]`

Valid selections:
- 3 + 6 + 5 + 1 + 8 = 23 → not divisible
- 3 + 6 + 5 + 1 = 15 → divisible
- 3 + 6 + 8 = 17 → not divisible

Answer = **18** (3 + 6 + 1 + 8)

---

## 🧠 Why This Works

- Any sum can be categorized by its remainder mod 3.
- We only care about the **maximum sum** per remainder.
- Each update considers whether adding the current number improves a remainder class.

This avoids brute force subset enumeration.

---

## ⏱️ Complexity

- **Time:** O(n × 3) → **O(n)**
- **Space:** O(3) → **O(1)**

---

## 🔑 Key Insight  
Track the **best possible sum for each remainder modulo 3**, and update greedily using DP.
