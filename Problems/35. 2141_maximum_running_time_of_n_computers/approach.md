# 💡 Problem #2141: Maximum Running Time of N Computers
**Link:** [Problem](https://leetcode.com/problems/maximum-running-time-of-n-computers/)

---

## 🧠 Problem Understanding

You are given:
- `n` computers
- An array `batteries`, where `batteries[i]` is the capacity of the i-th battery

Rules:
- Each computer needs **one battery at a time**
- Batteries can be swapped between computers at any time
- A battery can power **only one computer at a time**

Goal:
➡️ Find the **maximum number of minutes** all `n` computers can run **simultaneously**.

---

## ⚙️ Key Insight

This is a **binary search on the answer** problem.

Let `T` be the running time we want to check.

For time `T` to be feasible:
- Each battery can contribute **at most `min(battery_capacity, T)` minutes**
- Total available power must satisfy:

`sum(min(bat, T)) ≥ n × T`

If this condition holds, then it’s possible to run all `n` computers for `T` minutes.

---

## 🧩 Binary Search Strategy

### Search Space
- **Lower bound:** `0`
- **Upper bound:** `sum(batteries) // n`
  - Even with perfect distribution, total power limits the maximum time.

### Feasibility Check
For a candidate `mid`:
`if sum(min(bat, mid) for bat in batteries) >= n * mid:`
`mid is feasible`

- If feasible → try a larger time
- If not → reduce time

---

## 🧠 Why This Works

- Feasibility is **monotonic**:
  - If we can run for `T` minutes, we can run for any `T' < T`
- That makes binary search valid
- The `min(bat, T)` cap ensures no battery contributes more than its capacity

---

## 🧮 Example

```
n = 2
batteries = [3, 3, 3]

Total power = 9
Max possible = 9 // 2 = 4

Check T = 4:
min(3,4) + min(3,4) + min(3,4) = 9 ≥ 8 → feasible

Answer = 4
```

---

## ⏱️ Complexity

- **Time:** O(m log S)
  - `m` = number of batteries
  - `S` = sum of battery capacities
- **Space:** O(1)

---

## 🔑 Key Insight  
Binary search the maximum running time, and for each candidate, check feasibility by summing capped battery contributions.
