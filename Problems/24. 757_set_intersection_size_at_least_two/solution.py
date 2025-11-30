from typing import List

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # Sort by end increasing, start decreasing
        intervals.sort(key=lambda x: (x[1], -x[0]))
        
        # The two largest chosen points
        p1, p2 = -1, -1
        result = 0
        
        for start, end in intervals:
            # No overlap → need 2 new points
            if p2 < start:
                p1, p2 = end - 1, end
                result += 2
            
            # Exactly 1 point overlaps → need 1 new point
            elif p1 < start:
                p1, p2 = p2, end
                result += 1
            
            # Else both p1, p2 already lie inside interval → do nothing
        
        return result
