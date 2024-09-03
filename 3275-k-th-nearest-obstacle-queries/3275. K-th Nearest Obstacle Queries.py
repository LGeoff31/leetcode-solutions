from sortedcontainers import SortedList
class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        a = SortedList()
        res = []
        for x,y in queries:
            a.add(abs(x) + abs(y))
            if k <= len(a):
                res.append(a[k-1])
            else:
                res.append(-1)
        return res