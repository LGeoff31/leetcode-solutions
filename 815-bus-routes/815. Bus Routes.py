class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # Idea: Create a undirected graph from routes and perform Dijstra's algorithm
        # It should store (min_num_buses, node)
        if source == target:return 0
        end_indicies = set()
        visited = set()
        queue = deque([])
        # Find all indicies with soure + Find all indicies with target
        lst = []
        for i in range(len(routes)):
            if source in routes[i]:
                lst.append((i, 1))
                visited.add(i)
            if target in routes[i]:
                end_indicies.add(i)
        for idx, val in lst:
            if idx in end_indicies:
                return 1
        queue.append(lst)


        
        # Create a graph showing which buses connect with other buses
        adj = defaultdict(list)
        dup_routes = []
        for arr in routes:
            dup_routes.append(set(arr))
        for i in range(len(routes)):
            for j in range(i+1, len(routes)):
                for elem in routes[i]:
                    if elem in dup_routes[j]:
                        # There is a connection between bus i <-> j
                        adj[i].append(j)
                        adj[j].append(i)
        
        # Perform a bfs from all elements in the indicies array
        while queue:
            indicies_arr = queue.popleft() #[(0, 1), (2, 1)]
            for idx, buses_used in indicies_arr:
                lst = []
                for nei in adj[idx]:
                    if nei not in visited:
                        visited.add(nei)
                        lst.append((nei, buses_used+1))
                        if nei in end_indicies:
                            return buses_used + 1
                queue.append(lst)
        return -1