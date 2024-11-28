class Solution:
    def expand(self, s: str) -> List[str]:
        res = []
        idx = 0
        while idx < len(s):
            if s[idx] == "{":
                lst = []
                idx += 1
                while idx < len(s) and s[idx] != "}":
                    if s[idx] == ",":
                        idx += 1
                        continue
                    else:
                        lst.append(s[idx])
                    idx += 1
                if not res:
                    res = lst 
                else:
                    new_res = []
                    for i in range(len(res)):
                        for c in lst:
                            new_res.append(res[i] + c)
                    res = new_res
            else:
                if not res:
                    res.append(s[idx])
                else:
                    for i in range(len(res)):
                        res[i] += s[idx]
            idx += 1
            print(res)
        return sorted(res)
