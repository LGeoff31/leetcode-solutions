from collections import Counter
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        res = ""
        a = set(s)
        dic = Counter(s)
        for letter in order:
            if letter in a:
                res += letter * dic[letter]

        for letter in a:
            if letter not in res:
                res += letter * dic[letter]
        return res

        


        