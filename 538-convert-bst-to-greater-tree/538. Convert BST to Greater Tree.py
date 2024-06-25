# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.runningSum = 0
        def inorder(node):
            # Inorder Traversal
            if node is not None:
                inorder(node.right)
                self.runningSum += node.val
                node.val = self.runningSum
                # print(node.val)
                inorder(node.left)
        inorder(root)
        return root