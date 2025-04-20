class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        last_g = last_p = last_m = -1
        for i in range(len(garbage) -1, -1, -1):
            if "G" in garbage[i] and last_g == -1:
                last_g = i
            if "P" in garbage[i] and last_p == -1:
                last_p = i
            if "M" in garbage[i] and last_m == -1:
                last_m = i
        res = 0
        for i in range(last_g + 1):
            res += garbage[i].count("G")
            if i-1 >= 0: res += travel[i-1]
        for i in range(last_p + 1):
            res += garbage[i].count("P")
            if i-1 >= 0: res += travel[i-1]
        for i in range(last_m + 1):
            res += garbage[i].count("M")
            if i-1 >= 0: res += travel[i-1]
        return res
