class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        min_suf = [0] * n
        min_suf[-1] = nums[-1]
        
        for i in range(n - 2, -1, -1):
            min_suf[i] = min(nums[i], min_suf[i + 1])
        
        cur_max = -1
        
        for i in range(n):
            if nums[i] > cur_max:
                cur_max = nums[i]
            if cur_max - min_suf[i] <= k:
                return i
                
        return -1