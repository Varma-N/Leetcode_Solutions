# Problem 1260: Shift 2D Grid

## Intuition
The core idea is to leverage the modulo operator (%) to handle the shifting process. Each time the grid shifts, the elements move one step in the grid. We use the modulo operation to ensure that the element's index within the shifted grid stays within the boundaries. 

## Approach
1. **Initialization:**
   - Obtain the dimensions of the input grid (`m` for rows, `n` for columns).
   - Calculate the `total` number of elements in the grid after shifting `k` times. 
   - Create a result grid `res` with dimensions `m x n`, filled with zeros.

2. **Shift Logic:**
   - Iterate through each element in the input grid.
   - Calculate the `new_idx` for the element after shifting.
   - The `new_idx` is calculated using modulo operation to ensure that the index stays within the boundaries of the grid after the shift operation. 
   - Update the corresponding element in the `res` grid using the `new_idx`.

3. **Return:**
   - Return the `res` grid, which represents the shifted grid after `k` shifts.

## Complexity Analysis
* **Time Complexity:** $O(m*n)$
    * The nested loops iterate through each element in the grid once, resulting in a time complexity of `O(m*n)`.
* **Space Complexity:** $O(m*n)$
    * The `res` grid is created with `m * n` dimensions to store the shifted grid.