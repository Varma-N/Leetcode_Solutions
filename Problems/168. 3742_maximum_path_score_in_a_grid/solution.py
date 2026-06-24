from typing import List

class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[[-1] * (k + 1) for _ in range(n)] for _ in range(m)]
        dp[0][0][0] = 0
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                val = grid[i][j]
                cell_cost = 0 if val == 0 else 1
                cell_score = val
                
                for c in range(cell_cost, k + 1):
                    res_up = dp[i-1][j][c - cell_cost] if i > 0 else -1
                    res_left = dp[i][j-1][c - cell_cost] if j > 0 else -1
                    
                    prev_max_score = max(res_up, res_left)
                    
                    if prev_max_score != -1:
                        dp[i][j][c] = prev_max_score + cell_score
        ans = max(dp[m-1][n-1])
        return ans

        