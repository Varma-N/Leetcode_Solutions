# 💡 Problem #1018: Binary Prefix Divisible By 5
**Link:** [Problem](https://leetcode.com/problems/binary-prefix-divisible-by-5/)

---

## 🧠 Problem Understanding

You are given a binary array `nums`.

For each prefix `nums[0..i]`:
- Treat it as a binary number.
- Check whether it is divisible by **5**.
- Return a boolean list of results for every prefix.

---

## ⚙️ Key Insight

Directly converting each prefix to an integer is inefficient and can overflow.

Instead, we use **modular arithmetic**.

### Binary number rule:
If the current remainder is `rem`, then after adding a new bit `b`:
`new_value = rem * 2 + b`
`new_remainder = (rem * 2 + b) % 5`


This allows us to:
- Track divisibility **without building large numbers**
- Use constant space

---

## 🧩 Step-by-Step Logic

1. Initialize `rem = 0`
2. For each bit `b` in `nums`:
   - Update remainder:
     ```
     rem = (rem * 2 + b) % 5
     ```
   - If `rem == 0`, prefix is divisible by 5
3. Append the boolean result

---

## 🧮 Example

```
nums = [1,0,1,1,1]

Prefixes (binary → decimal):
1 → 1 → ❌
10 → 2 → ❌
101 → 5 → ✅
1011 → 11 → ❌
10111 → 23 → ❌

Output:
[False, False, True, False, False]
```

---

## 🧠 Why This Works

Divisibility depends only on the remainder, not the full number.

By keeping the remainder modulo 5, we:
- Avoid overflow
- Keep the algorithm linear
- Use constant memory

---

## ⏱️ Complexity

- **Time:** O(n)
- **Space:** O(1)

---

## 🔑 Key Insight  
Use a rolling modulo to evaluate divisibility of growing binary prefixes efficiently.
