# 💡 Problem #3318: Find X-Sum of All K-Long Subarrays I
**Link:** [LeetCode #3318](https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/)

---

## 🧠 Approach

### 🔍 Problem Understanding
We are given:
- An integer array `nums`.
- Two integers `k` and `x`.

We must find, for every subarray of length `k`, the **X-sum** defined as:
1. Count the frequency of each number within the subarray.
2. Sort the numbers first by **frequency (descending)**, and then by **value (descending)**.
3. Take the top `x` numbers after sorting.
4. Sum all occurrences of those top `x` numbers within that window.
5. Repeat for all possible subarrays of size `k`.

Return a list of these sums in order.

---

### ⚙️ Intuition
For each sliding window of size `k`:
1. Compute frequency counts for all numbers in the window.
2. Sort numbers by:
   - Frequency (higher first)
   - Value (higher first if frequencies tie)
3. Take the top `x` distinct numbers according to this ranking.
4. Sum all instances of these numbers in the window.

Since constraints are small (values ≤ 50), we can safely use an array of size 51 for frequencies.

---

### 🧩 Step-by-Step Example
#### Example:
**Input:**  
```
nums = [1, 2, 2, 3, 3, 3]
k = 3
x = 2
```

**Process:**
- Window 1: [1, 2, 2]
  - freq = {1:1, 2:2}
  - Sorted = [(2,2), (1,1)]
  - Top 2 values = {2, 1}
  - Sum = 2 + 2 + 1 = 5

- Window 2: [2, 2, 3]
  - freq = {2:2, 3:1}
  - Sorted = [(2,2), (1,3)]
  - Top 2 values = {2, 3}
  - Sum = 2 + 2 + 3 = 7

- Window 3: [2, 3, 3]
  - freq = {2:1, 3:2}
  - Sorted = [(2,3), (1,2)]
  - Top 2 values = {3, 2}
  - Sum = 3 + 3 + 2 = 8

- Window 4: [3, 3, 3]
  - freq = {3:3}
  - Sorted = [(3,3)]
  - Top 2 values = {3}
  - Sum = 3 + 3 + 3 = 9

✅ **Output:** `[5, 7, 8, 9]`

---

### 🧠 Why This Works
- Using a frequency array allows O(1) counting since all values are within [1, 50].
- Sorting is cheap because we only sort up to 50 elements.
- Selecting the top `x` elements ensures we respect both frequency and value priority.

---

### ⏱️ Time Complexity
- **O((n - k + 1) * 50 log 50)**  
  → For each window, frequency counting and sorting take constant time since value range is fixed.
- Effectively **O(n)** for practical constraints.

### 💾 Space Complexity
- **O(1)** — frequency array is fixed size (51 elements).

---

✅ **Key Insight:**  
Since `nums[i]` values are bounded, we can brute-force each window efficiently without needing advanced sliding window optimizations.
