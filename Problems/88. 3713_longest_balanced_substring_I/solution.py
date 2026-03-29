class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        best = 0
        
        # Hoist to local variables for speed in tight loops
        nums_local = nums
        
        for i in range(n):
            # Early termination: impossible to beat current best
            if n - i <= best:
                break
            
            seen_even = set()
            seen_odd = set()
            cnt_even = 0
            cnt_odd = 0
            
            # Inner loop expansion
            for j in range(i, n):
                x = nums_local[j]
                if x & 1:  # Odd number (bitwise check is fastest)
                    if x not in seen_odd:
                        seen_odd.add(x)
                        cnt_odd += 1
                else:  # Even number
                    if x not in seen_even:
                        seen_even.add(x)
                        cnt_even += 1
                
                # Check balance with explicit counters (avoid len() calls)
                if cnt_even == cnt_odd:
                    cur_len = j - i + 1
                    if cur_len > best:
                        best = cur_len
        
        return best
