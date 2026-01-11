# 💡 Problem #3583: Count Special Triplets
**Link:** https://leetcode.com/problems/count-special-triplets/

---

## 🧠 Problem Understanding

You are given an integer array `nums`.

A triplet `(i, j, k)` is called **special** if:
`i < j < k`
`nums[i] == 2 * nums[j]`
`nums[k] == 2 * nums[j]`

Your task is to count the number of such triplets and return the result modulo **10⁹ + 7**.

---

## ⚙️ Key Insight

Fix the **middle index `j`**.

For a fixed `j`, we need:
- Some `nums[i] = 2 * nums[j]` on the **left**
- Some `nums[k] = 2 * nums[j]` on the **right**

If:
`left_count = number of occurrences of (2 * nums[j]) before j`
`right_count = number of occurrences of (2 * nums[j]) after j`

Then the number of valid triplets with middle index `j` is:
`left_count × right_count`

We just need to compute this efficiently for all `j`.

---

## 🧩 Algorithm Strategy

1. Build a frequency map `right` containing counts of all elements.
2. Initialize an empty frequency map `left`.
3. Iterate `j` from left to right:
   - Decrease `right[nums[j]]` (current index moves from right side to middle)
   - Let `target = 2 * nums[j]`
   - Add `left[target] * right[target]` to the answer
   - Increase `left[nums[j]]`
4. Return the result modulo **10⁹ + 7**

---

## 🧮 Example

```
nums = [2,1,2,4,2]

At j = 1 (nums[j] = 1):
target = 2
left_count = 1
right_count = 2
contribution = 2
```

---

## 🧠 Why This Works

- Every valid triplet has a unique middle index `j`
- Splitting counts into left and right avoids nested loops
- Hash maps give O(1) average lookup

---

## ⏱️ Complexity

- **Time:** O(n)
- **Space:** O(n)

---

## 🔑 Key Insight  
Fix the middle element and count matching values on both sides using frequency maps.
