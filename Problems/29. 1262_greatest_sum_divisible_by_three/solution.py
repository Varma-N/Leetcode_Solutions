from typing import List

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # dp[r] = maximum sum with remainder r mod 3
        dp = [0, float('-inf'), float('-inf')]
        
        for num in nums:
            new_dp = dp[:]  # snapshot current state
            for r in range(3):
                if dp[r] != float('-inf'):
                    new_sum = dp[r] + num
                    new_r = new_sum % 3
                    new_dp[new_r] = max(new_dp[new_r], new_sum)
            dp = new_dp
        
        return dp[0]
