# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(head1, head2):
            if head1 is None and head2 is None: #if both null
                return True
            if not head1 or not head2: #if one of them is null
                return False
            if head1.val != head2.val:
                return False
            
            
            return isSameTree(head1.left, head2.left) and isSameTree(head1.right, head2.right)

        if isSameTree(root, subRoot):
            return True
        if root is None:
            return False
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        
        
        
        