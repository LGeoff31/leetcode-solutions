class Solution:
    def sortSentence(self, s: str) -> str:
        lst = []
        s = s.split()
        for word in s:
            lst.append((int(word[-1]), word[:-1]))
        lst.sort()
        a=[]
        for x in lst:
            a.append(x[1])
        return " ".join(a)
