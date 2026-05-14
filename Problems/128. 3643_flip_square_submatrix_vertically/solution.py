class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        top_row, bottom_row = x, x + k - 1 
        start_col, end_col = y, y + k - 1
        i = top_row
        j = bottom_row
        while i < j:
            for col in range(start_col, end_col + 1):
                grid[i][col], grid[j][col] = grid[j][col], grid[i][col]
            i += 1
            j -= 1
        return grid
