class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        queue = deque([[1,1]])
        dist1 = [-1] * (n+1)
        dist2 = [-1] * (n+1)
        dist1[1] = 0
        dist2[1] = -1
        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        while queue:
            node, freq = queue.popleft()
            timeTaken = dist1[node] if freq == 1 else dist2[node]
            # timeTaken is under red bracket
            if (timeTaken // change) % 2 == 1:
                timeTaken = (timeTaken // change + 1) * change + time
            else:
                timeTaken += time
            for nei in adj[node]:
                if dist1[nei] == -1:
                    dist1[nei] = timeTaken
                    queue.append([nei, 1])
                elif dist2[nei] == -1 and dist1[nei] != timeTaken:
                    if nei == n: return timeTaken
                    dist2[nei] = timeTaken
                    queue.append([nei, 2])

        return 0

        