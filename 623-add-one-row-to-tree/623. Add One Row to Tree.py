# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            newRoot = TreeNode(val)
            newRoot.left = root
            return newRoot
        def dfs(d, node):
            if d == depth - 1:
                tempLeft = node.left
                tempRight = node.right
                newLeft = TreeNode(val)
                newRight = TreeNode(val)
                newLeft.left = tempLeft
                newRight.right = tempRight
                node.left = newLeft
                node.right = newRight
            else:
                if node.left: dfs(d+1, node.left)
                if node.right: dfs(d+1, node.right)

        dfs(1, root)
        return root
        