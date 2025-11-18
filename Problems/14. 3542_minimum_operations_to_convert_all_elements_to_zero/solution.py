from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        stack = []
        operations = 0
        
        for x in nums:
            # End any taller active segments
            while stack and stack[-1] > x:
                stack.pop()

            # Ignore zero heights
            if x == 0:
                continue

            # New rising segment detected
            if not stack or stack[-1] < x:
                stack.append(x)
                operations += 1
        
        return operations
