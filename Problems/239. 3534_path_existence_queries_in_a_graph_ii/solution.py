class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        s = sorted(list(set(nums)))
        m = len(s)
        val_to_idx = {val: i for i, val in enumerate(s)}
        
        LOG = 18
        jump = [[0] * LOG for _ in range(m)]
        
        right_ptr = 0
        for i in range(m):
            while right_ptr < m and s[right_ptr] <= s[i] + maxDiff:
                right_ptr += 1
            jump[i][0] = right_ptr - 1
            
        for j in range(1, LOG):
            for i in range(m):
                jump[i][j] = jump[jump[i][j-1]][j-1]
                
        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)
                continue
                
            val_u, val_v = nums[u], nums[v]
            if val_u == val_v:
                ans.append(1)
                continue
                
            A = min(val_u, val_v)
            B = max(val_u, val_v)
            
            start = val_to_idx[A]
            target = val_to_idx[B]
            
            curr = start
            steps = 0
            
            for j in range(LOG - 1, -1, -1):
                if jump[curr][j] < target:
                    curr = jump[curr][j]
                    steps += 1 << j
                    
            if jump[curr][0] < target:
                ans.append(-1)
            else:
                ans.append(steps + 1)
                
        return ans