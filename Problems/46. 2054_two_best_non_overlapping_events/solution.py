import heapq
from typing import List

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[0])

        min_heap = []  # (endTime, value)
        best_past_value = 0
        max_sum = 0

        for start, end, value in events:
            while min_heap and min_heap[0][0] < start:
                _, past_value = heapq.heappop(min_heap)
                best_past_value = max(best_past_value, past_value)

            max_sum = max(max_sum, value + best_past_value)

            heapq.heappush(min_heap, (end, value))

        return max_sum
