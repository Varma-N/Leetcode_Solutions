class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        small_num, large_num = nums[0], nums[-1]
        while large_num:
            small_num, large_num = large_num, small_num % large_num
        return small_num
        