# Problem 3225: Maximum Score From Grid Operations

## Intuition
The solution utilizes a dynamic programming approach to compute the maximum score. By calculating the sum of scores based on adjacent black cells and pre-computing potential values, we can efficiently determine the final score for each column.  

## Approach
1. **Initialization:** 
    * We create an `INF` constant (negative infinity) to represent the initial score being considered.
2. **Building the DP Table (`dp`)**:
   * The `dp` table will store the maximum achievable scores, where `dp[i][j]` represents the maximum score for a column with `j` columns and the current value in grid at `i`. 
3. **Dynamic Programming:**
    * We iteratively fill the `dp` table using a loop over each cell in the grid.  
    * For each cell, we need to consider all possible scenarios of adjacent black cells. 
4. **Score Calculation and Update (`new_dp`)**:
   * The `new_dp` table will keep track of updated scores after considering adjacent black cells. 

5. **Calculating the Final Score:**
    *  The final score is calculated by finding the maximum value in the `dp` table which represents the total grid score.


## Complexity Analysis
* **Time Complexity:** $O(n * n)$
    * The main operations take O(n) time, where n is the size of the grid. 
* **Space Complexity:** $O(n^2)$ 
    *  We create a `dp` table to store calculated scores for each row.