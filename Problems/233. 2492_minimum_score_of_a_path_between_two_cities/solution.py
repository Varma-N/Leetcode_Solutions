from collections import defaultdict, deque
from typing import List
import math

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))
            
        min_score = math.inf
        visited = {1}
        queue = deque([1])
        
        while queue:
            node = queue.popleft()
            for neighbor, weight in graph[node]:
                min_score = min(min_score, weight)
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        return min_score