class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        s = sum(nums)
        f = sum(i * val for i, val in enumerate(nums))
        max_f = f
        
        for x in reversed(nums):
            f += s - n * x
            max_f = max(max_f, f)
        
        return max_f


        