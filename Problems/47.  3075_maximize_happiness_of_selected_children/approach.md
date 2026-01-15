# 💡 Problem #3075: Maximize Happiness of Selected Children
**Link:** [Problem](https://leetcode.com/problems/maximize-happiness-of-selected-children/)

---

## 🧠 Problem Understanding

You are given:
- An array `happiness`, where `happiness[i]` is the happiness value of the i-th child
- An integer `k`, the number of children you must select

Rules:
- When you select a child, **all remaining children lose 1 happiness**
- Happiness cannot go below 0

Goal:
➡️ Maximize the **total happiness** of the `k` selected children.

---

## ⚙️ Key Insight

To maximize total happiness:
- Always pick the child with the **highest current happiness**
- Since every selection reduces future happiness by 1, the `i`-th pick loses exactly `i` happiness

So for the child chosen at index `i`:
`effective_happiness = max(0, happiness[i] - i)`

---

## 🧩 Greedy Strategy

1. Sort the `happiness` array in **descending order**
2. Select the top `k` children
3. For each selected child at index `i`:
   - Add `max(0, happiness[i] - i)` to the total

This greedy approach is optimal because:
- High initial happiness suffers less relative loss
- Selecting lower happiness earlier only reduces future gains

---

## 🧮 Example

```
happiness = [5,3,2], k = 2

Sorted: [5,3,2]

Pick 5 → contributes 5
Pick 3 → contributes 3 - 1 = 2

Total = 7
```

---

## 🧠 Why This Works

- The happiness reduction depends only on the number of picks so far
- Sorting ensures we always reduce the **largest values last**
- No dynamic programming is needed

---

## ⏱️ Complexity

- **Time:** O(n log n)
- **Space:** O(1) (in-place sort)

---

## 🔑 Key Insight  
Pick children in descending happiness order and subtract the number of prior selections — a clean greedy solution.
