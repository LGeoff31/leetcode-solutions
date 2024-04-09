class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        res = []
        for arr in words:
            a = arr.split(separator)
            print(a)
            c = []
            for b in a:
                if b == separator or b == "":
                    continue
                else:
                    c.append(b)
            for p in c:
                res.append(p)

        return res

        