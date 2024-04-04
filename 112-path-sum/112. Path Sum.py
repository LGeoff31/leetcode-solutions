# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        def dfs(node, currSum):
            if not node.left and not node.right:
                return currSum == targetSum
            res = False
            if node.left:
                res = res or dfs(node.left, currSum + node.left.val)
            if node.right:
                res = res or dfs(node.right, currSum + node.right.val)
            return res
        return dfs(root, root.val)