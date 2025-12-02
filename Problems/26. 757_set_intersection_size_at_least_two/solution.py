from typing import List

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # Sort by: end ASC, start DESC
        intervals.sort(key=lambda x: (x[1], -x[0]))
        
        # Last two selected points
        p1, p2 = -1, -1  
        result = 0
        
        for start, end in intervals:
            
            # Case 1: No overlap with {p1, p2}
            if p2 < start:
                p1, p2 = end - 1, end
                result += 2
            
            # Case 2: Exactly one overlap
            elif p1 < start:
                p1, p2 = p2, end
                result += 1
            
            # Case 3: Already have ≥2 points inside interval → do nothing
        
        return result
