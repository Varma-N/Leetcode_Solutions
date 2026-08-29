# Problem 1301: Number of Paths with Max Score

## Intuition
Given a square board of characters, we need to find the maximum sum of numeric characters achievable in a path from bottom right to top left, while considering obstacles.  A path will be formed by moving diagonally, and only if there are no obstacles, the current path will be considered.  The algorithm will utilize dynamic programming to explore all paths and calculate the maximum sum.  

## Approach
1. **Initialization:** 
   - The `dp` array of dimensions `(n x n)` is initialized. 
   - `dp[n-1][n-1]` is set to `[0, 1]` representing that the path from the bottom right to top left has a sum of 0 and the number of paths to reach this is 1.

2. **Iteration:** 
   - The code iterates through the `dp` array in the reverse order, starting from the bottom right to the top left, using the nested loops. 
   - **Conditions for Moving:** 
     - If the current cell is an obstacle (`board[i][j] == 'X'`) or we have reached the bottom left cell (`i == n - 1 and j == n - 1`), the iteration continues without further calculation.
   - **Calculating Maximum Sum and Number of Paths:**
      - For each cell `dp[i][j]`, the algorithm calculates the maximum sum of numeric characters that can be collected and the number of such paths that can be taken. 
      - We calculate `max_sum` and `ways` for each cell.
      - The code checks if the number of paths to reach the current cell is greater than 0. 
      - If yes, the code updates the `max_sum` and `ways`.

3. **Storing Results:**
   - After the loop completes, the algorithm retrieves the maximum sum and number of paths from the `dp` array. 

4. **Result:**
   - If there exists a path to the top left cell and the sum is greater than 0, the algorithm returns the maximum sum.
   - If there are no paths, the algorithm returns `[0, 0]`.


## Complexity Analysis
* **Time Complexity:** $O(N^2)$
    * The time complexity is determined by the nested loops that iterate through the `dp` array. 
* **Space Complexity:** $O(N^2)$
    * The space complexity is determined by the `dp` array, which stores the maximum sum and number of paths for each cell in the grid.