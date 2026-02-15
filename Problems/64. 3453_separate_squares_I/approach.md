# 3453. Separate Squares I

## 🧠 Problem Approach

We are given multiple axis-aligned squares on a 2D plane.  
Each square is defined by:
- `x` → left coordinate (not needed for this problem)
- `y` → bottom coordinate
- `l` → side length

Our goal is to find a **horizontal line (y = constant)** such that the **total area of all squares below the line equals half of the total area**.

---

## 🚀 Step-by-Step Approach

### 1. Compute Total Area
- Each square contributes an area of `l × l`.
- Sum the areas of all squares.
- The target area is `total_area / 2`.

---

### 2. Define Binary Search Range
- The lowest possible line is the **minimum `y`** among all squares.
- The highest possible line is the **maximum `y + l`** among all squares.
- The answer must lie within this vertical range.

---

### 3. Helper Function: `area_below(y_line)`
For a given horizontal line `y = y_line`, calculate how much area lies below it:

For each square:
- If the line is **below the square**, it contributes `0`.
- If the line is **above the square**, it contributes its full area `l²`.
- If the line cuts through the square, it contributes:`(y_line - y) × l`

Sum contributions from all squares.

---

### 4. Binary Search for the Exact Line
- Perform binary search on the `y`-axis.
- At each midpoint:
- Compute area below the line.
- If area < target → move the line upward.
- Otherwise → move the line downward.
- Repeat enough iterations (e.g., 60) to ensure precision up to `1e-5`.

---

### 5. Return the Result
- The final `y` value after binary search is the required horizontal separation line.

---

## ⏱️ Time Complexity

- Let `n` be the number of squares.
- Each binary search iteration processes all squares: **O(n)**.
- Fixed number of iterations (≈60).

**Overall Time Complexity:** 
`O(n)`

---

## 💾 Space Complexity

- Only constant extra space is used.

**Overall Space Complexity:**  
`O(1)`
