# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        lst = []
        
        def traverse(node):
            if node:
                traverse(node.left)
                lst.append(node.val)
                traverse(node.right)
        traverse(root)
        #[1,2,3,4]
        def bst(l, r):
            if l > r:
                return
            mid = (l + r) // 2
            node = TreeNode(lst[mid])
            node.left = bst(l, mid-1) #0, 1
            node.right = bst(mid+1, r)
            return node

        return bst(0, len(lst) - 1)
        