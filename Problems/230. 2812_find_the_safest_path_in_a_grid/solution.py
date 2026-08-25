import collections
import heapq
from typing import List

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[n-1][n-1]:
            return 0

        safe = [[-1] * n for _ in range(n)]
        q = collections.deque()
        
        for r in range(n):
            for c in range(n):
                if grid[r][c]:
                    q.append((r, c))
                    safe[r][c] = 0
        
        dirs = (0, 1, 0, -1, 0)
        
        while q:
            r, c = q.popleft()
            for i in range(4):
                nr, nc = r + dirs[i], c + dirs[i+1]
                if 0 <= nr < n and 0 <= nc < n and safe[nr][nc] == -1:
                    safe[nr][nc] = safe[r][c] + 1
                    q.append((nr, nc))

        pq = [(-safe[0][0], 0, 0)]
        grid[0][0] = -1 
        
        while pq:
            s, r, c = heapq.heappop(pq)
            if r == n - 1 and c == n - 1:
                return -s
            
            for i in range(4):
                nr, nc = r + dirs[i], c + dirs[i+1]
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] != -1:
                    grid[nr][nc] = -1
                    heapq.heappush(pq, (max(s, -safe[nr][nc]), nr, nc))
        
        return 0