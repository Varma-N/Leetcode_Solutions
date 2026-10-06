class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        freq_tracker = {}
        left, max_length = 0, 0
        for right in range(n):
            freq_tracker[nums[right]] = freq_tracker.get(nums[right], 0) + 1 
            while freq_tracker[nums[right]] > k:  
                freq_tracker[nums[left]] -= 1
                left += 1
            current_max_length = right - left + 1
            max_length = max(current_max_length, max_length)
        return max_length

