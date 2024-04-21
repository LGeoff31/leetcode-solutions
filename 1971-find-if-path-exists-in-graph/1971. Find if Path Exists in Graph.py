class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = set()
        queue = deque([source])
        graph = defaultdict(list)
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node==destination: return True
                for nxt in graph[node]:
                    if nxt not in visited:
                        queue.append(nxt)
                visited.add(node)
        return False
                
            
            
            
        