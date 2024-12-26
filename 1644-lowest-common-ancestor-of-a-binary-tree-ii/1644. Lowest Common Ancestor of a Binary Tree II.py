# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        nodes = set()
        def dfs(node):
            if node:
                nodes.add(node.val)
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        print('reached', nodes, p.val, q.val)
        if p.val not in nodes or q.val not in nodes: return None
        print('reached')
        def contains(node):
            if not node:
                return None
            if node == p or node == q:
                return node
            left = contains(node.left)
            right = contains(node.right)
            if left and right:
                return node
            
            return left if left else right

        return contains(root)