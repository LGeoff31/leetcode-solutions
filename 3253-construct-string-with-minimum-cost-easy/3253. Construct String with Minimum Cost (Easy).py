class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        @cache
        def dfs(currWord):
            if currWord == target:
                return 0
            if len(currWord) >= len(target) or not (target.startswith(currWord)):
                return 1e9 
            res = 1e9
            for i, w in enumerate(words):
                res = min(res, costs[i] + dfs(currWord + w))
            return res
        ans = dfs("")
        return ans if ans != 1e9 else -1 