# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, curr):
            if not node:
                return 0
            
            if node.left is None and node.right is None:
                return int(curr+str(node.val), 2)
            
            return dfs(node.left, curr + str(node.val)) + dfs(node.right, curr + str(node.val))
        
        return dfs(root, "")

