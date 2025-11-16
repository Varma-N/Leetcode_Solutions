# 💡 Problem #1611: Minimum One Bit Operations to Make Integers Zero
**Link:** https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/

---

## 🧠 Problem Understanding

You are allowed to perform only one operation repeatedly:

- Choose an index `i`  
- Flip (toggle) `bit[i]`
- **If** `i > 0`, you must **also** flip all bits in `range [i-1 ... 0]`

The goal is to transform the binary representation of integer `n` into **0**, using the **minimum number of operations**.

---

## ⚙️ Key Observation

The described operation **exactly matches the inverse transformation of Gray Code**.

- Gray Code representation ensures **only one bit changes at a time**.
- The minimum number of operations to convert `n → 0` equals the decimal value of the **Gray Code of `n`**.
- Computation of Gray Code from binary is:
  
```
g = b ^ (b >> 1) ^ (b >> 2) ... until shift becomes zero
```

This matches the loop logic:  
`res ^= n; n >>= 1`

Therefore, this problem is solved using Gray code transformation — **no DP, recursion, or BFS needed**.

---

## 🧩 Step-by-Step Intuition

Example: `n = 3` → binary `011`

Gray code transform:
```
res = 0
n = 011 → res = 000 ^ 011 = 011
n = 001 → res = 011 ^ 001 = 010
n = 000 → stop
```

Result = binary `010` → decimal **2**

Meaning: **minimum 2 operations needed**.

---

## ⏱️ Time Complexity
- Binary length is `O(log n)`
- Each step shifts once → **O(log n)** total

## 💾 Space Complexity
- **O(1)** — few integer variables

---

## 🔑 Key Insight
This problem is equivalent to computing:
```
answer = binary_to_graycode(n)
```
Where graycode(x) can be computed by repeatedly XOR'ing with right shifts.

---
