from functools import cache
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffix_sum = [0] * n
        suffix_sum[-1] = piles[-1]
        
        for i in range(n - 2, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
            
        @cache
        def dfs(i, M):
            if i + 2 * M >= n:
                return suffix_sum[i]
            
            best = 0
            for x in range(1, 2 * M + 1):
                best = max(best, suffix_sum[i] - dfs(i + x, max(M, x)))
                
            return best
            
        return dfs(0, 1)