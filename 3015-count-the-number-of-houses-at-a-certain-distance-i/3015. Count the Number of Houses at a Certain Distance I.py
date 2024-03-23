class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        # Initialize a list to store the count of pairs for each distance
        res = [0] * n
        
        # Create an adjacency list for the houses and streets
        adjacency_list = defaultdict(list)
        for i in range(1, n):
            adjacency_list[i].append(i + 1)
            adjacency_list[i + 1].append(i)
        
        # Add the additional street connecting house x and house y
        adjacency_list[x].append(y)
        adjacency_list[y].append(x)
        
        # Define a BFS function to find the minimum distance from a house
        def bfs(i):
            q = deque()
            visit = set()
            q.append((i, 0))
            visit.add(i)

            while q:
                i, dist = q.popleft()
                if dist > 0:
                    res[dist - 1] += 1
                for nei in adjacency_list[i]:
                    if nei not in visit:
                        visit.add(nei)
                        q.append((nei, dist + 1))

        # Iterate through each house and perform BFS
        for i in range(1, n + 1):
            bfs(i)
        
        return res
        