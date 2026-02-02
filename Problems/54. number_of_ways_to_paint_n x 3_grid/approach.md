# 1411. Number of Ways to Paint N × 3 Grid

## 🧩 Problem Overview

You are given an `n × 3` grid and 3 different colors.  
Your task is to count the number of ways to paint the grid such that:

- No two adjacent cells in the **same row** have the same color
- No two adjacent cells in the **same column** have the same color

Return the number of valid ways modulo **10⁹ + 7**.

---

## 💡 Key Insight

Each row can be painted in only **two valid pattern types**:

### 1. Type A (ABA pattern)
- The first and third cells have the **same color**
- The middle cell has a **different color**
- Example: `Red, Blue, Red`
- Total possibilities per row: **6**

### 2. Type B (ABC pattern)
- All three cells have **different colors**
- Example: `Red, Blue, Green`
- Total possibilities per row: **6**

We use **dynamic programming** to track how many ways we can build the grid row by row using these two pattern types.

---

## 🔁 State Transitions

Let:
- `a` = number of ways where the previous row is **Type A**
- `b` = number of ways where the previous row is **Type B**

For each new row:

- A new **Type A** row can follow:
  - 3 Type A rows
  - 2 Type B rows  
`new_a = 3a + 2b`

- A new **Type B** row can follow:
- 2 Type A rows
- 2 Type B rows  
`new_b = 2a + 2b`

All operations are done modulo `10⁹ + 7`.

---

## 🚀 Algorithm

1. Initialize:
 - `a = 6` (Type A patterns for row 1)
 - `b = 6` (Type B patterns for row 1)
2. Iterate from row 2 to row `n`
3. Update `a` and `b` using the transition formulas
4. Return `a + b`

---

## 🧠 Time & Space Complexity

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)` (constant space)
