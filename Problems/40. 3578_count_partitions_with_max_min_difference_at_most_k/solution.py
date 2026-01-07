from typing import List
from collections import deque

class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        # dp[i] = number of ways to partition nums[0..i-1]
        dp = [0] * (n + 1)
        dp[0] = 1
        
        # prefix[i] = dp[0] + ... + dp[i-1]
        prefix = [0] * (n + 2)
        prefix[1] = 1  # dp[0]
        
        min_deque = deque()  # increasing values
        max_deque = deque()  # decreasing values
        
        left = 0
        
        for right in range(n):
            # Maintain min deque
            while min_deque and nums[min_deque[-1]] >= nums[right]:
                min_deque.pop()
            min_deque.append(right)
            
            # Maintain max deque
            while max_deque and nums[max_deque[-1]] <= nums[right]:
                max_deque.pop()
            max_deque.append(right)
            
            # Shrink window until valid
            while nums[max_deque[0]] - nums[min_deque[0]] > k:
                if min_deque[0] == left:
                    min_deque.popleft()
                if max_deque[0] == left:
                    max_deque.popleft()
                left += 1
            
            # DP transition
            dp[right + 1] = (prefix[right + 1] - prefix[left]) % MOD
            prefix[right + 2] = (prefix[right + 1] + dp[right + 1]) % MOD
        
        return dp[n] % MOD
