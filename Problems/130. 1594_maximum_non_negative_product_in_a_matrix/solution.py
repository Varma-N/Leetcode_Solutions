class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m = len(grid)
        n = len(grid[0])
        
        # dp_max[i][j] stores the maximum product to reach cell (i, j)
        # dp_min[i][j] stores the minimum product to reach cell (i, j)
        # We need both because a negative number can flip a min product to a max product.
        dp_max = [[0] * n for _ in range(m)]
        dp_min = [[0] * n for _ in range(m)]
        
        # Base Case: Initialize the starting cell (0, 0)
        dp_max[0][0] = grid[0][0]
        dp_min[0][0] = grid[0][0]
        
        # Iterate through every cell in the grid
        for i in range(m):
            for j in range(n):
                # Skip the starting cell as it's already initialized
                if i == 0 and j == 0:
                    continue
                
                # List to store all possible products coming from top or left
                candidates = []
                
                # If we can come from the Top (i-1, j)
                if i > 0:
                    # Multiply current value with both max and min from the top
                    # We check both because grid[i][j] might be negative
                    candidates.append(dp_max[i-1][j] * grid[i][j])
                    candidates.append(dp_min[i-1][j] * grid[i][j])
                
                # If we can come from the Left (i, j-1)
                if j > 0:
                    # Multiply current value with both max and min from the left
                    candidates.append(dp_max[i][j-1] * grid[i][j])
                    candidates.append(dp_min[i][j-1] * grid[i][j])
                
                # Update the current cell's max and min based on all candidates
                dp_max[i][j] = max(candidates)
                dp_min[i][j] = min(candidates)
        
        # The result is the maximum product at the bottom-right corner
        result = dp_max[m-1][n-1]
        
        # Condition: Return -1 if the maximum product is negative
        if result < 0:
            return -1
        
        # Condition: Return result modulo 10^9 + 7 (only if non-negative)
        return result % MOD

        
