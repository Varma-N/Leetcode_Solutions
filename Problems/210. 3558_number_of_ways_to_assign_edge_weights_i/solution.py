import collections
class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        n = len(edges)
        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        max_depth = 0
        queue = collections.deque([(1,0)])
        visited = {1}
        while queue:
            u, depth = queue.popleft()
            max_depth = max(max_depth, depth)

            for v in adj[u]:
                if v not in visited:
                    visited.add(v)
                    queue.append((v, depth + 1))
        return pow(2, max_depth - 1, 10**9 + 7)