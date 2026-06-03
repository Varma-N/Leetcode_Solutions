from collections import defaultdict
class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        indices_map = defaultdict(list)
        for index, val in enumerate(nums):
            indices_map[val].append(index)
        
        min_dist = float('inf')
        found = False
        for val in indices_map:
            indices = indices_map[val]
            if len(indices) < 3:
                continue
            for z in range(len(indices) - 2):
                found = True
                current_dist = 2 * (indices[z+2] - indices[z])
                if current_dist < min_dist:
                    min_dist = current_dist
                    
        return min_dist if found else -1

            
