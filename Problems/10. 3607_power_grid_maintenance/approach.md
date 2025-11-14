# 💡 Problem #3607: Power Grid Maintenance
**Link:** https://leetcode.com/problems/power-grid-maintenance/  

---

## 🧠 Problem Understanding

You are given:

- `c` → number of stations labeled `1..c`
- `connections` → undirected edges representing wires between stations
- `queries`:
  - `[1, x]` → Request the smallest *online* station in x’s connected component  
  - `[2, x]` → Take station x offline

A station that is offline **cannot** be returned as an answer, even if it's the smallest.

If no online station exists in the component, return `-1`.

---

## ⚙️ Key Observations

### 1️⃣ Connected components **never change**
Stations only go offline — connections never change.  
So we can precompute all connected components **once**.

### 2️⃣ Each component needs fast access to:
- The **smallest online station**  
- This can be done using a **min-heap** per component

### 3️⃣ Lazy Deletion
When a station goes offline:
- We DO NOT remove it immediately from the heap  
- Instead, when query type 1 checks the heap top:
  - Pop stations while they are offline  
  - Eventually, the top is the smallest *online* station

### 4️⃣ Query Complexity
- Component search: **O(1)**
- Heap cleanup: amortized **O(log n)**
- Very efficient for large inputs

---

## 🧩 Step-by-Step Solution Outline

### ✔️ Step 1: Build adjacency list  
Create `graph[u] → neighbors`.

### ✔️ Step 2: Find all connected components  
Use DFS to build:
- `comp_groups`: list of components (each is list of nodes)
- `comp_index_of_node[i]`: maps each station to its component index

### ✔️ Step 3: Create a min-heap for each component  
Each heap stores its stations, sorted by value.

### ✔️ Step 4: Maintain an `offline[]` array  
If a station is turned offline, mark it.

### ✔️ Step 5: Process queries  
#### • Type 2 → `offline[x] = True`  
#### • Type 1:
- If x is online → return x
- Else:
  - Look at x’s component heap
  - Pop until the top is online
  - If heap empty → return -1  
  - Else → return heap[0]

---

## ⏱️ Time Complexity

### Preprocessing
- Building components via DFS: **O(c + edges)**

### Per Query
- Type 1: amortized **O(log c)**  
- Type 2: **O(1)**

### Total
**O((c + edges) + q log c))** — very efficient.

---

## 💾 Space Complexity
- Graph adjacency list: **O(c + edges)**
- Component mapping and heaps: **O(c)**
- Offline array: **O(c)**

---

## 🧠 Key Insight
Precompute connected components and use a **min-heap with lazy deletion** to efficiently answer "find smallest online station in component" queries under dynamic offline updates.
