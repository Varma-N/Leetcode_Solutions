# 💡 Problem #1590: Make Sum Divisible by P
**Link:** [Problem](https://leetcode.com/problems/make-sum-divisible-by-p/)

---

## 🧠 Problem Understanding

You are given:
- An integer array `nums`
- An integer `p`

You may remove **one contiguous subarray** (possibly empty) from `nums`.

Goal:
- Make the **sum of the remaining elements divisible by `p`**
- Return the **minimum length** of such a subarray
- If impossible, return `-1`

---

## ⚙️ Key Insight

Let:
`total = sum(nums)`
`r = total % p`
  
- If `r == 0`, the total sum is already divisible by `p` → return `0`
- Otherwise, we need to remove a subarray whose sum is congruent to `r (mod p)`

This turns the problem into:
> Find the **shortest subarray** with sum % p == r

---

## 🧩 Prefix Modulo Technique

Define:
`prefix_mod[j] = (nums[0] + ... + nums[j]) % p`

For a subarray `(i+1 ... j)`:
`subarray_sum % p = (prefix_mod[j] - prefix_mod[i]) % p`

We want:
`(prefix_mod[j] - prefix_mod[i]) % p == r`
`→ prefix_mod[i] == (prefix_mod[j] - r) % p`

So for each `j`, we just need to check whether we’ve seen:
`target = (prefix_mod[j] - r) % p`

---

## 🧱 Algorithm Steps

1. Compute `total % p`
2. If it’s zero → return `0`
3. Initialize:
```
mod_index = {0: -1}
prefix_mod = 0
min_len = n
```
4. Iterate over the array:
- Update `prefix_mod`
- Compute `target`
- If `target` exists in `mod_index`, update `min_len`
- Store/update `prefix_mod` index
5. Return `min_len` if valid, else `-1`

---

## 🧮 Example
```
nums = [3,1,4,2], p = 6
total = 10 → r = 4

Remove subarray [4] → remaining sum = 6 → divisible by 6
Answer = 1
```

---

## ⏱️ Complexity

- **Time:** O(n)
- **Space:** O(p) in worst case (hashmap of remainders)

---

## 🔑 Key Insight  
Remove the **smallest subarray** whose sum modulo `p` equals the total remainder — use prefix sums and modular arithmetic to find it efficiently.
