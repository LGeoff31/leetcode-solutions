class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        res = []
        colorCount = {}
        ballCount = {}

        for ball, newColor in queries:
            if ball in ballCount:
                oldColor = ballCount[ball]
                colorCount[oldColor] -= 1
                if colorCount[oldColor] == 0:
                    del colorCount[oldColor]
            colorCount[newColor] = 1 + colorCount.get(newColor, 0)
            ballCount[ball] = newColor
            res.append(len(colorCount))
        return res