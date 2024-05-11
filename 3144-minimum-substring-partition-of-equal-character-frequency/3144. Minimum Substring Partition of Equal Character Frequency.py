class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        n = len(s)

        def check(dic):
            return len(set(dic.values())) == 1
        @cache
        def dfs(i):
            res = n - i
            dic = Counter()
            for j in range(i, n):
                dic[s[j]] += 1
                if check(dic):
                    res = min(res, 1 + dfs(j+1))
            return res

        return dfs(0)