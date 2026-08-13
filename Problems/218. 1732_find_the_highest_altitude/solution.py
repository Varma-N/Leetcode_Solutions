class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = float('-inf')
        current = 0
        for i in gain:
            current = current + i
            if current > res:
                res = current
        return max(0, res)
            

