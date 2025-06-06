# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        preorder -> current, left, right
        inorder -> left, current, right

        Observations:
        - We know the roow will be the same as the first element in the inorder
        - We can identify where the parent node is within the inorder array, everything to the left is on the left subtree, everything to right is right subtree
        - Generate the tree recursively
        """
        def dfs(preorder, inorder):
            if len(preorder) == 1:
                return TreeNode(preorder[0])
            if not preorder:
                return None
            parent = TreeNode(preorder[0])
            split_idx = inorder.index(preorder[0]) # 1
            parent.left = dfs(preorder[1 : split_idx + 1], inorder[:split_idx])
            parent.right = dfs(preorder[split_idx + 1 : ], inorder[split_idx+1 : ])
            return parent
        return dfs(preorder, inorder)

