class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return []
        l, r = 0, len(p) - 1
        dic = defaultdict(int)
        for i in range(len(p)):
            dic[s[i]] += 1
        target = Counter(p)
        res = []
        # if dic == target:
        #     res.append(0)


        while r < len(s):
            if dic == target:
                res.append(l)
            r += 1
            if r == len(s): break
            dic[s[r]] += 1
            dic[s[l]] -= 1
            if dic[s[l]] == 0:
                del dic[s[l]] 
            l += 1
        return res





        