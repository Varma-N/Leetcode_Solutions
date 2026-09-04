from collections import deque

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()
        ans = 0
        
        for i in range(n):
            if i not in visited:
                comp_nodes = 0
                comp_edges = 0
                q = deque([i])
                visited.add(i)
                
                while q:
                    curr = q.popleft()
                    comp_nodes += 1
                    comp_edges += len(adj[curr])
                    for neighbor in adj[curr]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            q.append(neighbor)
                            
                if comp_edges // 2 == comp_nodes * (comp_nodes - 1) // 2:
                    ans += 1
                    
        return ans