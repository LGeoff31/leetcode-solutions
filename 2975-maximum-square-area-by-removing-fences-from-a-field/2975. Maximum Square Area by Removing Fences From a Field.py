class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        MOD = 10**9+7
        hFences.append(1)
        hFences.append(m)
        vFences.append(1)
        vFences.append(n)
        hFences.sort()
        vFences.sort()
        print(hFences)
        print(vFences)

        widths = set()
        for i in range(len(vFences)):
            for j in range(i+1, len(vFences)):
                widths.add(vFences[j] - vFences[i])
        heights = set()
        for i in range(len(hFences)):
            for j in range(i+1, len(hFences)):
                heights.add(hFences[j] - hFences[i])
        res = -1
        for num in widths:
            if num in heights:
                res = max(res, num*num)
        if res > MOD: return res % MOD
        return res