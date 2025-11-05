# Problem: 3354. Make Array Elements Equal to Zero
🔗 [LeetCode Link](https://leetcode.com/problems/make-array-elements-equal-to-zero/)

### 🗓️ Solved On
October 28, 2025 - Day 1 of my LeetCode streak 🎯

---

### 💡 Approach

The problem involves simulating operations on an array where selecting a position with value `0` triggers movement in one direction (left or right), alternating each time we reduce a non-zero element.

#### Key Steps:
1. For every index `i` where `nums[i] == 0`, try two simulations:
   - Move **left first** (`direction = -1`)
   - Move **right first** (`direction = +1`)
2. In each simulation:
   - If current element is non-zero, decrement it and flip direction.
   - If it’s zero, just move in the same direction.
   - Stop when the pointer goes out of bounds.
3. If all elements become `0` after simulation, count that direction as **valid**.

#### Example
Input: `nums = [0,1,1]`  
Simulation starting from index `0`:
- Move right → reduce elements alternately until all zeros.  
Valid simulation count = 2.

---

### 🧮 Complexity
- **Time Complexity:** O(n²) (worst case for simulation)
- **Space Complexity:** O(n) (copying array per simulation)

---

### 🧠 Intuition
This brute-force simulation ensures correctness by exploring every possible valid path.  
Though not optimal, it’s perfectly fine for the problem’s constraints and clear to reason about.

---

### ✅ Result
Returns the total number of valid starting positions/directions that lead to all elements becoming zero.
