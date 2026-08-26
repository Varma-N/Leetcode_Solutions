# Problem 3286: Find a Safe Walk Through a Grid

## Intuition
The core idea is to use a breadth-first search (BFS) to explore all possible safe paths from the starting cell to the destination cell. This algorithm employs a queue (q) to keep track of the cells to be explored. The distance between the current cell and the destination cell is the minimum path cost, which is the sum of the cell's cost and the distance from the starting cell.

## Approach
1. **Initialization:**
    * `m` and `n`: Represent the number of rows and columns in the grid.
    * `dist`: A 2D array used to store the minimum distances from the starting cell. Initialize all cells with `infinity` and set the distance to the starting cell to the cell's value (i.e., grid[0][0]). 
    * `q`: A deque (double-ended queue) to store the cells to be explored in a Breadth-First Search (BFS) order. Initialize it with the starting cell (0, 0).
    * `directions`: A list of tuples representing the 4 possible moves: up, down, left, and right.

2. **BFS Exploration:**
    * **Loop:** Iterate as long as the queue is not empty.
    * **Dequeue:** Extract the first cell from the queue (represented by `r` and `c`).
    * **Explore Neighbors:** Iterate through the adjacent cells in the `directions` list: `(0, 1), (1, 0), (0, -1), (-1, 0)`.
    * **Check Validity:** If the neighbor cell is within the grid boundaries and is not blocked (i.e., grid[nr][nc] == 0):
        * **Cost Calculation:** Calculate the cost of moving to the neighbor cell by adding the cell's cost and the distance from the starting cell.
        * **Update Distance:** If the calculated cost is less than the existing distance to the neighbor cell, update the `dist` array. 
        * **Enqueue Neighbors:** If the cell is not blocked, add the neighbor cell to the queue for exploration.  
    * **Destination Check:** After the loop completes, check if the destination cell (`m-1`, `n-1`) is reachable. If so, return `True`. Otherwise, return `False`.

## Complexity Analysis
* **Time Complexity:** $O(m * n)$ - The BFS algorithm explores the grid layer-by-layer, with `m * n` cells to be visited.
    * Detailed explanation of why: The algorithm explores all cells in a breadth-first manner, and each cell is visited at most once. 
* **Space Complexity:** $O(m * n)$ - The `dist` array stores the minimum distances, and the queue `q` stores the explored cells.
    * Detailed explanation of why: The `dist` array and the queue `q` have a size proportional to the grid's size.
