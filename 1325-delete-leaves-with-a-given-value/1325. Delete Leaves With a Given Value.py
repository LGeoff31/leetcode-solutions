# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(node):
            if not node: return
            if node.left:
                if node.left.left is None and node.left.right is None and node.left.val == target:
                    node.left = None
            if node.right:
                if node.right.left is None and node.right.right is None and node.right.val == target:
                    node.right = None
            
            dfs(node.left)
            dfs(node.right)
        for i in range(3000):
            dfs(root)
        if root.left is None and root.right is None and root.val == target:
            return None
        return root
            
        