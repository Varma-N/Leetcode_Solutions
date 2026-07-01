class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        stack = []
        
        for num in nums:
            min_val = num
            max_val = num
            count = 1
            
            while stack and stack[-1][1] > min_val:
                prev_min, prev_max, prev_count = stack.pop()
                min_val = min(min_val, prev_min)
                max_val = max(max_val, prev_max)
                count += prev_count
                
            stack.append([min_val, max_val, count])
            
        ans = []
        for _, max_val, count in stack:
            ans.extend([max_val] * count)
            
        return ans
            