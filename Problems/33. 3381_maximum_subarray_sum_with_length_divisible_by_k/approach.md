# 💡 Problem #3381: Maximum Subarray Sum With Length Divisible by K
**Link:** [Problem](https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/)

---

## 🧠 Problem Understanding

You are given:
- An integer array `nums`
- An integer `k`

You must find the **maximum subarray sum** such that:
`(length of subarray) % k == 0`

Return the maximum possible sum.  
If no valid subarray exists, return `0`.

---

## ⚙️ Key Insight

Let:
`prefix[i] = sum(nums[0 : i])`

For a subarray `(i, j]`:
`length = j - i`
`sum = prefix[j] - prefix[i]`

The length condition:
`(j - i) % k == 0`
`→ j % k == i % k`

### 🔑 Core Idea
For each index `j`, we want the **smallest prefix[i]** such that:
`i % k == j % k`

Then:
`max sum = prefix[j] - min_prefix[j % k]`

---

## 🧩 Algorithm Strategy

1. Compute prefix sums.
2. Maintain an array:
```
min_prefix[r] = minimum prefix sum seen so far
for indices where index % k == r
```
3. Iterate `j` from `1 → n`:
- Compute remainder `r = j % k`
- If `min_prefix[r]` exists:
  ```
  max_sum = max(max_sum, prefix[j] - min_prefix[r])
  ```
- Update `min_prefix[r] = min(min_prefix[r], prefix[j])`

The modulo grouping automatically enforces the **length divisible by k** constraint.

---

## 🧮 Example

```
nums = [1,2,3,4,5], k = 2

prefix = [0,1,3,6,10,15]

Valid subarrays (length % 2 == 0):
[1,2] → 3
[3,4] → 7
[2,3,4,5] → 14 ← max
```

Answer = **14**

---

## 🧠 Why This Works

- Prefix sums convert subarray sums into differences.
- Grouping by index modulo `k` guarantees valid lengths.
- Tracking minimum prefix per group ensures maximum difference.

This avoids brute-force O(n²) enumeration.

---

## ⏱️ Complexity

- **Time:** O(n)
- **Space:** O(k)

---

## 🔑 Key Insight  
Group prefix sums by index modulo `k`, and maximize the difference within each group.
