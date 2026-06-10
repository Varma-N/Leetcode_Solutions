class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def reverse_num(n):
            # Mathematical reversal handles leading zeros automatically
            # e.g., 120 -> 0*10 + 21 -> 21
            rev = 0
            while n > 0:
                rev = rev * 10 + (n % 10)
                n //= 10
            return rev

        # Key: The value we are looking for (the target)
        # Value: The last index where a number that reverses to 'Key' appeared
        target_map = {}
        min_dist = float('inf')

        for j, val in enumerate(nums):
            # 1. Check if the current value matches a previously seen number's reverse
            if val in target_map:
                dist = j - target_map[val]
                if dist < min_dist:
                    min_dist = dist
            
            # 2. Store the reverse of the current number as a "target" for future indices
            # Rule: reverse(nums[i]) == nums[j]. 
            # So we store reverse(nums[j]) to match a future nums[k]
            rev_val = reverse_num(val)
            target_map[rev_val] = j

        return min_dist if min_dist != float('inf') else -1
