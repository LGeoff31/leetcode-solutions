# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        dic = defaultdict(int)
        def subtree_sum(node):
            if not node:
                return 0
            print('running', node.val)
            a, b = subtree_sum(node.left), subtree_sum(node.right)
            dic[node.val + a+b] += 1
            return node.val + a+b
        subtree_sum(root)
        print(dic)
        maxFreq = max(dic.values())
        res = []
        for key in dic:
            if dic[key] == maxFreq:
                res.append(key)
        return res