# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        parent = {}
        def dfs(node, prev):
            if node:
                if prev:
                    parent[node] = prev
                dfs(node.left, node)
                dfs(node.right, node)
        dfs(root, None)
        def max_depth(node):
            if node:
                return 1 + max(max_depth(node.left), max_depth(node.right))
            return 0

        depth = max_depth(root)

        leaf_nodes = []
        def dfs2(node, level):
            if node:
                if level == depth:
                    leaf_nodes.append(node)
                
                dfs2(node.left, level + 1)
                dfs2(node.right, level + 1)
        dfs2(root, 1)
        if len(leaf_nodes) == 1: return leaf_nodes[0]
        queue = deque(leaf_nodes)
        visited = set()
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node == root: return node
                up_node = parent[node]
                if up_node not in visited:
                    visited.add(up_node)
                    queue.append(up_node)
            if len(queue) == 1:
                return queue[0]
        return None
        # print(parent)
        # print()
        # print(leaf_nodes)
        # return 

        