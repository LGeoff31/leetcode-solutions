class Solution:
    def minDays(self, n: int) -> int:
        cache = {}
        def dfs(oranges):
            if oranges == 0:
                return 0
            if oranges == 1:
                return 1
            if oranges in cache:
                return cache[oranges]
            print(oranges, oranges%3)
            cache[oranges] = 1 + min(oranges%2 + dfs(oranges//2), oranges%3 + dfs(oranges//3))
            return cache[oranges]
        a =  dfs(n)
        print(cache)
        return a

        