# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        lst = []
        if not root: return 0

        def dfs(node, currString):
            if not node.left and not node.right:
                lst.append(int(currString))
            
            if node.left:
                dfs(node.left, currString + str(node.left.val))
            if node.right:
                dfs(node.right, currString + str(node.right.val))

        dfs(root, str(root.val))
        return sum(lst)
        