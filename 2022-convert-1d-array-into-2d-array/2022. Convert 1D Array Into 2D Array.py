class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        rows, cols = m, n
        if len(original) != m*n: return []
        res = []
        for r in range(rows):
            lst = []
            for c in range(cols):
                lst.append(original[cols*r+c])
            res.append(lst)

        return res

        