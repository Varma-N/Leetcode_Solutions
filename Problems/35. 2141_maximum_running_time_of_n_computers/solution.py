from typing import List

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        left, right = 0, sum(batteries) // n
        
        while left < right:
            mid = (left + right + 1) // 2
            
            if sum(min(bat, mid) for bat in batteries) >= n * mid:
                left = mid
            else:
                right = mid - 1
        
        return left
