from typing import List
from collections import defaultdict

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        # Step 1: Group all indices by their value
        indices_map = defaultdict(list)
        for i, val in enumerate(nums):
            indices_map[val].append(i)
        
        res = [0] * len(nums)
        
        # Step 2: For each group of indices, calculate distances using prefix sums
        for val, idxs in indices_map.items():
            n = len(idxs)
            if n <= 1:
                continue
            
            # Calculate the total sum of indices for this value to help with the "right side"
            total_sum = sum(idxs)
            prefix_sum = 0
            
            for i, curr_idx in enumerate(idxs):
                # Using the derived formula:
                # Left side distances: (i * curr_idx) - prefix_sum
                # Right side distances: (total_sum - prefix_sum - curr_idx) - (n - 1 - i) * curr_idx
                
                left_dist = (i * curr_idx) - prefix_sum
                
                # Suffix sum is (total_sum - prefix_sum - curr_idx)
                suffix_sum = total_sum - prefix_sum - curr_idx
                right_dist = suffix_sum - (n - 1 - i) * curr_idx
                
                res[curr_idx] = left_dist + right_dist
                
                # Update prefix_sum for the next index in the group
                prefix_sum += curr_idx
                
        return res
        