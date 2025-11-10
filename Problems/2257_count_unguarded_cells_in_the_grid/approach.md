# 💡 Problem #2257: Count Unguarded Cells in the Grid
**Link:** [LeetCode #2257](https://leetcode.com/problems/count-unguarded-cells-in-the-grid/)

---

## 🧠 Approach

### 🔍 Problem Understanding
You are given:
- A grid of size `m x n`.
- A list of guard positions.
- A list of wall positions.

Each **guard** can see (guard) cells in all **four directions** — up, down, left, and right — until their vision is blocked by a **wall** or another **guard**.

We must count how many cells are **unguarded** after all guards mark their visible areas.

---

### ⚙️ Intuition
1. Represent the grid as a 2D matrix.
2. Mark:
   - `'W'` for walls,
   - `'G'` for guards,
   - `'.'` for empty cells.
3. For every guard, simulate visibility in all 4 directions:
   - Continue marking cells as `'V'` (visible) until:
     - You reach a wall or another guard, or
     - You go out of grid bounds.
4. After processing all guards, count cells that remain `'.'` (unguarded).

---

## 🧩 Step-by-Step Example
### Example:
**Input:**

```
m = 4, n = 6
guards = [[0,0],[1,1],[2,3]]
walls = [[0,1],[2,2],[1,4]]
```
### Step 1 — Initial grid
```
G W . . . .
. G . . W .
. . W G . .
. . . . . .
```

### Step 2 — Simulate guard visibility
Guards mark visible cells in all 4 directions until blocked.

After marking:

```
G W V V . .
. G V V W .
. V W G V V
V V V V V V
```

### Step 3 — Count unguarded cells
Count remaining `'.'` → those are unguarded.

✅ **Output:** `7`

---

## 🧠 Why This Works
- Simulation ensures every cell's status is tracked accurately.  
- Using `'V'` for visible cells avoids double-counting.  
- Boundaries and blocking rules are straightforward with direction vectors.

---

## ⏱️ Time Complexity
- **O(m × n × 4)** in the worst case, since each guard can scan the full grid in four directions.
  (Practically faster due to early blocking.)
- **O(m × n)** space for the grid representation.

---

## 💾 Space Complexity
- **O(m × n)** for the grid matrix.

---

✅ **Key Insight:**  
By explicitly simulating each guard’s line of sight, we can accurately count unguarded cells without complex math or prefix structures.
