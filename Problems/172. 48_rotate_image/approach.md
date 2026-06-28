# Problem 48: Rotate Image

## Intuition
A straightforward approach to rotate an image by 90 degrees is to swap rows and columns. By iterating through the matrix, we can swap elements in a way that achieves this rotation in-place. We essentially perform a transpose of the matrix followed by reversing the order of each row in the transposed matrix.

## Approach
1. **Transpose:**  Transpose the matrix. This effectively flips the rows and columns.
   * Iterate through the outer loop `i` from 0 to `n - 1`.
   * For `j` from `i + 1` to `n - 1`, swap elements at positions `[i][j]` and `[j][i]`, effectively transposing the rows and columns.

2. **Reverse Rows:** After transposing, reverse the order of each row in the transposed matrix.
   * Iterate through the outer loop `i` from 0 to `n - 1`.
   * Reverse the elements within each row by using the list slicing technique `matrix[i] = [matrix[i][j] for j in range(len(matrix[i]))]`

## Complexity Analysis
* **Time Complexity:** $O(N^2)$ 
    * We iterate through every element of the matrix. The swapping operations take O(N) time, and transposing takes O(N).  The overall complexity is dominated by these steps. 
* **Space Complexity:** $O(1)$
    * We only modify the input matrix in-place without creating any additional data structures other than the output matrix (which is also part of the same array), thus making space complexity constant.