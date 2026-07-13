class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums1_set = set(nums1)
        for i in nums2:
            if i in nums1_set:
                return i
        return -1
        