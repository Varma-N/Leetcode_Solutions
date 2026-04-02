class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0.0] * (k + 1) for k in range(101)]
        
        dp[0][0] = poured
        
        for row in range(query_row + 1):
            for glass in range(row + 1):
                if dp[row][glass] > 1:
                    overflow = (dp[row][glass] - 1) / 2.0
                    dp[row][glass] = 1
                    dp[row + 1][glass] += overflow
                    dp[row + 1][glass + 1] += overflow
        
        return min(1, dp[query_row][query_glass])
