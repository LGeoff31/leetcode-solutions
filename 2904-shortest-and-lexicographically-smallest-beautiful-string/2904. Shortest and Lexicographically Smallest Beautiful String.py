class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        res = "*" * 100
        l, r = 0, 0
        count = [0, 0]
        if s.count("1") == k and len(s) == k: return s
        
        def increment(i):
            if s[i] == "0":
                count[0] += 1
            else:
                count[1] += 1
        
        increment(0)
        def decrement(i):
            if s[i] == "0":
                count[0] -= 1
            else:
                count[1] -= 1

        while r < len(s):
            while r < len(s) and count[1] != k:
                r += 1
                if r == len(s): break
                increment(r)
            if r == len(s): 
                if count[1] == k:
                    return s
                break
            # Once if is valid
            if len(s[l: r+1]) < len(res):
                res = s[l : r+1]
            elif len(s[l: r+1]) == len(res):
                res = min(res, s[l: r+1])
            decrement(l)
            l += 1



        return res if res != "*" * 100 else ""
        
        