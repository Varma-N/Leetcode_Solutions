from collections import defaultdict, deque
import heapq
from typing import List

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        # Build adjacency list
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        
        # Component labeling via DFS
        visited = [False] * (c + 1)
        comp_index_of_node = [-1] * (c + 1)
        comp_groups = []
        
        comp_counter = 0
        for i in range(1, c + 1):
            if not visited[i]:
                stack = [i]
                visited[i] = True
                comp = []
                
                while stack:
                    node = stack.pop()
                    comp.append(node)
                    comp_index_of_node[node] = comp_counter
                    
                    for neighbor in graph[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            stack.append(neighbor)
                
                comp_groups.append(comp)
                comp_counter += 1
        
        # Create min-heap for each component
        heaps = []
        for comp in comp_groups:
            heapq.heapify(comp)
            heaps.append(comp)
        
        offline = [False] * (c + 1)
        result = []
        
        for typ, x in queries:
            # Type 2 → take station offline
            if typ == 2:
                offline[x] = True
            
            # Type 1 → return smallest online station in x's component
            else:
                if not offline[x]:
                    result.append(x)
                else:
                    comp_idx = comp_index_of_node[x]
                    heap = heaps[comp_idx]
                    
                    # Lazy deletion of offline nodes
                    while heap and offline[heap[0]]:
                        heapq.heappop(heap)
                    
                    if heap:
                        result.append(heap[0])
                    else:
                        result.append(-1)
        
        return result
