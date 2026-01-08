# 💡 Problem #1523: Count Odd Numbers in an Interval Range
**Link:** [Problem](https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/)

---

## 🧠 Problem Understanding

You are given two integers:
- `low`
- `high`

Your task is to count how many **odd numbers** exist in the **inclusive range** `[low, high]`.

---

## ⚙️ Key Insight

Instead of iterating through the range, we use a **mathematical observation**.

### Count of odd numbers from `0` to `x` (inclusive):
`(x + 1) // 2`

Why?
- Every two consecutive numbers contain exactly one odd number.
- Adding 1 ensures correct counting when `x` itself is odd.

---

## 🧩 Applying to a Range

To count odd numbers in `[low, high]`:

`odd_count = odds_up_to(high) - odds_up_to(low - 1)`

Which simplifies to:
`((high + 1) // 2) - (low // 2)`

---

## 🧮 Example

```
low = 3, high = 7
Odd numbers = 3, 5, 7 → 3

Calculation:
(7 + 1) // 2 - 3 // 2
= 4 - 1
= 3
```

---

## ⏱️ Complexity

- **Time:** O(1)
- **Space:** O(1)

---

## 🔑 Key Insight  
Count odds using arithmetic instead of iteration — parity math gives a constant-time solution.
