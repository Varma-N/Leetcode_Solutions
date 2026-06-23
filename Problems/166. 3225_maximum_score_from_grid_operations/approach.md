# Problem 3225: Maximum Score From Grid Operations

## Intuition
The maximum score is achieved by strategically coloring adjacent black cells, aiming to maximize the number of white cells within the color-adjacent columns.  We can achieve this using dynamic programming, breaking down the problem into subproblems and storing solutions for reuse.

## Approach
1. **Initialization:** 
    * Create `P` matrix: This matrix stores the sum of all grid values for each column from row 0 to n (size = n * n).  It's initialized by iterating through each cell, summing up values in each column starting from the top row.

2. **DP Array Setup:**
    * Initialize `dp` matrix: This matrix stores the maximum score that can be achieved using a certain number of operations on the grid (size = n * (n+1)). 
     * Set base case: `dp[0][j] = 0` for all j.

3. **Dynamic Programming Loop:**  
    * Iterate through each cell in the grid (`c`): 
       * Create a new `new_dp` matrix of same size as `dp`.
       * Initialize `pref` and `cur` arrays:
           * `pref`: Stores the maximum score achieved by colorizing the jth column to the leftmost position. 
           * `cur`: Represents the best score found so far.  
       * Calculate `pref` for each row (`j`) using the previously calculated values.
      * Next, calculate `suff_ge`: This matrix stores the maximum score achieved by colorizing the jth column to the rightmost position.   
        * Iterate through the grid from bottom to top, calculating scores based on the current value and previous calculations. 

    *  Use `new_dp` to update `dp`.

4. **Result:** Finally, calculate the maximum score for all cells in the grid by taking the maximum of the `dp` array.


## Complexity Analysis
* **Time Complexity:** $O(n^2)$ - We are iterating through each cell of the grid and performing calculations.  
* **Space Complexity:** $O(n^2)$ - The time complexity is driven by the size of our `P` matrix, which reflects the total number of operations performed on the grid.