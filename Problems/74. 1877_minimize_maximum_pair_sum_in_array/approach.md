# 1877. Minimize Maximum Pair Sum in Array

## Problem Statement
Given an array `nums` of even length `n`, pair up the elements into `n / 2` pairs such that:
- Each element is in exactly one pair
- The **maximum pair sum** is minimized

Return the **minimized maximum pair sum**.

---

## Intuition
To minimize the maximum pair sum, we should **balance** the pairs:
- Pair the **smallest** element with the **largest**
- Pair the **second smallest** with the **second largest**
- And so on...

This greedy approach ensures no single pair becomes unnecessarily large.

> 🎯 **Why this works?**  
> If we pair two large numbers together, their sum will dominate the result. By pairing large with small, we "distribute" the large values and keep all pair sums as balanced as possible.

---

## Step-by-Step Approach

1. **Sort the array** in ascending order
- [3, 5, 2, 3] → [2, 3, 3, 5]

2. **Use two pointers**:
- `left` starts at index `0` (smallest)
- `right` starts at index `n-1` (largest)

3. **Form pairs** by adding `nums[left] + nums[right]`
- Pair 1: 2 + 5 = 7
- Pair 2: 3 + 3 = 6

4. **Track the maximum** pair sum encountered
- max_pair_sum = max(7, 6) = 7

5. **Move pointers inward** and repeat until all pairs are formed

6. **Return** the minimized maximum pair sum

---

## Example Walkthrough

**Input:** `nums = [3, 5, 2, 3]`
- Step 1: Sort → [2, 3, 3, 5]
- Step 2: Pair formation:
- i=0: nums[0] + nums[3] = 2 + 5 = 7
- i=1: nums[1] + nums[2] = 3 + 3 = 6
- Step 3: max(7, 6) = 7
- Output: 7
  
**Input:** `nums = [3, 5, 4, 2, 4, 6]`
- Step 1: Sort → [2, 3, 4, 4, 5, 6]
- Step 2: Pair formation:
- 2+6=8, 3+5=8, 4+4=8
- Step 3: max(8, 8, 8) = 8
- Output: 8


---

## Complexity Analysis

| Complexity | Value | Explanation |
|------------|-------|-------------|
| **Time**   | O(n log n) | Sorting dominates; pairing loop is O(n) |
| **Space**  | O(1) or O(n)* | O(1) extra space if sort is in-place; O(n) if language sort creates new array |

> *Python's `sort()` is in-place (Timsort), so auxiliary space is O(1).
