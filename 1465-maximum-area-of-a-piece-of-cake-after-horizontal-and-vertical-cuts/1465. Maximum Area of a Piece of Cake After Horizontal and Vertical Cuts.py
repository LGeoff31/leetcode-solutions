class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        MOD = 10 ** 9 + 7
        horizontalCuts.sort()
        verticalCuts.sort()
        horizontalCuts = [0] + horizontalCuts + [h]
        verticalCuts = [0] + verticalCuts + [w]
        heights = []
        widths = []
        res = 0
        for i in range(1, len(horizontalCuts)):
            heights.append(horizontalCuts[i] - horizontalCuts[i-1])
        for j in range(1, len(verticalCuts)):
            widths.append(verticalCuts[j] - verticalCuts[j-1])
        heights.sort()
        widths.sort()
        return heights[-1] * widths[-1] % MOD