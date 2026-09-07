import math
class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        m = max(nums)
        dp = [[0] * (m + 1) for _ in range(m + 1)]
        dp[0][0] = 1
        
        for x in nums:
            new_dp = [[0] * (m + 1) for _ in range(m + 1)]
            for g1 in range(m + 1):
                for g2 in range(m + 1):
                    if dp[g1][g2]:
                        v = dp[g1][g2]
                        new_dp[g1][g2] = (new_dp[g1][g2] + v) % MOD
                        
                        ng1 = math.gcd(g1, x) if g1 else x
                        new_dp[ng1][g2] = (new_dp[ng1][g2] + v) % MOD
                        
                        ng2 = math.gcd(g2, x) if g2 else x
                        new_dp[g1][ng2] = (new_dp[g1][ng2] + v) % MOD
            dp = new_dp
            
        ans = sum(dp[g][g] for g in range(1, m + 1)) % MOD
        return ans