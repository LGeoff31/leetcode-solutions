class Solution:
    def getDiameter(self, graph, nodes):
        def bfs(start):
            dist = [-1] * nodes
            q = [start]
            dist[start] = 0
            farNode = start
            while q:
                curr = q.pop(0)
                for next in graph[curr]:
                    if dist[next] == -1:
                        dist[next] = dist[curr] + 1
                        q.append(next)
                        if dist[next] > dist[farNode]:
                            farNode = next
            return farNode, dist[farNode]
        
        return bfs(bfs(0)[0])[1]

    def minimumDiameterAfterMerge(self, tree1, tree2):
        n, m = len(tree1) + 1, len(tree2) + 1
        g1, g2 = [[] for _ in range(n)], [[] for _ in range(m)]
        
        for edge in tree1:
            g1[edge[0]].append(edge[1])
            g1[edge[1]].append(edge[0])
        for edge in tree2:
            g2[edge[0]].append(edge[1])
            g2[edge[1]].append(edge[0])
        
        d1 = self.getDiameter(g1, n)
        d2 = self.getDiameter(g2, m)
        return max(d1, d2, (d1 + 1) // 2 + (d2 + 1) // 2 + 1)