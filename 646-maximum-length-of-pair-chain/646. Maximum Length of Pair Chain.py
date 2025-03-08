class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        # DP?
        # dp[i] = max chain starting at ith pair
        starts = [start for start, _ in pairs]
        @cache
        def dfs(i):
            if i == len(pairs):
                return 0
            s, e = pairs[i]
            idx = bisect_right(starts, e)
            return max(1 + dfs(idx), dfs(i+1))
        return dfs(0)