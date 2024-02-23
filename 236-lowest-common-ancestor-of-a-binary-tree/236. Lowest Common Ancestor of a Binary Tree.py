# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def findPath(node, arr, target):
            
            if node is None:
                return None
            elif node.val == target:
                return arr
            else:
                a = findPath(node.left, arr + [node], target)
                if a is None:
                    return findPath(node.right, arr + [node], target)
                else:
                    return a

        lst1 = findPath(root, [], p.val)
        lst2 = findPath(root, [], q.val)
        a = [c.val for c in lst1]
        b = [d.val for d in lst2]
        lst1 = lst1[::-1]
        lst2 = lst2[::-1]
        print("lst1", a)
        print("lst2", b)
        if len(lst1) > len(lst2):
            for i in range(len(lst1)):
                if lst1[i] == p:
                    if i+1 < len(lst1) and q not in lst1[i+1:]:
                        return lst1[i]
                    elif i+1 == len(lst1):
                        return lst1[i]
                if lst1[i] == q:
                    if i+1 < len(lst1) and p not in lst1[i+1:]:
                        return lst1[i]
                    elif i+1 == len(lst1):
                        return lst1[i]
                if lst1[i] in lst2:
                    return lst1[i]
        else:
            for i in range(len(lst2)):
                if lst2[i] == p:
                    if i+1 < len(lst2) and q not in lst2[i+1:]:
                        return lst2[i]
                    elif i+1 == len(lst2):
                        return lst2[i]
                if lst2[i] == q:
                    if i+1 < len(lst2) and p not in lst2[i+1:]:
                        return lst2[i]
                    elif i+1 == len(lst2):
                        return lst2[i]
                if lst2[i] in lst1:
                    return lst2[i]
        
