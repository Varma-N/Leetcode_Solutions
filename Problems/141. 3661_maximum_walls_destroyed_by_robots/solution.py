import bisect
from typing import List

class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        n = len(robots)
        if n == 0:
            return 0
        
        # Pair up robots with their distances and sort them by position
        rob_dist = sorted(zip(robots, distance))
        
        # Any wall sharing a position with a robot is guaranteed to be destroyed
        rob_positions = {r for r, _ in rob_dist}
        base_destroyed = 0
        filtered_walls = []
        
        for w in walls:
            if w in rob_positions:
                base_destroyed += 1
            else:
                filtered_walls.append(w)
        
        filtered_walls.sort()
        
        # Edge case: No walls strictly between/outside robots
        if not filtered_walls:
            return base_destroyed
            
        # DP State Variables
        # dp[0]: Max walls destroyed up to current gap if the current robot fires LEFT
        # dp[1]: Max walls destroyed up to current gap if the current robot fires RIGHT
        dp = [0, 0]
        
        # Process Gap 0: (walls entirely before the very first robot)
        R0, D0 = rob_dist[0]
        idx_end = bisect.bisect_left(filtered_walls, R0)
        
        if idx_end > 0:
            limit_L = R0 - D0
            C_suff_0 = idx_end - bisect.bisect_left(filtered_walls, limit_L, 0, idx_end)
        else:
            C_suff_0 = 0
            
        dp[0] = C_suff_0
        dp[1] = 0  # Firing right covers nothing in Gap 0
        
        # Process Gaps 1 to n-1 (walls strictly between adjacent robots)
        for k in range(1, n):
            R_prev, D_prev = rob_dist[k-1]
            R_curr, D_curr = rob_dist[k]
            
            idx_start = bisect.bisect_right(filtered_walls, R_prev)
            idx_end = bisect.bisect_left(filtered_walls, R_curr)
            N_k = idx_end - idx_start
            
            if N_k > 0:
                limit_R = R_prev + D_prev
                limit_L = R_curr - D_curr
                
                # Prefix covered by the left robot firing right
                C_pref = bisect.bisect_right(filtered_walls, limit_R, idx_start, idx_end) - idx_start
                # Suffix covered by the right robot firing left
                C_suff = idx_end - bisect.bisect_left(filtered_walls, limit_L, idx_start, idx_end)
                
                # Check if coverage bounds overlap (covers all walls in this specific gap)
                if limit_R >= limit_L:
                    W_k_11 = N_k 
                else:
                    W_k_11 = C_pref + C_suff
            else:
                C_pref = 0
                C_suff = 0
                W_k_11 = 0
            
            # Transition DP states
            new_dp0 = max(dp[0] + C_suff, dp[1] + W_k_11)
            new_dp1 = max(dp[0] + 0,      dp[1] + C_pref)
            
            dp[0], dp[1] = new_dp0, new_dp1
        
        # Process Gap N: (walls entirely after the last robot)
        Rn_1, Dn_1 = rob_dist[-1]
        idx_start = bisect.bisect_right(filtered_walls, Rn_1)
        idx_end = len(filtered_walls)
        
        if idx_start < idx_end:
            C_pref_n = bisect.bisect_right(filtered_walls, Rn_1 + Dn_1, idx_start, idx_end) - idx_start
        else:
            C_pref_n = 0
            
        # The best outcome is the base walls + the optimal sequence from the DP array
        return base_destroyed + max(dp[0], dp[1] + C_pref_n)
