# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: TreeNode | None, start: int) -> int:
        graph = defaultdict(list)

        def generate_graph(node):
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                generate_graph(node.left)

            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                generate_graph(node.right)


        generate_graph(root)

        seen = {start}
        queue = deque([start])
        levels = 0

        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                for nei in graph[node]:
                    if nei not in seen:
                        seen.add(nei)
                        queue.append(nei)
            
            levels += 1
    
        return levels - 1