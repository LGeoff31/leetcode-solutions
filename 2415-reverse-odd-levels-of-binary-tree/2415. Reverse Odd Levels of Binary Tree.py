# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        print(root)
        lst = []
        queue = deque([root])
        while queue:
            lst.append([node.val for node in queue])
            for i in range(len(queue)):
                node = queue.popleft()
                if node.right and node.left:
                    queue.append(node.left)
                    queue.append(node.right)
        # print(lst)
        for i in range(len(lst)):
            if i % 2 == 1:
                lst[i] = lst[i][::-1]
        # print(lst)
        # print(lst)
        root = TreeNode(lst[0][0])
        prev = [TreeNode(node) for node in lst[-1]]
        # print(lst)
        new_lst = []
        for arr in lst:
            a = []
            for node in arr:
                a.append(TreeNode(node))
            new_lst.append(a)
        lst = new_lst
        # lst = [[TreeNode(node) for node in arr] for arr in lst]
        # print('lst', lst[-1], len(lst))
        # print(lst[1])
        # print(len(lst))
        prev = [TreeNode(node.val) for node in lst[-1]]
        # print("prev", prev)
        for level in range(len(lst) -2, -1, -1):
            # print('reqched')
            nodes = lst[level]
            # print('nodes', nodes)
            idx = 0
            for i in range(len(nodes)):
                nodes[i].left = prev[idx]
                idx += 1
                nodes[i].right = prev[idx]
                idx += 1
            # print('NODES', nodes)
            prev = nodes
        # print("lst", lst)
        node = lst[0][0]
        # print(node)
        # root = node
        # root.left = lst[1][0]
        # root.right = lst[1][1]
        # print(root)
        print(node)
        return node
        # def dfs(node, level):
        #     if not node:
        #         return
        #     print(node.val, level)

        #     if level % 2 == 1 and node.left and node.right:
        #         temp = node.left.val
        #         node.left.val = node.right.val
        #         node.right.val = temp
        #     if node.left and node.right:
        #         dfs(node.left, level + 1)
        #         dfs(node.right, level + 1)
        #     return node
        # return dfs(root, -1)
