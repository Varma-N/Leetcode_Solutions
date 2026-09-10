from bisect import bisect_right

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_val = max(nums)
        count = [0] * (max_val + 1)
        for num in nums:
            count[num] += 1
            
        exact = [0] * (max_val + 1)
        for g in range(max_val, 0, -1):
            multiples_count = sum(count[m] for m in range(g, max_val + 1, g))
            pairs = multiples_count * (multiples_count - 1) // 2
            for m in range(g * 2, max_val + 1, g):
                pairs -= exact[m]
            exact[g] = pairs
            
        prefix = [0] * (max_val + 1)
        for i in range(1, max_val + 1):
            prefix[i] = prefix[i - 1] + exact[i]
            
        return [bisect_right(prefix, q) for q in queries]