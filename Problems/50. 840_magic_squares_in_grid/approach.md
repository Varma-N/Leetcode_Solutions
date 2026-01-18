# 💡 Problem #840: Magic Squares In Grid
**Link:** [Problem](https://leetcode.com/problems/magic-squares-in-grid/)

---

## 🧠 Problem Understanding

You are given a 2D grid of integers.

A **3×3 magic square** must satisfy **all** of the following:

1. It contains **all numbers from 1 to 9 exactly once**
2. The sum of:
   - Each row
   - Each column
   - Both diagonals  
   is **15**

Your task is to count how many **3×3 subgrids** inside the given grid are magic squares.

---

## ⚙️ Key Observations

- The smallest magic square is **exactly 3×3**
- Any valid 3×3 magic square using numbers `1..9` must sum to **15**
- The center of a valid magic square is always **5** (optional optimization, not required)

---

## 🧩 Strategy

1. Slide a **3×3 window** across the grid
2. For each window:
   - Check uniqueness and range of numbers (`1..9`)
   - Check row sums
   - Check column sums
   - Check both diagonals
3. Count how many windows satisfy all conditions

---

## 🧩 Detailed Checks

### 1️⃣ Valid Numbers
- All values must be between `1` and `9`
- No duplicates allowed

### 2️⃣ Rows
`grid[i+r][j] + grid[i+r][j+1] + grid[i+r][j+2] == 15`

### 3️⃣ Columns
`grid[i][j+c] + grid[i+1][j+c] + grid[i+2][j+c] == 15`

### 4️⃣ Diagonals
`grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] == 15`
`grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j] == 15`

---

## 🧮 Example
```
grid = [
[4,3,8,4],
[9,5,1,9],
[2,7,6,2]
]

There is exactly 1 magic square:
[
[4,3,8],
[9,5,1],
[2,7,6]
]
```

---

## 🧠 Why This Works

- Constraints are small enough to allow brute-force checking
- Each 3×3 window is independent
- Explicit validation avoids false positives

---

## ⏱️ Complexity

- **Time:** O(m × n)
  - Each 3×3 check is constant work
- **Space:** O(1)

---

## 🔑 Key Insight  
A magic square is defined by strict numeric and sum constraints — validating them directly is the safest approach.
