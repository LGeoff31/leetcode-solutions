class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        def dfs(currString, seen):
            if currString[-n:] in seen:
                return
            seen.add(currString[-n:])
            if len(seen) == k ** n:
                return currString
            for i in range(k):
                nxt = dfs(currString + str(i), seen)
                if nxt:
                    return nxt
            seen.remove(currString[-n:])
        return dfs("0" * n, set())
