# 💡 Problem #1437: Check If All 1's Are at Least Length K Places Away
**Link:** https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/

---

## 🧠 Problem Understanding

You are given a binary array `nums` and an integer `k`.

We must verify whether **every pair of consecutive 1's** in the array is separated by **at least `k` zeros**.

Meaning for any two indices `i < j` where:

`nums[i] = nums[j] = 1`

It must hold that:
`(j - i - 1) >= k`

If this condition is violated even once, return `False`.

---

## ⚙️ Key Insight

We simply track the index of the **previous '1'** using a variable `last_one_index`.

Steps:
1. Iterate through the array.
2. Whenever we see a `1`:
   - If it is not the first `1`, check if the distance from the previous `1` meets the condition.
   - If distance < k → return `False`.
3. Update `last_one_index`.
4. If we finish scanning without violations → return `True`.

---

## 🧩 Example
### Example 1:

```
nums = [1,0,0,0,1], k = 2
Distance = 3 - 0 - 1 = 2 → OK
Answer: True
```

### Example 2:
```
nums = [1,0,1], k = 2
Distance = 2 - 0 - 1 = 1 < 2 → Invalid
Answer: False
```

---

## ⏱️ Complexity

- **Time:** O(n) — single pass  
- **Space:** O(1) — uses constant memory

---

## 🔑 Key Insight  
Track only the last seen '1' — the problem reduces to simple distance comparisons.

