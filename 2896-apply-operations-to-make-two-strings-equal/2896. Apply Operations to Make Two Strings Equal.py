class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        lst = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                lst.append(i)
        if len(lst)%2==1: return -1


        @cache
        def dfs(i, j):
            if i >= j: 
                return 0
            return min(x + dfs(i+1, j-1), lst[j] - lst[j-1] + dfs(i, j-2), lst[i+1]-lst[i] + dfs(i+2, j))


        return dfs(0, len(lst) - 1)


        