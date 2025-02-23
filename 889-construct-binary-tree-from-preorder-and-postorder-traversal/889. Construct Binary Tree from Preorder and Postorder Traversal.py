# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Pre-order: Current, Left, Right
        # Post-order: Left, Right, Current
        lookup1 = {}
        lookup2 = {}
        for i in range(len(postorder)):
            lookup1[preorder[i]] = i
            lookup2[postorder[i]] = i
        
        def dfs(arr, offset):
            if not arr:
                return None
            if len(arr) == 1:
                return TreeNode(arr[0])
            root = TreeNode(arr[0])
            size = lookup2[arr[1]] + 1 - offset
            root.left = dfs(arr[1 : 1 + size], offset) 
            offset += size
            root.right = dfs(arr[1+size : ], offset) 
            return root
    
        return dfs(preorder, 0)