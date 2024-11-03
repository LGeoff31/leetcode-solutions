class Solution:
    def sameEndSubstringCount(self, s: str, queries: List[List[int]]) -> List[int]:
        lst = [[0] * 26 for _ in range(len(s))]
        lst[0][ord(s[0]) - ord("a")] = 1
        for i in range(1, len(s)):
            # Add all previous
            for j in range(26):
                lst[i][j] = lst[i-1][j]
            lst[i][ord(s[i]) - ord("a")] += 1
        res = []
        for l, r in queries:
            ans = 0
            if l == 0:
                # Its just lst[r]
                for j in range(26):
                    ans += lst[r][j] * (lst[r][j] + 1) // 2
            else:
                for j in range(26):
                    lst[r][j] -= lst[l- 1][j]
                for j in range(26):
                    ans += lst[r][j] * (lst[r][j] + 1) // 2
                # Restore
                for j in range(26):
                    lst[r][j] += lst[l- 1][j]
            res.append(ans)
        return res
