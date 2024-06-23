# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        self.res = []
        def height(node):
            if not node:
                return 0
            return max(1 + height(node.left), 1 + height(node.right))
        # h = height(root)
        # print(h)
        def dfs(node, lst):
            if not node:
                return
            if targetSum == sum(lst)+node.val and node.left is None and node.right is None: 
                self.res.append(lst + [node.val])
                return
            
            dfs(node.left, lst + [node.val])
            dfs(node.right, lst + [node.val])
        dfs(root, [])
        return self.res
