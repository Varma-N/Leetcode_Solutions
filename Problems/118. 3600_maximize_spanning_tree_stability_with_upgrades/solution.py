import sys
from typing import List
from bisect import bisect_left

class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        must_edges = []
        opt_edges = []
        for u, v, s, must in edges:
            if must:
                must_edges.append((u, v, s))
            else:
                opt_edges.append((u, v, s))
        
        # DSU state for mandatory edges
        must_p = list(range(n))
        must_r = [0] * n
        components = n
        min_must_s = float('inf')
        
        # Helper for find with path compression (iterative)
        def find(i, p):
            root = i
            while p[root] != root:
                root = p[root]
            curr = i
            while curr != root:
                nxt = p[curr]
                p[curr] = root
                curr = nxt
            return root
        
        # Helper for union
        def union(i, j, p, r):
            root_i = find(i, p)
            root_j = find(j, p)
            if root_i != root_j:
                if r[root_i] < r[root_j]:
                    root_i, root_j = root_j, root_i
                p[root_j] = root_i
                if r[root_i] == r[root_j]:
                    r[root_i] += 1
                return True
            return False
            
        # Process mandatory edges
        for u, v, s in must_edges:
            if s < min_must_s:
                min_must_s = s
            if not union(u, v, must_p, must_r):
                return -1 # Cycle in mandatory edges
            else:
                components -= 1
        
        # Check global connectivity with all optional edges
        check_p = must_p[:]
        check_r = must_r[:]
        curr_comp = components
        
        for u, v, s in opt_edges:
            if union(u, v, check_p, check_r):
                curr_comp -= 1
        
        if curr_comp > 1:
            return -1
            
        # Sort optional edges by strength for binary search optimization
        opt_edges.sort(key=lambda x: x[2])
        m_opt = len(opt_edges)
        opt_s = [x[2] for x in opt_edges]
        
        # Binary search range
        # Stability cannot exceed the minimum strength of any mandatory edge.
        # If no mandatory edges, max possible stability is bounded by max upgraded optional edge (2 * 10^5).
        if min_must_s == float('inf'):
            high = 200000
        else:
            high = min_must_s
            
        low = 1
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            
            # Check feasibility of stability 'mid'
            curr_p = must_p[:]
            curr_r = must_r[:]
            curr_comp = components
            upgrades = 0
            possible = True
            
            # Identify ranges in sorted optional edges
            # Free edges: s >= mid (no upgrade needed)
            idx_free = bisect_left(opt_s, mid)
            # Paid edges: s < mid but 2*s >= mid => s >= ceil(mid/2)
            idx_paid = bisect_left(opt_s, (mid + 1) // 2)
            
            # Process Free Edges first (cost 0)
            if curr_comp > 1:
                for i in range(idx_free, m_opt):
                    u, v, s = opt_edges[i]
                    if union(u, v, curr_p, curr_r):
                        curr_comp -= 1
                        if curr_comp == 1:
                            break
            
            if curr_comp == 1:
                ans = mid
                low = mid + 1
                continue
            
            # Process Paid Edges (cost 1)
            if curr_comp > 1:
                for i in range(idx_paid, idx_free):
                    u, v, s = opt_edges[i]
                    if union(u, v, curr_p, curr_r):
                        curr_comp -= 1
                        upgrades += 1
                        if upgrades > k:
                            possible = False
                            break
                        if curr_comp == 1:
                            break
            
            if possible and curr_comp == 1:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return ans
        
