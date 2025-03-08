class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        dic = Counter(s[:k])
        if k > len(s): return 0
        def valid(dic):
            for key in dic:
                if dic[key] > 1:
                    return False
            return True
        res = valid(dic)
        for i in range(k, len(s)):
            dic[s[i-k]] -= 1
            dic[s[i]] = 1 + dic.get(s[i], 0)
            if valid(dic):
                res += 1
        return int(res)
