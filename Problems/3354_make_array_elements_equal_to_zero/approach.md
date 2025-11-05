# 💡 Problem #3354: Make Array Elements Equal to Zero
**Link:** [LeetCode #3354](https://leetcode.com/problems/make-array-elements-equal-to-zero/)

---

## 🧠 Approach

1. Iterate through every index `i` in the array.
2. If `nums[i]` is `0`, simulate two directions:
   - Left (`-1`)
   - Right (`+1`)
3. Each simulation works like this:
   - Create a copy of the array (`arr = nums[:]`).
   - Move from the starting position in the given direction.
   - If the current element is zero, move forward in the same direction.
   - If it’s non-zero, decrease it by 1 and reverse the direction.
   - Continue until the pointer goes out of array bounds.
4. After finishing the simulation, check if all elements became zero.
5. Count all valid directions that successfully make the array zero.

---

## ⏱️ Time Complexity
O(n²) — because for each starting index, we simulate up to `n` steps in the worst case.

## 💾 Space Complexity
O(n) — due to array copy for each simulation.

---

✅ This approach simulates all possible valid starting points and ensures correctness through direction reversal.
