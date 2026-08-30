class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        removed = 0
        max_end = -1
        
        for start, end in intervals:
            if end <= max_end:
                removed += 1
            else:
                max_end = end
                
        return len(intervals) - removed
        