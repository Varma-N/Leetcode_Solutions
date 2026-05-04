class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7

        dp = [[[0] * 2 for _ in range(one + 1)] for _ in range(zero + 1)]

        dp[0][0][0] = 1
        dp[0][0][1] = 1


        for i in range(zero + 1):
            for j in range(one + 1):
                if i == 0 and j == 0:
                    continue

                if i == 0:
                    dp[i][j][0] = 0

                else:
                    val = (dp[i-1][j][0] + dp[i-1][j][1]) % MOD

                    if i > limit:
                        val = (val - dp[i-limit-1][j][1] + MOD) % MOD

                    if i == 1:
                        val = (val - dp[0][j][0] + MOD) % MOD
                    dp[i][j][0] = val

                if j == 0:
                    dp[i][j][1] = 0
                else: 
                    val = (dp[i][j-1][1] + dp[i][j-1][0]) % MOD
                    if j > limit:
                        val = (val - dp[i][j-limit-1][0] + MOD) % MOD
                    if j == 1:
                        val = (val - dp[i][0][1] + MOD) % MOD
                    dp[i][j][1] = val

        return (dp[zero][one][0] + dp[zero][one][1]) % MOD
