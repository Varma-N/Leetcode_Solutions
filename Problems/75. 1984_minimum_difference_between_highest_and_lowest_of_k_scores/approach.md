# 💡 Problem #1984: Minimum Difference Between Highest and Lowest of K Scores
**Link:** https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/

---

## 🧠 Problem Understanding

You are given:
- An integer array `nums`
- An integer `k`

You must choose **k elements** such that the difference between the maximum and minimum selected elements is minimized.

Return that minimum possible difference.

---

## ⚙️ Key Insight

To minimize:
```
nums = [9,4,1,7], k = 2

Sorted → [1,4,7,9]

Windows:
[1,4] → 3
[4,7] → 3
[7,9] → 2

Answer = 2
```

---

## ⏱️ Complexity

- **Time:** O(n log n) (due to sorting)
- **Space:** O(1)

---

## 🔑 Key Insight  
Sorting transforms the problem into finding the smallest difference among all size-k consecutive windows.
