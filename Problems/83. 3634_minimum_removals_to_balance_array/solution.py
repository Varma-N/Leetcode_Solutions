class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        left = 0
        max_keep = 0
        for right in range(n):
            while nums[right] > k * nums[left]:
                left += 1
            max_keep = max(max_keep, right - left + 1)
        return n - max_keep
            
