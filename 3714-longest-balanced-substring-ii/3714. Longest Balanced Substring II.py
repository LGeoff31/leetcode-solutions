class Solution:
    def longestBalanced(self, s: str) -> int:
        def fn1():
            res = 0
            cnt = 1
            for i in range(1, len(s)):
                if s[i] == s[i-1]:
                    cnt += 1
                else:
                    cnt = 1
                res = max(res, cnt)
            return max(res,1)
        def targets(letter1, letter2):
            res = 0
            a = 0
            b = 0
            dic = {0: -1}
            for i in range(len(s)):
                if s[i] != letter1 and s[i] != letter2:
                    a = 0
                    b = 0
                    dic = {0 : i}
                else:
                    a += letter1 == s[i]
                    b += letter2 == s[i]
                    if (a-b) in dic:
                        res = max(res, i - dic[a-b])
                    else:
                        dic[a-b] = i
            return res
                
        def fn2():
            print('boo', targets("a","b"), targets("a", "c"), targets("b", "c"))
            return max(targets("a","b"), targets("a", "c"), targets("b", "c"))
        
        def fn3():
            dic = {} # (a-b, a-c)
            dic[(0, 0)] = -1
            a,b,c = 0, 0, 0
            res = 0
            for i in range(len(s)):
                a += s[i] == "a"
                b += s[i] == "b"
                c += s[i] == "c"
                if (a-b, a-c) in dic:
                    res = max(res, i - dic[(a-b, a-c)])
                else:
                    dic[(a-b, a-c)] = i
            return res
        print(fn1(), fn2(), fn3())
        return max(fn1(), fn2(), fn3())