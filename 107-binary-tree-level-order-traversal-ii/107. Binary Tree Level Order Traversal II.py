# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res = [[root.val]]
        q = deque([[root]])
        while q:
            arr = q.popleft()
            lst = []
            for node in arr:
                if node:
                    lst.append(node.left)
                    lst.append(node.right)
            valid = False
            for node in lst:
                if node:
                    valid = True
            if valid:
                q.append(lst)
            else:
                break
            a = []
            for node in lst:
                if node:
                    a.append(node.val)
            res.append(a)
            # break


        return res[::-1]

        