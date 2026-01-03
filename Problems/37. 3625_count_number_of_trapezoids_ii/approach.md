# 💡 Problem #3625: Count Number of Trapezoids II
**Link:** [Problem](https://leetcode.com/problems/count-number-of-trapezoids-ii/)

---

## 🧠 Problem Understanding

You are given a set of points on a 2D plane.

A **trapezoid** is formed by:
- Choosing **two distinct pairs of points**
- Such that the two line segments formed are **parallel**
- And the two segments are **not collinear** (i.e., they do not lie on the same line)

Your task is to count the number of distinct trapezoids that can be formed.

---

## ⚙️ Key Observations

### 1️⃣ Parallelism via Slopes
Two line segments are parallel **iff** they have the same slope.

So:
- For every pair of points, compute the **slope** of the line segment.
- Group segments by slope.

---

### 2️⃣ Avoid Collinear Overcounting
Segments with:
- Same slope **and**
- Same intercept

lie on the **same infinite line**, and do **not** form a trapezoid.

So for each slope:
- Count pairs of segments
- Subtract pairs that share the same intercept

---

### 3️⃣ Parallelogram Overcount Correction
A **parallelogram** is counted **twice** as a trapezoid:
- It has two pairs of parallel sides
- Both pairs get counted in the slope grouping

Key property of parallelograms:
- Diagonals share the **same midpoint**
- Opposite sides have **same slope**

So:
- For every pair of points, compute the **midpoint**
- Group slopes by midpoint
- Subtract pairs with same midpoint & slope (these correspond to parallelograms)

---

## 🧩 Algorithm Breakdown

### Step 1: Enumerate all point pairs
For each pair `(i, j)`:
- Compute slope `s`
- Compute line intercept `b`
- Compute midpoint `(x1 + x2, y1 + y2)`

Store:
- `slope → list of intercepts`
- `midpoint → list of slopes`

---

### Step 2: Count parallel segment pairs
For each slope group:
- Let intercept counts be `c1, c2, ...`
- Count pairs from different intercepts:
`sum over i<j of (ci * cj)`

This counts all trapezoids **including parallelograms**.

---

### Step 3: Subtract parallelograms
For each midpoint group:
- Group slopes
- Count slope pairs using the same accumulation method
- Subtract these counts from the total

---

## 🧮 Why This Works

- Parallel sides → slope grouping
- Same line exclusion → intercept grouping
- Parallelogram correction → midpoint + slope grouping

This cleanly separates:
- Valid trapezoids
- Invalid collinear cases
- Overcounted parallelograms

---

## ⏱️ Complexity

Let `n` be number of points.

- Pair enumeration: **O(n²)**
- Hash map processing: **O(n²)**

Total:
- **Time:** O(n²)
- **Space:** O(n²)

---

## 🔑 Key Insight  
Count all parallel segment pairs, then subtract parallelogram cases using midpoint symmetry.
