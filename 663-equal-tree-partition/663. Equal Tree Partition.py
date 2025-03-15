# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        # Find the total sum of the tree
        # The target for each subtree will be half the sum
        # Find a subtree that has that sum, if its found return True
        # If non-exist, return False
        cache = {}
        def dfs(node):
            if not node:
                return 0
            cache[node] = node.val + dfs(node.left) + dfs(node.right)
            return cache[node]
        dfs(root)
        totalSum = cache[root]
        targetSum = totalSum / 2
        for node in cache:
            if cache[node] == targetSum and node != root:
                return True
        return False