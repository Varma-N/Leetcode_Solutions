# 💡 Problem #3432: Count Partitions with Even Sum Difference
**Link:** [Problem](https://leetcode.com/problems/count-partitions-with-even-sum-difference/)

---

## 🧠 Problem Understanding

You are given an integer array `nums`.

You need to count the number of ways to split the array into **two non-empty contiguous parts** such that:

`(abs(sum(left) - sum(right))) is even`

---

## ⚙️ Key Insight

Let:
```
total = sum(nums)
left_sum = sum(nums[0..i])
right_sum = total - left_sum
```

The difference is:
`|left_sum - right_sum|`
`= |2 * left_sum - total|`

### 🔑 Parity Observation
- `2 * left_sum` is always **even**
- Therefore, the parity of the expression depends **only on `total`**

So:
- If `total` is **even** → difference is even for **every split**
- If `total` is **odd** → difference is odd for **every split**

---

## 🧩 Counting Valid Partitions

- There are exactly `n - 1` ways to split an array of length `n`
- If `total` is even → all splits are valid
- If `total` is odd → no split is valid

---

## 🧮 Example

```
Example 1:
nums = [1,2,3,4]
total = 10 (even)

Number of valid partitions = n - 1 = 3
```
```
Example 2

nums = [1,2,3]
total = 6 (even)

Valid partitions = 2
```
```
Example 3
nums = [1,2]
total = 3 (odd)

Valid partitions = 0
```

---

## ⏱️ Complexity

- **Time:** O(n) (just sum)
- **Space:** O(1)

---

## 🔑 Key Insight  
The parity of the sum difference depends **only on the total sum**, not on where you split.
