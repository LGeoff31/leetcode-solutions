# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        lst1, lst2 = [], []

        def dfs(node, arr):
            if node is None: return
            if node.left is None and node.right is None: arr.append(node.val)
            dfs(node.left, arr)
            dfs(node.right, arr)
        dfs(root1, lst1)
        dfs(root2, lst2)
        print(lst1)
        print(lst2)
        return lst1 == lst2
            
            

        