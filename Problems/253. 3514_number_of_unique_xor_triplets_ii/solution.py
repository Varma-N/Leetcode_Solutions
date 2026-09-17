class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        u = set(nums)
        p = {x ^ y for x in u for y in u}
        return len({x ^ y for x in u for y in p})