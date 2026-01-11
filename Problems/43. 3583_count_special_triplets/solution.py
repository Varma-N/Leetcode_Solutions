from typing import List

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        
        left = {}
        right = {}
        
        # Initialize right frequency map
        for x in nums:
            right[x] = right.get(x, 0) + 1
        
        result = 0
        
        for j in range(len(nums)):
            # Move nums[j] from right to middle
            right[nums[j]] -= 1
            
            target = nums[j] * 2
            left_count = left.get(target, 0)
            right_count = right.get(target, 0)
            
            result += left_count * right_count
            
            # Add nums[j] to left map
            left[nums[j]] = left.get(nums[j], 0) + 1
        
        return result % MOD
