from collections import defaultdict, deque

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        if n == 1:
            return 1  # sum is guaranteed divisible by k

        # build graph
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # current degree and running sums (you had this already)
        deg = [len(adj[i]) for i in range(n)]
        dic = {i: values[i] % k for i in range(n)}  # keep mod k to avoid growth

        # init queue with leaves
        queue = deque([i for i in range(n) if deg[i] == 1])

        res = 0
        while queue:
            u = queue.popleft()
            if deg[u] == 0:
                # already processed after neighbor update
                continue

            # find the ONLY remaining neighbor (deg > 0)
            parent = -1
            for v in adj[u]:
                if deg[v] > 0:
                    parent = v
                    break

            if dic[u] % k == 0:
                # cut here -> this becomes a component
                res += 1
                # remove edge u-parent
                deg[u] -= 1
                if parent != -1:
                    deg[parent] -= 1
                    if deg[parent] == 1:
                        queue.append(parent)
            else:
                # pass remainder upward to parent
                if parent != -1:
                    dic[parent] = (dic[parent] + dic[u]) % k
                    deg[parent] -= 1
                    if deg[parent] == 1:
                        queue.append(parent)
                # remove u
                deg[u] -= 1

        # After peeling, one node (or none) may remain with deg==0.
        # Because total sum is divisible by k, that last component is valid.
        return res+1
