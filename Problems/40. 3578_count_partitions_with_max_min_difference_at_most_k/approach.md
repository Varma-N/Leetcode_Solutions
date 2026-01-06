# 💡 Problem #3578: Count Partitions With Max-Min Difference at Most K
**Link:** [Problem](https://leetcode.com/problems/count-partitions-with-max-min-difference-at-most-k/)

---

## 🧠 Problem Understanding

You are given:
- An integer array `nums`
- An integer `k`

You want to count the number of ways to partition `nums` into contiguous subarrays such that:

`(max value in subarray - min value in subarray) ≤ k` <br>
Return the total number of valid partitions modulo **10⁹ + 7**.

---

## ⚙️ Key Observations

1. This is a **partition DP** problem.
2. Validity of a segment depends on **range constraint (max − min ≤ k)**.
3. Brute force checking all partitions is impossible.

We need:
- A fast way to validate segments
- A fast way to sum DP transitions

---

## 🧩 DP Definition

Let:
`dp[i] = number of valid ways to partition nums[0..i-1]`
Final answer:
`dp[n]`
---

## 🔄 Transition

For a valid segment ending at index `right`, starting at index `left`:

`dp[right + 1] += dp[left] + dp[left + 1] + ... + dp[right]`
This is a **range sum DP transition**, which we optimize using prefix sums.

---

## ⚙️ Maintaining Valid Window (Sliding Window)

To ensure: 

`max(nums[left..right]) - min(nums[left..right]) ≤ k`


We use:
- **Monotonic increasing deque** → track minimum
- **Monotonic decreasing deque** → track maximum

While the window becomes invalid:
- Move `left` forward
- Remove outdated indices from deques

This guarantees:
- Window is always valid
- Each index enters and exits deques once → O(n)

---

## 📐 Prefix Sum Optimization

Define:


prefix[i] = dp[0] + dp[1] + ... + dp[i-1]


Then:


dp[right + 1] = prefix[right + 1] - prefix[left]


This turns the DP transition into **O(1)** per index.

---

## 🧮 Example (Conceptual)


```
nums = [1,3,2], k = 1

Valid partitions:
[1][3][2]
[1,3][2]
[1][3,2]

Answer = 3
```

---

## ⏱️ Complexity

- **Time:** O(n)
  - Sliding window + DP
- **Space:** O(n)
  - DP + prefix arrays

---

## 🔑 Key Insight  
Combine **sliding window range validation** with **prefix-sum optimized DP** to count valid partitions efficiently.
