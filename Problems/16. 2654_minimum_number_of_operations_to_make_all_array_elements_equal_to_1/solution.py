from typing import List
from math import gcd

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        size = len(nums)
        ones = 0
        total_g = 0

        # Count ones and compute total GCD
        for val in nums:
            if val == 1:
                ones += 1
            total_g = gcd(total_g, val)

        # Case 1: Some elements are already 1
        if ones > 0:
            return size - ones

        # Case 2: No 1s and total GCD != 1 → impossible
        if total_g != 1:
            return -1

        # Case 3: No 1s but possible → find smallest subarray with GCD = 1
        best = size
        for i in range(size):
            g = 0
            for j in range(i, size):
                g = gcd(g, nums[j])
                if g == 1:
                    best = min(best, j - i + 1)
                    break

        # Total operations = best + size - 2
        return best + size - 2
