# Maximum Matrix Sum - Approach

## Problem Overview
Given an `n x n` integer matrix, you may perform any number of operations where each operation selects two adjacent cells (sharing a side) and multiplies both values by `-1`. The goal is to maximize the sum of all elements in the matrix after performing operations.

## Key Insight
Each operation flips the signs of exactly two elements simultaneously, which leads to two critical observations:

1. **Parity Preservation**: The parity (even/odd count) of negative numbers remains invariant under any sequence of operations. Flipping two signs changes the negative count by -2, 0, or +2—all even changes.

2. **Sign Mobility**: Through chained operations across adjacent cells, negative signs can be effectively "transported" to any position in the matrix since the grid forms a connected graph.

## Step-by-Step Approach

### Step 1: Single-Pass Matrix Analysis
Traverse every element in the matrix exactly once to compute three essential values:
- **Sum of absolute values (`total`)**: Accumulate the absolute value of each element. This represents the theoretical maximum sum achievable if all elements could be made positive.
- **Negative count (`negative_count`)**: Track the total number of negative elements in the original matrix.
- **Minimum absolute value (`min_abs`)**: Identify the smallest absolute value across all elements in the matrix.

### Step 2: Parity-Based Decision
Determine the optimal sign configuration based on the parity of `negative_count`:
- **Even negative count**: All negative values can be eliminated through paired operations. The maximum achievable sum equals `total`.
- **Odd negative count**: Exactly one negative value must remain (due to parity constraint). To maximize the total sum, this negative should be assigned to the element with the smallest absolute value. The maximum sum becomes `total - 2 × min_abs` (converting a positive `min_abs` to negative `-min_abs` reduces the total sum by `2 × min_abs`).

### Step 3: Result Calculation
Apply the parity-based formula to compute and return the maximum possible sum of the matrix.

## Why This Works
- When the negative count is even, negatives can be perfectly paired and eliminated through operations (e.g., flip adjacent negatives to positives).
- When the negative count is odd, we can concentrate all negative signs into a single element via sign transportation across the grid. Choosing the element with the smallest absolute value minimizes the penalty to the total sum.
- The adjacency constraint does not limit sign mobility in a connected grid—any sign can be moved to any position through a sequence of operations.

## Complexity Analysis

- **Time Complexity**: O(n²)  
  Single traversal of all n² elements in the matrix.

- **Space Complexity**: O(1)  
  Only three scalar variables used (`total`, `negative_count`, `min_abs`), independent of input size.
