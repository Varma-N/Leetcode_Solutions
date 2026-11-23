class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        if (m + n - 1) % 2 != 0:
            return False

        if grid[0][0] == ')' or grid[m-1][n-1] == '(':
            return False

        visited = set()

        def dfs(row, col, balance):
            if row >= m or col >= n:
                return False

            if (row, col, balance) in visited:
                return False

            if grid[row][col] == '(':
                new_balance = balance + 1
            else:
                new_balance = balance - 1

            if new_balance < 0:
                return False

            if row == m - 1 and col == n-1:
                return new_balance == 0

            if dfs(row+1, col, new_balance) or dfs(row, col+1, new_balance):
                return True
            
            visited.add((row, col, balance))
            return False
        
        return dfs(0, 0, 0)