# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right: return True

        def dfs(node1, node2):
            if node1 is None and node2 is None: return True
            if node1 is None or node2 is None: return False
            if node1.val != node2.val: return False
            return dfs(node1.left, node2.right) and dfs(node1.right, node2.left)
        return dfs(root.left, root.right)


        