# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        The largest path sum 
        """
        self.max_element = -1e9
        def dfs(node):
            if not node:
                return 0

            return max(max(max(dfs(node.left), dfs(node.right)), 0) + node.val, 0)
        self.res = 0
        def traverse_tree(node):
            if not node:
                return
            self.max_element = max(self.max_element, node.val)
            self.res = max(self.res, node.val + dfs(node.left) + dfs(node.right))
            traverse_tree(node.left)
            traverse_tree(node.right)
        traverse_tree(root)
        print(self.max_element)
        if self.res == 0:
            return self.max_element
        return self.res