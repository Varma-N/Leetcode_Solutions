# 💡 Problem #2483: Minimum Penalty for a Shop
**Link:** [Problem](https://leetcode.com/problems/minimum-penalty-for-a-shop/)

---

## 🧠 Problem Understanding

You are given a string `customers` where:
- `'Y'` means a customer arrives at that hour
- `'N'` means no customer arrives

The shop can close at **any hour `j`** (0 ≤ j ≤ n).

Penalty rules:
- If the shop is **closed** at hour `j` and a customer arrives (`'Y'`) → penalty +1
- If the shop is **open** at hour `j` and no customer arrives (`'N'`) → penalty +1

Goal:
➡️ Find the **earliest hour** at which the total penalty is minimized.

---

## ⚙️ Key Insight

Think of the penalty in two parts:
- Customers `'Y'` **after closing** → penalty
- Customers `'N'` **before closing** → penalty

Instead of recomputing penalties for each hour, we:
- Start with the penalty if the shop closes at hour `0`
- Adjust the penalty **incrementally** as we move the closing hour forward

---

## 🧩 Initial State

If the shop closes at hour `0`:
- All `'Y'` customers cause penalty

So:

`penalty = count of 'Y' in customers`

This is our initial penalty.

---

## 🔄 Incremental Update

As we move the closing hour from `j` to `j + 1`:

- If `customers[j] == 'Y'`:
  - This customer is no longer missed
  - Penalty **decreases by 1**
- If `customers[j] == 'N'`:
  - Shop stayed open unnecessarily
  - Penalty **increases by 1**

Track the minimum penalty and the earliest hour where it occurs.

---

## 🧮 Example

```
customers = "YYNY"

Initial penalty (close at 0) = 3

Hour 1:
Y → penalty = 2

Hour 2:
Y → penalty = 1 ← minimum

Hour 3:
N → penalty = 2

Hour 4:
Y → penalty = 1
```

Best closing hour = **2**

---

## 🧠 Why This Works

- Each hour changes the penalty by at most ±1
- We scan once, updating penalties in O(1)
- Earliest minimum is preserved naturally

---

## ⏱️ Complexity

- **Time:** O(n)
- **Space:** O(1)

---

## 🔑 Key Insight  
Start with all missed customers, then adjust the penalty incrementally as the closing hour moves forward.
