# 1895. Largest Magic Square

## Approach

To efficiently find the largest magic square within a given grid, we utilize prefix sums to optimize calculation times and iterate from the largest possible square size downwards.

### 1. Prefix Sum Precomputation
Calculating the sum of rows and columns repeatedly for every possible subgrid leads to redundant computations. To optimize this, we precompute **prefix sums** for both rows and columns:
- **Row Prefix Sums:** Store cumulative sums for each row. This allows calculating the sum of any horizontal segment in `O(1)` time.
- **Column Prefix Sums:** Store cumulative sums for each column. This allows calculating the sum of any vertical segment in `O(1)` time.

### 2. Iteration Strategy
Since the goal is to find the **largest** magic square, we iterate through possible square sizes `k` starting from the maximum possible dimension (`min(rows, cols)`) down to `2`.
- This ensures that the first valid magic square found is the largest possible one.
- If the loop completes without finding a magic square of size `k >= 2`, the default result is `1` (as a `1x1` grid is trivially a magic square).

### 3. Validation Logic
For each possible top-left corner `(i, j)` and size `k`, we validate the subgrid using the following steps:
1. **Target Sum:** Calculate the sum of the first row of the subgrid to establish the target magic sum.
2. **Row Check:** Verify that all `k` rows in the subgrid sum to the target using the row prefix sums.
3. **Column Check:** Verify that all `k` columns in the subgrid sum to the target using the column prefix sums.
4. **Diagonal Check:** Calculate the sum of the main diagonal (top-left to bottom-right) and the anti-diagonal (top-right to bottom-left) directly. Both must equal the target sum.
5. If all conditions are met, return `k`.

## Complexity Analysis

### Time Complexity
- **Prefix Sum Construction:** `O(m * n)`, where `m` is the number of rows and `n` is the number of columns.
- **Search and Validation:** We iterate through possible sizes `k` from `min(m, n)` down to `2`. For each size, we iterate through all possible top-left positions (`O(m * n)`). Inside the validation function, we iterate `k` times to check rows, columns, and diagonals.
- **Total:** `O(m * n * min(m, n)^2)`. Given the constraint that `m, n <= 50`, this approach is efficient enough.

### Space Complexity
- **`O(m * n)`**: We store two additional 2D arrays for the row and column prefix sums, each having dimensions proportional to the input grid.
