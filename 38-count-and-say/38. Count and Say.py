class Solution:
    def countAndSay(self, n: int) -> str:
        dp = [0] * 30
        dp[0] = "1"
        def convert(num):
            if len(num) == 1: return "1" + num
            num += "@"
            res = ""
            count = 1
            prevChar = num[0]
            for i in range(1, len(num)):
                if num[i] != num[i-1]:
                    res += str(count) + prevChar
                    count = 1
                else:
                    count += 1
                prevChar = num[i]
            return res

        for i in range(1, 30):
            dp[i] = convert(dp[i-1])
        print(dp)
        return dp[n-1]


        