class Solution:
    def largestGoodInteger(self, num: str) -> str:
        num = str(num)
        res = ""
        for i in range(0, len(num) -2):
            if num[i] == num[i+1] == num[i+2]:
                res = max(res, num[i:i+3])
        return res