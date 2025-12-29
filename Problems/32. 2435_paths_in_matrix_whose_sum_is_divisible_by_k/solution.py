from typing import List

class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        # dp[i][j][r] = number of paths to (i, j) with sum % k == r
        dp = [[[0] * k for _ in range(n)] for _ in range(m)]
        
        # Base case
        dp[0][0][grid[0][0] % k] = 1
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                
                val = grid[i][j]
                
                # From top
                if i > 0:
                    for r in range(k):
                        if dp[i - 1][j][r]:
                            nr = (r + val) % k
                            dp[i][j][nr] = (dp[i][j][nr] + dp[i - 1][j][r]) % MOD
                
                # From left
                if j > 0:
                    for r in range(k):
                        if dp[i][j - 1][r]:
                            nr = (r + val) % k
                            dp[i][j][nr] = (dp[i][j][nr] + dp[i][j - 1][r]) % MOD
        
        return dp[m - 1][n - 1][0]
