from typing import List

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        
        # d1[i][j] stores sum of main diagonal ending at grid[i-1][j-1]
        # Dimensions (m+1) x (n+1)
        d1 = [[0] * (n + 1) for _ in range(m + 1)]
        
        # d2[i][j] stores sum of anti-diagonal ending at grid[i-1][j-1]
        # Dimensions (m+1) x (n+2) to handle c+2 index safely
        d2 = [[0] * (n + 2) for _ in range(m + 1)]
        
        for r in range(m):
            for c in range(n):
                d1[r+1][c+1] = grid[r][c] + d1[r][c]
                d2[r+1][c+1] = grid[r][c] + d2[r][c+2]
                
        def get_d1(r1, c1, r2, c2):
            # Sum from (r1, c1) to (r2, c2) along main diagonal
            # Assumes r1 <= r2, c1 <= c2
            return d1[r2+1][c2+1] - d1[r1][c1]
            
        def get_d2(r1, c1, r2, c2):
            # Sum from (r1, c1) to (r2, c2) along anti-diagonal
            # Assumes r1 <= r2, c1 >= c2
            return d2[r2+1][c2+1] - d2[r1][c1+2]
            
        sums = set()
        
        for r in range(m):
            for c in range(n):
                # k=0 case (single cell rhombus)
                sums.add(grid[r][c])
                
                # Calculate max possible k for this top vertex (r, c)
                # Bottom vertex row: r + 2k < m  => 2k <= m - 1 - r
                # Left vertex col: c - k >= 0    => k <= c
                # Right vertex col: c + k < n    => k <= n - 1 - c
                max_k = min((m - 1 - r) // 2, c, n - 1 - c)
                
                for k in range(1, max_k + 1):
                    # Vertices coordinates
                    tr, tc = r, c             # Top
                    rr, rc = r + k, c + k     # Right
                    br, bc = r + 2*k, c       # Bottom
                    lr, lc = r + k, c - k     # Left
                    
                    # Calculate sum of 4 edges
                    # Top -> Right
                    s1 = get_d1(tr, tc, rr, rc)
                    # Right -> Bottom
                    s2 = get_d2(rr, rc, br, bc)
                    # Left -> Bottom (equivalent to Bottom -> Left for sum)
                    s3 = get_d1(lr, lc, br, bc)
                    # Top -> Left (equivalent to Left -> Top for sum)
                    s4 = get_d2(tr, tc, lr, lc)
                    
                    # Subtract vertices because they are counted twice (once in each adjacent edge)
                    current_sum = s1 + s2 + s3 + s4 - (grid[tr][tc] + grid[rr][rc] + grid[br][bc] + grid[lr][lc])
                    sums.add(current_sum)
                    
        sorted_sums = sorted(list(sums), reverse=True)
        return sorted_sums[:3]
