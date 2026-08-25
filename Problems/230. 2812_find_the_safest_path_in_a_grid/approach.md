# Problem 2812: Find the Safest Path in a Grid

## Intuition
The key to solving this problem is to use a breadth-first search (BFS) approach with a priority queue. Initially, we mark the cell with a thief as visited. Then, we use BFS to explore all possible paths leading to the destination cell. We calculate the safeness factor for each path, which is the minimum distance from any cell in the path to any thief in the grid.

## Approach
1. **Initialization:**
   *  Create a `safe` 2D array of size `n x n` to store the safeness factor for each cell.
   *  Create a queue `q` to store cells to be explored.
   *  For each cell `grid[r][c]`, check if it's a thief. If yes, append it to the queue and mark the safeness factor of that cell as 0. 
2. **BFS:**
   *  While the queue `q` is not empty:
     *  Pop the first cell from the queue and mark it as visited.
     *  For each of the four adjacent cells (`dirs` array):
       *  If the adjacent cell is within the grid bounds and it has not been visited before:
         *  Update the safeness factor of the adjacent cell. 
         *  Append the adjacent cell to the queue.
3. **Backtracking and Evaluation:**
   *  Use a priority queue `pq` to store the cells to be evaluated, and the safeness factor.
   *  While the priority queue is not empty:
     *  Pop the cell with the maximum safeness factor from the priority queue. 
     *  Check if the current cell is the destination cell. If yes, return -s. 
     *  If not, explore the adjacent cells (same logic as step 2) and update the priority queue with their safeness factors. 
4.  **Return:** 
   * If there is no path leading to the destination cell, return 0.

## Complexity Analysis
* **Time Complexity:** $O(N^2)$ 
   *  BFS explores all cells in a grid, resulting in a time complexity of $O(N^2)$. 
* **Space Complexity:** $O(N)$
   * The `safe` array and the `q` queue have a space complexity of $O(N)$ due to the size of the grid.