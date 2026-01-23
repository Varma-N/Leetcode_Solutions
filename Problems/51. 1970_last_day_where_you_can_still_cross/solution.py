from typing import List

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        # Convert to 0-based indexing
        cells = [(r - 1, c - 1) for r, c in cells]
        
        # Grid: 1 = water, 0 = land
        grid = [[1] * col for _ in range(row)]
        
        n = row * col
        parent = list(range(n + 2))
        rank = [0] * (n + 2)
        
        TOP = n
        BOTTOM = n + 1
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return
            if rank[rx] < rank[ry]:
                rx, ry = ry, rx
            parent[ry] = rx
            if rank[rx] == rank[ry]:
                rank[rx] += 1
        
        def get_id(r, c):
            return r * col + c
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Process days in reverse
        for day in range(len(cells) - 1, -1, -1):
            r, c = cells[day]
            grid[r][c] = 0
            curr = get_id(r, c)
            
            if r == 0:
                union(curr, TOP)
            if r == row - 1:
                union(curr, BOTTOM)
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 0:
                    union(curr, get_id(nr, nc))
            
            if find(TOP) == find(BOTTOM):
                return day
        
        return 0
