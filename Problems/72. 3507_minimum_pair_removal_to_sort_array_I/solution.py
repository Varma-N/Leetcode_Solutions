class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def is_sorted(arr):
             return all(arr[i] <= arr[i+1] for i in range(len(arr) - 1))
        count = 0

        while not is_sorted(nums):
            min_val = float('inf')
            idx = 0
            
            for i in range(len(nums) - 1):
                current_min = nums[i] + nums[i+1]
                if current_min < min_val:
                    min_val = current_min
                    idx = i
            nums = nums[:idx] + [min_val] + nums[idx + 2:]
            count += 1

        return count
