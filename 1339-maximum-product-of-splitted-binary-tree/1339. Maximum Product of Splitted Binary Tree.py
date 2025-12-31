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
        lst = []
        def prefix_tree(node):
            # LEAF NODE
            if node.right is None and node.left is None:
                lst.append(node.val)
                return node.val
            
            if node.right:
                node.val += prefix_tree(node.right)
            if node.left:
                node.val += prefix_tree(node.left)
            
            lst.append(node.val)
            return node.val
        
        prefix_tree(root)
        total_sum = max(lst)
        for n in lst:
            res = max(res, n * (total_sum - n))
        return res % MOD

        