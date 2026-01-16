class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        MOD = 10 ** 9 + 7

        rows, cols = m, n
        hFences.sort()
        vFences.sort()
        hFences = [1] + hFences + [m]
        vFences = [1] + vFences + [n]

        heights = set()
        for i in range(len(hFences)):
            for j in range(i+1, len(hFences)):
                height = hFences[j] - hFences[i]
                heights.add(height)
        res = 0
        for i in range(len(vFences)):
            for j in range(i+1, len(vFences)):
                width = vFences[j] - vFences[i]
                if width in heights:
                    res = max(res, width * width)
        if res == 0: return -1
        return res % MOD