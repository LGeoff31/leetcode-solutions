class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        lst = list(range(1, m+1))
        res = []
        for q in queries:
            idx = lst.index(q)
            res.append(idx)
            lst.remove(q)
            lst = [q] + lst
        return res