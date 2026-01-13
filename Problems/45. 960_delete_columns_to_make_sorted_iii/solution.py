from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        
        # dp[j] = length of longest valid sequence ending at column j
        dp = [1] * m
        
        for j in range(m):
            for i in range(j):
                # check if column i can come before column j
                valid = True
                for r in range(n):
                    if strs[r][i] > strs[r][j]:
                        valid = False
                        break
                if valid:
                    dp[j] = max(dp[j], dp[i] + 1)
        
        # minimum deletions = total columns - longest valid subsequence
        return m - max(dp)
