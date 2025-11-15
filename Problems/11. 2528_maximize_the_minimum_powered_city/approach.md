# 💡 Problem #2528: Maximize the Minimum Powered City
**Link:** https://leetcode.com/problems/maximize-the-minimum-powered-city/

---

## 🧠 Problem Understanding

You are given:
- `stations[i]`: initial power of a station at city `i`
- Each station affects cities within radius `r`
- You may build **k additional stations** anywhere
- Your goal: **maximize the minimum total power across all cities**

A city's total power =  
`sum of stations in range [i - r, i + r]`

---

## ⚙️ Core Insight

This is a classic:

**“Binary search the answer + greedy validation using a difference array”** problem.

Why?

We want to check:  
❓ *Is it possible to make every city have power ≥ X using at most k new stations?*  

If YES → try a higher X  
If NO → lower X

This forms a monotonic property → ideal for **binary search**.

---

## 🧩 Step-by-Step Strategy

### 1️⃣ Precompute initial power for each city
For each city `i`, compute the total power contributed by stations in `[i - r, i + r]`.

Use a sliding window to compute this in **O(n)**.

---

### 2️⃣ Binary Search on the Answer
The minimum possible power is `min(power)`.  
The maximum possible power is `max(power) + k`.

Binary search the answer between `[low, high]`.

---

### 3️⃣ `canAchieve(target)` — Greedy Check
For each city in order:
- Track how much added station power is currently affecting it using a **difference array**.
- Compute effective power = initial power + accumulated additions.
- If it’s < target:
  - We must add new stations.
  - Add exactly enough stations to hit the target.

Where do we add them?
- Place additions at city `i + r`, the **furthest possible city whose station still covers city i**.
- Use difference array to apply its effect until `(i + r) + r`.

Track total stations used → must not exceed k.

This check runs in **O(n)**.

---

## 🧠 Why This Works

### ✔️ Binary search gives us the optimal target minimum.  
### ✔️ Difference array allows us to simulate station placement efficiently.  
### ✔️ Greedy strategy ensures minimal required additions are used at each step.  
### ✔️ Overall complexity is **O(n log k)** — perfect for constraints.

---

## ⏱️ Time Complexity
- Sliding window preprocessing: **O(n)**
- Each binary search check: **O(n)**
- Total: **O(n log( maxPower ))**

## 💾 Space Complexity
- **O(n)** for the difference array

---

## ⭐ Key Insight
By always placing new stations at the furthest possible city that still covers the current weak city, we guarantee minimal resource usage — enabling a greedy optimal strategy.
