class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1: return [[1]]
        if numRows == 2: return [[1], [1,1]]

        res = [[1], [1,1]]
        for i in range(2, numRows):
            prevArr = res[-1]
            curr = []
            curr.append(prevArr[0])
            for j in range(1, len(prevArr)):
                curr.append(prevArr[j] + prevArr[j-1])
            curr.append(1)
            res.append(curr)
        return res