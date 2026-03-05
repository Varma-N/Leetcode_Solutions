# 💡 Problem #3650: Minimum Cost Path with Edge Reversals
**Link:** https://leetcode.com/problems/minimum-cost-path-with-edge-reversals/

---

## 🧠 Problem Understanding

You are given:
- `n` nodes labeled `0 → n-1`
- A list of directed edges `[u, v, w]`

Each edge represents:
- A normal direction from `u → v` with cost `w`

However, you are also allowed to **reverse the direction** of an edge.
If you reverse the edge, the cost becomes:

`2 × w`

Goal:

Find the **minimum cost** to travel from node `0` to node `n-1`.

If it is impossible, return `-1`.

---

## ⚙️ Key Insight

Instead of dynamically reversing edges during traversal, we can **pre-build the graph** with both possibilities:

For every edge:
`u → v with cost w`
`v → u with cost 2w`


This converts the problem into a **standard shortest path problem**.

---

## 🧩 Algorithm Strategy

1. Build an adjacency list:
   - `(u → v, cost = w)`
   - `(v → u, cost = 2w)`  (representing reversal)

2. Use **Dijkstra's algorithm** to compute the shortest path.

3. Maintain:
`dist[i] = minimum cost to reach node i`

4. Use a **priority queue (min-heap)** to always process the lowest-cost node first.

5. Stop early if node `n-1` is reached.

---

## 🧮 Example (Conceptual)
```
Edge: 0 → 1 (cost 5)

Graph becomes:

0 → 1 (cost 5)
1 → 0 (cost 10)
```

Dijkstra then naturally chooses the cheaper option.

---

## ⏱️ Complexity

Let:
`V = number of nodes`
`E = number of edges`

Time:
`O(E log V)`

Space:
`O(V + E)`

---

## 🔑 Key Insight
Model edge reversal as an additional edge with double cost and solve using Dijkstra’s shortest path algorithm.
