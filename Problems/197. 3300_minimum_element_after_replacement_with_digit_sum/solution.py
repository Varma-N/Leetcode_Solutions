class Solution:
    def minElement(self, nums: List[int]) -> int:
        min_element = float('inf')
        for num in nums:
            res = 0
            while num:
                res +=  num % 10
                num = num // 10
            min_element = min(min_element, res)
        return min_element
                    


        