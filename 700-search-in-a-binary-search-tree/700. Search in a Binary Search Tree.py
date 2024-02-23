# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def dfs(node, target):
            if node is None:
                return None
            elif node.val == target:
                return node
            elif node.val > target:
                return dfs(node.left, target)
            else:
                return dfs(node.right, target)
        
        return dfs(root, val)
        