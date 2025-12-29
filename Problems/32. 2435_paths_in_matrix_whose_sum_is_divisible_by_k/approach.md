# 💡 Problem #2435: Paths in Matrix Whose Sum Is Divisible by K
**Link:** [Problem](https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/)

---

## 🧠 Problem Understanding

You are given:
- A 2D grid `grid` of size `m × n`
- An integer `k`

You start at the **top-left cell (0,0)** and want to reach the **bottom-right cell (m-1,n-1)**.

Rules:
- You may move **only right or down**
- The **sum of values** along the path must be **divisible by `k`**

Return the **number of such paths**, modulo **10⁹ + 7**.

---

## ⚙️ Key Insight

A path’s divisibility by `k` depends **only on the remainder modulo `k`**, not the full sum.

So instead of tracking full sums, we track:
`(sum % k)`

This leads to a **3D dynamic programming** solution.

---

## 🧩 Dynamic Programming State

Define:
`dp[i][j][r] = number of paths to cell (i, j)`
`such that path sum % k == r`

- `i` → row index
- `j` → column index
- `r` → remainder modulo `k`

---

## 🧱 Initialization

At the starting cell `(0,0)`:
`dp[0][0][grid[0][0] % k] = 1`

There is exactly one way to start, with remainder equal to the value at the first cell.

---

## 🔄 Transitions

To reach cell `(i, j)` with value `grid[i][j]`:

### From the top `(i-1, j)`:
`dp[i][j][(r + grid[i][j]) % k] += dp[i-1][j][r]`

### From the left `(i, j-1)`:
`dp[i][j][(r + grid[i][j]) % k] += dp[i][j-1][r]`

All updates are taken modulo **10⁹ + 7**.

---

## 🎯 Final Answer

We want paths ending at `(m-1, n-1)` whose sum is divisible by `k`:
`dp[m-1][n-1][0]`

---

## 🧮 Example

```
grid = [[5,2,4],
[3,0,5],
[0,7,2]]
k = 3
```

We count all right/down paths whose sum % 3 == 0.

---

## ⏱️ Complexity

- **Time:** O(m × n × k)
- **Space:** O(m × n × k)

---

## 🔑 Key Insight  
Track path sums **by remainder modulo k** instead of full sums — this makes the problem tractable with DP.

