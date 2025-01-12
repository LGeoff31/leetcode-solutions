# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dic = defaultdict(int)
        def dfs(node):
            if node:
                dic[node.val] += 1
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        res = []
        freq = -1e9
        for key in dic:
            freq = max(freq, dic[key])
        for key in dic:
            if dic[key] == freq:
                res.append(key)
        return res