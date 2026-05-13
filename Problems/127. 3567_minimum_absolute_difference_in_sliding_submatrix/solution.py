class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]
        for i in range(m - k + 1):
            for j in range(n - k + 1):
                submatrix_values = []
                for r in range(i, i + k):
                    for c in range(j, j + k):
                        submatrix_values.append(grid[r][c])
                unique_values = list(set(submatrix_values))
                if len(unique_values) < 2:
                    ans[i][j] = 0
                    continue
                unique_values.sort()
                min_diff = float('inf')
                for idx in range(len(unique_values) - 1):
                    diff = abs(unique_values[idx] - unique_values[idx+1])
                    if diff < min_diff:
                        min_diff = diff
                ans[i][j] = min_diff
                
        return ans
