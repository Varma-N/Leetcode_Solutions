from collections import Counter
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        count = Counter(nums)
        max_len = 1
        
        if 1 in count:
            ones = count[1]
            if ones % 2 == 0:
                ones -= 1
            max_len = max(max_len, ones)
            
        for num in count:
            if num == 1:
                continue
            
            curr_len = 0
            curr = num
            
            while count[curr] >= 2:
                curr_len += 2
                curr *= curr
                
            if count[curr] > 0:
                curr_len += 1
            else:
                curr_len -= 1
                
            max_len = max(max_len, curr_len)
            
        return max_len
        