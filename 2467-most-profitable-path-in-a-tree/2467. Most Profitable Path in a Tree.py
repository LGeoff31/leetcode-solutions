class Solution:
    def mostProfitablePath(self, edges: list[list[int]], bob: int, amount: list[int]) -> int:
        # bfs?
        # dp on every node.

        # every node with no neighbors is leaf, except 0. Update max score from that node.
        #initially, alice opens door 0
        # bob opens door bob. Sets amount[bob] = 0.
        # then bfs. Keep in mind bob's next node.
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # first, bfs to find Bob's path?
        bobPath = [bob]
        def findBobPath(prev, root):
            if root == 0:
                return True
            for neighbor in graph[root]:
                if neighbor == prev:
                    continue
                bobPath.append(neighbor)
                if findBobPath(root, neighbor):
                    return True
                bobPath.pop()
            return False
        findBobPath(None, bob)
        bobIndex = 0
        print(bobPath)

        q = deque([(0, 0)])
        visited = set([0])
        maxProfit = float("-inf")
        while q:
            for _ in range(len(q)):
                node, money = q.popleft()
                visited.add(node)
                if bobIndex < len(bobPath) and bobPath[bobIndex] == node:
                    money += int(amount[node] / 2)
                else:
                    money += amount[node]
                if len(graph[node]) == 1 and node != 0:
                    maxProfit = max(maxProfit, money)
                for neighbor in graph[node]:
                    if neighbor in visited:
                        continue
                    q.append((neighbor, money))
            if bobIndex < len(bobPath):
                amount[bobPath[bobIndex]] = 0
            bobIndex += 1
        return maxProfit

