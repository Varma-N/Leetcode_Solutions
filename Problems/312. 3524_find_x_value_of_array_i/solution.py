class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        dp = [0] * k
        
        for num in nums:
            new_dp = [0] * k
            val = num % k
            new_dp[val] += 1
            for i in range(k):
                if dp[i]:
                    new_dp[(i * val) % k] += dp[i]
            
            for i in range(k):
                ans[i] += new_dp[i]
                dp[i] = new_dp[i]
                
        return ans