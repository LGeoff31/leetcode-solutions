class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms) #4

        self.visited = set()
        self.visited.add(0)

        def dfs(idx):
            for key in rooms[idx]:
                if key not in self.visited:
                    self.visited.add(key)
                    dfs(key)
        for key in rooms[0]:
            self.visited.add(key)
            dfs(key)

        return len(self.visited) == n

        