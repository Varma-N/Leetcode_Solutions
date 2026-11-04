# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.matching_nodes = 0
        
        def post_order(node):
            if not node:
                return (0, 0)
            
            # 1. Traverse left and right subtrees
            left_sum, left_count = post_order(node.left)
            right_sum, right_count = post_order(node.right)
            
            # 2. Calculate sum and count for the current subtree
            curr_sum = node.val + left_sum + right_sum
            curr_count = 1 + left_count + right_count
            
            # 3. Check if the average equals the node's value (integer division)
            if node.val == curr_sum // curr_count:
                self.matching_nodes += 1
            
            # 4. Return to parent
            return (curr_sum, curr_count)
            
        post_order(root)
        
        return self.matching_nodes