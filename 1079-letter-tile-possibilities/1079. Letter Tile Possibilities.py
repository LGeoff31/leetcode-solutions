class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def dfs(size, dic, count):
            if count == size:
                return 1
            res = 0
            keys = dic.copy().keys()
            for key in keys:
                dic[key] -= 1
                if dic[key] == 0:
                    del dic[key]
                res += dfs(size, dic, count + 1)
                dic[key] += 1
            return res
            
        res = 0
        for i in range(1, len(tiles) + 1):
            res += dfs(i, Counter(tiles), 0)
        return res
