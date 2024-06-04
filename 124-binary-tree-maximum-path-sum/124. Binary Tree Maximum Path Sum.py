# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int: 
        ans = [root.val]


        def dfs(node):
            if node is None: return 0


            l_max = max(0, dfs(node.left))
            r_max = max(0, dfs(node.right))

            ans[0] = max(ans[0], node.val + l_max + r_max)

            return node.val + max(l_max, r_max)
        dfs(root)
        return ans[0]