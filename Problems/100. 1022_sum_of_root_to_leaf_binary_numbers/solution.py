# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, current_val):
        # 1. Base Case: If node doesn't exist, return 0
            if not node:
                return 0
            
            # 2. Update the current binary number
            # Shift left by 1 bit (multiply by 2) and add current node's value
            current_val = (current_val << 1) | node.val
            
            # 3. Base Case: If it is a leaf, return the completed number
            if not node.left and not node.right:
                return current_val
            
            # 4. Recursive Step: Sum the results from left and right subtrees
            return dfs(node.left, current_val) + dfs(node.right, current_val)

        # Start DFS from root with initial value 0
        return dfs(root, 0)
