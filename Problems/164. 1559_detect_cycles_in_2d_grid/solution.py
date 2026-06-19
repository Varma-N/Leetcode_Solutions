class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c, pr, pc, char):
            """
            r, c: current coordinates
            pr, pc: parent coordinates (where we came from)
            char: the target character we are tracking for a cycle
            """
            visited.add((r, c))
            
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == char:
                    if (nr, nc) in visited and (nr, nc) != (pr, pc):
                        return True
                    
                    if (nr, nc) not in visited:
                        if dfs(nr, nc, r, c, char):
                            return True
            return False

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited:
                    if dfs(r, c, -1, -1, grid[r][c]):
                        return True
                        
        return False
        