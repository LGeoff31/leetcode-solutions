# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10 ** 9 + 7
        lst = []

        def dfs(node):
            nonlocal lst
            if node.left is None and node.right is None:
                lst.append(node.val)
                return node.val
            
            if node.left:
                node.val += dfs(node.left)
            if node.right:
                node.val += dfs(node.right)
            lst.append(node.val)
            return node.val

        dfs(root)
        print(lst)
        res = 0
        total_sum = max(lst)
        for subtree_sum in lst:
            counter = total_sum - subtree_sum
            res = max(res, subtree_sum * counter)

        return res % MOD
