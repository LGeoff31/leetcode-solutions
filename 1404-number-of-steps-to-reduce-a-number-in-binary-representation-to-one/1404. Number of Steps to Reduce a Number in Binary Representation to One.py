class Solution:
    def numSteps(self, s: str) -> int:
        num = 0
        for i in range(len(s) - 1, -1, -1):
            num += int(s[i]) * (2 ** (len(s) - i - 1 ))
        steps = 0
        while num != 1:
            if num % 2 == 0:
                num //= 2
            else:
                num += 1
            steps+=1
        return steps
        