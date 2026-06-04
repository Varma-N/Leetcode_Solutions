from typing import List
import math

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        pos_map = {}
        for index, val in enumerate(nums):
            if val not in pos_map:
                pos_map[val] = []
            pos_map[val].append(index)
        
        min_dist = float('inf')
        found = False
        for val in pos_map:
            indices = pos_map[val]
            if len(indices) >= 3:
                found = True
                for i in range(len(indices) - 2):
                    current_dist = 2 * (indices[i+2] - indices[i])
                    if current_dist < min_dist:
                        min_dist = current_dist
        
        return min_dist if found else -1
