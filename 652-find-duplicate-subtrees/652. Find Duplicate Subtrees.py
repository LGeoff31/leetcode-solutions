# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        dic = defaultdict(int)
        def traverse(node):
            if not node:
                return ""
            representation = "(" + traverse(node.left) + ")" + "(" + traverse(node.right) + ")" + str(node.val)
            dic[representation] += 1
            if dic[representation] == 2:
                res.append(node)
            return representation
        res = []
        traverse(root)
        # for key in dic:
        #     if dic[key] > 1:
        #         res.append(key)
        return res