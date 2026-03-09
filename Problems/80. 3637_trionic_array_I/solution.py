class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 4:  # Minimum 4 elements required (0,1,2,3)
            return False
        
        # Step 1: inc_prefix[i] = True iff [0..i] is strictly increasing
        inc_prefix = [True] * n
        for i in range(1, n):
            inc_prefix[i] = inc_prefix[i-1] and (nums[i-1] < nums[i])
        
        # Step 2: inc_suffix[i] = True iff [i..n-1] is strictly increasing
        inc_suffix = [True] * n
        for i in range(n-2, -1, -1):
            inc_suffix[i] = (nums[i] < nums[i+1]) and inc_suffix[i+1]
        
        # Step 3: dec_len[i] = length of maximal strictly decreasing run starting at i
        dec_len = [1] * n
        for i in range(n-2, -1, -1):
            if nums[i] > nums[i+1]:
                dec_len[i] = dec_len[i+1] + 1
        
        # Step 4: next_true[i] = smallest j >= i where inc_suffix[j] is True
        next_true = [float('inf')] * n
        next_true[-1] = n-1 if inc_suffix[-1] else float('inf')
        for i in range(n-2, -1, -1):
            next_true[i] = i if inc_suffix[i] else next_true[i+1]
        
        # Step 5: Check all valid p (1 <= p <= n-3)
        for p in range(1, n-2):  # p must allow q >= p+1 and q <= n-2
            # Skip if prefix isn't strictly increasing OR no decreasing step after p
            if not inc_prefix[p] or dec_len[p] < 2:
                continue
            
            # Max q in decreasing run (capped at n-2 for valid suffix start)
            max_q = min(p + dec_len[p] - 1, n-2)
            if p + 1 > max_q:  # No valid q in range
                continue
            
            # O(1) check: exists q in [p+1, max_q] with valid increasing suffix?
            if next_true[p+1] <= max_q:
                return True
        
        return False
