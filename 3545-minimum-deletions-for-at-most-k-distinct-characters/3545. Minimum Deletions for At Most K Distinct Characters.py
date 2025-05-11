class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        dic = Counter(s)
        lst = sorted([(dic[key], key) for key in dic], reverse=True)
        res = 0
        for i in range(k, len(lst)):
            res += lst[i][0]
        return res
