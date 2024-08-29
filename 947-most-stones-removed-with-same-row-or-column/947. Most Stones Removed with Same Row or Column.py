class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        groups = 0
        visited = set()
        def dfs(idx):
            visited.add(idx)
            for nei in adj[idx]:
                if nei not in visited:
                    dfs(nei)

        adj = defaultdict(list)
        for i, (x1, y1) in enumerate(stones):
            for j, (x2, y2) in enumerate(stones):
                if i != j and (x1==x2 or y1 == y2):
                    adj[i].append(j)
        for i in range(len(stones)):
            if i not in visited:
                dfs(i)
                groups += 1
        return len(stones) - groups