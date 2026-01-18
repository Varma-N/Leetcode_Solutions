from typing import List

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        if len(grid) < 3 or len(grid[0]) < 3:
            return 0

        def is_magic(i: int, j: int) -> bool:
            seen = set()

            # Check values 1..9 and uniqueness
            for r in range(3):
                for c in range(3):
                    val = grid[i + r][j + c]
                    if val < 1 or val > 9 or val in seen:
                        return False
                    seen.add(val)

            # Check rows
            for r in range(3):
                if sum(grid[i + r][j:j + 3]) != 15:
                    return False

            # Check columns
            for c in range(3):
                if sum(grid[i + r][j + c] for r in range(3)) != 15:
                    return False

            # Check diagonals
            if grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2] != 15:
                return False
            if grid[i][j + 2] + grid[i + 1][j + 1] + grid[i + 2][j] != 15:
                return False

            return True

        count = 0
        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                if is_magic(i, j):
                    count += 1

        return count
