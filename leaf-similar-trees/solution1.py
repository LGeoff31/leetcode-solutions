# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        lst1 = []
        lst2 = []

        def dfs(head, typer):
            if typer == "a":
                if head is None:
                    return
                if head.left is None and head.right is None:
                    lst1.append(head.val)
                dfs(head.left, "a")
                dfs(head.right, "a")
            else:
                if head is None:
                    return
                if head.left is None and head.right is None:
                    lst2.append(head.val)
                dfs(head.left, "b")
                dfs(head.right, "b")
        dfs(root1, "a")
        dfs(root2, "b")
        return lst1 == lst2
