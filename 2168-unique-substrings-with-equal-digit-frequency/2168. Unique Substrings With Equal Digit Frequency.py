class Solution:
    def equalDigitFrequency(self, s: str) -> int:
        res = 0
        visited = set()
        def valid(dic):
            lst = list(dic.values())
            lst.sort()
            # print(lst)
            return lst[0] == lst[-1]
        for l in range(len(s)):
            curr = ""
            dic = defaultdict(int)
            for r in range(l, len(s)):  
                curr += s[r]
                dic[s[r]] += 1
                if curr not in visited and valid(dic):
                    res += 1
                    visited.add(curr)
        return res