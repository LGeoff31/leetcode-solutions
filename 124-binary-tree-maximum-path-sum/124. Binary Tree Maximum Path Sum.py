# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int: 
        #note if all negative, return the largest node value
        cache = {}
        def dfs(node):
            if node in cache:
                return cache[node]
            if node is None:
                return 0
            if node.left is None and node.right is None: #leave node
                return node.val
            max_path_at_node = node.val +  max(dfs(node.left), dfs(node.right), 0) #choose max path eihter left or right
            cache[node] = max(max_path_at_node, 0) #if leaf node is negative, you dont want to really take it
            return cache[node]
        self.res = -1e9
        
        def traversal(node):
            if node is None:
                return
            self.res = max(self.res, node.val + max(dfs(node.left),0) + max(dfs(node.right), 0))
            # print("cache", cache)
            traversal(node.left)
            traversal(node.right)
        traversal(root)
        return self.res

        