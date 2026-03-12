# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = defaultdict(list) # {col_1: []}
        def dfs(node, col, row):
            if not node:
                return
            
            dic[col].append((row, node.val))
            dfs(node.left, col - 1, row+1)
            dfs(node.right, col + 1, row+1)
        dfs(root, 0, 0)
        res = []
        min_val = min(dic.keys())
        max_val = max(dic.keys())
      
        for i in range(min_val, max_val+1):
            a = dic[i]
            a.sort()
            lst = []
            b = []
            print(a)
            if len(a) == 1:
                res.append([a[0][1]])
            else:
                for j in range(len(a) - 1):
                    if a[j][0] != a[j+1][0]:
                        b.sort()
                        lst.extend(b)
                        b = []
                        lst.append(a[j][1])
                    else:
                        b.append(a[j][1])
        
                if a[-1][0] == a[-2][0]:
                    b.append(a[-1][1])
                if b: 
                    b.sort()
                    lst.extend(b)

                if a[-1][0] != a[-2][0]:
                    lst.append(a[-1][1])
                res.append(lst)
        return res
