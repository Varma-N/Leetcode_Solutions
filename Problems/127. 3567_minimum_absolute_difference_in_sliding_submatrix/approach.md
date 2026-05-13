# 3567. Minimum Absolute Difference in Sliding Submatrix

## Overview
This document outlines the step-by-step approach to solving the "Minimum Absolute Difference in Sliding Submatrix" problem. The objective is to evaluate every `k x k` contiguous submatrix within a given `m x n` grid and determine the minimum absolute difference between any two distinct elements inside each submatrix.

## Step-by-Step Approach

The logic relies on a direct simulation method, evaluating each submatrix individually, extracting its unique elements, and finding the closest pair via sorting. Here is the detailed breakdown:

### 1. Initialize the Result Matrix
* Determine the dimensions of the input `grid`, denoted as `m` (total rows) and `n` (total columns).
* Create a 2D result matrix initialized with zeros. Since a sliding window of size `k x k` can fit into the grid `m - k + 1` times vertically and `n - k + 1` times horizontally, the dimensions of the result matrix will be `(m - k + 1) x (n - k + 1)`.

### 2. Iterate Through All Submatrices
* Use two nested loops to iterate through all valid top-left coordinates `(i, j)` of every possible `k x k` submatrix.
* The outer loop index `i` ranges from `0` to `m - k`.
* The inner loop index `j` ranges from `0` to `n - k`.

### 3. Extract Submatrix Elements
* For each starting position `(i, j)`, initialize an empty list to hold the values.
* Use another set of nested loops to iterate exactly `k` steps horizontally and vertically from the starting position to collect all `k * k` elements of the current submatrix.

### 4. Isolate Unique Values
* Convert the collected list of submatrix elements into a Set. This efficiently removes all duplicate integers, leaving only unique values. Convert the set back to a list for further processing.
* **Edge Case Optimization:** If the list of unique values has fewer than 2 elements (i.e., the entire submatrix consists of the exact same number), the absolute difference is `0`. Record `0` in the result matrix for this position and immediately skip to the next submatrix.

### 5. Sort and Find Minimum Difference
* If there are 2 or more distinct values, sort the list of unique numbers in ascending order. Sorting guarantees that the pair of numbers with the minimum absolute difference will be immediately adjacent to each other in the list.
* Initialize a variable (`min_diff`) to track the minimum difference, starting with a value of infinity.
* Loop through the sorted list, calculating the absolute difference between the element at the current index and the element at the next index.
* Update the `min_diff` variable if the newly calculated difference is smaller than the current recorded minimum.

### 6. Store Results and Return
* Assign the calculated `min_diff` to the corresponding cell `[i][j]` in the result matrix.
* Once all top-left starting positions have been processed, return the final populated result matrix.

## Complexity Analysis

### Time Complexity
* **Grid Traversal:** The algorithm checks `(m - k + 1) * (n - k + 1)` submatrices.
* **Submatrix Processing:** For every submatrix, we iterate through `k^2` elements to collect them. 
* **Sorting:** Sorting the unique elements takes at worst `O(U log U)` time, where `U` is the number of unique elements (`U <= k^2`). Therefore, sorting takes `O(k^2 * log(k^2))`, which simplifies to `O(k^2 * log(k))`.
* **Overall Time Complexity:** `O((m - k + 1) * (n - k + 1) * (k^2 + k^2 * log(k)))`. In Big-O notation, this evaluates to **`O(m * n * k^2 * log(k))`** in the worst-case scenario.

### Space Complexity
* **Output Space:** The generated result matrix requires `O((m - k + 1) * (n - k + 1))` space.
* **Auxiliary Space:** During each iteration, a list and a set are created to store the elements of the current `k x k` submatrix. In the worst case (all elements are unique), these data structures will hold `k^2` elements.
* **Overall Auxiliary Space Complexity:** **`O(k^2)`** to process each submatrix (excluding the space required for the final output array).
