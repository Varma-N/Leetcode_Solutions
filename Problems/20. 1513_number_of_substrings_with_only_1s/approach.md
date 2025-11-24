# 💡 Problem #1513: Number of Substrings With Only 1s
**Link:** https://leetcode.com/problems/number-of-substrings-with-only-1s/

---

## 🧠 Problem Understanding

We need to count all substrings of `s` that contain **only '1'** characters.

Example:
- `"111"` contains: `"1", "1", "1", "11", "11", "111"` → 6 substrings

This can be computed using **math on consecutive segments** of '1's.

---

## ⚙️ Key Insight

The string is made of alternating segments:

`11100111101...`


For each maximal segment of `'1'` with length `L`, the number of valid substrings is:
` 1 + 2 + 3 + ... + L = L * (L + 1) / 2 `


So the task reduces to:

1. Scan the string.
2. Track lengths of consecutive `1`s.
3. Every time a `'0'` appears, compute the contribution of the previous streak.
4. Sum all contributions modulo \(10^9 + 7\).

---

## 🧩 Example

`s = "0110111"`

Segments:
```
"11" → 2 * 3 / 2 = 3
"111" → 3 * 4 / 2 = 6
```

Total = **9**

---

## 🧠 Why This Works

Counting all substrings directly is O(n²).  
But observing the structure of consecutive ones gives us an O(n) mathematical shortcut.

Each `'1'` extends all previous substrings ending there.

---

## ⏱️ Complexity

- **Time:** O(n)
- **Space:** O(1)

---

## 🔑 Key Insight  
Process the string in one pass; count substrings from each consecutive `'1'` segment using the arithmetic series formula.

