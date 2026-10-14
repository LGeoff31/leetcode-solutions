class Solution:
    def maxSumOfSquares(self, num: int, _sum: int) -> str:
        res = [0] * num

        i = 0
        while _sum > 0 and i < len(res):
            res[i] = min(_sum, 9)
            _sum -= min(_sum, 9)
            i += 1
        
        if _sum > 0:
            return ""
        
        return "".join(str(c) for c in res)