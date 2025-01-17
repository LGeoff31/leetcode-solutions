class Solution:
    def countArrangement(self, n: int) -> int:
        def dfs(idx, visited):
            if idx == n:
                # print(visited)
                return 1
            res = 0
            for i in range(1, n+1):
                if i not in visited and (i%(idx+1) == 0 or (idx+1) % i == 0):
                    visited.add(i)
                    res += dfs(idx+1, visited)
                    visited.remove(i)
                # print("res", res)
            return res
        return dfs(0, set())
            