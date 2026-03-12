# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        def dfs(node, prevTaken):
            if not node:
                return 0
            
            if prevTaken:
                return dfs(node.left, False) + dfs(node.right, False)
            
            take = node.val + dfs(node.left, True) + dfs(node.right, True)
            skip = dfs(node.left, False) + dfs(node.right, False)
            return max(take, skip)

        return dfs(root, False)
