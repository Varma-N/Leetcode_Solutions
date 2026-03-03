# 💡 Problem #1200: Minimum Absolute Difference
**Link:** https://leetcode.com/problems/minimum-absolute-difference/

---

## 🧠 Problem Understanding

You are given a distinct integer array `arr`.

Your task is to:
- Find all pairs of elements with the **minimum absolute difference**
- Return the pairs in **ascending order**

---

## ⚙️ Key Insight

The smallest absolute difference between any two numbers will always occur between **adjacent elements after sorting**.

Why?

Because sorting arranges numbers in increasing order, and the smallest gap must exist between neighbors.

---

## 🧩 Algorithm Strategy

1. Sort the array
2. First pass:
   - Compute the minimum difference between consecutive elements
3. Second pass:
   - Collect all adjacent pairs whose difference equals the minimum difference

---

## 🧮 Example
```
arr = [4,2,1,3]

Sorted → [1,2,3,4]

Differences:
2-1 = 1
3-2 = 1
4-3 = 1

Minimum difference = 1

Result:
[[1,2], [2,3], [3,4]]
```

---

## 🧠 Why This Works

- Sorting guarantees adjacent elements have the smallest possible gap
- Only O(n) scanning needed after sorting
- No need for nested loops

---

## ⏱️ Complexity

- **Time:** O(n log n) (sorting)
- **Space:** O(1) (excluding output list)

---

## 🔑 Key Insight  
After sorting, the minimum absolute difference must appear between adjacent elements.
