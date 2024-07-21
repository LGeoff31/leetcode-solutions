class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def dfs(src, adj, path, visited, order):
            if src in path:
                return False
            if src in visited:
                return True
            visited.add(src)
            path.add(src)
            for nei in adj[src]:
                if not dfs(nei, adj, path, visited, order):
                    return False
            order.append(src)
            path.remove(src)
            return True
            
        def t_sort(edges):
            adj = defaultdict(list)
            for u, v in edges:
                adj[u].append(v)
            path, visited = set(), set()
            order = []
            for i in range(1, k+1):
                if not dfs(i, adj, path, visited, order):
                    return []
            return order[::-1]
        rows = t_sort(rowConditions)
        cols = t_sort(colConditions)
        print("rows", rows)
        print("cols", cols)

        row_dic = {val: idx for idx, val in enumerate(rows)}
        col_dic = {val: idx for idx, val in enumerate(cols)}
        if not rows or not cols:
            return []
        res = [[0] * k for _ in range(k)]
        print(row_dic, col_dic)
        for i in range(1, k+1):
            res[row_dic[i]][col_dic[i]] = i
        return res
            
        