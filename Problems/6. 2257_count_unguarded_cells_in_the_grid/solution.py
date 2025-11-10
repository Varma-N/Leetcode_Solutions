from typing import List

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [['.' for _ in range(n)] for _ in range(m)]

        for r, c in walls:
            grid[r][c] = 'W'

        for r, c in guards:
            grid[r][c] = 'G'

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for r, c in guards:
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                while 0 <= nr < m and 0 <= nc < n:
                    if grid[nr][nc] == 'W' or grid[nr][nc] == 'G':
                        break
                    if grid[nr][nc] == '.':
                        grid[nr][nc] = 'V'
                    nr += dr
                    nc += dc

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '.':
                    count += 1
        
        return count
