class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        a = s.split()
        dic = {}
        if len(a) != len(pattern): return False
        for i,letter in enumerate(pattern):
            if a[i] in dic.values() and letter not in dic:
                return False
            if letter in dic and a[i] != dic[letter]:
                return False
            dic[letter] = a[i]
        return True
        