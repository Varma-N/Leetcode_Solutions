from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        r = total % p
        if r == 0:
            return 0

        prefix_mod = 0
        mod_index = {0: -1}
        min_len = len(nums)

        for j in range(len(nums)):
            prefix_mod = (prefix_mod + nums[j]) % p
            target = (prefix_mod - r) % p

            if target in mod_index:
                min_len = min(min_len, j - mod_index[target])

            mod_index[prefix_mod] = j

        return min_len if min_len < len(nums) else -1
