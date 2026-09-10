# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        res = 0
        node_to_subtree_sum = {}

        def dfs(node):
            nonlocal res 
            if not node:
                return 0, 0
            
            total_subtree_sum, total_nodes = node.val, 1
            a1, a2 = dfs(node.left)
            b1, b2 = dfs(node.right)
            total_subtree_sum += a1 + b1
            total_nodes += a2 + b2

            node_to_subtree_sum[node] = floor(total_subtree_sum / total_nodes)
            if node_to_subtree_sum[node] == node.val:
                res += 1

            return total_subtree_sum, total_nodes
        
        dfs(root)
        return res

        print(node_to_subtree_sum)
        return 0