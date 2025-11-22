from typing import List

class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        # Initialize difference matrix
        diff = [[0] * (n + 1) for _ in range(n + 1)]
        
        # Apply each query using difference mechanism
        for r1, c1, r2, c2 in queries:
            diff[r1][c1] += 1
            diff[r1][c2 + 1] -= 1
            diff[r2 + 1][c1] -= 1
            diff[r2 + 1][c2 + 1] += 1

        # Build result matrix using 2D prefix sums
        mat = [[0] * n for _ in range(n)]
        
        # Row-wise prefix sum
        for i in range(n):
            for j in range(n):
                mat[i][j] = diff[i][j]
                if j > 0:
                    mat[i][j] += mat[i][j - 1]

        # Column-wise prefix sum
        for j in range(n):
            for i in range(1, n):
                mat[i][j] += mat[i - 1][j]

        return mat
