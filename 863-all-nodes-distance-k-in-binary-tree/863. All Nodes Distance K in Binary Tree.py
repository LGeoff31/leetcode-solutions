# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        adj = defaultdict(list)

        def dfs(node, prev):
            print(node.val, prev)
            if prev is not None:
                adj[node.val].append(prev)
            if node.left:
                adj[node.val].append(node.left.val)
                dfs(node.left, node.val)
            if node.right:
                adj[node.val].append(node.right.val)
                dfs(node.right, node.val)
        dfs(root, None)
        print(adj)
        queue = deque([target.val])

        visited = set()
        visited.add(target.val)
        for j in range(k):
            for i in range(len(queue)):
                node = queue.popleft()
                for nei in adj[node]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append(nei)
            print(queue)

        return list(queue)
