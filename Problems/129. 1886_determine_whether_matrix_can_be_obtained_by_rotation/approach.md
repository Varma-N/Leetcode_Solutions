# 1886. Determine Whether Matrix Can Be Obtained By Rotation

The objective of this problem is to determine if a source matrix `mat` can be transformed into a `target` matrix by rotating it in 90-degree increments. Since a 360-degree rotation returns the matrix to its original state, we only need to evaluate four possible orientations: 0°, 90°, 180°, and 270°.

---

### Step-by-Step Approach

#### 1. State Verification Loop
The algorithm initiates a loop that runs exactly four times. In each iteration, it checks if the current state of `mat` is identical to `target`. If a match is found at any point, the function immediately returns `True`.

#### 2. Matrix Transformation Logic
If the matrices do not match, the algorithm applies a 90-degree clockwise rotation. This transformation can be achieved through two distinct logic paths:

*   **Coordinate Mapping:** 
    A new matrix is constructed by iterating through every cell `(i, j)`. The value at the original row `i` and column `j` is moved to a new position where the original row index determines the distance from the right edge, and the original column index becomes the new row index. The formula used is: `new_matrix[j][n - 1 - i] = matrix[i][j]`.

*   **Row Reversal and Transposition:** 
    This optimized approach involves two sub-steps:
    1.  **Vertical Flip:** Reversing the order of the rows in the matrix.
    2.  **Transposition:** Using the `zip` function to convert the rows of the flipped matrix into columns. This effectively reorients the data into a 90-degree clockwise rotation using built-in Python functions.

#### 3. Space and Time Optimization
The first approach is more explicit and helpful for understanding coordinate geometry, while the second approach leverages Python's internal optimizations for better memory management and execution speed. Both ensure that the original data is transformed systematically until all four rotation possibilities are exhausted.

#### 4. Final Conclusion
If the loop completes all four cycles without a successful comparison, it indicates that no amount of 90-degree rotations will make `mat` equal to `target`. The function then returns `False`.

---

### Complexity Analysis

| Metric | Complexity | Description |
| :--- | :--- | :--- |
| **Time Complexity** | $O(N^2)$ | We perform a constant number of rotations (at most 4). In each rotation, we visit every element in the $N \times N$ matrix to either move it or compare it. |
| **Space Complexity** | $O(N^2)$ | Each rotation requires the creation of a temporary structure to hold the transformed elements of the $N \times N$ matrix. |
