import heapq

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]

        for u, v, w in edges:
            # original edge
            adj[u].append((v, w))
            # reversed edge
            adj[v].append((u, 2 * w))

        INF = 10**18
        dist = [INF] * n
        dist[0] = 0

        pq = [(0, 0)]

        while pq:
            cost, u = heapq.heappop(pq)

            if cost > dist[u]:
                continue

            if u == n - 1:
                return cost

            for v, w in adj[u]:
                new_cost = cost + w
                if new_cost < dist[v]:
                    dist[v] = new_cost
                    heapq.heappush(pq, (new_cost, v))

        return -1
