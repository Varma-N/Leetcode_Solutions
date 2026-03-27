from typing import List

class SegmentTree:
    def __init__(self, n: int):
        self.n = n
        self.min_balance = [0] * (4 * n)
        self.max_balance = [0] * (4 * n)
        self.lazy = [0] * (4 * n)
    
    def push(self, node: int, start: int, end: int) -> None:
        if self.lazy[node] != 0:
            self.min_balance[node] += self.lazy[node]
            self.max_balance[node] += self.lazy[node]
            if start != end:
                self.lazy[node * 2] += self.lazy[node]
                self.lazy[node * 2 + 1] += self.lazy[node]
            self.lazy[node] = 0
    
    def update(self, node: int, start: int, end: int, l: int, r: int, val: int) -> None:
        self.push(node, start, end)
        
        if start > r or end < l:
            return
        
        if l <= start and end <= r:
            self.lazy[node] += val
            self.push(node, start, end)
            return
        
        mid = (start + end) // 2
        self.update(node * 2, start, mid, l, r, val)
        self.update(node * 2 + 1, mid + 1, end, l, r, val)
        
        self.min_balance[node] = min(self.min_balance[node * 2], self.min_balance[node * 2 + 1])
        self.max_balance[node] = max(self.max_balance[node * 2], self.max_balance[node * 2 + 1])
    
    def get_leftmost(self, node: int, start: int, end: int) -> int:
        self.push(node, start, end)
        
        # Prune if zero cannot exist in this segment
        if self.min_balance[node] > 0 or self.max_balance[node] < 0:
            return -1
        
        if start == end:
            return start if self.min_balance[node] == 0 else -1
        
        mid = (start + end) // 2
        left_result = self.get_leftmost(node * 2, start, mid)
        if left_result != -1:
            return left_result
        return self.get_leftmost(node * 2 + 1, mid + 1, end)


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        prev_index = {}
        st = SegmentTree(n)
        max_len = 0
        
        for i in range(n):
            # +1 for even, -1 for odd
            val = 1 if (nums[i] & 1) == 0 else -1
            
            # If this number appeared before, remove its contribution from [0, prev]
            if nums[i] in prev_index:
                prev = prev_index[nums[i]]
                st.update(1, 0, n - 1, 0, prev, -val)
            
            # Add contribution to [0, i] (net effect: add to (prev, i])
            st.update(1, 0, n - 1, 0, i, val)
            prev_index[nums[i]] = i
            
            # Find leftmost start index where balance == 0
            left = st.get_leftmost(1, 0, n - 1)
            if left != -1 and left <= i:
                max_len = max(max_len, i - left + 1)
        
        return max_len
