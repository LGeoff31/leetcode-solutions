class Solution:
    def countHomogenous(self, s: str) -> int:
        res = 0
        if not len(s):
            return 0
        if len(s) == 1:
            return 1

        def sum_formula(num):
            return int(num*(num+1)*0.5)
        counter = 1
        for i in range(0, len(s)-1):
            if s[i] != s[i+1]:
                res += sum_formula(counter)
                counter = 1
            else:
                counter += 1
        if s[-1] == s[-2]:
            res += sum_formula(counter)
        else:
            res += 1

        return res % (10**9+7)
