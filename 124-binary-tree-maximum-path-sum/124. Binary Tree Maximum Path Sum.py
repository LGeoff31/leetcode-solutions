class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -10**9

        def dfs(node):
            nonlocal res
            if not node:
                return 0

            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            res = max(res, node.val + left + right)

            return node.val + max(left, right)

        dfs(root)
        return res
