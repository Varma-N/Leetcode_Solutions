# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nodes = []
        
        # Step 1: In-order traversal to collect nodes in sorted order
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            nodes.append(node)
            inorder(node.right)
        
        inorder(root)
        
        # Step 2: Build balanced BST from sorted nodes
        def build_balanced(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            node = nodes[mid]
            node.left = build_balanced(left, mid - 1)
            node.right = build_balanced(mid + 1, right)
            return node
        
        return build_balanced(0, len(nodes) - 1)
