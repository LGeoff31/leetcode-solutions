class Solution:
    def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:
        res = 0
        def transform(i):
            start, end = s[i], t[i]
            # Going forward
            ans1 = 0
            idx = ord(s[i]) - 97
            while start != end:
                ans1 += nextCost[idx]
                idx += 1
                if idx == 26:
                    idx = 0
                    start = "a"
                else:
                    start = chr(ord(start) + 1)
            # Going backward
            start, end = s[i], t[i]
            ans2 = 0
            idx = ord(s[i]) - 97
            # print('idx', idx)
            while start != end:
                # print('reached')
                ans2 += previousCost[idx]
                idx -= 1
                if idx < 0:
                    idx = 25
                    start = "z"
                else:
                    start = chr(ord(start) - 1)
            # print(ans1, ans2)
            return min(ans1, ans2)
        for i in range(len(s)):
            res += transform(i)
        return res