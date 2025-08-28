class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        res = 0
        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        deg = [len(adj[i]) for i in range(n)]
        dic = {i : values[i] for i in range(n)} # node : curr_sum
        queue = deque([i for i in range(n) if deg[i] == 1])
        
        while queue:
            node = queue.popleft()
            if deg[node] == 0:
                # Already procecessed
                continue
            parent = -1
            for nei in adj[node]:
                if deg[nei] >= 1:
                    parent = nei
                    break
            if dic[node] % k == 0:
                res += 1
            else:
                if parent != -1:
                    dic[parent] += dic[node]
            deg[node] -= 1
            if parent != -1: 
                deg[parent] -= 1
                if deg[parent] == 1:
                    queue.append(parent)
        return res+1




