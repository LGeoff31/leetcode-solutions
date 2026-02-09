# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        lst = []

        def dfs(node):
            if node:
                lst.append(node.val)
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        lst.sort()
        print(lst)
        def build_bst(lst):
            if not lst:
                return None
            if len(lst) == 1:
                return TreeNode(lst[0])
            node = TreeNode(lst[len(lst) // 2])

            node.left = build_bst(lst[:len(lst)//2])
            node.right = build_bst(lst[len(lst)//2 + 1:])
            return node
        return build_bst(lst)