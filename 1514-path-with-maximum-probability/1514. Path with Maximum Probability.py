class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # Idea: Start from start node, and perform Dikjstra's algorithm on each node until you get to end
        # If all nodes are visited and end is not within it, return 0
        # Each node should have (num, probability value)
        # O(V + ElogV)
        adj = defaultdict(list) 
        for i in range(len(edges)): #O(E)
            u,v = edges[i]
            adj[u].append((v, succProb[i]))
            adj[v].append((u, succProb[i]))
        
        minHeap = [(-1, start_node)] #Weight : node
        visited = {}

        while minHeap: #O(V)
            w1, n1 = heapq.heappop(minHeap) #O(logV)
            w1 *= -1
            if n1 in visited:
                continue
            visited[n1] = w1
            for n2, w2 in adj[n1]: #O(E)
                if n2 not in visited:
                    heapq.heappush(minHeap, (-1*w1*w2, n2))
        if end_node in visited:
            return visited[end_node]   
        return 0