class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        res = 0
        def wavy(num):
            num = str(num)
            if len(num) < 3:
                return 0
            cnt = 0
            for i in range(1, len(num)-1):
                if int(num[i]) > max(int(num[i-1]), int(num[i+1])) or int(num[i]) < min(int(num[i-1]), int(num[i+1])):
                    cnt += 1
            return cnt
        for i in range(num1, num2+1):
            res += wavy(i)
        return res