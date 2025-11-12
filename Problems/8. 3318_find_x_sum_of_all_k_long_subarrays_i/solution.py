from typing import List

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        result = []
        
        for i in range(n - k + 1):
            window = nums[i:i + k]
            freq = [0] * 51  # since 1 <= nums[i] <= 50
            
            for num in window:
                freq[num] += 1

            candidates = [(freq[val], val) for val in range(1, 51) if freq[val] > 0]

            # Sort primarily by frequency (desc), then by value (desc)
            candidates.sort(key=lambda pair: (-pair[0], -pair[1]))
            
            # Select top x unique values
            top_vals = {val for _, val in candidates[:x]}
            
            # Compute sum of all instances of these top values
            total = sum(num for num in window if num in top_vals)
            result.append(total)
        
        return result
