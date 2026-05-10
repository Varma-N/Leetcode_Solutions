# Rhombus Sums in a Grid - Step-by-Step Approach

The problem involves finding the three largest unique sums of rhombus shapes within a 2D grid. A rhombus is defined by its four vertices, and its sum is the total of all values along its border.

## 1. Core Logic: Prefix Sums for Diagonals

Calculating the sum of every possible rhombus edge from scratch would be inefficient ($O(k)$ per rhombus). To optimize this, we use **2D Prefix Sums** specifically tailored for diagonals.

*   **Main Diagonals (`d1`):** We create a prefix sum array where `d1[i][j]` represents the sum of elements along the main diagonal (top-left to bottom-right) ending at `grid[i-1][j-1]`.
*   **Anti-Diagonals (`d2`):** We create a prefix sum array where `d2[i][j]` represents the sum of elements along the anti-diagonal (top-right to bottom-left) ending at `grid[i-1][j-1]`.



These arrays allow us to calculate the sum of any diagonal segment in **$O(1)$** time using the formula: `segment_sum = prefix[end] - prefix[start_offset]`.

## 2. Iterating Through Every Possible Rhombus

We iterate through every cell `(r, c)` in the grid, treating it as the **top vertex** of a potential rhombus.

1.  **Size 0 Rhombus:** Every single cell is technically a rhombus of side length $k=0$. We add the value of `grid[r][c]` to our collection of sums.
2.  **Determining Maximum Side Length ($k$):** For a top vertex at `(r, c)`, the maximum side length $k$ is limited by the grid boundaries:
    *   Bottom vertex must be within rows: $r + 2k < m$.
    *   Left vertex must be within columns: $c - k \ge 0$.
    *   Right vertex must be within columns: $c + k < n$.
3.  **Calculating the Border Sum:** For each valid $k \ge 1$, we identify the four vertices:
    *   **Top:** $(r, c)$
    *   **Right:** $(r + k, c + k)$
    *   **Bottom:** $(r + 2k, c)$
    *   **Left:** $(r + k, c - k)$
4.  **Summing the Edges:** We sum the four diagonal segments connecting these vertices using our prefix sum arrays. Since each vertex is shared by two edges (e.g., the top vertex is part of both the Top-Right and Top-Left edges), we subtract the values of the four vertices once to ensure they aren't double-counted.



## 3. Selecting the Top Three

To manage the results:
1.  Store all sums in a **Set** to automatically handle duplicates and ensure we only track unique values.
2.  Convert the set to a list and sort it in descending order.
3.  Return the first three elements. If the set has fewer than three elements, return all of them.

---

## Complexity Analysis

### Time Complexity
*   **Prefix Sum Calculation:** $O(M \cdot N)$ to traverse the grid and build the `d1` and `d2` arrays.
*   **Rhombus Iteration:** We iterate over $M \cdot N$ cells. For each cell, $k$ can grow up to $\min(M, N)/2$. The calculations inside the $k$-loop are $O(1)$. Thus, the total complexity is **$O(M \cdot N \cdot \min(M, N))$**.
*   **Sorting:** $O(S \log S)$, where $S$ is the number of unique sums. Since $S$ is bounded by the total number of rhombi, this is dominated by the iteration.

### Space Complexity
*   **Prefix Sum Arrays:** $O(M \cdot N)$ to store the auxiliary diagonal sum grids.
*   **Unique Sums:** In the worst case, $O(M \cdot N \cdot \min(M, N))$ to store the unique sums in a set.
*   **Overall:** **$O(M \cdot N \cdot \min(M, N))$**.
