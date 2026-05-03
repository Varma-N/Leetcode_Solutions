class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        dp = [[[0]*2 for _ in range(one+1)] for _ in range(zero+1)]
        dp[0][0][0] = 1
        dp[0][0][1] = 1
        
        for i in range(zero+1):
            for j in range(one+1):
                if i == 0 and j == 0: continue
                
                # Compute dp[i][j][0]
                for k in range(1, limit+1):
                    if i-k >= 0:
                        dp[i][j][0] = (dp[i][j][0] + dp[i-k][j][1]) % MOD
                    else:
                        break
                
                # Compute dp[i][j][1]
                for k in range(1, limit+1):
                    if j-k >= 0:
                        dp[i][j][1] = (dp[i][j][1] + dp[i][j-k][0]) % MOD
                    else:
                        break
                        
        return (dp[zero][one][0] + dp[zero][one][1]) % MOD
