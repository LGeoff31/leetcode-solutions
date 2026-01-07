# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        res = 0
        MOD = 10 ** 9 + 7
        def prefix_tree(node):
            # LEAF NODE
            if node.right is None and node.left is None:
                return node.val
            
            if node.right:
                node.val += prefix_tree(node.right)
            if node.left:
                node.val += prefix_tree(node.left)
            
            return node.val
        
        def get_max_product(node):
            nonlocal res
            # BREAK LEFT EDGE
            if node.left:
                left_subtree_sum = node.left.val
                right_subtree_sum = total_sum - left_subtree_sum
                print(left_subtree_sum, right_subtree_sum)
                res = max(res, left_subtree_sum * right_subtree_sum)
                get_max_product(node.left)
            # BREAK RIGHT EDGE
            if node.right:
                right_subtree_sum = node.right.val
                left_subtree_sum = total_sum - right_subtree_sum
                res = max(res, left_subtree_sum * right_subtree_sum)
                get_max_product(node.right)

        prefix_tree(root)
        total_sum = root.val
        get_max_product(root)
        return res % MOD

        