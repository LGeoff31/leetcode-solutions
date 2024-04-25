class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        lst = []
        for i in range(len(s)):
            lst.append(ord(s[i]) - ord("a"))
        
        m = defaultdict(int)
        res = 1

        for i in range(len(s)):
            local = 1
            for j in range(max(0, lst[i] - k), min(25, lst[i] + k) + 1):
                if j not in m:
                    continue
                res = max(res, m[j] + 1)
                local = max(local, m[j] + 1)
            
            m[lst[i]] = max(m[lst[i]], local)

        return res 

