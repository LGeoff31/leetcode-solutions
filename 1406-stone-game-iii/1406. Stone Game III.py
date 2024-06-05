class Solution:
    def stoneGameIII(self, values: List[int]) -> str:
        @cache
        def dfs(i):
            if i == len(values):
                return 0
            
            res = -1e9
            for j in range(i, min(i+3, len(values))):
                res = max(res, sum(values[i:j+1]) - dfs(j+1))
            return res


        if dfs(0) == 0: return "Tie"
        elif dfs(0) > 0: return 'Alice'
        else: return 'Bob'