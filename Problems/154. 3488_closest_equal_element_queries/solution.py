from collections import defaultdict
import bisect

class Solution:
    def solveQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        n = len(nums)
        res_arr = []
        
        val_to_indices = defaultdict(list)
        for idx, val in enumerate(nums):
            val_to_indices[val].append(idx)
            
        for qi in queries:
            target_val = nums[qi]
            indices = val_to_indices[target_val]
            
            if len(indices) <= 1:
                res_arr.append(-1)
                continue
            
            pos = bisect.bisect_left(indices, qi)
            min_dist = n
            
            candidates = []
            if pos > 0:
                candidates.append(indices[pos-1])
            if pos < len(indices) - 1:
                candidates.append(indices[pos+1])
            
            candidates.append(indices[0])
            candidates.append(indices[-1])
            
            for i in candidates:
                if i != qi:
                    dist = abs(qi - i)
                    min_dist = min(min_dist, dist, n - dist)
            
            res_arr.append(min_dist)
            
        return res_arr
