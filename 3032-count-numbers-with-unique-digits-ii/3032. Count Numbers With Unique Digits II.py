class Solution:
    def numberCount(self, a: int, b: int) -> int:
        res = 0
        def unique(i):
            a = str(i)
            visited = set()
            for c in a:
                if c in visited: return False
                visited.add(c)
            return True
        for i in range(a, b+1):
            res += unique(i)
        return res