class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        dic = defaultdict(list)
        for u,v in edges:
            dic[u].append(v)
            dic[v].append(u)
        self.res = 0
        def dfs(node, parent):
            subtree_sum = values[node]
            for child in dic[node]:
                if child != parent:
                    subtree_sum += dfs(child, node)
            if subtree_sum % k == 0:
                self.res += 1
                return 0
            return subtree_sum

        dfs(0, -1)
        return self.res