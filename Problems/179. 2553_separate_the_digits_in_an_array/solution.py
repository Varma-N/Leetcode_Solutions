class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            result.extend(int(d) for d in str(num))
        return result
            

            