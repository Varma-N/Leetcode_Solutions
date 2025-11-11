# 💡 Problem #1578: Minimum Time to Make Rope Colorful
**Link:** [LeetCode #1578](https://leetcode.com/problems/minimum-time-to-make-rope-colorful/)

---

## 🧠 Approach

### 🔍 Problem Understanding
You’re given:
- A string `colors` where each character represents the color of a balloon on a rope.
- An integer array `neededTime` where `neededTime[i]` is the time required to remove the `i-th` balloon.

You must remove balloons so that **no two consecutive balloons have the same color**, while **minimizing the total removal time**.

---

### ⚙️ Intuition
If two or more **consecutive balloons** have the same color, we need to remove all but one of them.  
To minimize total time:
- **Keep the balloon** that takes the **maximum time to remove**, and
- **Remove all others** in that color group.

This ensures we spend the least possible total time.

---

### 🧩 Step-by-Step Logic
1. Traverse the `colors` string using two pointers:  
   - `i` → start of the group of same-colored balloons  
   - `j` → used to move through the group
2. For each group of same colors:
   - Calculate the total removal time (`total_time`)
   - Track the maximum single removal time (`max_time`)
3. The cost for that group = `total_time - max_time`  
   (since we remove all except the one that takes the most time)
4. Add that to the global `total_cost`.
5. Move `i` to the start of the next color group and repeat.

---

### 🧮 Example Walkthrough

**Input:**

```
colors = "abaac"
neededTime = [1, 2, 3, 4, 5]
```

**Step-by-step:**
```
'a' (index 0) → next is 'b' → no repeat → cost = 0

'b' (index 1) → next is 'a' → no repeat → cost = 0

'a', 'a' (indices 2,3) → repeated → total_time = 3+4 = 7, max_time = 4
→ remove one balloon → add (7 - 4) = 3 to total_cost

'c' (index 4) → single → cost = 0
```

✅ **Total Cost = 3**

---

### 🧠 Why This Works
- Greedy works because decisions for each color group are independent.
- We only care about minimizing time *within each same-color segment*.

---

### ⏱️ Time Complexity
- **O(n)** — single pass through the rope.
- Each balloon is processed exactly once.

### 💾 Space Complexity
- **O(1)** — only uses a few counters and pointers.

---

✅ **Key Insight:**  
To minimize time, always **keep the most expensive balloon** in each color group and **remove the rest**.
