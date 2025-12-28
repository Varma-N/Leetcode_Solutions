# 💡 Problem #1015: Smallest Integer Divisible by K
**Link:** [Problem](https://leetcode.com/problems/smallest-integer-divisible-by-k/)

---

## 🧠 Problem Understanding

You are given an integer `k`.

You need to find the **length of the smallest positive integer** consisting only of digit `'1'` (a *repunit*) such that the number is **divisible by `k`**.

If no such number exists, return `-1`.

Examples of repunit numbers:
`1, 11, 111, 1111, ...`

---

## ⚙️ Key Observations

### 1️⃣ When is it impossible?
If `k` is divisible by **2 or 5**, then **no repunit** can be divisible by `k`.

Why?
- All repunit numbers end with `1`
- Numbers divisible by 2 must end in even digit
- Numbers divisible by 5 must end in `0` or `5`

So:
`new_remainder = (r * 10 + 1) % k`

---

### 3️⃣ Pigeonhole Principle
There are only `k` possible remainders (`0` to `k-1`).

If after `k` steps we haven’t seen remainder `0`, the pattern will repeat and **no solution exists**.

So we only need to try at most `k` iterations.

---

## 🧩 Algorithm Steps

1. If `k % 2 == 0` or `k % 5 == 0` → return `-1`
2. Initialize:
`remainder = 1 % k`
`length = 1`
3. While remainder ≠ 0 and length ≤ k:
`remainder = (remainder * 10 + 1) % k`
`length += 1`
4. Return `length`

---

## 🧮 Example

```
k = 3

1 % 3 = 1
11 % 3 = 2
111 % 3 = 0

Answer = 3
```

---

## ⏱️ Complexity

- **Time:** O(k)
- **Space:** O(1)

---

## 🔑 Key Insight  
Track only the **remainder modulo k**, and stop after `k` iterations using the pigeonhole principle.
