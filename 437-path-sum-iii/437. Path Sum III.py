# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.res = 0
        def dfs(node, currSum):
            if not node:
                return 0
            if currSum + node.val == targetSum:
                return 1 + dfs(node.left, currSum + node.val) + dfs(node.right, currSum + node.val) 
            return dfs(node.left, currSum + node.val) + dfs(node.right, currSum + node.val) 
        def traverse(node):
            if not node:
                return
            self.res += dfs(node, 0)
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        return self.res



