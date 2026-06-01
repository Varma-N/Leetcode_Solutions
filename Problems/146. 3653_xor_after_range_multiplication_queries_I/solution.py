class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        for q in queries:
            li, ri, ki, vi = q
            idx = li
            while idx <= ri:
                nums[idx] = (nums[idx] * vi) % (10 ** 9 + 7)
                idx += ki
            res = nums[0]
        for i in range(1, len(nums)):
            res = res ^ nums[i]
        return res
