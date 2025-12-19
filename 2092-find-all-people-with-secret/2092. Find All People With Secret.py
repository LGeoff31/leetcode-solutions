from collections import defaultdict

class Solution:
    def findAllPeople(self, n, meetings, firstPerson):
        meetings.sort(key=lambda x: x[2])
        secret = set([0, firstPerson])

        i = 0
        while i < len(meetings):
            time = meetings[i][2]
            graph = defaultdict(list)
            people = set()

            # collect all meetings at same time
            while i < len(meetings) and meetings[i][2] == time:
                x, y, _ = meetings[i]
                graph[x].append(y)
                graph[y].append(x)
                people.add(x)
                people.add(y)
                i += 1

            # find components that should get secret
            queue = []
            visited = set()

            for p in people:
                if p in secret:
                    queue.append(p)
                    visited.add(p)

            # BFS only inside this timestamp
            while queue:
                cur = queue.pop()
                for nei in graph[cur]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append(nei)

            # update secret holders
            secret |= visited

        return list(secret)
