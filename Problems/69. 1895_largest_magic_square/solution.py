class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # Build row prefix sums
        row_prefix = [[0] * (n + 1) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                row_prefix[i][j + 1] = row_prefix[i][j] + grid[i][j]
        
        # Build column prefix sums  
        col_prefix = [[0] * n for _ in range(m + 1)]
        for j in range(n):
            for i in range(m):
                col_prefix[i + 1][j] = col_prefix[i][j] + grid[i][j]
        
        def get_row_sum(row, start_col, end_col):
            return row_prefix[row][end_col + 1] - row_prefix[row][start_col]
        
        def get_col_sum(col, start_row, end_row):
            return col_prefix[end_row + 1][col] - col_prefix[start_row][col]
        
        def is_magic_square(r, c, k):
            # Calculate target sum from first row
            target = get_row_sum(r, c, c + k - 1)
            
            # Check all rows
            for i in range(r, r + k):
                if get_row_sum(i, c, c + k - 1) != target:
                    return False
            
            # Check all columns
            for j in range(c, c + k):
                if get_col_sum(j, r, r + k - 1) != target:
                    return False
            
            # Check main diagonal (top-left to bottom-right)
            diag1_sum = 0
            for i in range(k):
                diag1_sum += grid[r + i][c + i]
            if diag1_sum != target:
                return False
            
            # Check anti-diagonal (top-right to bottom-left)
            diag2_sum = 0
            for i in range(k):
                diag2_sum += grid[r + i][c + k - 1 - i]
            if diag2_sum != target:
                return False
            
            return True
        
        # Try from largest possible size down to 2
        max_size = min(m, n)
        for k in range(max_size, 1, -1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    if is_magic_square(i, j, k):
                        return k
        
        # If no magic square of size >= 2 found, return 1
        return 1
