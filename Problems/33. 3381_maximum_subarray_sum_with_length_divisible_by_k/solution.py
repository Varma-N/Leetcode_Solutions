from typing import List

class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k > n:
            return 0
        
        # Prefix sum
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        
        # min_prefix[r] = minimum prefix[i] seen where i % k == r
        min_prefix = [float('inf')] * k
        min_prefix[0] = 0  # prefix[0] at index 0
        
        max_sum = float('-inf')
        
        for j in range(1, n + 1):
            r = j % k
            
            if min_prefix[r] != float('inf'):
                max_sum = max(max_sum, prefix[j] - min_prefix[r])
            
            min_prefix[r] = min(min_prefix[r], prefix[j])
        
        return max_sum if max_sum != float('-inf') else 0
