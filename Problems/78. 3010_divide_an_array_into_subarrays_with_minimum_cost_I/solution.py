class Solution:
    def minimumCost(self, nums: List[int]) -> int:
       first = nums[0]
       remaining = nums[1:]
       remaining.sort()
       return first + remaining[0] + remaining[1]
            
        
        
