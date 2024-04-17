# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        lst = []
        print(chr(97))
        def dfs(node, string):
            print(string)
            if node.left == None and node.right == None: #leaf
                lst.append(string + chr(97 + node.val))

            if node.right: dfs(node.right, string + chr(97+node.val))
            if node.left: dfs(node.left, string + chr(97+node.val))
        dfs(root, "")

        for i in range(len(lst)):
            lst[i] = lst[i][::-1]
        return sorted(lst)[0]
