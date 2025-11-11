from typing import List

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total_cost = 0
        i = 0
        n = len(colors)
        
        while i < n:
            j = i
            total_time = 0
            max_time = 0
            
            while j < n and colors[j] == colors[i]:
                total_time += neededTime[j]
                max_time = max(max_time, neededTime[j])
                j += 1
            
            if j - i > 1:
                total_cost += total_time - max_time
            i = j  
        
        return total_cost
