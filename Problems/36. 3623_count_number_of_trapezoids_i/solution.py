from typing import List
from collections import defaultdict

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9 + 7
        
        # Count points on each horizontal line (same y)
        ycount = defaultdict(int)
        for x, y in points:
            ycount[y] += 1
        
        # Number of horizontal segments per y: C(n, 2)
        segs = []
        for cnt in ycount.values():
            if cnt >= 2:
                segs.append(cnt * (cnt - 1) // 2)
        
        # Need at least two y-levels with segments
        if len(segs) < 2:
            return 0
        
        # Sum over all pairs using prefix sums
        ans = 0
        prefix_sum = 0
        for s in segs:
            ans = (ans + s * prefix_sum) % MOD
            prefix_sum = (prefix_sum + s) % MOD
        
        return ans
