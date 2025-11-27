# 💡 Problem #2154: Keep Multiplying Found Values by Two
**Link:** https://leetcode.com/problems/keep-multiplying-found-values-by-two/

---

## 🧠 Problem Understanding

You are given:
- An integer array `nums`
- An integer `original`

Your task:
- While `original` exists in `nums`, multiply it by 2.
- Return the final value after this repeated doubling.

---

## ⚙️ Key Insight

This is a **direct simulation** problem.

Steps:
1. Check if `original` is present in `nums`.
2. If yes → multiply it by 2.
3. Repeat until `original` is not found in the array.
4. Return the final number.

Observations:
- No trick or optimization is required.
- Searching with `in` works since constraints are small.
- For better efficiency, converting `nums` to a set gives O(1) lookups.

---

## 🧩 Example
### Example:
```
nums = [5,3,6,1,12]
original = 3
3 in nums → multiply → 6
6 in nums → multiply → 12
12 in nums → multiply → 24
24 not in nums → stop

Output = 24
```

---

## ⏱️ Complexity

### Using list search (your implementation)
- Worst-case: O(n × number_of_doublings)

### Using a set (optimized option)
- O(n) preprocessing + O(#doublings) lookup

Space: O(1) for list method, O(n) for optional set.

---

## 🔑 Key Insight  
Just simulate the process — this is a straightforward iterative doubling check.

