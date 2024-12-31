# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.res = 0
        # Traverse the tree
        def dfs(node):
            if not node:
                return
            self.res += validPaths(node, 0)
            dfs(node.left)
            dfs(node.right)
        
        def validPaths(node, currSum):
            if not node:
                return 0
            if currSum + node.val == targetSum:
                return 1 + validPaths(node.left, currSum + node.val) + validPaths(node.right, currSum + node.val)
            return validPaths(node.left, currSum + node.val) + validPaths(node.right, currSum + node.val)

        dfs(root)
        return self.res