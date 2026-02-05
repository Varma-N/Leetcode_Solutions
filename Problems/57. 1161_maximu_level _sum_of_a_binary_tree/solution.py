# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
from typing import Optional

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([root])
        max_sum = float('-inf')
        min_level = 1
        current_level = 1
        
        while queue:
            level_sum = 0
            level_size = len(queue)
            
            # Process all nodes at the current level
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                
                # Add children to queue for next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Check if current level has a better sum
            if level_sum > max_sum:
                max_sum = level_sum
                min_level = current_level
            
            current_level += 1
        
        return min_level
