class Solution:
    def minCost(self, n: int, _edges: List[List[int]]) -> int:
        dist = defaultdict(int)
        edges = defaultdict(list)
        reversed_edges = defaultdict(list)


        for i in range(n):
            dist[i] = float('inf')

        for u,v,w in _edges:
            edges[u].append((v, w))
            reversed_edges[v].append((u, 2*w))
        

        queue = deque([(0, 0)])

        while queue:
            node, weight = queue.popleft()
            # try going in right direction
            for nei, nei_w in edges[node]:
                if nei_w + weight < dist[nei]:
                    print('reached', nei)
                    dist[nei] = nei_w + weight
                    queue.append((nei, nei_w + weight))
            # try going in reverse direction
            for nei, nei_w in reversed_edges[node]:
                if nei_w + weight < dist[nei]:
                    dist[nei] = nei_w + weight
                    queue.append((nei, nei_w + weight))
        print('dist', dist)
        return dist[n-1] if dist[n-1] != float('inf') else -1