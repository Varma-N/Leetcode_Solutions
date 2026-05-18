class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        total_sum = 0
        row_sums = [0] * m
        col_sums = [0] * n 
        for r in range(m):
            for c in range(n):
                val = grid[r][c]
                total_sum += val
                row_sums[r] += val
                col_sums[c] += val
        if total_sum % 2 != 0:
            return False
    
        target = total_sum // 2
    
        current_sum = 0
        for r in range(m - 1):
            current_sum += row_sums[r]
            if current_sum == target:
                return True

        current_sum = 0
        for c in range(n - 1):
            current_sum += col_sums[c]
            if current_sum == target:
                return True

        return False 

        
