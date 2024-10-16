from sortedcontainers import SortedList
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # Technically longest is length a+b+c unless you have constraint
        # Prob bet to decrease longest by 2, followed by 1 in another one
       
        turn = 0 # 0: a, 1: b, 2: c
        if b == max(a,b,c): turn = 1
        if c == max(a,b,c): turn = 2
        res = ""
        while True:
            if turn == 0:
                if a==0:
                    return res
                if a == 1 or max(a,b,c) - a >= 2:
                    res += "a"
                    a -= 1
                else:
                    res += "aa"
                    a -= 2

                if b == max(b,c): turn = 1
                else: turn = 2
            elif turn == 1:
                if b == 0: return res
                if b == 1 or max(a,b,c) - b >= 1:
                    res += "b"
                    b -= 1
                else:
                    res += "bb"
                    b -= 2
                if a == max(a,c): turn = 0
                else: turn = 2
            else:
                if c == 0: return res
                if c == 1 or max(a,b,c) - c >= 2:
                    res += "c"
                    c -= 1
                else:
                    res += "cc"
                    c -= 2
                if a == max(a,b): turn = 0
                else: turn = 1