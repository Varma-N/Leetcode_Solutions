class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        adj = [[] for _ in range(n)]
        in_degree = [0] * n
        for u, v, cost in edges:
            if online[u] and online[v]:
                adj[u].append((v, cost))
                in_degree[v] += 1
        
        top_order = []
        queue = [i for i in range(n) if in_degree[i] == 0]
        for u in queue:
            top_order.append(u)
            for v, _ in adj[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
        
        low, high = 0, 10**9
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            dist = [float('inf')] * n
            dist[0] = 0
            
            for u in top_order:
                if dist[u] != float('inf'):
                    for v, cost in adj[u]:
                        if cost >= mid:
                            if dist[u] + cost < dist[v]:
                                dist[v] = dist[u] + cost
            
            if dist[n - 1] <= k:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return ans