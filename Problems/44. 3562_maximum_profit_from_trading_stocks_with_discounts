# 💡 Problem #3562: Maximum Profit from Trading Stocks with Discounts
**Link:** [Problem](https://leetcode.com/problems/maximum-profit-from-trading-stocks-with-discounts/)

---

## 🧠 Problem Understanding

You are given:

- `n` employees arranged in a **hierarchy tree**
- Each employee has:
  - `present[i]`: current stock price
  - `future[i]`: future stock price
- If a manager buys stock, their **direct subordinates get a 50% discount**
- A total **budget** limits how much you can spend

Goal:
➡️ **Maximize total profit** while respecting:
- Hierarchical discount rules
- Budget constraint
- You may choose to buy or skip any employee’s stock

---

## ⚙️ Key Challenges

1. Decisions are **dependent**:
   - Buying a manager affects children’s prices
2. Structure is a **tree**, not a flat list
3. Budget introduces a **knapsack constraint**
4. Must consider:
   - Buy current employee or not
   - How that choice affects children

This is a classic **Tree DP + Knapsack Merge** problem.

---

## 🧩 DP State Definition

Define a recursive DP on the tree:
`dfs(node, boss_bought) → dp array`

Where:
- `boss_bought` ∈ {True, False}
- `dp[cost]` = maximum profit achievable in the subtree rooted at `node`
  using exactly `cost` money

---

## 🧱 Base Case

If the node has **no children**:
- Either:
  - Don’t buy → cost = 0, profit = 0
  - Buy → cost = price, profit = future − price

Price depends on `boss_bought`.

---

## 🔄 Transitions

For each node, consider **two scenarios**:

---

### 1️⃣ Node NOT bought

- Cost = 0
- Profit = 0
- Children do **not** receive discount
- Merge children DP arrays assuming `boss_bought = False`

This is a **multi-knapsack merge** over children.

---

### 2️⃣ Node IS bought

- Cost = discounted or full price
- Profit = `future − price`
- Children receive discount → `boss_bought = True`
- Merge children DP arrays under discounted condition

---

### 🔀 Final Merge

For every possible cost:
`dp[cost] = max(dp_not_bought[cost], dp_bought[cost])`

---

## ⚙️ Optimization Techniques Used

- **Memoization (`lru_cache`)** to avoid recomputation
- **Tuple DP storage** to allow caching
- **Bottom-up knapsack merging**
- **Negative infinity sentinel** to mark invalid states

---

## 🧮 Final Answer

- Start DFS from the root (CEO)
- CEO has no boss → `boss_bought = False`
- Take the **maximum profit** from the resulting DP array

---

## ⏱️ Complexity

Let:
- `n` = number of nodes
- `B` = budget

### Time:
- Worst-case: `O(n × B²)` due to knapsack merges

### Space:
- `O(n × B)` for DP storage

This is acceptable given constraints and unavoidable due to dependency structure.

---

## 🔑 Key Insight

This problem combines:
- **Tree DP**
- **State dependency**
- **Knapsack merging**

The correct solution requires modeling *buy vs skip* decisions at every node while propagating discount effects downward — a true systems-level DP problem.
