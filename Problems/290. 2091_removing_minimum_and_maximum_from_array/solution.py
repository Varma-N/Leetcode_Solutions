class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        i = nums.index(min(nums))
        j = nums.index(max(nums))
        n = len(nums)
        
        if i > j:
            i, j = j, i
            
        return min(j + 1, n - i, i + 1 + n - j)