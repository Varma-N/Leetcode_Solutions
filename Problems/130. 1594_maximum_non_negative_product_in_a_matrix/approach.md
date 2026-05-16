# Maximum Non Negative Product in a Matrix - Step-by-Step Approach

## Approach: Dynamic Programming

When traversing the grid, the path's product can flip between positive and negative depending on the signs of the numbers encountered. To find the maximum product, we must track both the maximum and minimum possible products at each cell, as multiplying a large negative product by a negative grid value will result in a large positive product.

### Step-by-Step Breakdown:

**1. Initialize State Tables**
* Determine the dimensions of the grid, let $m$ be the number of rows and $n$ be the number of columns.
* Create two 2D arrays (DP tables) of the same size, `dp_max` and `dp_min`.
* `dp_max[i][j]` will store the maximum possible product to reach cell `(i, j)`.
* `dp_min[i][j]` will store the minimum possible product to reach cell `(i, j)`.

**2. Set the Base Case**
* For the starting cell at the top-left corner `(0, 0)`, the only possible product is the value of the cell itself.
* Initialize both `dp_max[0][0]` and `dp_min[0][0]` with `grid[0][0]`.

**3. Traverse the Grid**
* Use nested loops to iterate through every cell in the matrix row by row. 
* Skip the starting cell `(0, 0)` since it is already initialized.

**4. Evaluate Candidate Products**
* For each cell `(i, j)`, you can arrive from either the cell directly above `(i-1, j)` or the cell directly to the left `(i, j-1)`.
* Create a collection of candidate products for the current cell.
* **If arriving from the Top:** Multiply the current cell's value `grid[i][j]` by both `dp_max[i-1][j]` and `dp_min[i-1][j]`. Add both results to the candidates.
* **If arriving from the Left:** Multiply the current cell's value `grid[i][j]` by both `dp_max[i][j-1]` and `dp_min[i][j-1]`. Add both results to the candidates.

**5. Update Current Cell State**
* Find the highest value among your candidates and assign it to `dp_max[i][j]`.
* Find the lowest value among your candidates and assign it to `dp_min[i][j]`.

**6. Extract Result and Apply Modulo**
* After fully traversing the grid, the maximum product to reach the bottom-right corner will be stored in `dp_max[m-1][n-1]`.
* Check if this final maximum product is strictly less than 0. If it is, return `-1` as requested by the problem constraints.
* If it is non-negative, return the result modulo $10^9 + 7$ as the final answer.

---

## Complexity Analysis
* **Time Complexity:** $\mathcal{O}(m \times n)$ 
  We iterate through every cell in the $m \times n$ grid exactly once. For each cell, we perform a constant O(1) number of operations (multiplications and max/min comparisons).
* **Space Complexity:** $\mathcal{O}(m \times n)$
  We allocate two additional matrices (`dp_max` and `dp_min`) of the same size as the input grid to store the intermediate states. (Note: This can be optimized to $\mathcal{O}(n)$ by only storing the previous row's DP values, but based on the provided solution structure, it takes $\mathcal{O}(m \times n)$ space).
