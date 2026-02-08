# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        def height(node):
            if not node:
                return 0
            
            return 1 + max(height(node.left), height(node.right))
        
        def trav(node):
            if not node:
                return True
            
            return abs(height(node.left) - height(node.right)) <= 1 and trav(node.left) and trav(node.right)
        
        return trav(root)