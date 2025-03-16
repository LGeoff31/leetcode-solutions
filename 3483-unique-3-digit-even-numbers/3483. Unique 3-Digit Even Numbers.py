class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        res = 0
        for i in range(100, 1000):
            valid = True
            for d in str(i):
                if digits.count(int(d)) < str(i).count(d) or int(str(i)[-1])%2==1:
                    valid = False
            if valid:
                res += 1
        return res