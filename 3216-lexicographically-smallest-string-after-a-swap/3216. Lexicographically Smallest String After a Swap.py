class Solution:
    def getSmallestString(self, s: str) -> str:
        lst = [int(num) for num in s]
        for i in range(1, len(lst)):
            if lst[i]%2 == lst[i-1]%2 and str(lst[i-1]) > str(lst[i]):
                lst[i-1], lst[i] = lst[i], lst[i-1]
                break
        res = ""
        for a in lst:
            res += str(a)
        return res


        