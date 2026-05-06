import math
from typing import List

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        # Sort workerTimes to process faster workers first.
        # This helps in early termination inside can_finish if total_reduced >= mountainHeight.
        workerTimes.sort()
        
        # Helper function to check if it's possible to reduce the mountain height to 0 within 'time' seconds.
        def can_finish(time: int) -> bool:
            total_reduced = 0
            for w in workerTimes:
                # For a worker with base time w, the time to reduce height by x is w * x * (x + 1) / 2.
                # We need w * x * (x + 1) / 2 <= time
                # => x * (x + 1) <= 2 * time / w
                # Let limit = floor(2 * time / w)
                # We need to find max integer x such that x^2 + x - limit <= 0.
                # The positive root of x^2 + x - limit = 0 is (-1 + sqrt(1 + 4*limit)) / 2.
                # So x = floor((-1 + sqrt(1 + 4*limit)) / 2).
                
                limit = (2 * time) // w
                delta = 1 + 4 * limit
                x = (math.isqrt(delta) - 1) // 2
                
                total_reduced += x
                if total_reduced >= mountainHeight:
                    return True
            return total_reduced >= mountainHeight

        # Binary search for the minimum time.
        # Lower bound: 1 second (minimum possible time since heights and times are >= 1)
        # Upper bound: The time taken if the fastest worker does all the work alone.
        # Max time approx 10^6 * 10^5 * 10^5 / 2 = 5 * 10^15.
        
        low = 1
        # Calculate a safe upper bound based on the fastest worker
        min_w = workerTimes[0]
        high = min_w * mountainHeight * (mountainHeight + 1) // 2
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            if can_finish(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans
