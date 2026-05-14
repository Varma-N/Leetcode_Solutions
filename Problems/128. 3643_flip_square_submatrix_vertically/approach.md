# Flip Square Submatrix Vertically

This document outlines the algorithmic approach to flipping a square submatrix vertically within a given 2D grid.

## Problem Description
Given a 2D grid, the goal is to flip a square submatrix of size $k \times k$ vertically. The submatrix is defined by its top-left corner at coordinates $(x, y)$.

## Step-by-Step Approach

1.  **Identify Submatrix Boundaries**: 
    Determine the range of rows and columns that constitute the submatrix.
    - The rows range from index $x$ to $x + k - 1$.
    - The columns range from index $y$ to $y + k - 1$.

2.  **Initialize Row Pointers**: 
    Set up two pointers (or indices) to manage the vertical flip:
    - A `top` pointer starting at the first row of the submatrix ($x$).
    - A `bottom` pointer starting at the last row of the submatrix ($x + k - 1$).

3.  **Vertical Swap Iteration**: 
    Iterate while the `top` pointer is less than the `bottom` pointer:
    - This ensures that we only swap rows until we reach the middle of the submatrix.

4.  **Column-wise Element Exchange**: 
    For each pair of rows pointed to by `top` and `bottom`, iterate through every column within the submatrix's column boundaries (from $y$ to $y + k - 1$).
    - Swap the element at `grid[top][column]` with the element at `grid[bottom][column]`.

5.  **Update Pointers**: 
    After swapping all elements in the current row pair:
    - Increment the `top` pointer to move toward the center.
    - Decrement the `bottom` pointer to move toward the center.

6.  **Return Result**: 
    Once the pointers meet or cross, the vertical flip of the submatrix is complete. Return the modified grid.

## Complexity Analysis

### Time Complexity
**O(k²)**
- The algorithm iterates through half of the rows in the $k \times k$ submatrix ($rac{k}{2}$).
- For each row pair, it iterates through all $k$ columns to perform the swap.
- Total operations are proportional to $rac{k}{2} \times k$, which simplifies to $O(k^2)$.

### Space Complexity
**O(1)**
- The flip is performed in-place. No additional data structures that scale with the input size are used, excluding the space required for the output (if the grid is modified in-situ).
