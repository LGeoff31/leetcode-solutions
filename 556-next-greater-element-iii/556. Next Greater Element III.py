class Solution:
    def nextGreaterElement(self, n: int) -> int:
        def decreasing(s):
            for i in range(1, len(s)):
                if int(s[i]) > int(s[i-1]):
                    return False
            return True
        if decreasing(str(n)): return -1
        n = str(n)
        lst = [c for c in n]
        length = len(n)
        i = length - 1
        while i >= 0 and int(n[i-1]) >= int(n[i]):
            i -= 1
        j = length - 1
        while 0 <= j and j > i and not(int(n[i-1]) < int(n[j]) < int(n[i])):
            j -= 1
        print(i,j)
        lst[i-1], lst[j] = lst[j], lst[i-1]
        lst[i:] = sorted(lst[i:])
        if int("".join(lst)) > 2 ** 31 - 1: return -1
        return int("".join(lst))

        2147483648 
        2147483647