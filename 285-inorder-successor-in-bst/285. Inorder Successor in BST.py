# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        lst = []
        def inorder(node):    
            if node:
                inorder(node.left)
                lst.append(node.val)
                inorder(node.right)
        inorder(root)
        if lst.index(p.val) == len(lst) - 1:
            return None
        goal = lst[lst.index(p.val)+1]
        self.ans = None
        def dfs(node):
            if not node:
                return
            if node.val == goal:
                self.ans = node
                return
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return self.ans