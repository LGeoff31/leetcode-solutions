class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """

        dp[node] = max path sum where node is the root of the path
        
        """
        @cache
        def dfs(node):
            if not node:
                return 0
            
            return max(node.val + max(dfs(node.left), dfs(node.right)), 0)
        self.res = 0
        negative_found = True
        largest_val = -float('inf')
        @cache
        def traverse(node):
            nonlocal negative_found, largest_val
            if not node:
                return 0
            if node.val >= 0:
                negative_found = False
            largest_val = max(largest_val, node.val)
            self.res = max(self.res, node.val + dfs(node.left) + dfs(node.right))
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        return self.res if not negative_found else largest_val