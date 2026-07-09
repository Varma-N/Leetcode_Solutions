class Solution:
    def findMin(self, nums: List[int]) -> int:
        last_index = len(nums)-1
        if nums[0] > nums[last_index]:
            while nums[last_index] > nums[last_index - 1]:
                last_index -= 1
            return nums[last_index]
        return nums[0]
        
         

        