# Problem 3742: Maximum Path Score in a Grid

## Intuition
The maximum path score problem can be solved using dynamic programming. We explore all possible paths from the starting cell to the ending cell and keep track of the best score achievable at each cell. This approach leverages recursion and memoization to avoid redundant calculations.

## Approach
1. **Initialization:** Initialize a 2D DP array `dp` where `dp[i][j]` represents the maximum path score reachable from cell (i, j) with a cost of `c`.  `dp[0][0][0] = 0`, representing the starting point at a cost of 0.

2. **Base Case:** If we're at the starting cell, its score is determined by the value of the cell. 
3. **Iteration:** Traverse through all cells using `i` and `j`. For each cell:
    * Calculate the score based on the current cell's value (`val`) and cost (`cell_cost`). 
    * Consider the possible movement (down or right) for the current cell, updating the DP values for the next level.  We explore all possible paths from the starting cell to the ending cell.
4. **Recursion:** If there are moves available in the direction of movement, we recursively explore the path using the `res_up` and `res_left` variables. This allows us to determine the maximum score achievable at the current position considering the cost constraint.


## Complexity Analysis
* **Time Complexity:** $O(m * n * k)$ 
    * The number of cells we need to explore is proportional to  the grid's dimensions (m x n). The total time complexity is therefore a function of the product of these dimensions and the maximum possible score (k) since we iterate through all cells.
* **Space Complexity:** $O(m * n * k)$ 
    * We use `dp` to store calculated values at each cell.  The memory complexity of the DP array depends on the grid's size, and the number of entries in the DP table (k + 1) is determined by the cost limit.