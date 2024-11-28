class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        n = len(s) // k
        dic = {}
        for i in range(0, len(s), n):
            dic[s[i: i+n]] = 1 + dic.get(s[i:i+n], 0)
        print(dic)
        for i in range(0, len(t), n):
            if t[i:i+n] not in dic:
                return False
            dic[t[i:i+n]] -= 1
            if dic[t[i:i+n]] == 0:
                del dic[t[i:i+n]]

        return True