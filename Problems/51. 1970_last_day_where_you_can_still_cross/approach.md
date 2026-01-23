# 💡 Problem #1970: Last Day Where You Can Still Cross
**Link:** [Problem](https://leetcode.com/problems/last-day-where-you-can-still-cross/)

---

## 🧠 Problem Understanding

You are given:
- A grid of size `row × col`
- A list `cells`, where `cells[i] = [r, c]` means that cell `(r, c)` becomes **water** on day `i + 1`

Rules:
- You start at the **top row**
- You want to reach the **bottom row**
- You can only move through **land**
- You may move in **4 directions**

Goal:
➡️ Find the **latest day** such that it is still possible to cross from the top row to the bottom row.

---

## ⚙️ Key Insight

Instead of simulating flooding day-by-day forward (which is hard to undo), we **reverse the process**:

- Start with the grid **fully flooded**
- Add land **backwards**, from the last day to the first
- The moment the **top row connects to the bottom row**, that day is the answer

This turns the problem into a **dynamic connectivity** problem.

---

## 🧩 Why Union-Find (DSU)?

We need to efficiently:
- Merge adjacent land cells
- Check whether **any path exists** from top to bottom

Union-Find supports both operations in near O(1) time.

---

## 🧱 DSU Setup

- Each cell is mapped to a unique ID:
`id = r * col + c`
- Add two **virtual nodes**:
- `TOP` → connected to all land cells in row 0
- `BOTTOM` → connected to all land cells in last row

If:
`find(TOP) == find(BOTTOM)`
then a crossing exists.

---

## 🔄 Algorithm Steps

1. Convert `cells` to **0-based indexing**
2. Initialize grid as all **water**
3. Initialize Union-Find with:
   - `row * col + 2` nodes
4. Process days **in reverse**:
   - Turn current cell into land
   - Union with neighboring land cells
   - Union with `TOP` or `BOTTOM` if applicable
5. When `TOP` and `BOTTOM` become connected → return current day

---

## 🧮 Example (Conceptual)

```
Forward:
Day 1 → flood
Day 2 → flood
Day 3 → flood ❌ (no path)

Reverse:
Add land from Day 3 → no path
Add land from Day 2 → no path
Add land from Day 1 → path exists ✅
```

Answer = **Day 1**

---

## 🧠 Why This Works

- Connectivity is **monotonic** in reverse:
  - Once a path exists, it will exist for all earlier days
- Reverse processing avoids complex backtracking
- Virtual nodes simplify top-to-bottom connectivity checks

---

## ⏱️ Complexity

- **Time:** O((row × col) α(row × col))
- **Space:** O(row × col)

Where `α` is the inverse Ackermann function (effectively constant).

---

## 🔑 Key Insight  
Reverse the flooding process and use Union-Find to detect the first moment top and bottom connect.
