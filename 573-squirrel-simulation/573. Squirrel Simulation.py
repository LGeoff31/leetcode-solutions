class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        n =  set()
        for r,c in nuts:
            n.add((r,c))
        dic = {}
        for r in range(height):
            for c in range(width):
                if (r,c) in n:
                    dic[(r,c)] = abs(r-tree[0]) + abs(c-tree[1])
        print(dic)
        res = 1e9
        totalSum = 0
        for key in dic:
            r,c = key
            totalSum += abs(r-tree[0]) + abs(c-tree[1])
        for key in dic:
            r,c = key
            res = min(res, abs(r-squirrel[0]) + abs(c-squirrel[1])  + (2*totalSum) - dic[(r,c)])
        return res

