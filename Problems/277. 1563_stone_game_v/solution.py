from functools import lru_cache
class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + stoneValue[i]
        
        dp = [[0] * n for _ in range(n)]
        max_l = [[0] * n for _ in range(n)]
        max_r = [[0] * n for _ in range(n)]
        
        for i in range(n):
            max_l[i][i] = stoneValue[i]
            max_r[i][i] = stoneValue[i]
        
        for i in range(n - 1, -1, -1):
            m = i - 1
            for j in range(i + 1, n):
                target = prefix[j+1] + prefix[i]
                while m + 1 < j and 2 * prefix[m + 2] <= target:
                    m += 1
                
                res = 0
                if m >= i:
                    res = max_l[i][m]
                if 2 * prefix[m + 1] == target:
                    res = max(res, max_r[m+1][j])
                elif m + 1 < j:
                    res = max(res, max_r[m+2][j])
                    
                dp[i][j] = res
                sum_ij = prefix[j+1] - prefix[i]
                max_l[i][j] = max(max_l[i][j-1], sum_ij + res)
                max_r[i][j] = max(max_r[i+1][j], sum_ij + res)
                
        return dp[0][n-1]