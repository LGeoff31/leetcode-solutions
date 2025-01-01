class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        # n -> s
        # 1 -> 1
        # 2 -> 2
        # 3 -> 3
        values = {x for seq in sequences for x in seq}
        graph = {x : [] for x in values}
        indegree = {x: 0 for x in values}

        for seq in sequences:
            for i in range(len(seq) - 1):
                graph[seq[i]].append(seq[i+1])
                indegree[seq[i+1]] += 1
        queue = deque([])
        for node in values:
            if indegree[node] == 0:
                queue.append(node)
        # Start the BFS
        res = []

        while queue:
            if len(queue) > 1:
                return False
            for i in range(len(queue)):
                node = queue.popleft()
                res.append(node)
                for nei in graph[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        queue.append(nei)

        return res == nums


        print(values)
        return False