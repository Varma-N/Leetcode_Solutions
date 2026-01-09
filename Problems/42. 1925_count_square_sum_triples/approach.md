# 💡 Problem #1925: Count Square Sum Triples
**Link:** [Problem](https://leetcode.com/problems/count-square-sum-triples/)

---

## 🧠 Problem Understanding

You are given an integer `n`.

You must count the number of **square sum triples** `(a, b, c)` such that:

`a² + b² = c²`

with the constraints:
`1 ≤ a, b, c ≤ n`

Order matters:
- `(a, b, c)` and `(b, a, c)` are considered **different** if `a ≠ b`.

---

## ⚙️ Core Idea

This problem is based on **Pythagorean triples**.

Since `n` is small (≤ 250), a brute-force approach is efficient and safe.

---

## 🧩 Algorithm Strategy

1. Iterate `a` from `1` to `n`
2. Iterate `b` from `1` to `n`
3. Compute:
`c² = a² + b²`
4. Check if `c²` is a **perfect square**
5. If:
- `c * c == c²`
- `c ≤ n`
then `(a, b, c)` is a valid triple
6. Increment the count

---

## 🧮 Example

For `n = 5`:

Valid triples include:
`(3, 4, 5)`
`(4, 3, 5)`

Answer = **2**

---

## 🧠 Why This Works

- We directly test the mathematical condition
- Perfect square check ensures correctness
- Constraints are small enough to allow double loops

---

## ⏱️ Complexity

- **Time:** O(n²)
- **Space:** O(1)

---

## 🔑 Key Insight  
Brute force all `(a, b)` pairs and verify whether `a² + b²` forms a valid square within bounds.
