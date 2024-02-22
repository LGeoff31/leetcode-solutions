# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0
        res = 1

        def dfs(node, maxVal):
            if node is None: return 0
            if node.val >= maxVal: 
                maxVal = node.val
                return 1 + dfs(node.left, maxVal) + dfs(node.right, maxVal)
            else:
                return dfs(node.left, maxVal) + dfs(node.right, maxVal)
        left = dfs(root.left, root.val)
        right = dfs(root.right, root.val)
        print(left)
        print(right)
        return res + left + right
