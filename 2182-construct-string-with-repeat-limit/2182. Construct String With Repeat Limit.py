class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        lst = sorted(list(set([c for c in s])), reverse=True)
        dic = Counter(s)
        idx = 0
        res = ""
        while idx < len(lst):
            idx_temp = idx + 1
            while dic[lst[idx]] > 0:
                res += lst[idx] * min(dic[lst[idx]], repeatLimit)
                dic[lst[idx]] -= min(dic[lst[idx]], repeatLimit)
                if dic[lst[idx]] == 0:
                    break
                else:
                    if idx_temp >= len(lst): break
                    res += lst[idx_temp]
                    dic[lst[idx_temp]] -= 1
                    if dic[lst[idx_temp]] == 0:
                        idx_temp += 1
            print(res)
            idx += 1
        return res
