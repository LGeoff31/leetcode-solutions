# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        lst = []
        def inorder(node):
            if node:
                inorder(node.left)
                lst.append(node.val)
                inorder(node.right)
        inorder(root)
        idx = bisect_left(lst, target)
        l, r = idx-1, idx
        if len(lst) == 1:
            return lst
        if l == -1:
            return lst[0: k]
        if r == len(lst):
            return lst[len(lst) - k : ]
        res = []
        print(lst, l, r)
        valid = False
        while len(res) != k and not valid:
            if abs(target - lst[r]) <= abs(target - lst[l]):
                res.append(lst[r])
                if len(res) == k: break
                r += 1
                if r == len(lst):
                    while len(res) != k:
                        res.append(lst[l])
                        l -= 1
                    valid = True
            else:
                res.append(lst[l])
                l -= 1
                if len(res) == k: break
                if l == -1:
                    while len(res) != k:
                        res.append(lst[r])
                        r += 1
                    valid = True
        print(lst)
        return res