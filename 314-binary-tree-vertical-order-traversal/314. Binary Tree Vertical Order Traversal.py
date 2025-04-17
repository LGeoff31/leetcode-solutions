# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        dic = defaultdict(list)
        queue = deque([[root, 0]])

        while queue:
            for i in range(len(queue)):
                node, col = queue.popleft()
                dic[col].append(node.val)

                if node.left:
                    queue.append([node.left, col - 1])
                if node.right:
                    queue.append([node.right, col + 1])
        res = []
        for i in range(min(dic.keys()), max(dic.keys()) + 1):
            res.append(dic[i])
        return res