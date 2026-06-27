# 💡 Problem #3321: Find X-Sum of All K-Long Subarrays II
**Link:** [LeetCode #3321](https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-ii/)

---

## 🧠 Approach

### 🔍 Problem Understanding
We are given an array `nums`, and integers `k` and `x`.

For every contiguous subarray of length `k`, we must compute the **X-Sum**:

1. Count the frequency of each element inside the window.
2. Sort numbers by  
   - **frequency** (descending)  
   - then by **value** (descending).
3. Take the top `x` numbers after this ranking.
4. Multiply each chosen number by its frequency within the window and sum them.
5. Slide the window and repeat efficiently for every position.

---

### ⚙️ Why an Efficient Method Is Needed
The direct O(n × 50 log 50) brute-force method (like in Problem #3318) becomes slow when `n` is large.  
We need a **dynamic sliding-window structure** to update frequencies in O(log n) time.

---

## 🧩 Step-by-Step Logic

### 1️⃣  Data Structures
- `fm`: a dictionary mapping `num → frequency`.
- `low`: a `SortedList` holding all candidates **not currently in top x**.
- `top`: a `SortedList` maintaining exactly the **x highest (freq, num)** pairs.
- `curr`: running sum of `freq × num` for all items in `top`.

Each element is stored as a pair `(frequency, value)` so they can be ordered directly.

---

### 2️⃣  The `change()` Function
Handles insertion/removal of one occurrence of a number as the window slides.

Steps:
1. Remove the old `(freq, num)` from whichever list (`low` or `top`) currently contains it.  
   If it was in `top`, subtract its contribution from `curr`.
2. Update `fm[num] += count` (`count` = +1 for entering, −1 for leaving window).
3. Reinsert the new `(freq, num)` if the frequency is still positive.
4. Balance the two sets:
   - Fill `top` until it contains `x` elements (moving best pairs from `low`).
   - If an element in `low` becomes better than the smallest in `top`, swap them and update `curr`.

This guarantees that after every update,  
`top` always holds the `x` highest (frequency, value) pairs.

---

### 3️⃣  Sliding the Window
Iterate `i` from 0 to n − 1:
- Add `nums[i]` → `change(nums[i], +1)`
- Remove `nums[i − k]` when `i ≥ k` → `change(nums[i − k], −1)`
- After index `i ≥ k − 1`, append `curr` to results.

---

### 🧮 Example
**Input:**  
```
nums = [1, 2, 2, 3, 3, 3]
k = 3
x = 2
```

**Output:**  
`[5, 7, 8, 9]`

Matches the results from the brute-force version (Problem #3318) but runs much faster.

---

### 🧠 Why This Works
The combination of two `SortedList`s acts like a **balanced priority partition**:
- `top` → best `x` elements contributing to the current X-Sum.
- `low` → remaining candidates.

When elements enter or leave the window, the structure quickly re-balances while maintaining order by both frequency and value.

---

### ⏱️ Time Complexity
- Each update (`change`) costs **O(log n)** due to sorted operations.
- For all `n` elements: **O(n log n)** overall.

### 💾 Space Complexity
- **O(n)** in the worst case for frequency maps and lists (bounded by number of unique elements).

---

✅ **Key Insight:**  
Maintain two dynamically balanced sorted sets — one tracking the current top x contributors, and one for the rest — so each window’s X-Sum can be updated in logarithmic time without recomputing frequencies from scratch.

