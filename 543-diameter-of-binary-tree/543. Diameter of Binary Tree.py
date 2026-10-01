# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        longest_diameter = 0

        def explore_nodes(node):
            nonlocal longest_diameter

            if not node:
                return 0
            
            left, right = explore_nodes(node.left), explore_nodes(node.right)
            longest_diameter = max(longest_diameter, 1 + left + right)

            return 1 + max(left, right)
        
        explore_nodes(root)
        return longest_diameter - 1