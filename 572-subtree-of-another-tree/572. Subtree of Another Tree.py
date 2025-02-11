# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def equal(node1, node2):
            if node1 and node2:
                return node1.val == node2.val and equal(node1.left, node2.left) and equal(node1.right, node2.right)
            return not(node1 or node2)
        if equal(root, subRoot):
            return True
        if root is None:
            return False
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)