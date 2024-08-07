# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # DP: At each node, you want to return the maximum amount of money you can get with the subtree for both (Taking that node vs Not taking that node)
        @cache
        def dfs(node, take): # If take is true, then you're taking the current node # O(n)
            if not node:
                return 0
            
            if take:
                return node.val + dfs(node.left, not take) + dfs(node.right, not take)
            else:
                return max(dfs(node.left, not take) + dfs(node.right, not take), dfs(node.left, take) + dfs(node.right, not take), dfs(node.left, not take) + dfs(node.right, take), dfs(node.left, take) + dfs(node.right, take))
            
        
        return max(dfs(root, False), dfs(root, True))

        