# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        def validBST(node, l, r):
            if not node:
                return 0
            if node.val <= l or node.val >= r:
                return 1e9
            return 1 + validBST(node.left, l, node.val) + validBST(node.right, node.val, r)
        res = 0
        def dfs(node):
            nonlocal res
            if not node:
                return
            val = validBST(node, -1e9, 1e9)
            if val < 1e9:
                res = max(res, val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return res

