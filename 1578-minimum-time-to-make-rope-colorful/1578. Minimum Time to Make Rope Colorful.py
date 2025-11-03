class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0
        # if len(colors) >= 2 and colors[0] == colors[1] and neededTime[0] < neededTime[1]:
        #     res = neededTime[0]
        prevColor = (colors[0], 0)
        for i in range(1, len(colors)):
            if colors[i] == prevColor[0]:
                res += min(neededTime[i], neededTime[prevColor[1]])
                if neededTime[i] > neededTime[prevColor[1]]:
                    prevColor = (colors[i], i)
            else:
                prevColor = (colors[i], i)
        return res