class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        bob_hashmap = {bob:0}
        def dfs(node, prev, time):
            if node == 0:
                bob_hashmap[node] = time
                return True
            for nei in adj[node]:
                if nei == prev:
                    continue
                if dfs(nei, node, time + 1):
                    bob_hashmap[node] = time
                    return True
            return False

        dfs(bob, -1, 0)
        queue = deque([[0, amount[0]]])
        visited = {0}
        time = 1
        res = -1e9
        print(bob_hashmap)
        print('fuck')
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if len(adj[node[0]]) == 1 and node[0] != 0:
                    res = max(res, node[1])
                for nei in adj[node[0]]:
                    if nei not in visited:
                        visited.add(nei)
                        if nei not in bob_hashmap or time < bob_hashmap[nei]:
                            queue.append([nei, node[1] + amount[nei]])
                        elif time == bob_hashmap[nei]:
                            queue.append([nei, node[1] + amount[nei]//2])
                        else:
                            queue.append([nei, node[1]])
            time += 1
            print(queue)
        return res