class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        start = min(nums)
        stop = max(nums)

        nums_set = set(nums)

        return [x for x in range(start, stop) if x not in nums_set]
