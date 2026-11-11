class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        min_lengths = [float('inf')] * n
        
        left = 0
        current_sum = 0
        best_so_far = float('inf')
        min_result = float('inf')
        
        for right in range(n):
            current_sum += arr[right]
            
            while current_sum > target and left <= right:
                current_sum -= arr[left]
                left += 1
                
            if current_sum == target:
                curr_len = right - left + 1
                
                if left > 0 and min_lengths[left - 1] != float('inf'):
                    min_result = min(min_result, curr_len + min_lengths[left - 1])
                    
                best_so_far = min(best_so_far, curr_len)
                
            min_lengths[right] = best_so_far
            
        return min_result if min_result != float('inf') else -1