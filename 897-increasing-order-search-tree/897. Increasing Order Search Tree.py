# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        inorder = []

        def inorder_traversal(node):
            if not node:
                return
            
            # left, curr, right
            inorder_traversal(node.left)
            inorder.append(node)
            inorder_traversal(node.right)

        inorder_traversal(root)
        print(inorder)
        inorder[0].left = None
        inorder[0].right = None

        root = inorder[0]
        curr = root
        for node in inorder[1:]:
            node.left = None
            node.right = None
            curr.right = node
            curr = curr.right

        return root
