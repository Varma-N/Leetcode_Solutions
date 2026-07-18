class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        dp = [0] * n 
        
        def dfs(i: int) -> int:
            if dp[i] != 0:
                return dp[i]
            
            max_visited = 1
            
            for x in range(1, d + 1):
                j = i + x
                if j >= n or arr[j] >= arr[i]:
                    break
                max_visited = max(max_visited, 1 + dfs(j))
                
            for x in range(1, d + 1):
                j = i - x
                if j < 0 or arr[j] >= arr[i]:
                    break
                max_visited = max(max_visited, 1 + dfs(j))
                
            dp[i] = max_visited
            return dp[i]
        
        overall_max = 0
        for i in range(n):
            overall_max = max(overall_max, dfs(i))
            
        return overall_max
        