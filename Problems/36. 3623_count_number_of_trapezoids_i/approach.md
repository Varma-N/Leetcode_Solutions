# 💡 Problem #3623: Count Number of Trapezoids I
**Link:** [Problem](https://leetcode.com/problems/count-number-of-trapezoids-i/)

---

## 🧠 Problem Understanding

You are given a list of points on a 2D plane.

A **trapezoid** (for this problem) is formed by choosing:
- Two **distinct horizontal lines** (different `y` values), and
- Two points on each line, forming **two horizontal segments** that are parallel.

Your task is to count how many such trapezoids can be formed.

Return the answer modulo **10⁹ + 7**.

---

## ⚙️ Key Insight

1. A trapezoid is defined by **two horizontal segments** on **different y-levels**.
2. On a fixed horizontal line (same `y`), if there are `n` points, the number of horizontal segments is:
`C(n, 2) = n * (n - 1) / 2`
3. For two different y-levels with `s1` and `s2` segments respectively, the number of trapezoids formed is:
`s1 * s2`
4. So the problem reduces to:
- Count points per `y`
- Compute segments per `y`
- Sum products over all **pairs of distinct y-levels**

---

## 🧩 Algorithm Steps

1. Count how many points lie on each horizontal line (`ycount[y]`).
2. For each `y` with at least 2 points, compute:
`segments = C(count, 2)`
3. Store all such segment counts in a list `segs`.
4. Compute the sum of products over all pairs `i < j` in `segs`.

To do step 4 efficiently in linear time, use a **prefix sum**:
`ans = sum(segs[i] * sum(segs[0..i-1]))`

---

## 🧮 Example

If horizontal segment counts are:
`segs = [3, 5, 2]`

Trapezoids:
`35 + 32 + 5*2 = 31`

---

## ⏱️ Complexity

- **Time:** O(n + k), where `n` = number of points, `k` = number of y-levels with ≥2 points
- **Space:** O(k)

---

## 🔑 Key Insight  
Count horizontal segments per y-level, then count trapezoids by pairing segments from different levels using prefix sums.
