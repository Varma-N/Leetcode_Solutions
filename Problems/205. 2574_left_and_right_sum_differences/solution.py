class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        current_left_sum = 0
        current_right_sum = sum(nums)
        for i in range(n):    
            current_right_sum -= nums[i]
            res.append(abs(current_left_sum - current_right_sum))
            current_left_sum += nums[i]
        return res


        