from typing import List
from collections import defaultdict, Counter
from math import inf

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        slope_i = defaultdict(list)
        mid_s = defaultdict(list)
        n = len(points)

        # Enumerate all point pairs
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx, dy = x2 - x1, y2 - y1

                # Compute slope and intercept
                if dx != 0:
                    s = dy / dx
                    b = (y1 * dx - x1 * dy) / dx
                else:
                    s = inf
                    b = x1

                slope_i[s].append(b)

                # Compute midpoint (no division needed)
                mid = (x1 + x2, y1 + y2)
                mid_s[mid].append(s)

        result = 0

        # Count pairs of parallel segments with different intercepts
        for intercepts in slope_i.values():
            if len(intercepts) <= 1:
                continue
            c = Counter(intercepts)
            acc = 0
            for cnt in c.values():
                result += acc * cnt
                acc += cnt

        # Subtract parallelogram overcounts (same midpoint & slope)
        for slopes in mid_s.values():
            if len(slopes) <= 1:
                continue
            c = Counter(slopes)
            acc = 0
            for cnt in c.values():
                result -= acc * cnt
                acc += cnt

        return result
