class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        flat_grid = [element for row in grid for element in row]
        
        base_remainder = flat_grid[0] % x
        for value in flat_grid:
            if value % x != base_remainder:
                return -1
        
        flat_grid.sort()
        n = len(flat_grid)
        median_target = flat_grid[n // 2]
        
        total_operations = 0
        for value in flat_grid:
            total_operations += abs(value - median_target) // x
        
        return total_operations
