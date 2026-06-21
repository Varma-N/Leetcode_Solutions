# Problem 2033: Minimum Operations to Make a Uni-Value Grid

## Approach

### Step-by-Step Breakdown

1.  **Flatten and Validate:**
    * Convert the 2D grid into a 1D list (`flat_grid`) to simplify processing.
    * Check if all elements can be made equal by verifying if they all share the same remainder when divided by `x`. If `value % x` is not consistent for all elements, return `-1`, as it is impossible to transform them into a uniform value using increments or decrements of `x`.
2.  **Sort and Find Median:**
    * Sort the `flat_grid` in ascending order.
    * The mathematical property required here is that to minimize the sum of absolute differences $\sum |a_i - k|$, the target value $k$ must be the median of the dataset.
    * Select the median element as the `median_target`.
3.  **Calculate Operations:**
    * Iterate through each element in the sorted list.
    * For each element, calculate the number of operations required to reach the `median_target` using the formula `abs(value - median_target) // x`.
    * Sum these values to get the total minimum operations.



## Complexity Analysis

* **Time Complexity:** $O(N \log N)$
    * Where $N = m \cdot n$ is the total number of elements in the grid. Flattening takes $O(N)$, checking remainders takes $O(N)$, and sorting takes $O(N \log N)$. The final summation loop takes $O(N)$. The sorting step dominates the overall time complexity.
* **Space Complexity:** $O(N)$
    * We create a flat array of size $N$ to store the grid elements, leading to linear space complexity.
