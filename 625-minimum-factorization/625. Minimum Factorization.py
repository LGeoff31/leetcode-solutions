class Solution:
    def smallestFactorization(self, num: int) -> int:
        # 48 = 2x3x2x2x2
        if num == 1: return 1
        lst = []
        i = 9
        while i != 1:
            while num % i == 0:
                lst.append(i)
                num //= i
            i -= 1
        lst.sort()
        for i in range(len(lst)):
            lst[i] = str(lst[i])
        if num > 9: return 0
        print(lst)
        if int("".join(lst)) > 2 ** 31 - 1: return 0
        return int("".join(lst))