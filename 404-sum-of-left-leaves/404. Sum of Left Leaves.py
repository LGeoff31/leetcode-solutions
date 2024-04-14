# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(node):
            print(node.val)
            if node.left:
                if node.left.left is None and node.left.right is None:
                    self.res+=node.left.val
            if node.right: dfs(node.right)
            if node.left: dfs(node.left)
        # if root.left is None: return 0
        dfs(root)
        return self.res
        