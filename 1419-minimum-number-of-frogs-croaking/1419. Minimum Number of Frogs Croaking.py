class Solution:
    def minNumberOfFrogs(self, c: str) -> int:
        dic = defaultdict(int)
        res = 0 
        if max(Counter(c).values()) != min(Counter(c).values()): return -1
        e,f,g,h,i = 0,0,0,0,0
        for m in c:
            if m=='c':
                e+=1
            if m=='r':
                f+=1
            if m=='o':
                g+=1
            if m=='a':
                h+=1
            if m=='k':
                i+=1
            if not(e>=f>=g>=h>=i):
                return -1
        f = 0
        for char in c:
            if char == "c":
                dic['c'] += 1
                f += 1
                res = max(res, f)
            if char == "r":
                dic['c'] -= 1
                dic['r'] += 1
            if char == "o":
                dic['o'] += 1
                dic['r'] -= 1
            if char == "a":
                dic['a'] += 1
                dic['o'] -= 1
            if char == "k":
                dic['k'] += 1
                dic['a'] -= 1
                f -= 1
        for key in dic:
            if dic[key] < 0: return -1
        return res

            