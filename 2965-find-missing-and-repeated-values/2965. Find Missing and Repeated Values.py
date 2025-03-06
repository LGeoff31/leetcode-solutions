class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        res = [num for arr in grid for num in arr]
        maxNUm = len(res)
        m = [-1, -1]
        for i in range(1, maxNUm + 1):
            if i not in res:
                m[-1] = i
            if res.count(i) == 2:
                m[0] = i
        return m