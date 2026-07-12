from collections import deque, defaultdict
from typing import List

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        
        if n <= 1:
            return 0
            
        graph = defaultdict(list)
        for i, val in enumerate(arr):
            graph[val].append(i)
            
        queue = deque([0])
        visited = {0}
        steps = 0
        
        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                
                if curr == n - 1:
                    return steps
                    
                for neighbor in graph[arr[curr]]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
                        
                graph[arr[curr]].clear()
                
                if curr + 1 < n and (curr + 1) not in visited:
                    visited.add(curr + 1)
                    queue.append(curr + 1)
                    
                if curr - 1 >= 0 and (curr - 1) not in visited:
                    visited.add(curr - 1)
                    queue.append(curr - 1)
            
            steps += 1
            
        return -1