class Solution:
    def generateTag(self, caption: str) -> str:
        res = "#"
        a = caption.split()
        for i in range(len(a)):
            curr = ""
            word = a[i]
            for c in word:
                if word.isalpha():
                    curr += c
            if i == 0:
                res += curr.lower()
            else:
                res += curr[0].upper() + curr[1:].lower()
        return res[:100]