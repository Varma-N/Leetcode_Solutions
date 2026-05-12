# 3070. Count Submatrices with Top-Left Element and Sum Less Than k

## Step-by-Step Approach

This algorithm utilizes an in-place 2D Prefix Sum technique to efficiently calculate the sum of submatrices originating from the top-left corner. 

1.  **Initialization:** Determine the dimensions of the grid ($m$ rows and $n$ columns) and initialize a counter variable (`count`) to keep track of the valid submatrices.
2.  **Iterate Through the Grid:** Loop through each cell in the matrix row by row, and column by column.
3.  **Calculate Boundary Values:** For the current cell at `(i, j)`, identify the prefix sums of its immediate neighbors:
    *   **Top:** The value directly above (`i-1, j`). Treat as $0$ if out of bounds.
    *   **Left:** The value directly to the left (`i, j-1`). Treat as $0$ if out of bounds.
    *   **Diagonal:** The value to the top-left (`i-1, j-1`). Treat as $0$ if out of bounds.
4.  **Compute 2D Prefix Sum:** Update the current cell's value to represent the total sum of the submatrix from `(0, 0)` to `(i, j)`. This is done using the inclusion-exclusion principle: 
    *   `New Value = Original Value + Top + Left - Diagonal`
    *   *Note: We subtract the diagonal because its area was added twice (once in 'Top' and once in 'Left').*
5.  **Evaluate Against k:** Check if this newly calculated submatrix sum is less than or equal to $k$.
    *   **If valid ($\le k$):** Increment the `count` by $1$.
    *   **If invalid ($> k$):** Break out of the current row's loop. Because the matrix contains non-negative integers, moving further to the right in the same row will only increase the sum. Breaking early optimizes the execution time.
6.  **Return Result:** After iterating through the necessary parts of the grid, return the final `count`.

## Time and Space Complexity

*   **Time Complexity:** $\mathcal{O}(m \times n)$
    In the worst-case scenario, the algorithm visits every cell in the $m \times n$ grid exactly once to calculate the prefix sum. While the `break` statement provides a significant optimization by skipping unnecessary cells, the upper bound remains strictly proportional to the size of the grid.
*   **Space Complexity:** $\mathcal{O}(1)$
    The algorithm operates entirely in-place by overwriting the original input `grid` with the prefix sums. No additional data structures scaling with the input size are allocated.
