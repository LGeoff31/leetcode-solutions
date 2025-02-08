# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        id_to_node = {}
        def map_id_to_node(node):
            if not node: return
            id_to_node[id(node)] = node
            map_id_to_node(node.left)
            map_id_to_node(node.right)
        map_id_to_node(root)
        def val(node_id):
            if node_id not in id_to_node: return 0
            node = id_to_node[node_id]
            total = node.val
            if node.left:
                total += val(id(node.left))
            if node.right:
                total += val(id(node.right))
            return total
        self.res = 0
        def dfs(node):
            if node:
                self.res += abs(val(id(node.left)) - val(id(node.right)))
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return self.res