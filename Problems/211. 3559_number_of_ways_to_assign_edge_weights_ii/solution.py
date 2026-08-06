class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        LOG = 18
        up = [[0] * LOG for _ in range(n + 1)]
        depth = [0] * (n + 1)
        
        queue = [1]
        head = 0
        visited = [False] * (n + 1)
        visited[1] = True
        
        while head < len(queue):
            curr = queue[head]
            head += 1
            for neighbor in adj[curr]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    depth[neighbor] = depth[curr] + 1
                    up[neighbor][0] = curr
                    queue.append(neighbor)
                    
        for j in range(1, LOG):
            for i in range(1, n + 1):
                if up[i][j-1] != 0:
                    up[i][j] = up[up[i][j-1]][j-1]
                    
        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            for j in range(LOG):
                if (diff >> j) & 1:
                    u = up[u][j]
            if u == v:
                return u
            for j in range(LOG - 1, -1, -1):
                if up[u][j] != up[v][j]:
                    u = up[u][j]
                    v = up[v][j]
            return up[u][0]

        MOD = 10**9 + 7
        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)
            else:
                lca = get_lca(u, v)
                dist = depth[u] + depth[v] - 2 * depth[lca]
                ans.append(pow(2, dist - 1, MOD))
        return ans
