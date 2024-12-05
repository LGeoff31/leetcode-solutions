class Solution:
    def canChange(self, start: str, target: str) -> bool:
        a = ""
        b = ""
        g,h = [], []
        x,y = [], []
        for i, c in enumerate(start):
            if c == "L":
                a += c
                g.append(i)
            elif c == "R":
                a += c
                h.append(i)
        for i,c in enumerate(target):
            if c == "L":
                b += c
                x.append(i)
            elif c == "R":
                b += c
                y.append(i)
        valid = True
        if len(g) != len(x) or len(h) != len(y): return False
        for i in range(len(g)):
            # checking the lefts
            if g[i] < x[i]:
                return False
        for i in range(len(h)):
            if h[i] > y[i]:
                return False

        return a == b