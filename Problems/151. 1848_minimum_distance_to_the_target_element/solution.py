class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        min_dis = float('inf')
        for i in range(len(nums)):
            if nums[i] == target:
                min_dis = min(min_dis, abs(i-start))
        return min_dis
        
