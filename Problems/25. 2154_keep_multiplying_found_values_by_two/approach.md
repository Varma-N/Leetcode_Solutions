# 💡 Problem #2154: Keep Multiplying Found Values by Two
**Link:** https://leetcode.com/problems/keep-multiplying-found-values-by-two/

---

## 🧠 Problem Understanding

You are given:
- A list of integers `nums`
- An integer `original`

Process:
- If `original` appears in `nums`, multiply it by **2**
- Repeat this until `original` is no longer in `nums`
- Return the final value

This problem is a straightforward simulation task.

---

## ⚙️ Key Insight

Each time `original` is found inside the array:
- It should be doubled
- This new value is then checked again

This continues until the value stops appearing in the list.

This is direct, with no trick or greedy structure needed.

---

## 🧩 Example

Input:
`nums = [5,3,6,1,12]`
`original = 3`

Process:
```
3 → found → double → 6
6 → found → double → 12
12 → found → double → 24
24 → not found → stop
```
Answer:
24

---

## 🧠 Optimization Note

Checking `original in nums` is `O(n)`.

If needed, we could improve this by converting to a set for `O(1)` lookup:
`num_set = set(nums)`
`while original in num_set:`
`original *= 2`

But constraints are small enough that the simple version is perfectly fine.

---

## ⏱️ Time Complexity

### Current implementation
- `O(n × k)` where `k` = number of times doubling occurs

### Optimized (set-based)
- `O(n + k)`

Space:  
- O(1) for list-based version  
- O(n) for set-based version (optimized)

---

## 🔑 Key Insight  
Simply keep doubling until the number disappears — no extra structure needed.
