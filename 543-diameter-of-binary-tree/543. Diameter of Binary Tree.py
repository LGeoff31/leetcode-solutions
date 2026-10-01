# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        longest_diameter = 0

        def get_longest_length_down(node): # O(T)
            if not node:
                return 0
            
            return 1 + max(get_longest_length_down(node.left), get_longest_length_down(node.right))

        def explore_nodes(node):
            nonlocal longest_diameter

            if not node:
                return

            longest_diameter = max(longest_diameter, 1 + get_longest_length_down(node.left) + get_longest_length_down(node.right))
            
            explore_nodes(node.left)
            explore_nodes(node.right)
        
        explore_nodes(root)
        return longest_diameter - 1