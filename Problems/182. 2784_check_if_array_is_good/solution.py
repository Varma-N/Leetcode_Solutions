class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        max_ele = nums[-1]
        if len(nums) != max_ele + 1 or nums[-2] != max_ele:
            return False
        for i in range(max_ele-1):
            if nums[i] + 1 != nums[i+1]: return False
        return True

          
        