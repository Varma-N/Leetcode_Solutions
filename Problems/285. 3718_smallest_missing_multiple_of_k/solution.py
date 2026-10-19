class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        multiple_set = set(nums)
        multiple = k
        while k in multiple_set:
            k += multiple
        return k