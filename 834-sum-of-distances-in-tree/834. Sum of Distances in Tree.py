class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        output = [0] * n
        count = [1] * n
        self.root = 0

        def dfs(curr, parent, depth):
            o = 1
            for child in graph[curr]:
                if child != parent:
                    o +=dfs(child, curr, depth+1)
                    self.root += depth+1
            count[curr] = o
            return o
        
        def dfs2(cur, parent, ans_p):
            output[cur] = ans_p
            for child in graph[cur]:
                if child != parent:
                    dfs2(child, cur, ans_p + (n-count[child] - count[child]))
        dfs(0, -1, 0)
        dfs2(0, -1, self.root)
        return output