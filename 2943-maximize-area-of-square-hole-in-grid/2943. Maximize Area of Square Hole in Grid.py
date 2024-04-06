class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()
        maxHorz = 1
        maxVert = 1
        count=1
        for i in range(1, len(hBars)):
            if hBars[i] - hBars[i-1] == 1:
                count+=1
            else:
                count = 1
            maxHorz = max(maxHorz, count)
        count = 1
        for i in range(1, len(vBars)):
            if vBars[i] - vBars[i-1] == 1:
                count+=1
            else:
                count = 1
            maxVert = max(maxVert, count)
        print(maxVert, maxHorz)
        return min(maxVert+1, maxHorz+1) ** 2

        