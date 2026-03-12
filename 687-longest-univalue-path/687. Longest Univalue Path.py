# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        self.res = 0
        @cache
        def dfs(node):
            if not node:
                return 0
            
            leftLen = dfs(node.left)
            rightLen = dfs(node.right)
            left_path = right_path = 0
            if node.left and node.left.val == node.val:
                left_path = leftLen + 1
            if node.right and node.right.val == node.val:
                right_path = rightLen + 1
            self.res = max(self.res, left_path + right_path)
            return max(left_path, right_path)
            
        dfs(root)
        return self.res
            
