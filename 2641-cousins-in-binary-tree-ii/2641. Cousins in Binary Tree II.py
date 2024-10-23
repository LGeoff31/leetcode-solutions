# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dic = {}

        def dfs(node):
            if node:
                if node.left: dic[node.left] = node
                if node.right: dic[node.right] = node
                dfs(node.left)
                dfs(node.right)
        
        queue = deque([[root]])
        lst = [[root.val]]

        while queue:
            a = []
            b = []
            arr = queue.popleft()

            for i in range(len(arr)):
                node = arr[i]
                if node.left: 
                    a.append(node.left)
                    b.append(node.left.val)
                if node.right:
                    a.append(node.right)    
                    b.append(node.right.val)
            if a:
                queue.append(a)

            lst.append(b)
        lst.pop()
        for i in range(len(lst)):
            lst[i] = sum(lst[i])

        dfs(root)
        dic2 = {}
        def dfs3(node):
            if node:
                dic2[node] = node.val
                dfs3(node.left)
                dfs3(node.right)
        dfs3(root)
        def dfs2(node, level):
            if node:
                if level <= 1:
                    node.val = 0
                    dfs2(node.right, level + 1)
                    dfs2(node.left, level + 1)
                else:
                    if node != dic[node].right and dic[node].right:
                        node.val = lst[level - 1] - node.val - dic2[dic[node].right]

                    elif node != dic[node].left and dic[node].left:
                        node.val = lst[level - 1] - node.val - dic2[dic[node].left]
                    else:
                        node.val = lst[level - 1] - node.val
                    if node.left: dfs2(node.left, level + 1)
                    if node.right: dfs2(node.right, level + 1)
        
        
        dfs2(root, 1)

        return root