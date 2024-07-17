# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        res = []
        lst = set(to_delete)
        def dfs(node, is_root):
            if not node:
                return None
            is_deleted = node.val in lst
            if is_root and not is_deleted:                
                res.append(node)
            node.left = dfs(node.left, is_deleted)
            node.right = dfs(node.right, is_deleted)
            return None if is_deleted else node


        dfs(root, True)
        return res
        