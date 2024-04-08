# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.head = TreeNode()
        def preOrder(node):
            res = []
            if not root: return None
            res.append(node.val)
            if node.left: res += preOrder(node.left)
            if node.right: res += preOrder(node.right)
            return res
        if root is None: return 0
        arr = preOrder(root)
        root.left = None
        itr = root
        idx = 1
        while idx < len(arr):
            itr.right = TreeNode(arr[idx])
            idx+=1
            itr = itr.right

        return itr
        